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

    # Filter out unusably-small or empty tracks
    tracks = [t for t in tracks if t["lines"] > 5]

    # Stable sort: by name (alphabetical), so Q0 == first alphabetically
    tracks.sort(key=lambda t: t["name"].lower())

    print(f"  kept {len(tracks)} non-trivial tracks")

    proposals = {}
    for i, t in enumerate(tracks):
        if i >= 100:
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
        }

    overflow = tracks[100:]
    out = {
        "_help": (
            "Full codeBank tracks as type='track' cells in column Q. "
            "Each cell's code is the entire track. Useful for jumping to "
            "a known scene/jam. Run with `compo.cell_run('Q0')` (no auto-"
            "stop — these are long compositions)."
        ),
        "proposed": proposals,
        "overflow_count": len(overflow),
        "overflow_sample": [t["name"] for t in overflow[:20]],
    }
    OUT_FILE.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"wrote {len(proposals)} track proposals to {OUT_FILE}")
    if overflow:
        print(f"  ({len(overflow)} more tracks beyond Q99)")

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
            # Strip None values for cleanliness
            body = {k: v for k, v in proposal.items() if v is not None and k != "source"}
            existing[coord] = body
            added += 1

        with tempfile.NamedTemporaryFile("w", dir=str(GRID_DIR), delete=False,
                                         suffix=".json") as tf:
            json.dump(existing, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)
        print(f"merged into cells.json: +{added} tracks, "
              f"{skipped_occupied} Q-coords kept as-is")
        print(f"  -> run `compo.cell_reload()` in your FoxDot session")


if __name__ == "__main__":
    main()
