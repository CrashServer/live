#!/usr/bin/env python3
"""Extract live-session atoms from log_sessions/*.txt into the grid.

The log_sessions/ folder contains 354 .txt files from real gigs/jams.
Each line is a FoxDot statement actually evaluated live — gold for the
grid because these are battle-tested, in-context musical lines (not
codeBank snippets).

STRATEGY
- Read all log_sessions/*.txt sequentially. Maintain Clock.bpm / Scale /
  Root context as we scan so each atom inherits the live state at the
  time it was played.
- Capture lines of the form `pX >> synth(...)` — single-line, unique.
- Dedupe by exact string. Pick most-diverse subset per (column, tempo-decade)
  to avoid filling cells with near-identical variations.
- Map each line to a column via SYNTH_TO_COL (reused from extract_all.py).
- Lines whose synths are unmapped go to **O** (overflow A-H, bass-family)
  or **P** (overflow G-I, lead/pad/keys-family).
- Top-up under-filled columns (J/K/L/M/N) without disturbing existing
  cells. Each column gets a max-capacity guard.

USAGE
    python3 grid/extract_logs.py             # write log_atoms_extracted.json
    python3 grid/extract_logs.py --merge     # also fill empty grid slots
"""
import json
import os
import re
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

# Reuse mapping from extract_all.py — same logic, no duplication
sys.path.insert(0, str(Path(__file__).parent))
from extract_all import SYNTH_TO_COL, classify_sample_player, bpm_to_row  # noqa: E402

LOG_DIR = Path.home() / "live" / "log_sessions"
GRID_DIR = Path.home() / "live" / "grid"
CELLS_FILE = GRID_DIR / "cells.json"
OUT_FILE = GRID_DIR / "log_atoms_extracted.json"

PLAYER_RE = re.compile(r'^([a-z]+\d+)\s*>>\s*([a-zA-Z_]+)\s*\(')
BPM_RE = re.compile(r'Clock\.bpm\s*=\s*([0-9]+)')
SCALE_RE = re.compile(r'Scale\.default\s*=\s*["\']([^"\']+)')
ROOT_RE = re.compile(r'Root\.default\s*=\s*["\']?([A-Za-z#b0-9]+)')

# Fallback columns for synths not in SYNTH_TO_COL
# O: experimental bass/perc/drum-family overflow
# P: experimental lead/pad/keys-family overflow
BASS_LIKE = {"sub", "wobble", "growl", "fuzz", "rumble", "low"}
LEAD_LIKE = {"saw", "sine", "lead", "syn", "key", "pad", "string",
             "arp", "pluck", "stab", "bell", "rhodes", "ep"}


def column_for_synth(synth_name):
    """Map synth name → grid column. Heuristic fallback to O/P."""
    if synth_name in SYNTH_TO_COL:
        return SYNTH_TO_COL[synth_name]
    name_lo = synth_name.lower()
    if any(t in name_lo for t in BASS_LIKE):
        return "O"
    if any(t in name_lo for t in LEAD_LIKE):
        return "P"
    return None  # skip


def scan_logs():
    """Walk log_sessions, return list of atom dicts with tempo/scale/root context."""
    files = sorted(LOG_DIR.glob("*.txt"))
    print(f"scanning {len(files)} session files...")
    atoms = []
    seen_exact = set()
    cur_bpm = None
    cur_scale = None
    cur_root = None
    for f in files:
        # Reset context per file (each session has its own state)
        cur_bpm = cur_scale = cur_root = None
        try:
            text = f.read_text(errors='replace')
        except Exception as e:
            print(f"  failed {f.name}: {e}")
            continue
        for raw in text.splitlines():
            ln = raw.rstrip()
            if not ln:
                continue
            # Update context
            mb = BPM_RE.search(ln)
            if mb:
                try:
                    cur_bpm = int(mb.group(1))
                except ValueError:
                    pass
            ms = SCALE_RE.search(ln)
            if ms:
                cur_scale = ms.group(1)
            mr = ROOT_RE.search(ln)
            if mr:
                cur_root = mr.group(1)
            # Atom candidate
            m = PLAYER_RE.match(ln)
            if not m:
                continue
            if len(ln) < 35:
                continue
            if ln in seen_exact:
                continue
            seen_exact.add(ln)
            player, synth = m.group(1), m.group(2)
            # MidiOut is MIDI routing, not a synth — skip
            if synth == "MidiOut":
                continue
            atoms.append({
                "code": ln,
                "player": player,
                "synth": synth,
                "tempo": cur_bpm,
                "scale": cur_scale,
                "root": cur_root,
                "source_file": f.name,
                "length": len(ln),
            })
    print(f"  scanned {len(seen_exact)} unique synth-assign lines")
    return atoms


def assign_columns(atoms):
    """Map each atom to (col, tempo_decade). Drop unmapped."""
    placed = []
    unmapped = Counter()
    for a in atoms:
        # First check sample-player special handling
        col = None
        if a["synth"] in ("play", "loop", "noloop", "stretch"):
            col = classify_sample_player(a["code"], a["synth"])
            # play() with non-literal pattern (vars, PEuclid, etc.) → drums by default
            if col is None and a["synth"] == "play":
                col = "F"
        if col is None:
            col = column_for_synth(a["synth"])
        if col is None:
            unmapped[a["synth"]] += 1
            continue
        a["col"] = col
        placed.append(a)
    print(f"  placed: {len(placed)} atoms")
    if unmapped:
        print(f"  unmapped synths (top 15): {unmapped.most_common(15)}")
    return placed


def diversify(atoms, max_per_bucket=8):
    """For each (col, tempo_decade) bucket, keep at most N most-distinct atoms.

    'Distinct' = different synth name preferred, then longer codes (richer
    parameterization). Greedy: pick longest unseen-synth first, fall back
    to length-sorted otherwise.
    """
    buckets = defaultdict(list)
    for a in atoms:
        decade = (a["tempo"] // 10) if a["tempo"] else 0
        buckets[(a["col"], decade)].append(a)

    kept = []
    for key, lst in buckets.items():
        lst.sort(key=lambda x: -x["length"])
        seen_synths = set()
        picked = []
        # Pass 1: one of each synth
        for a in lst:
            if a["synth"] in seen_synths:
                continue
            seen_synths.add(a["synth"])
            picked.append(a)
            if len(picked) >= max_per_bucket:
                break
        # Pass 2: fill remaining slots with longest extras
        if len(picked) < max_per_bucket:
            for a in lst:
                if a in picked:
                    continue
                picked.append(a)
                if len(picked) >= max_per_bucket:
                    break
        kept.extend(picked)
    print(f"  after diversification: {len(kept)} atoms")
    return kept


def load_existing_cells():
    if not CELLS_FILE.exists():
        return {}
    return json.loads(CELLS_FILE.read_text())


def build_proposals(atoms, existing):
    """For each atom, find first empty row in its column (rows 0..199).

    Column capacity: 200. Skip rows already occupied. Pack densely from
    row 0 upward, jumping past occupied rows.
    """
    occupied = defaultdict(set)
    for coord in existing:
        if len(coord) >= 2 and coord[0].isalpha() and coord[1:].isdigit():
            col = coord[0]
            row = int(coord[1:])
            occupied[col].add(row)

    # Group atoms by column, then place
    by_col = defaultdict(list)
    for a in atoms:
        by_col[a["col"]].append(a)

    proposals = {}
    placed_count = Counter()
    overflow_count = Counter()
    for col, lst in by_col.items():
        # Sort by tempo (so rows roughly correlate to tempo)
        lst.sort(key=lambda a: (a["tempo"] or 999, -a["length"]))
        row_iter = (r for r in range(200) if r not in occupied[col])
        for a in lst:
            try:
                row = next(row_iter)
            except StopIteration:
                overflow_count[col] += 1
                continue
            coord = f"{col}{row}"
            label_parts = [a["synth"]]
            if a["tempo"]:
                label_parts.append(f"@ {a['tempo']}")
            if a["root"]:
                label_parts.append(a["root"])
            if a["scale"]:
                label_parts.append(a["scale"])
            label = " ".join(label_parts) + f" (live)"
            body = {
                "code": a["code"],
                "label": label,
                "type": "atom",
                "synth": a["synth"],
                "source": f"log_sessions/{a['source_file']}",
            }
            if a["tempo"]:
                body["tempo"] = a["tempo"]
            if a["root"]:
                body["root"] = a["root"]
            if a["scale"]:
                body["scale"] = a["scale"]
            if a["root"] and a["scale"]:
                body["key"] = f"{a['root']} {a['scale']}"
            proposals[coord] = body
            placed_count[col] += 1
    return proposals, placed_count, overflow_count


def main():
    merge = "--merge" in sys.argv

    if not LOG_DIR.exists():
        print(f"log_sessions/ not found at {LOG_DIR}", file=sys.stderr)
        sys.exit(1)

    atoms = scan_logs()
    placed = assign_columns(atoms)
    kept = diversify(placed, max_per_bucket=8)

    existing = load_existing_cells()
    proposals, placed_count, overflow = build_proposals(kept, existing)

    print()
    print(f"== PROPOSAL SUMMARY ==")
    print(f"  total cells to place: {len(proposals)}")
    print(f"  per column:")
    for col in sorted(placed_count):
        ov = f" (+{overflow[col]} overflow)" if overflow[col] else ""
        print(f"    {col}: {placed_count[col]}{ov}")
    print()

    out = {
        "_help": (
            "Atoms extracted from log_sessions/ — real live-performance lines, "
            "battle-tested. Placed into existing role columns and overflow O/P. "
            "Merge with `--merge` flag to fill empty slots in cells.json."
        ),
        "proposed": proposals,
    }
    OUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"wrote {len(proposals)} proposals to {OUT_FILE}")

    if merge:
        added = 0
        for coord, body in proposals.items():
            if coord in existing:
                continue  # safety
            existing[coord] = body
            added += 1
        with tempfile.NamedTemporaryFile("w", dir=str(GRID_DIR), delete=False,
                                         suffix=".json") as tf:
            json.dump(existing, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)
        print(f"merged into cells.json: +{added} atoms")
        print(f"  -> run `compo.cell_reload()` in your FoxDot session")


if __name__ == "__main__":
    main()
