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

BPM_RE   = re.compile(r'Clock\.bpm\s*=\s*(?:lininf\s*\(\s*)?([0-9]+)')
SCALE_RE = re.compile(r'Scale\.default\s*=\s*["\']([^"\']+)')
ROOT_RE  = re.compile(r'Root\.default\s*=\s*["\']?([A-Za-z#b0-9]+)')


def parse_header(code):
    """Return (name, category) from the first two comment lines.

    Format:  # <name> [bpm]        ← line 1
             # <category>          ← line 2 (optional)
    """
    name = cat = None
    ci = 0
    for line in code.strip().splitlines()[:6]:
        s = line.strip()
        if not s.startswith('#'):
            break
        content = s.lstrip('#').strip()
        if not content:
            continue
        ci += 1
        if ci == 1:
            # Name = everything before — or a trailing bare number
            m = re.match(r'^(.+?)(?:\s+[—–]\s+.*|\s+\d+\s*$)', content)
            name = (m.group(1) if m else re.sub(r'\s+\d+$', '', content)).strip() or None
        elif ci == 2:
            cat = content
            break
    return name, cat


def analyze_track(path):
    """Return {code, tempo, scale, root, key, name, category, source, lines, bytes}."""
    text = path.read_text(errors='replace')
    bpms   = BPM_RE.findall(text)
    scales = SCALE_RE.findall(text)
    roots  = ROOT_RE.findall(text)
    tempo  = int(bpms[0]) if bpms else None
    scale  = scales[0] if scales else None
    root   = roots[0].strip('"\'') if roots else None
    key    = None
    if root and scale: key = f"{root} {scale}"
    elif root:         key = root
    elif scale:        key = scale
    name, category = parse_header(text)
    return {
        "code":     text,
        "tempo":    tempo,
        "scale":    scale,
        "root":     root,
        "key":      key,
        "name":     name or path.stem,
        "category": category,
        "source":   path.name,        # filename (used as source_file)
        "lines":    text.count("\n") + 1,
        "bytes":    len(text),
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
        proposals[coord] = {
            "code":            t["code"],
            "label":           t["name"],      # clean name from header comment
            "type":            "track",
            "tempo":           t["tempo"],
            "key":             t["key"],
            "scale":           t["scale"],
            "root":            t["root"],
            "source":          "codeBank",
            "source_file":     t["source"],    # filename.py
            "attack_category": t["category"],  # from 2nd comment line
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
            body = {k: v for k, v in proposal.items() if v is not None}
            if coord in existing:
                cell = existing[coord]
                changed = False
                # Back-fill source_file
                if not cell.get("source_file") and proposal.get("source_file"):
                    cell["source_file"] = proposal["source_file"]
                    changed = True
                # Back-fill label (replace auto-generated "(NL)" labels or missing)
                if proposal.get("label") and (
                    not cell.get("label") or re.search(r'\(\d+L\)$', cell.get("label", ""))
                ):
                    cell["label"] = proposal["label"]
                    changed = True
                # Back-fill attack_category if not yet set
                if proposal.get("attack_category") and not cell.get("attack_category"):
                    cell["attack_category"] = proposal["attack_category"]
                    changed = True
                if changed:
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
