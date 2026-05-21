#!/usr/bin/env python3
"""Extract candidate grid cells from existing codeBank tracks.

Scans ~/live/codeBank/*.py, finds one-line `player >> synth(...)` declarations,
classifies them by synth → grid column and Clock.bpm context → row band, and
writes proposals to ~/live/grid/cells_extracted.json for human review.

USAGE
    python3 grid/extract_from_codebank.py           # scan codeBank, write proposals
    python3 grid/extract_from_codebank.py --merge   # also auto-merge unambiguous
                                                    # proposals into cells.json

The merge mode only adds cells whose coord is NOT already populated. Existing
cells in cells.json are NEVER overwritten — re-running is safe.
"""
import json
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

CODEBANK_DIR = Path.home() / "live" / "codeBank"
GRID_DIR     = Path.home() / "live" / "grid"
CELLS_FILE   = GRID_DIR / "cells.json"
OUT_FILE     = GRID_DIR / "cells_extracted.json"

# Synth → column mapping
SYNTH_TO_COL = {
    # Pads (A)
    "pianovel": "A", "varsaw": "A", "sinepad": "A", "ethpad": "A",
    "darkpad": "A", "pad2": "A", "soprano": "A", "choir": "A",
    "viola": "A", "varicelle": "A", "keys": "A", "a_vpad": "A",
    "a_poly": "A", "pasha": "A", "waves": "A", "prophet": "A",
    "pads": "A", "angel": "A",

    # Bass (B)
    "dbass": "B", "lbass": "B", "cbass": "B", "ebass": "B",
    "sawbass": "B", "subbass": "B", "fbass": "B", "pumpbass": "B",
    "superbass": "B", "abass": "B", "bbass": "B", "pbass": "B",
    "glitchbass": "B", "acidbass": "B", "wobble": "B",
    "bass": "B", "jbass": "B", "dafbass": "B", "dbss": "B",
    "a_xbass": "B", "a_bassry": "B", "reese": "B",

    # Kick (C) — compkick + drum synthesizers
    "compkick": "C", "prodrums": "C", "a_bd": "C",

    # Snare/clap (D)
    "industrialsnare": "D", "a_sn": "D", "a_cy": "D",

    # Hihat/click (E)
    "click": "E", "pumphihat": "E", "a_hhat": "E",

    # Lead 1 (G) — melodic, single voice
    "faim": "G", "alva": "G", "darklead": "G", "prof": "G",
    "creep": "G", "lapin": "G", "vati": "G", "blip": "G",
    "dab": "G", "swiss": "G", "ssaw": "G", "karp": "G",
    "guit": "G", "fmsynth": "G", "supersaw": "G",
    "pluck": "G", "mpluck": "G", "saw": "G", "sine": "G",
    "soft": "G", "svdk": "G", "a_glead": "G", "a_vlead": "G",
    "a_daftlead": "G", "a_daft": "G", "a_wave": "G",
    "donorgan": "G", "donorganpat": "G",
    "splitter": "G", "total": "G", "sitar": "G", "dirt": "G",
    "twang": "G", "snick": "G", "arpymod": "G", "latoo": "G",

    # Lead 2 / aux modular (H)
    "plaitsX": "H", "plaits": "H", "cs80": "H", "braids": "H",
    "rave": "H", "rsin": "H", "four": "H", "donk": "H",
    "a_gesa": "H", "a_gesa2": "H", "a_gesa3": "H", "a_fantom": "H",
    "ews": "H", "gesa": "H",

    # Chord stab (I)
    "hardstab": "I", "hoover": "I", "klank": "I", "organ": "I",
    "stress": "I", "a_stress": "I", "a_stab": "I", "stab": "I",
    "juno": "I",

    # Acid (J)
    "tb303": "J", "tb304": "J", "tb305": "J", "acidline": "J",
    "tekno": "J",

    # Texture (K)
    "industrialdrone": "K", "noise": "K", "brown": "K", "drone": "K",
    "ambi": "K", "drift": "K", "angst": "K",
    "sos": "K", "ikea": "K", "glitcher": "K", "splaffer": "K",
    "eeri": "K", "war": "K", "pink": "K",

    # Bell/percussive metallic (M)
    "bell": "M", "bell2": "M", "gong": "M", "glass": "M",
    "charm": "M", "marimba": "M", "compperc": "M", "noisehit": "M",
    "crackle": "M", "blip": "M", "space": "M", "spaceMmm": "M",
    "dopple": "M", "cluster": "M", "foghorn": "M", "horn": "M",
    "zap": "M", "growl": "M", "gsynth": "M", "dub": "M",
    "bellmod": "M", "star": "M",

    # Special: radio voice (L)
    "radio": "L",

    # Special player functions
    "breakcore": "F",  # custom breakcore player
}

# play() / loop() / stretch() / noloop() classification by content
def classify_sample_player(code, synth_kind):
    """Look at the play()/loop()/etc args to pick a column."""
    # play("X..o..", ...) — drum pattern, look at first 1-2 chars
    pattern_match = re.search(r'play\(\s*[r]?["\']([^"\']*)["\']', code)
    if pattern_match:
        pat = pattern_match.group(1)[:4].lower()  # first 4 chars, lowercased
        if any(c in pat for c in "xk"):
            return "C"  # kick
        if any(c in pat for c in "os"):
            return "D"  # snare
        if any(c in pat for c in "-h=:"):
            return "E"  # hihat
        if any(c in pat for c in "u"):
            return "D"  # bongo/snare-ish
        return "F"  # other drum loop / pattern
    if synth_kind == "loop":
        # loop("breakcore160_16", ...) — usually drums or atmo
        sample_name = re.search(r'loop\(\s*["\']([^"\']+)', code)
        if sample_name:
            name = sample_name.group(1).lower()
            if any(t in name for t in ("drum", "break", "beat", "rage", "psy", "house", "fill", "core", "junglemix", "ragedrum")):
                return "F"
            if any(t in name for t in ("amen", "circle")):
                return "F"
            if any(t in name for t in ("atmo", "drone", "screech", "wind", "spheric", "sundrone", "whitedwarf", "gscreech")):
                return "N"
            if any(t in name for t in ("vocal", "voice", "oldies", "ahh", "growl")):
                return "L"
            return "F"  # default loop bucket
    if synth_kind == "noloop":
        sample_name = re.search(r'noloop\(\s*["\']([^"\']+)', code)
        if sample_name:
            name = sample_name.group(1).lower()
            if "vocal" in name or "oldies" in name or "voice" in name:
                return "L"
        return "L"
    if synth_kind == "stretch":
        return "N"
    return None


def bpm_to_row(bpm):
    """Map BPM to a row index in the 30s convention (10 rows per 20 BPM)."""
    if bpm is None:
        return 35  # default mid
    if bpm < 80:
        return min(9, max(0, int((bpm - 60) / 2)))
    if bpm < 100:
        return 10 + min(9, max(0, int((bpm - 80) / 2)))
    if bpm < 120:
        return 20 + min(9, max(0, int((bpm - 100) / 2)))
    if bpm < 140:
        return 30 + min(9, max(0, int((bpm - 120) / 2)))
    if bpm < 160:
        return 40 + min(9, max(0, int((bpm - 140) / 2)))
    if bpm < 180:
        return 50 + min(9, max(0, int((bpm - 160) / 2)))
    return 60 + min(9, max(0, int((bpm - 180) / 2)))


PLAYER_RE = re.compile(r'^([a-z]\d+)\s*>>\s*([a-zA-Z_]+)\s*\(')
BPM_RE = re.compile(r'Clock\.bpm\s*=\s*(?:lininf\s*\(\s*)?([0-9]+)')
SCALE_RE = re.compile(r'Scale\.default\s*=\s*["\']([^"\']+)')
ROOT_RE = re.compile(r'Root\.default\s*=\s*["\']?([A-Za-z#b0-9]+)')


def extract_from_file(path):
    """Return list of dicts with rich metadata per atom.
    Captured fields: coord, code, label, source, synth, tempo, scale, root,
    key, instrument, type, player_name."""
    cells = []
    text = path.read_text(errors='replace')
    current_bpm = None
    current_scale = None
    current_root = None

    for lineno, line in enumerate(text.splitlines(), 1):
        # Update BPM context
        m = BPM_RE.search(line)
        if m:
            current_bpm = int(m.group(1))
            continue
        # Update Scale context
        sm = SCALE_RE.search(line)
        if sm:
            current_scale = sm.group(1)
        # Update Root context
        rm = ROOT_RE.search(line)
        if rm:
            current_root = rm.group(1).strip('"\'')
        # Both updates can co-exist on same line as a player call — only
        # skip the line if it's a STANDALONE clock/scale/root statement.
        # The check below (is it a player declaration?) decides whether
        # the line itself becomes a cell.

        stripped = line.split('#', 1)[0].strip()
        if not stripped:
            continue
        if stripped.startswith('~'):
            continue
        pm = PLAYER_RE.match(stripped)
        if not pm:
            continue

        player_name = pm.group(1)
        synth = pm.group(2)

        col = SYNTH_TO_COL.get(synth)
        if col is None:
            if synth in ("play", "loop", "noloop", "stretch"):
                col = classify_sample_player(stripped, synth)
            if col is None:
                cells.append({
                    "coord": None, "code": stripped,
                    "label": f"unknown synth: {synth}",
                    "source": f"{path.name}:{lineno}",
                    "synth": synth, "tempo": current_bpm,
                    "scale": current_scale, "root": current_root,
                    "unclassified": True,
                })
                continue

        row = bpm_to_row(current_bpm)
        coord = f"{col}{row}"
        track_name = path.stem
        label = f"{synth} from {track_name}"
        if current_bpm:
            label += f" @ {current_bpm}"

        key = None
        if current_root and current_scale:
            key = f"{current_root} {current_scale}"
        elif current_root:
            key = current_root
        elif current_scale:
            key = current_scale

        cells.append({
            "coord": coord,
            "code": stripped,
            "label": label,
            "source": f"{path.name}:{lineno}",
            "synth": synth,
            "tempo": current_bpm,
            "scale": current_scale,
            "root": current_root,
            "key": key,
            "instrument": synth,
            "type": "atom",
            "player_name": player_name,
            "unclassified": False,
        })

    return cells


def deduplicate(cells):
    """Within the same coord, keep at most a few proposals (deduplicate by code)."""
    by_coord = defaultdict(list)
    unclassified = []
    for c in cells:
        if c.get("unclassified"):
            unclassified.append(c)
            continue
        by_coord[c["coord"]].append(c)

    # Within each coord, drop duplicate code lines (keep distinct ones)
    deduped = {}
    for coord, group in by_coord.items():
        seen_code = set()
        keep = []
        for c in group:
            sig = c["code"][:120]  # first 120 chars as signature
            if sig in seen_code:
                continue
            seen_code.add(sig)
            keep.append(c)
        deduped[coord] = keep

    return deduped, unclassified


def main():
    merge_mode = '--merge' in sys.argv

    if not CODEBANK_DIR.exists():
        print(f"codeBank not found at {CODEBANK_DIR}", file=sys.stderr)
        sys.exit(1)

    py_files = sorted(CODEBANK_DIR.glob("*.py"))
    print(f"scanning {len(py_files)} files in {CODEBANK_DIR}...")

    all_cells = []
    for p in py_files:
        try:
            all_cells.extend(extract_from_file(p))
        except Exception as e:
            print(f"  failed: {p.name}: {e}")

    print(f"  found {len(all_cells)} candidate lines")

    deduped, unclassified = deduplicate(all_cells)

    # Stats
    by_col = defaultdict(int)
    for coord, group in deduped.items():
        by_col[coord[0]] += len(group)

    print(f"  classified into columns: " + ", ".join(
        f"{col}={by_col[col]}" for col in sorted(by_col.keys())))
    print(f"  unclassified: {len(unclassified)}")

    # Write proposals
    out = {
        "_help": (
            "Auto-extracted candidate cells from codeBank. Review and pick "
            "which to import into cells.json. Multiple proposals per coord "
            "are listed — keep the one that fits or move alternates to other "
            "rows (e.g. B32 -> B33 for variation)."
        ),
        "proposed_by_coord": {
            coord: [{
                "code": c["code"],
                "label": c["label"],
                "source": c["source"],
                "synth": c["synth"],
                "tempo": c.get("tempo"),
                "key": c.get("key"),
                "instrument": c.get("instrument"),
            } for c in group]
            for coord, group in sorted(deduped.items())
        },
        "unclassified": [{
            "code": c["code"],
            "synth": c["synth"],
            "source": c["source"],
        } for c in unclassified],
    }
    OUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nwrote proposals to {OUT_FILE}")

    if merge_mode:
        # Load existing cells.json
        if CELLS_FILE.exists():
            existing = json.loads(CELLS_FILE.read_text())
        else:
            existing = {}

        added = 0
        skipped_occupied = 0
        enriched_existing = 0
        for coord, group in deduped.items():
            best = group[0]
            cell_body = {
                "code": best["code"],
                "label": best["label"],
                "type": "atom",
                "tempo": best.get("tempo"),
                "key": best.get("key"),
                "scale": best.get("scale"),
                "root": best.get("root"),
                "instrument": best.get("instrument"),
            }
            # Strip None values for cleanliness
            cell_body = {k: v for k, v in cell_body.items() if v is not None}

            if coord in existing:
                # ENRICH only — add any missing metadata fields without
                # overwriting code/label or existing fields. Keeps user
                # edits intact.
                cur = existing[coord]
                changed = False
                for k, v in cell_body.items():
                    if k in ("code", "label"):
                        continue  # preserve user edits
                    if k not in cur:
                        cur[k] = v
                        changed = True
                if changed:
                    enriched_existing += 1
                else:
                    skipped_occupied += 1
                continue
            # Add new
            existing[coord] = cell_body
            added += 1

        # Write back atomically
        import tempfile
        with tempfile.NamedTemporaryFile('w', dir=str(GRID_DIR), delete=False,
                                         suffix='.json') as tf:
            json.dump(existing, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)
        print(f"\nmerged into cells.json: +{added} new, "
              f"{enriched_existing} enriched (metadata added), "
              f"{skipped_occupied} coords kept as-is")
        print(f"  -> run `compo.cell_reload()` in your FoxDot session")


if __name__ == "__main__":
    main()
