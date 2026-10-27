#!/usr/bin/env python3
"""Extract multi-player "scene cells" from #@section markers in codeBank tracks.

Many svdk tracks are structured as numbered sections via the convention:
    #@intro(32)
    p1 >> ethpad(...)
    b1 >> dbass(...)
    ...

Each `#@name(beats)` block holds a coherent scene — multiple players coming
in/out together. This script captures each block as a single multi-line cell.

Scene cells live in column S, sequential rows S0..S99. Up to 100 scenes/pass.

USAGE
    python3 grid/extract_sections.py            # write scenes_extracted.json
    python3 grid/extract_sections.py --merge    # also auto-fill S0..S99 in
                                                  cells.json
"""
import json
import os
import re
import sys
import tempfile
from pathlib import Path

CODEBANK_DIR = Path.home() / "live" / "codeBank"
GRID_DIR = Path.home() / "live" / "grid"
CELLS_FILE = GRID_DIR / "cells.json"
OUT_FILE = GRID_DIR / "scenes_extracted.json"

SECTION_RE = re.compile(r"^\s*#@\s*([a-zA-Z_]\w*)\s*\((\d+)b?\)\s*")
BPM_RE = re.compile(r"Clock\.bpm\s*=\s*(?:lininf\s*\(\s*)?([0-9]+)")


def extract_sections_from_file(path):
    text = path.read_text(errors="replace")
    current = None
    current_bpm = None
    out = []

    for line in text.splitlines():
        m = BPM_RE.search(line)
        if m:
            current_bpm = int(m.group(1))

        sm = SECTION_RE.match(line)
        if sm:
            if current and current["lines"]:
                out.append(_finalize(current))
            current = {
                "name": sm.group(1),
                "beats": int(sm.group(2)),
                "lines": [],
                "source": path.name,
                "bpm": current_bpm,
            }
            continue

        if current is not None:
            current["lines"].append(line)

    if current and current["lines"]:
        out.append(_finalize(current))

    return out


def _finalize(sec):
    code = "\n".join(sec["lines"]).strip()
    return {
        "name": sec["name"],
        "beats": sec["beats"],
        "code": code,
        "source": sec["source"],
        "bpm": sec["bpm"],
    }


def main():
    merge = "--merge" in sys.argv

    if not CODEBANK_DIR.exists():
        print(f"codeBank not found at {CODEBANK_DIR}", file=sys.stderr)
        sys.exit(1)

    files = sorted(CODEBANK_DIR.glob("*.py"))
    print(f"scanning {len(files)} files for #@sections...")

    all_sections = []
    skipped_empty = 0
    for p in files:
        try:
            for s in extract_sections_from_file(p):
                non_trivial = [
                    ln for ln in s["code"].splitlines()
                    if ln.strip() and not ln.strip().startswith("#")
                ]
                if len(non_trivial) < 2:
                    skipped_empty += 1
                    continue
                all_sections.append(s)
        except Exception as e:
            print(f"  failed: {p.name}: {e}")

    all_sections.sort(key=lambda s: (s["source"], s["name"]))
    print(f"  found {len(all_sections)} non-trivial sections "
          f"({skipped_empty} skipped as too small)")

    proposals = {}
    for i, s in enumerate(all_sections):
        if i >= 100:
            break
        coord = f"S{i}"
        label = f"{s['name']} from {Path(s['source']).stem}"
        if s["bpm"]:
            label += f" @ {s['bpm']} ({s['beats']}b)"
        else:
            label += f" ({s['beats']}b)"
        proposals[coord] = {
            "code": s["code"],
            "label": label,
            "source": s["source"],
            "bpm": s["bpm"],
            "beats": s["beats"],
            "section_name": s["name"],
        }

    overflow = all_sections[100:]
    out = {
        "_help": (
            "Multi-player scene cells extracted from #@section markers in "
            "codeBank tracks. Run a scene with `compo.cell_run('S0', 64)`."
        ),
        "proposed": proposals,
        "overflow_count": len(overflow),
        "overflow_sample": [f"{s['source']}:{s['name']}" for s in overflow[:20]],
    }
    OUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"wrote {len(proposals)} proposals to {OUT_FILE}")
    if overflow:
        print(f"  ({len(overflow)} more sections didn't fit in S0..S99)")

    if merge:
        existing = {}
        if CELLS_FILE.exists():
            existing = json.loads(CELLS_FILE.read_text())

        added = 0
        skipped_occupied = 0
        for coord, proposal in proposals.items():
            if coord in existing:
                skipped_occupied += 1
                continue
            existing[coord] = {
                "code": proposal["code"],
                "label": proposal["label"],
            }
            added += 1

        with tempfile.NamedTemporaryFile("w", dir=str(GRID_DIR), delete=False,
                                         suffix=".json") as tf:
            json.dump(existing, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)
        print(f"merged into cells.json: +{added} new, "
              f"{skipped_occupied} S-coords kept as-is")
        print(f"  -> run `compo.cell_reload()` in your FoxDot session")


if __name__ == "__main__":
    main()
