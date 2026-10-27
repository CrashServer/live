#!/usr/bin/env python3
"""Generate pattern-recipe atoms — parameterized demos of FoxDot's pattern
toolkit, including svdk's custom additions.

Each cell is a single playable line showing a specific pattern technique
(PEuclid rhythm, PBal style, PLife chaos, PMarkov walk, etc.) with a
sensible synth carrier. Cells are routed to role columns based on the
carrier synth so PEuclid drum recipes land in F, bass recipes in B, etc.

This complements the live-session atoms (which are svdk's own choices)
with a curated, comprehensive showcase of every pattern primitive available.

USAGE
    python3 grid/extract_patterns.py             # dry-run
    python3 grid/extract_patterns.py --merge     # fill empty grid slots
"""
import json
import os
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

GRID_DIR = Path.home() / "live" / "grid"
CELLS_FILE = GRID_DIR / "cells.json"

# Each recipe = (carrier_col, label_prefix, code)
# Carrier columns: B=bass, C=kick, D=snare, E=hat, F=play/drums,
# G=lead, H=lead2, A=pad, I=stab, K=texture, M=bell
RECIPES = []

# ─── PEuclid: rhythmic distribution ────────────────────────────
for n, k, label in [
    (3, 8, "tresillo"), (5, 8, "cinquillo"), (7, 16, "complex"),
    (3, 16, "sparse"), (9, 16, "dense"), (5, 12, "12-bar"),
]:
    RECIPES.append(("F", f"PEuclid({n},{k}) {label}",
        f'd1 >> play("X", dur=PEuclid({n},{k})/2, amp=PEuclid({n},{k})*0.8)'))
for n, k, lo, hi in [(5, 8, 0, 7), (7, 16, 0, 12), (3, 8, -7, 7)]:
    RECIPES.append(("G", f"PEuclid2({n},{k},{lo},{hi}) pitch",
        f'p1 >> pluck(PEuclid2({n},{k},{lo},{hi}), dur=1/4, sus=0.3, amp=0.7)'))

# ─── PFDur: layered Euclidean (svdk custom) ────────────────────
RECIPES.append(("F", "PFDur layered fill (3,5,7 in 16)",
    'd1 >> play("X.o-", dur=PFDur((3,16),(5,16),(7,16))/2, amp=0.8)'))
RECIPES.append(("B", "PFDur dense bass density",
    'b1 >> dbass([0,0,3,0], dur=PFDur((3,8),(5,8))/2, oct=4, sus=0.3)'))

# ─── PBal: balanced rhythm styles (svdk custom, 8 styles) ──────
for style in ["clave", "rumba", "reggae", "swing", "salsa", "cumbia",
              "quick", "polyrhythm"]:
    RECIPES.append(("F", f"PBal '{style}' groove",
        f'd1 >> play("X.o-", dur=PBal("{style}", 16)/2, amp=0.8)'))

# ─── PSwing (svdk custom): swing delay ─────────────────────────
for amount in [0.1, 0.15, 0.2, 0.25, 0.3]:
    RECIPES.append(("E", f"PSwing({amount}) hat shuffle",
        f'h1 >> play("-", dur=1/4, delay=PSwing({amount}, 8), amp=0.5)'))

# ─── Pacc (svdk custom): 4 accent types ────────────────────────
for acc_type in ["backbeat", "four-on-floor", "offbeat", "ghost"]:
    RECIPES.append(("F", f"Pacc '{acc_type}' accents",
        f'd1 >> play("X x X x X x X x ", dur=1/4, amp=Pacc("{acc_type}"))'))

# ─── PLife: cellular automaton (svdk custom) ───────────────────
for chaos, rule in [(0.0, "wolfram-0"), (0.2, "wolfram-90"),
                    (0.4, "wolfram-110"), (0.6, "wolfram-150"),
                    (0.8, "wolfram-30"), (1.0, "wolfram-254")]:
    RECIPES.append(("G", f"PLife chaos={chaos} ({rule})",
        f'p1 >> pluck(PLife(16, chaos={chaos}), dur=1/4, sus=0.3, amp=0.7)'))

# ─── melody() Markov generator (svdk custom) ──────────────────
RECIPES.append(("G", "melody() Markov pentatonic",
    'l1 >> pluck(melody({0:[2,4], 2:[0,4], 4:[2,0,7], 7:[4,5]}), dur=1/2, sus=0.4)'))
RECIPES.append(("G", "melody() Markov ascending",
    'l1 >> svdk(melody({0:[2], 2:[4], 4:[5], 5:[7], 7:[9], 9:[0]}), dur=1/4, oct=5)'))

# ─── PMarkov / PChords (var dict required) ────────────────────
RECIPES.append(("I", "PChords I-V-vi-IV",
    'c1 >> klank(PChords([I, V, VI, IV]), dur=4, sus=3.5, amp=0.6)'))
RECIPES.append(("I", "PChords ii-V-I jazz",
    'c1 >> klank(PChords([II, V, I]), dur=2, sus=1.8, amp=0.6)'))

# ─── PStutter: pattern repeats ─────────────────────────────────
RECIPES.append(("G", "PStutter([0,2,4], 3) repeat",
    'p1 >> pluck(PStutter([0,2,4,7], 3), dur=1/4, sus=0.3, amp=0.7)'))
RECIPES.append(("E", "PStutter hat triplet feel",
    'h1 >> play(PStutter("-", 3), dur=1/12, amp=0.5)'))

# ─── PWhite / PRand / PWalk: stochastic ────────────────────────
RECIPES.append(("G", "PRand pentatonic pluck",
    'l1 >> pluck(PRand([0,2,4,5,7]), dur=1/4, sus=0.3, amp=0.6)'))
RECIPES.append(("G", "PWalk(-7,7,1) gentle melody",
    'l1 >> svdk(PWalk(8, [-7,7,1]), dur=1/2, sus=0.5, amp=0.6)'))
RECIPES.append(("M", "PWhite(0,12) chromatic scatter",
    'm1 >> bell(PWhite(0,12), dur=1/2, sus=0.4, amp=0.5)'))

# ─── PShuf / PAlt / PZip: combinatorial ────────────────────────
RECIPES.append(("G", "PShuf([0,2,4,5,7]) randomized order",
    'p1 >> svdk(PShuf([0,2,4,5,7,9]), dur=1/2, sus=0.4, amp=0.6)'))
RECIPES.append(("G", "PAlt(A,B) alternating phrase",
    'p1 >> pluck(PAlt([0,2,4], [7,5,4]), dur=1/4, sus=0.3, amp=0.6)'))
RECIPES.append(("B", "PZip bass+rhythm zip",
    'b1 >> dbass(PZip([0,0,3,0], [0,2,4,7]), dur=1/4, oct=4, sus=0.3)'))

# ─── PSine / PTri / PSquare: shape patterns ────────────────────
for shape in ["PSine", "PTri", "PSquare"]:
    RECIPES.append(("A", f"{shape}(16) shape modulation",
        f'p1 >> sinepad([0,2,4,7], dur=1/2, sus=0.5, amp={shape}(16)*0.5+0.5)'))

# ─── PFibMod: Fibonacci modulo (Generators.py) ─────────────────
RECIPES.append(("M", "PFibMod(8, 12) Fibonacci series",
    'p1 >> bell(PFibMod(8, 12), dur=1/2, sus=0.4, amp=0.6)'))

# ─── PIndex / PTree: structured ────────────────────────────────
RECIPES.append(("G", "PIndex into chord pool",
    'p1 >> pluck(PIndex([0,2,4,5,7,9,11], PRand(0,7)), dur=1/4)'))

# ─── PRange / PTri (Sequences) ─────────────────────────────────
RECIPES.append(("G", "PRange(0,8) ramp",
    'p1 >> svdk(PRange(0,8), dur=1/4, sus=0.3, amp=0.6)'))
RECIPES.append(("G", "PTri(0,8) triangle wave",
    'p1 >> svdk(PTri(0,8), dur=1/4, sus=0.3, amp=0.6)'))

# ─── var/linvar/sinvar/expvar (TimeVar): time-varying ──────────
RECIPES.append(("B", "var() chord progression",
    'b1 >> dbass(var([0,-3,-5,-2], 8), dur=1/2, oct=4, sus=0.4, amp=0.7)'))
RECIPES.append(("A", "linvar() smooth filter sweep",
    'p1 >> sinepad([0,2,4], dur=4, sus=4, lpf=linvar([400,4000], 16))'))
RECIPES.append(("A", "sinvar() filter LFO",
    'p1 >> sinepad([0,2,4], dur=4, sus=4, lpf=sinvar([400,4000], 8))'))
RECIPES.append(("A", "expvar() exp ramp",
    'p1 >> sinepad([0,2,4], dur=4, sus=4, lpf=expvar([200,8000], 16))'))
RECIPES.append(("B", "Pvar() pattern of patterns",
    'b1 >> dbass(Pvar([P[0,0,3,0], P[0,3,5,3]], 8), dur=1/2, oct=4)'))

# ─── PGroups: stutter & delay micro-textures ───────────────────
RECIPES.append(("G", "P* stutter (0,2,4)",
    'p1 >> pluck([P*(0,2,4), 5, 7], dur=1/4, sus=0.3, amp=0.6)'))
RECIPES.append(("G", "P^ delay (0,2,0.5)",
    'p1 >> pluck([P^(0,2,0.5), 4, 5], dur=1/4, sus=0.3, amp=0.6)'))
RECIPES.append(("I", "Chord tuple (0,2,4)",
    'c1 >> klank([(0,2,4), (3,5,7), (-1,2,5)], dur=2, sus=1.8, amp=0.6)'))

# ─── Player methods: every, follow, sometimes, unison ──────────
RECIPES.append(("G", ".every(8, 'shuffle') periodic mutation",
    'p1 >> pluck([0,2,4,7], dur=1/4, sus=0.3).every(8, "shuffle")'))
RECIPES.append(("G", ".every(4, 'amp', 1.5) accent every 4",
    'p1 >> pluck([0,2,4,7], dur=1/4, sus=0.3).every(4, "amp", 1.5)'))
RECIPES.append(("G", ".unison(3) detuned cluster",
    'p1 >> svdk([0,2,4,7], dur=1/2, sus=0.4, amp=0.5).unison(3)'))
RECIPES.append(("G", ".sometimes('stutter', 4) random stutter",
    'p1 >> pluck([0,2,4,7], dur=1/4).sometimes("stutter", 4)'))
RECIPES.append(("G", ".rarely('amen') rare break swap",
    'd1 >> play("X.o.", dur=1/2).rarely("amen")'))
RECIPES.append(("G", ".often('drop') frequent silence",
    'd1 >> play("X.o.", dur=1/2).often("drop")'))
RECIPES.append(("F", ".penta() pentatonic filter",
    'p1 >> svdk(PRand(0,12), dur=1/4, sus=0.3).penta()'))

# ─── Conditional FX: boolean as effect value (svdk technique) ──
RECIPES.append(("G", "Conditional shape: shape=p1.degree==2",
    'p1 >> svdk([0,2,4,7], dur=1/2, sus=0.4, shape=p1.degree==2, amp=0.6)'))

# ─── follow(): player attribute following (svdk custom) ────────
RECIPES.append(("B", "follow() chord progression",
    'b1 >> dbass([0], dur=1/2, oct=4, degree=follow(p1), amp=0.7)'))

# ─── Tempo / scale / root utility ──────────────────────────────
for bpm in [88, 120, 132, 140, 160, 174, 180]:
    RECIPES.append(("K", f"Tempo set to {bpm}", f'Clock.bpm = {bpm}'))
for sc in ["minor", "major", "minorPentatonic", "majorPentatonic",
           "dorian", "phrygian", "harmonicMinor", "melodicMinor",
           "chromatic", "wholeTone"]:
    RECIPES.append(("K", f"Scale → {sc}", f'Scale.default = "{sc}"'))
for root in ["C", "D", "E", "F", "G", "A", "B", "C#", "F#"]:
    RECIPES.append(("K", f"Root → {root}", f'Root.default = "{root}"'))


def main():
    merge = "--merge" in sys.argv

    existing = {}
    if CELLS_FILE.exists():
        existing = json.loads(CELLS_FILE.read_text())

    occupied = defaultdict(set)
    for coord in existing:
        if len(coord) >= 2 and coord[0].isalpha() and coord[1:].isdigit():
            occupied[coord[0]].add(int(coord[1:]))

    proposals = {}
    by_col = defaultdict(list)
    for r in RECIPES:
        col, label, code = r
        by_col[col].append((label, code))

    for col, lst in by_col.items():
        row_iter = (r for r in range(400) if r not in occupied[col])
        for label, code in lst:
            try:
                row = next(row_iter)
            except StopIteration:
                print(f"WARN: col {col} full, dropped: {label}")
                continue
            coord = f"{col}{row}"
            proposals[coord] = {
                "code": code,
                "label": f"pattern: {label}",
                "type": "atom",
                "source": "pattern-recipes",
            }

    print(f"built {len(proposals)} pattern recipes")
    counts = defaultdict(int)
    for c in proposals: counts[c[0]] += 1
    for col in sorted(counts): print(f"  {col}: +{counts[col]}")

    GRID_DIR.joinpath("patterns_extracted.json").write_text(
        json.dumps({"_help": "curated pattern-recipe atoms",
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
        print(f"merged: +{len(proposals)}")


if __name__ == "__main__":
    main()
