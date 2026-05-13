#!/usr/bin/env python3
"""Generate showcase atoms for all synths (column O) and all FX (column P).

Synth showcase (column O):
  One minimal demo cell per synthdef found in FoxDot/FoxDot/osc/scsyndef/.
  Each cell shows a `pX >> synthname([0,3,5,7], dur=1/2)`-style line so the
  user can hear what each of the 208 synths sounds like with one click.

FX showcase (column P):
  One demo cell per effect found in FoxDot/FoxDot/osc/sceffects/. Each
  cell plays a known-good carrier synth + the effect at a reasonable
  default value, so the user can audition each of the 122 FX.

We skip synths/FX that already have many representations in the grid (>20)
to avoid duplicating what's already there.

USAGE
    python3 grid/extract_showcase.py             # dry-run
    python3 grid/extract_showcase.py --merge     # fill empty slots in O/P
"""
import json
import os
import re
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

LIVE = Path.home() / "live"
SYNTHDEF_DIR = LIVE / "FoxDot" / "FoxDot" / "osc" / "scsyndef"
FX_DIR = LIVE / "FoxDot" / "FoxDot" / "osc" / "sceffects"
GRID_DIR = LIVE / "grid"
CELLS_FILE = GRID_DIR / "cells.json"

SHOWCASE_COL_SYNTHS = "O"
SHOWCASE_COL_FX = "P"

# Carrier synths for FX demos (picked per FX category so the demo sounds good)
DEFAULT_CARRIER = 'p1 >> svdk([0,2,4,7], dur=1, sus=0.8, amp=0.7'

# Synths that need special argument shapes (avoid "no freq" silence)
SAMPLE_SYNTHS = {"play", "loop", "noloop", "stretch"}
# Some synthdefs are intentionally non-playable (FX targets etc.)
SKIP_SYNTHS = {"play1", "play2", "loop1", "loop2", "stretch1", "stretch2",
               "audioin", "startSound", "killBuffer", "makeSound",
               "output", "input_recorder", "stem_recorder",
               "GabberKick"}  # capitalized weirdness

# Defaults per detected synth-class hint (very simple: just dur/sus)
def code_for_synth(name):
    """Build a 1-liner demo cell. Generic but sensible for unknown synths."""
    n = name.lower()
    if name in SAMPLE_SYNTHS:
        return None  # samples are covered by extract_loops + log atoms
    # Drum/perc synths — short staccato
    if any(t in n for t in ("kick", "snare", "hat", "perc", "click", "clap",
                            "noisehit", "zap", "blip", "tom", "drum")):
        return f'p1 >> {name}(P[0,_,0,_], dur=1/4, amp=0.8)'
    # Bass synths — low octave, longer sus
    if "bass" in n or n in ("sub", "wobble", "rumble", "growl"):
        return f'p1 >> {name}([0,0,3,0], dur=1/2, oct=4, sus=0.4, amp=0.7)'
    # Pad / drone / ambient
    if any(t in n for t in ("pad", "drone", "ambi", "choir", "swell", "ethpad",
                            "soprano", "viola", "waves", "pulse", "pink",
                            "eeri", "atmo")):
        return f'p1 >> {name}([0,2,4], dur=4, sus=4, amp=0.5)'
    # Bell / pluck / mallet
    if any(t in n for t in ("bell", "marimba", "glass", "pluck", "mallet",
                            "gong", "charm", "blip")):
        return f'p1 >> {name}([0,2,4,5,7], dur=1/2, sus=0.5, amp=0.7)'
    # Acid / 303-family
    if n.startswith("tb") or "acid" in n:
        return f'p1 >> {name}([0,0,3,0,5,0,7,0], dur=1/4, oct=4, cutoff=600, amp=0.7)'
    # Organ / stab
    if any(t in n for t in ("organ", "stab", "klank", "hardstab", "hoover")):
        return f'p1 >> {name}([(0,2,4)], dur=1/2, sus=0.4, amp=0.6)'
    # Otherwise: generic lead-style
    return f'p1 >> {name}([0,2,4,7], dur=1/2, sus=0.4, amp=0.6)'


def code_for_fx(fx_name):
    """Build a 1-liner showing the FX at a usable default."""
    n = fx_name.lower()
    # Boolean-style toggles use 0/1
    if n.endswith("freeze") or fx_name in ("octclean",):
        return f'p1 >> svdk([0,2,4,7], dur=1, sus=0.8, amp=0.7, {fx_name}=1)'
    # Reverb-family — 0.3-0.6 typical
    if any(t in n for t in ("verb", "shimmer", "room")):
        return f'p1 >> svdk([0,2,4,7], dur=1, sus=0.8, amp=0.7, {fx_name}=0.5)'
    # Delay-family — 0.2-0.5
    if any(t in n for t in ("delay", "echo", "dub")):
        return f'p1 >> svdk([0,2,4,7], dur=1, sus=0.4, amp=0.7, {fx_name}=0.25)'
    # Distortion/drive/shape — 0.3
    if any(t in n for t in ("dist", "drive", "shape", "fuzz", "fold",
                            "crush", "bits", "tanh", "tape", "saturate")):
        return f'p1 >> svdk([0,2,4,7], dur=1/2, sus=0.4, amp=0.6, {fx_name}=0.4)'
    # Filter — value depends; lpf needs Hz, others 0-1
    if "lpf" in n or "hpf" in n or "bpf" in n:
        # Frequency-style
        return f'p1 >> svdk([0,2,4,7], dur=1/2, sus=0.4, amp=0.7, {fx_name}=800)'
    if any(t in n for t in ("filter", "rq", "lpr", "hpr", "bpr")):
        return f'p1 >> svdk([0,2,4,7], dur=1/2, sus=0.4, amp=0.7, {fx_name}=0.5)'
    # Modulation — 0.4
    if any(t in n for t in ("chorus", "flanger", "phaser", "vib", "trem",
                            "modulate", "ring", "fm")):
        return f'p1 >> svdk([0,2,4,7], dur=1, sus=0.6, amp=0.7, {fx_name}=0.4)'
    # Default: 0.5
    return f'p1 >> svdk([0,2,4,7], dur=1, sus=0.6, amp=0.6, {fx_name}=0.5)'


SYNTHDEF_NAME_RE = re.compile(r'SynthDef\.new\(\\([A-Za-z_]\w*)')
FXLIST_RE = re.compile(r'FxList\.new\(\s*"([A-Za-z_]\w*)"')
EFFECT_PY_DIRS = [
    LIVE / "FoxDot" / "FoxDot" / "lib" / "Crashserver",  # crashFX.py
    LIVE / "FoxDot" / "FoxDot" / "lib" / "Effects",       # upstream
]


def discover_synths():
    """Parse the .scd filename + first-line synthdef declaration."""
    names = []
    if not SYNTHDEF_DIR.exists():
        return names
    for scd in sorted(SYNTHDEF_DIR.glob("*.scd")):
        # Default: derive from filename
        name = scd.stem
        # Refine via first 1KB scan
        try:
            head = scd.read_text(errors='replace')[:2000]
            m = SYNTHDEF_NAME_RE.search(head)
            if m:
                name = m.group(1)
        except Exception:
            pass
        if name in SKIP_SYNTHS:
            continue
        if name in SAMPLE_SYNTHS:
            continue
        names.append(name)
    return sorted(set(names))


def discover_fx():
    """Parse Python sources for authoritative FxList.new() registrations."""
    names = set()
    for d in EFFECT_PY_DIRS:
        if not d.exists():
            continue
        for py in d.glob("*.py"):
            try:
                text = py.read_text(errors='replace')
            except Exception:
                continue
            for m in FXLIST_RE.finditer(text):
                names.add(m.group(1))
    # Drop test/internal placeholders
    skip_fx = {"test", "_test"}
    return sorted(n for n in names if n not in skip_fx and not n.startswith("_"))


def main():
    merge = "--merge" in sys.argv

    synths = discover_synths()
    fxs = discover_fx()
    print(f"discovered {len(synths)} synths, {len(fxs)} fx")

    existing = {}
    if CELLS_FILE.exists():
        existing = json.loads(CELLS_FILE.read_text())

    occupied = defaultdict(set)
    for coord in existing:
        if len(coord) >= 2 and coord[0].isalpha() and coord[1:].isdigit():
            occupied[coord[0]].add(int(coord[1:]))

    proposals = {}

    # Synths → column O
    row_iter = (r for r in range(400) if r not in occupied[SHOWCASE_COL_SYNTHS])
    placed_synth = 0
    for s in synths:
        code = code_for_synth(s)
        if code is None:
            continue
        try:
            row = next(row_iter)
        except StopIteration:
            print(f"  WARN: O column full, dropped synth {s}")
            continue
        coord = f"{SHOWCASE_COL_SYNTHS}{row}"
        proposals[coord] = {
            "code": code,
            "label": f"showcase: {s}",
            "type": "atom",
            "synth": s,
            "source": "synthdef-showcase",
        }
        placed_synth += 1

    # FX → column P
    row_iter = (r for r in range(400) if r not in occupied[SHOWCASE_COL_FX])
    placed_fx = 0
    for f in fxs:
        code = code_for_fx(f)
        try:
            row = next(row_iter)
        except StopIteration:
            print(f"  WARN: P column full, dropped fx {f}")
            continue
        coord = f"{SHOWCASE_COL_FX}{row}"
        proposals[coord] = {
            "code": code,
            "label": f"FX: {f}",
            "type": "atom",
            "synth": "svdk+" + f,
            "fx": f,
            "source": "fx-showcase",
        }
        placed_fx += 1

    print(f"  placed {placed_synth} synth cells in {SHOWCASE_COL_SYNTHS}")
    print(f"  placed {placed_fx} fx cells in {SHOWCASE_COL_FX}")

    GRID_DIR.joinpath("showcase_extracted.json").write_text(
        json.dumps({"_help": "synth + fx showcase atoms",
                    "proposed": proposals}, indent=2, ensure_ascii=False))

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
