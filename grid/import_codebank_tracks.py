#!/usr/bin/env python3
"""Import 7 codeBank tracks into cells.json as rows 320-326.

Each track gets:
  - One row (320-326) where each player lives in its typed column (A=pad, B=bass, C=kick, ...)
  - A full-track starter cell in column S at the same row

Var/linvar/sinvar() are simplified to a single representative value so each
atom cell is standalone — performers can run any single cell without needing
the secs variable.

Run: python3 grid/import_codebank_tracks.py [--dry-run]
"""
import json, re, sys
from pathlib import Path

GRID_DIR     = Path.home() / "live" / "grid"
CODEBANK_DIR = Path.home() / "live" / "codeBank"
CELLS_FILE   = GRID_DIR / "cells.json"

DRY_RUN = "--dry-run" in sys.argv

# ── Track definitions ─────────────────────────────────────────
TRACKS = [
    ("ferment",  320, 170, "D",  "minor", "DnB — fbdelay dotted-8th rhythmics"),
    ("sediment", 321, 138, "C",  "minor", "dark techno — sinvar breathing"),
    ("glycine",  322,  88, "G",  "minor", "lo-fi soul — tape warmth, ghost hats"),
    ("splinter", 323, 163, "F",  "minor", "jungle — dual break loops, sample bank shift"),
    ("lurch",    324, 140, "Bb", "minor", "trap — 808 porta smear, PRand melody"),
    ("chrome",   325, 143, "F#", "minor", "drill — 808 porta drops, reverb saw"),
    ("redline",  326,  87, "A",  "minor", "boom bap — sample texture, off-beat stabs"),
]

# ── Player → column ───────────────────────────────────────────
PLAYER_COL = {
    "k1": "C", "k2": "C",
    "s1": "D", "s2": "D",
    "h1": "E", "h2": "E",   # h2 only added if E free
    "l1": "F", "l2": "F",   # l2 only added if F free
    "t1": "E",               # tight perc → hihat col (only if E free)
    "b1": "B",
    "b2": "J",               # secondary bass → acid col
    "b3": "K",
    "n1": "G",
    "n2": "H",
    "p1": "A",
    "m1": "I",
}

# ── Simplification helpers ────────────────────────────────────

def _pick_val(vals):
    """Return the best representative single value from a list.
    Prefers the first non-zero value; falls back to max."""
    for v in vals[1:]:          # skip index 0 (intro is often silent)
        if isinstance(v, (int, float)) and v != 0:
            return v
    return max((v for v in vals if isinstance(v, (int, float))), default=vals[0])

def simplify(code):
    """Replace var()/linvar()/sinvar() with single values for standalone use."""
    # Process in order: linvar/sinvar first, then bare var()
    # so that linvar([...]) is not mismatched by the var() pattern.

    # linvar([a, b], n) — use start value
    def sub_lin(m):
        try:
            a, b = json.loads(m.group(1))
            return str(a)
        except Exception:
            return m.group(0)

    code = re.sub(
        r'linvar\(\s*(\[[^\]]+\])\s*,\s*[\d.]+\)',
        sub_lin, code
    )

    # sinvar([a, b], n) — use midpoint
    def sub_sin(m):
        try:
            a, b = json.loads(m.group(1))
            v = (a + b) / 2
            return str(round(v, 4))
        except Exception:
            return m.group(0)

    code = re.sub(
        r'sinvar\(\s*(\[[^\]]+\])\s*,\s*[\d.]+\)',
        sub_sin, code
    )

    # var([...], anything) — negative lookbehind so we skip linvar/sinvar/expvar
    def sub_var(m):
        try:
            vals = json.loads(m.group(1).replace("(", "[").replace(")", "]"))
            if isinstance(vals, list) and vals:
                return str(_pick_val(vals))
        except Exception:
            pass
        return m.group(0)

    code = re.sub(
        r'(?<!lin)(?<!sin)(?<!exp)var\(\s*(\[[^\]]+\])\s*,\s*[^)]+\)',
        sub_var, code
    )

    return code

# ── Multi-line player extractor ───────────────────────────────

PLAYER_RE = re.compile(r'^([a-z]\d+)\s*>>')
EVERY_RE  = re.compile(r'^([a-z]\d+)\.every\(')

def extract_players(path):
    """Return {player_name: full_one_line_code} for all players in file."""
    lines = path.read_text().splitlines()
    players = {}
    every_calls = {}

    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.split('#', 1)[0].strip()

        m = PLAYER_RE.match(stripped)
        if m:
            player = m.group(1)
            parts  = [stripped]
            depth  = stripped.count('(') - stripped.count(')')
            j = i + 1
            while depth > 0 and j < len(lines):
                cont = lines[j].split('#', 1)[0].strip()
                if cont:
                    parts.append(cont)
                    depth += cont.count('(') - cont.count(')')
                j += 1
            code = re.sub(r'\s+', ' ', ' '.join(parts)).strip()
            players[player] = code
            i = j
            continue

        m2 = EVERY_RE.match(stripped)
        if m2:
            every_calls.setdefault(m2.group(1), []).append(stripped)

        i += 1

    # Append .every() calls to the relevant player
    for pname, calls in every_calls.items():
        if pname in players:
            players[pname] = players[pname] + '\n' + '\n'.join(calls)

    return players

# ── Full track loader ─────────────────────────────────────────

def full_track_code(path):
    """Return the complete file content stripped of blank lines and comments."""
    lines = []
    for line in path.read_text().splitlines():
        stripped = line.rstrip()
        # Keep code lines; drop pure comment lines but keep inline-comment lines
        if stripped.startswith('#'):
            continue
        lines.append(stripped)
    # Remove leading/trailing blank lines
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return '\n'.join(lines)

# ── Main ──────────────────────────────────────────────────────

def main():
    with open(CELLS_FILE) as f:
        cells = json.load(f)

    added = 0
    skipped = 0

    for (track_name, row, bpm, root, scale, desc) in TRACKS:
        src = CODEBANK_DIR / f"{track_name}.py"
        if not src.exists():
            print(f"  SKIP {track_name}: file not found")
            continue

        print(f"\n── {track_name}  (row {row}, {bpm} BPM, {root} {scale})")

        players = extract_players(src)
        used_cols = set()

        for pname, raw_code in players.items():
            col = PLAYER_COL.get(pname)
            if col is None:
                print(f"   {pname}: no column mapping — skipped")
                continue
            if col in used_cols:
                print(f"   {pname} → {col}{row}: column already used this row — skipped")
                continue

            coord = f"{col}{row}"
            if coord in cells:
                print(f"   {pname} → {coord}: occupied — skipped")
                skipped += 1
                continue

            atom_code  = simplify(raw_code)
            synth_m    = re.search(r'>>\s*([a-zA-Z_]+)\s*\(', raw_code)
            synth_name = synth_m.group(1) if synth_m else pname

            cell = {
                "code":       atom_code,
                "label":      f"{synth_name} from {track_name} @ {bpm}",
                "type":       "atom",
                "tempo":      bpm,
                "key":        f"{root} {scale}",
                "root":       root,
                "scale":      scale,
                "instrument": synth_name,
                "source":     f"codeBank/{track_name}.py",
            }

            used_cols.add(col)
            if not DRY_RUN:
                cells[coord] = cell
            added += 1
            print(f"   {pname} → {coord}  ({synth_name})")

        # Full track starter in column S
        s_coord = f"S{row}"
        if s_coord not in cells:
            full_code = full_track_code(src)
            n_lines   = full_code.count('\n') + 1
            cells[s_coord] = {
                "code":   full_code,
                "label":  f"starter: {track_name} — {desc} ({n_lines}L)",
                "type":   "starter",
                "tempo":  bpm,
                "key":    f"{root} {scale}",
                "root":   root,
                "scale":  scale,
                "source": f"codeBank/{track_name}.py",
            }
            if not DRY_RUN:
                pass  # already mutated above
            added += 1
            print(f"   full track → {s_coord}")
        else:
            print(f"   full track → {s_coord}: occupied — skipped")

    # Update _meta rows convention
    meta = cells.setdefault("_meta", {})
    conv = meta.setdefault("convention", {})
    rows = conv.setdefault("rows", {})
    rows["320-326"] = "svdk codeBank tracks: ferment/sediment/glycine/splinter/lurch/chrome/redline"

    if not DRY_RUN:
        import tempfile, os
        with tempfile.NamedTemporaryFile('w', dir=str(GRID_DIR), delete=False, suffix='.json') as tf:
            json.dump(cells, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)
        print(f"\n✓  cells.json updated: +{added} cells, {skipped} coords skipped (occupied)")
    else:
        print(f"\n[dry-run] would add {added} cells, skip {skipped} occupied coords")

if __name__ == "__main__":
    main()
