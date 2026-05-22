#!/usr/bin/env python3
"""Extract full codeBank tracks as 'track' type cells in column Q.

Each codeBank/*.py file becomes a single cell. Code = the entire file.
Metadata captured: tempo (primary BPM if multiple), key (root+scale),
type='track', source file name.

Up to 100 tracks fit in Q0..Q99. Files are sorted by name then assigned
sequentially.

USAGE
    python3 grid/extract_tracks.py             # write tracks_extracted.json
    python3 grid/extract_tracks.py --merge     # also fill Q0..Q99 in cells.json
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
OUT_FILE = GRID_DIR / "tracks_extracted.json"

BPM_RE = re.compile(r'Clock\.bpm\s*=\s*(?:lininf\s*\(\s*)?([0-9]+)')
SCALE_RE = re.compile(r'Scale\.default\s*=\s*["\']([^"\']+)')
ROOT_RE = re.compile(r'Root\.default\s*=\s*["\']?([A-Za-z#b0-9]+)')


def analyze_track(path):
    """Return {code, tempo, scale, root, key, name, source, lines, bytes}."""
    text = path.read_text(errors='replace')
    bpms = BPM_RE.findall(text)
    scales = SCALE_RE.findall(text)
    roots = ROOT_RE.findall(text)
    # Primary = first occurrence (typically the initial setting)
    tempo = int(bpms[0]) if bpms else None
    scale = scales[0] if scales else None
    root = roots[0].strip('"\'') if roots else None
    key = None
    if root and scale:
        key = f"{root} {scale}"
    elif root:
        key = root
    elif scale:
        key = scale
    return {
        "code": text,
        "tempo": tempo,
        "scale": scale,
        "root": root,
        "key": key,
        "name": path.stem,
        "source": path.name,
        "lines": text.count("\n") + 1,
        "bytes": len(text),
    }


def main():
    merge = "--merge" in sys.argv

    if not CODEBANK_DIR.exists():
        print(f"codeBank not found at {CODEBANK_DIR}", file=sys.stderr)
        sys.exit(1)

    files = sorted(CODEBANK_DIR.glob("*.py"))
    print(f"scanning {len(files)} files...")

    tracks = []
    for p in files:
        try:
            t = analyze_track(p)
            tracks.append(t)
        except Exception as e:
            print(f"  failed: {p.name}: {e}")

    # Filter out effectively empty files (blank or single-line stubs)
    tracks = [t for t in tracks if t["lines"] > 1]

    # Stable sort: by name (alphabetical), so Q0 == first alphabetically
    tracks.sort(key=lambda t: t["name"].lower())

    print(f"  kept {len(tracks)} non-trivial tracks")

    proposals = {}
    for i, t in enumerate(tracks):
        if i >= 400:
            break
        coord = f"Q{i}"
        label_parts = [t["name"]]
        if t["tempo"]:
            label_parts.append(f"@ {t['tempo']}")
        if t["key"]:
            label_parts.append(t["key"])
        label = " ".join(label_parts) + f" ({t['lines']}L)"
        proposals[coord] = {
            "code": t["code"],
            "label": label,
            "type": "track",
            "tempo": t["tempo"],
            "key": t["key"],
            "scale": t["scale"],
            "root": t["root"],
            "source": t["source"],
            "source_file": t["source"],  # t["source"] = path.name in analyze_track
        }

    out = {
        "_help": (
            "Full codeBank tracks as type='track' cells in column Q. "
            "Each cell's code is the entire .py file. source_file links "
            "back to the originating filename for two-way sync."
        ),
        "proposed": proposals,
        "total": len(proposals),
    }
    OUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"wrote {len(proposals)} track proposals to {OUT_FILE}")

    if merge:
        existing = {}
        if CELLS_FILE.exists():
            existing = json.loads(CELLS_FILE.read_text())

        added = 0
        patched = 0
        skipped = 0
        for coord, proposal in proposals.items():
            body = {k: v for k, v in proposal.items() if v is not None and k != "source"}
            if coord in existing:
                cell = existing[coord]
                if not cell.get("source_file") and proposal.get("source_file"):
                    # Back-fill source_file onto existing cell (migration step)
                    cell["source_file"] = proposal["source_file"]
                    patched += 1
                else:
                    skipped += 1
                continue
            existing[coord] = body
            added += 1

        with tempfile.NamedTemporaryFile("w", dir=str(GRID_DIR), delete=False,
                                         suffix=".json") as tf:
            json.dump(existing, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)
        print(f"merged into cells.json: +{added} new, {patched} patched source_file, "
              f"{skipped} unchanged")
        print(f"  -> run `compo.cell_reload()` in your FoxDot session")


if __name__ == "__main__":
    main()
