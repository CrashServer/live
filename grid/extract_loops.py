#!/usr/bin/env python3
"""Generate loop-showcase atoms from /home/svdk/UltimateSamples/{0,1,2}/_loop_/

Each named loop folder becomes a demo cell. The trailing digits in a loop
name encode its bar-length convention (e.g. drum16 = 16-beat loop, bass4 =
4-beat). We use that to set `dur=` so the cell plays musically out of the
box.

Loops are classified by name → grid column using keyword heuristics that
mirror the role columns already in use (drum/break → F, bass → B,
ambi/atmo/space → N, voice/vocal/oldies → L, etc.). Unclassified loops fall
back to F (general samples).

USAGE
    python3 grid/extract_loops.py             # dry-run
    python3 grid/extract_loops.py --merge     # fill empty grid slots
"""
import json
import os
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

LOOP_BANKS = [
    Path.home() / "UltimateSamples" / "0" / "_loop_",
    Path.home() / "UltimateSamples" / "1" / "_loop_",
    Path.home() / "UltimateSamples" / "2" / "_loop_",
]
GRID_DIR = Path.home() / "live" / "grid"
CELLS_FILE = GRID_DIR / "cells.json"
OUT_FILE = GRID_DIR / "loops_extracted.json"

# Skip these — not real loops
SKIP = {"__init__", "onsetDict", "serverVoice", "SPACE_SOUNDS_CATALOG",
        "EmptyFile", "description"}

# Loop-name keyword → grid column
LOOP_CATEGORY = [
    # (keyword substrings, column, label-category)
    (("ambi", "atmo", "drone", "cosmic", "nebula", "aurora", "centauri",
      "crab", "dune", "exoplanet", "ganymede", "mars", "saturn", "space",
      "sundrone", "whitedwarf", "solrot", "solmodes", "solarbells",
      "spherics", "quake", "satlightning", "flares", "carina", "elephant",
      "chorus", "shepard", "spaceMmm", "twinpeaks", "ubuntu", "whistler"),
        "N", "atmo"),
    (("drum", "break", "beat", "perc", "tom", "hat", "tabassa",
      "metaldrum", "electrodrum", "circledrum", "circdrum", "cindrum",
      "psydrum", "circlebreak", "ragedrum", "nbdrum", "revdrum", "xdrum",
      "xccongas", "wardrum", "surfDrum", "trap", "uk", "breakcore",
      "rytm", "rock", "metal", "indus", "industia", "ndirty", "nobledrum",
      "ghperc", "gperc", "gbreak", "gdrop", "gfill", "futurbeat", "drum",
      "noizebeat", "core", "pop", "swing", "house", "hiphop", "jungle"),
        "F", "drum/break"),
    (("bass", "sub", "xbass", "psybass", "ravebass", "nsbass", "tbass",
      "nbsub", "energicbass", "fbass", "bsbass", "housebass", "dubstepbass",
      "xtbass", "xxsbass", "xfadebass"),
        "B", "bass"),
    (("voice", "vocal", "oldies", "rvoice", "lynchvoice", "surfVoice",
      "vocalcrash", "vocalinfi", "voiceFr"),
        "L", "voice"),
    (("guitar", "gtr", "metalgtr", "ragegtr", "leadfunk", "surfGtr",
      "rockriff", "jazzguitar", "jazzkeys"),
        "G", "guitar"),
    (("pad", "nspad", "rhodes", "nrhodes", "piano", "nspiano", "xxpiano",
      "choir"),
        "A", "pad/keys"),
    (("synth", "metalsynth", "tsynth", "xxsynth", "xtech", "xvermin"),
        "H", "synth"),
    (("fx", "glitch", "drumglitch", "noise", "impulse", "zap", "stab",
      "stutter", "lynchcrazy", "lynchvoice", "psyfx"),
        "M", "fx"),
    (("loop", "intro", "fill", "seq", "frica", "jazza", "jazzb", "jazzc",
      "ragegrowl", "rageambi", "rageclean", "ragedrone", "gscreech",
      "auto", "futur", "psych", "cyber", "cyborg", "dance", "dub",
      "gab", "gapr", "half", "nbstabs", "nbstutter", "nbvarp",
      "nbhits", "nssub", "nszap", "berlin", "beru", "slaap", "wa",
      "voice", "long", "gbuild", "gtom", "gtop", "gcindrum",
      "jungleboy", "jungleangel", "junglebouncy", "junglecool",
      "jungleklanga", "junglesamourai"),
        "M", "loop"),
]

# AKWF wavetables are designed for warp() / chop() texture, not bar-loops.
# We still create cells but in column N (texture).
AKWF_COL = "N"

LOOP_DUR_RE = re.compile(r'(\d+)$')


def classify_loop(name):
    if name.startswith("AKWF"):
        return AKWF_COL, "wavetable"
    nlo = name.lower()
    for keywords, col, label_cat in LOOP_CATEGORY:
        if any(kw in nlo for kw in keywords):
            return col, label_cat
    return "F", "loop"  # fallback


def loop_dur(name):
    m = LOOP_DUR_RE.search(name)
    if not m:
        return 8  # default
    return int(m.group(1))


def demo_code(name, bank):
    """Generate a one-liner demo cell for this loop name + bank."""
    dur = loop_dur(name)
    # Sensible defaults: clamp dur to musical values
    if dur > 64:
        dur = 64
    if dur == 0:
        dur = 8
    # AKWF wavetables are short — use small dur
    if name.startswith("AKWF"):
        return f'l1 >> loop("{name}", dur=2, sample=PRand(8), rate=1, amp=0.6)'
    bank_arg = f", bank={bank}" if bank != 0 else ""
    return f'l1 >> loop("{name}", dur={dur}{bank_arg}, amp=0.7)'


def main():
    merge = "--merge" in sys.argv

    loops = []
    for bank_i, bdir in enumerate(LOOP_BANKS):
        if not bdir.exists():
            print(f"skip missing bank: {bdir}")
            continue
        for entry in sorted(bdir.iterdir()):
            if not entry.is_dir():
                continue
            name = entry.name
            if name in SKIP or name.startswith("."):
                continue
            loops.append({"name": name, "bank": bank_i})

    print(f"discovered {len(loops)} named loops across {len(LOOP_BANKS)} banks")

    # Load existing grid
    existing = {}
    if CELLS_FILE.exists():
        existing = json.loads(CELLS_FILE.read_text())

    # Build proposals
    occupied = defaultdict(set)
    for coord in existing:
        if len(coord) >= 2 and coord[0].isalpha() and coord[1:].isdigit():
            occupied[coord[0]].add(int(coord[1:]))

    by_col = defaultdict(list)
    for loop in loops:
        col, label_cat = classify_loop(loop["name"])
        loop["col"] = col
        loop["label_cat"] = label_cat
        by_col[col].append(loop)

    proposals = {}
    skipped_overflow = 0
    for col, lst in by_col.items():
        lst.sort(key=lambda L: L["name"].lower())
        row_iter = (r for r in range(400) if r not in occupied[col])
        for loop in lst:
            try:
                row = next(row_iter)
            except StopIteration:
                skipped_overflow += 1
                continue
            coord = f"{col}{row}"
            code = demo_code(loop["name"], loop["bank"])
            proposals[coord] = {
                "code": code,
                "label": f'{loop["name"]} ({loop["label_cat"]}, bank {loop["bank"]})',
                "type": "atom",
                "synth": "loop",
                "source": "UltimateSamples-loops",
                "loop_name": loop["name"],
                "bank": loop["bank"],
            }

    print(f"placed {len(proposals)} loop cells; {skipped_overflow} skipped (col full)")
    print("per column:")
    counts = defaultdict(int)
    for coord in proposals:
        counts[coord[0]] += 1
    for col in sorted(counts):
        print(f"  {col}: +{counts[col]}")

    OUT_FILE.write_text(json.dumps({"_help": "loop-name showcase atoms",
                                    "proposed": proposals},
                                   indent=2, ensure_ascii=False))
    print(f"wrote {OUT_FILE}")

    if merge:
        for coord, body in proposals.items():
            if coord not in existing:
                existing[coord] = body
        with tempfile.NamedTemporaryFile("w", dir=str(GRID_DIR), delete=False,
                                         suffix=".json") as tf:
            json.dump(existing, tf, indent=2, ensure_ascii=False)
            tmp = tf.name
        os.replace(tmp, CELLS_FILE)
        print(f"merged into cells.json: +{len(proposals)}")


if __name__ == "__main__":
    main()
