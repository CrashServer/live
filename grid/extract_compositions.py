#!/usr/bin/env python3
"""Curated composition starters — instant-launch multi-player setups.

Each cell is 4–10 lines of FoxDot establishing a complete genre vibe
(bass+drums+lead+pad). Drop one into the editor, evaluate, and you have
a jam going. Lines stay short so they can be tweaked easily live.

Lives in S/T columns at rows >= 200 (the original cap was 200, we expanded
to 400 so rows 200–399 are empty and available for scenes/starters).

USAGE
    python3 grid/extract_compositions.py             # dry-run
    python3 grid/extract_compositions.py --merge     # fill grid
"""
import json
import os
import sys
import tempfile
from pathlib import Path

GRID_DIR = Path.home() / "live" / "grid"
CELLS_FILE = GRID_DIR / "cells.json"

# Each starter = (column, label, tempo, key, code)
STARTERS = [
    ("S", "ambient bloom",    72, "C minor", '''Clock.bpm = 72
Scale.default = "minor"
Root.default = "C"
p1 >> sinepad([0,2,4,7], dur=8, sus=8, amp=linvar([0,0.4],32), lpf=sinvar([400,2400],16), shimmer=0.3)
p2 >> ethpad([(0,3,7),(2,5,9)], dur=16, sus=16, amp=0.2, cheapverb=0.5)
b1 >> subbass([0,0,-3,0], dur=2, oct=2, sus=1.5, amp=0.4, tape=0.2)
m1 >> bell(PRand([0,2,4,7,9]), dur=PDur(3,8), sus=0.3, amp=0.3, oct=6, cheapverb=0.5)'''),

    ("S", "dnb classic",      174, "D minor", '''Clock.bpm = 174
Scale.default = "minor"
Root.default = "D"
d1 >> play("X.o.X.o-", dur=1/2, sample=2, amp=0.8)
b1 >> subbass([0,0,3,0,0,5,0,0], dur=1/2, oct=3, sus=0.4, amp=0.8, drive=0.2)
s1 >> loop("amen8", dur=8, sample=PRand(4), amp=0.6, chop=4)
p1 >> klank([(0,3,7)], dur=4, sus=3, amp=0.3, cheapverb=0.5)
l1 >> pluck(melody({0:[3,5], 3:[5,7], 5:[7,3], 7:[0,3]}), dur=1/4, oct=5, amp=0.5)'''),

    ("S", "acid jam",         130, "A minor", '''Clock.bpm = 130
Scale.default = "minor"
Root.default = "A"
k1 >> compkick([1,_,_,_], dur=1/2, amp=0.8)
h1 >> play("-", dur=1/4, amp=PSeq([0.3,0.5,0.3,0.5]))
b1 >> tb303([0,0,3,0,0,5,0,-2], dur=1/4, oct=4, cutoff=linvar([500,2400],8), res=0.7, drive=0.3, amp=0.7)
d1 >> play("X.o.", dur=1/2, sample=4, amp=0.6)
c1 >> klank([(0,3,7)], dur=4, sus=3, amp=0.3)'''),

    ("S", "berlin techno",    132, "F minor", '''Clock.bpm = 132
Scale.default = "minor"
Root.default = "F"
k1 >> compkick([1], dur=1/2, amp=0.9)
h1 >> play("-", dur=1/2, amp=0.5, sample=1)
b1 >> dbass([0,0,0,3,0,0,5,0], dur=1/2, oct=4, sus=0.4, drive=0.3, lpf=linvar([400,2000],32), amp=0.7)
p1 >> hardstab([(0,3,7)], dur=PDur(3,8), sus=0.2, amp=0.4)
n1 >> loop("indus32", dur=32, amp=0.3, mverb=0.4)'''),

    ("S", "lofi hip hop",     88, "A minor", '''Clock.bpm = 88
Scale.default = "minor"
Root.default = "A"
d1 >> play("X.o.", dur=1/2, sample=8, amp=0.7, tape=0.4, tapedrive=0.3)
b1 >> pumpbass([0,0,3,0], dur=1/2, oct=4, sus=0.4, amp=0.7, lpf=800)
p1 >> pianovel([(0,3,7),(2,5,9)], dur=4, sus=3, amp=0.4, tape=0.5, cheapverb=0.4)
l1 >> pluck(melody({0:[2,3,5], 3:[0,5,7], 5:[3,7,9]}), dur=PDur(3,8), oct=5, amp=0.4)'''),

    ("S", "industrial",       128, "E minor", '''Clock.bpm = 128
Scale.default = "minor"
Root.default = "E"
k1 >> compkick([1], dur=1/2, amp=0.9, drive=0.2)
b1 >> dbass([0,0,3,0], dur=1/4, oct=4, sus=0.3, drive=0.4, shape=0.3, amp=0.7)
l1 >> war([0,0,3,5,3,0], dur=1/4, oct=5, cutoff=1200, beef=4, amp=0.6)
n1 >> loop("metaldrum16", dur=16, sample=PRand(4), amp=0.4, drive=0.3)
a1 >> doom([(0,3,7)], dur=8, sus=8, amp=0.3, cheapverb=0.5)'''),

    ("S", "trance build",     138, "C# minor", '''Clock.bpm = 138
Scale.default = "minor"
Root.default = "C#"
k1 >> compkick([1], dur=1/2, amp=0.9)
b1 >> dbass([0,0,0,0], dur=1/2, oct=3, sus=0.3, amp=0.6, leg=0.5)
p1 >> supersaw([0,3,5,7], dur=1/8, sus=0.15, amp=linvar([0.3,0.7],32), lpf=linvar([800,8000],32))
c1 >> klank([(0,3,7)], dur=2, sus=1.8, amp=0.4)
h1 >> play("-", dur=1/4, amp=0.4)'''),

    ("S", "drone metal",      66, "E minor", '''Clock.bpm = 66
Scale.default = "minor"
Root.default = "E"
b1 >> subbass([0,0,-5,0], dur=8, oct=2, sus=7.5, drive=0.5, amp=0.6, fuzz=0.3)
p1 >> doom([(0,3,7)], dur=16, sus=16, amp=0.4, drive=0.4, cheapverb=0.6)
n1 >> loop("ragedrone16", dur=16, amp=0.4, mverb=0.5)
d1 >> play("X...", dur=4, sample=2, amp=0.6, room=0.7)'''),

    ("S", "glitch IDM",       96, "B minor", '''Clock.bpm = 96
Scale.default = "minor"
Root.default = "B"
d1 >> play(PEuclid2(5,16,"X","."), dur=1/4, amp=0.7, crush=PRand(2,8), bits=PRand(6,12))
b1 >> dbass(PWalk(8,[-5,5,1]), dur=PDur(3,8), oct=4, sus=0.3, amp=0.7)
l1 >> pluck(PLife(16, chaos=0.6), dur=1/4, sus=0.2, oct=5, amp=0.5)
n1 >> loop("dnbfx16", dur=PDur(5,8), amp=0.4, chop=PRand(2,8))'''),

    ("S", "polyrhythm jam",   120, "G major", '''Clock.bpm = 120
Scale.default = "major"
Root.default = "G"
d1 >> play("X", dur=PBal("clave", 16)/2, amp=0.7)
h1 >> play("-", dur=PBal("rumba", 16)/2, amp=0.5)
b1 >> dbass([0,0,3,5], dur=PBal("reggae", 8)/2, oct=4, sus=0.4, amp=0.7)
l1 >> pluck([0,2,4,7], dur=PBal("salsa", 8)/2, sus=0.3, amp=0.6)'''),

    ("S", "spaceMmm ambient", 60, "C# minor", '''Clock.bpm = 60
Scale.default = "minor"
Root.default = "C#"
s1 >> loop("sundrone16", dur=16, amp=0.5, shimmer=0.4, cheapverb=0.6)
s2 >> loop("whitedwarf16", dur=16, amp=0.3, mverb=0.5)
b1 >> subbass([0], dur=16, oct=2, sus=15, amp=0.3, tape=0.3)
m1 >> bell([0,4,7,11], dur=PDur(3,16), sus=0.5, oct=6, amp=0.3, cheapverb=0.6)
p1 >> sinepad([(0,3,7),(2,5,9)], dur=32, sus=32, amp=0.2, lpf=sinvar([800,3200],16))'''),

    ("S", "psy goa",          145, "E minor", '''Clock.bpm = 145
Scale.default = "minor"
Root.default = "E"
k1 >> compkick([1], dur=1/2, amp=0.9)
b1 >> psybass([0], dur=1/4, oct=4, sus=0.2, cutoff=linvar([400,2800],8), res=0.7, amp=0.7)
l1 >> dab([0,3,5,7,3,0,2,5], dur=1/4, oct=5, amp=0.6, lpf=linvar([600,4800],16))
c1 >> hardstab([(0,3,7)], dur=PDur(3,8), sus=0.2, amp=0.5)
n1 >> loop("psyfx16", dur=16, amp=0.3, chop=4)'''),

    ("S", "footwork 160",     160, "D minor", '''Clock.bpm = 160
Scale.default = "minor"
Root.default = "D"
d1 >> play("X.o.X.o.", dur=PEuclid(5,8)/2, amp=0.8, sample=2)
b1 >> subbass(P[0,0,3,_,0,5,_,3], dur=1/2, oct=2, sus=0.4, amp=0.8)
s1 >> loop("vocalcrash8", dur=8, sample=PRand(4), amp=0.5, chop=8)
c1 >> klank([(0,3,7)], dur=4, sus=3.5, amp=0.3)'''),

    ("S", "breakcore frantic", 172, "F minor", '''Clock.bpm = 172
Scale.default = "minor"
Root.default = "F"
d1 >> play(PEuclid2(7,16,"X.","o-"), dur=1/4, amp=0.8, crush=PRand(2,8))
s1 >> loop("amen8", dur=PDur(5,8), sample=PRand(4), chop=PRand(2,8), amp=0.6)
b1 >> dbass(PWalk(8,[-5,5,1]), dur=PDur(3,8), oct=4, sus=0.2, drive=0.3, amp=0.7)
l1 >> war(PRand([0,3,5,7]), dur=1/8, oct=5, beef=6, amp=0.5)'''),

    ("S", "dub 80",           80, "G minor", '''Clock.bpm = 80
Scale.default = "minor"
Root.default = "G"
k1 >> compkick([1,_,_,_], dur=1/2, amp=0.9)
d1 >> play("..o.", dur=1/2, amp=0.6, room=0.7, sample=4)
b1 >> dbass([0,0,3,0], dur=1/2, oct=3, sus=0.4, amp=0.7, dub=0.5)
p1 >> klank([(0,3,7)], dur=4, sus=3, amp=0.4, echo=0.3, echotime=0.5)
l1 >> pluck([0,3,5,7], dur=PDur(3,8), sus=0.3, oct=5, amp=0.4, echo=0.4)'''),

    ("T", "DnB skeleton (minimal)", 174, "A minor", '''Clock.bpm = 174
Scale.default = "minor"
Root.default = "A"
d1 >> play("X.o.X.o-", dur=1/2, amp=0.8, sample=2)
b1 >> subbass([0,0,3,0], dur=1/2, oct=2, sus=0.4, amp=0.8)'''),

    ("T", "Techno skeleton",  132, "F minor", '''Clock.bpm = 132
Scale.default = "minor"
Root.default = "F"
k1 >> compkick([1], dur=1/2, amp=0.9)
h1 >> play("-", dur=1/2, amp=0.5)
b1 >> dbass([0,0,3,0], dur=1/4, oct=4, sus=0.3, amp=0.7)'''),

    ("T", "Hip-hop skeleton", 92, "D minor", '''Clock.bpm = 92
Scale.default = "minor"
Root.default = "D"
d1 >> play("X.o.", dur=1/2, sample=8, amp=0.7)
b1 >> pumpbass([0,0,3,0], dur=1/2, oct=4, sus=0.4, amp=0.7)'''),

    ("T", "Drum'n'bass roller", 174, "C minor", '''Clock.bpm = 174
Scale.default = "minor"
Root.default = "C"
d1 >> play("X-o-X-o-", dur=1/4, amp=0.7, sample=2)
b1 >> subbass([0,0,_,3,0,_,5,0], dur=1/4, oct=3, sus=0.2, amp=0.8, drive=0.3)
s1 >> loop("amen8", dur=8, amp=0.5, sample=PRand(4))'''),

    ("T", "Ambient drone",    60, "E minor", '''Clock.bpm = 60
Scale.default = "minor"
Root.default = "E"
p1 >> sinepad([0,2,4,7], dur=16, sus=16, amp=0.4, shimmer=0.4)
b1 >> subbass([0], dur=8, oct=2, sus=8, amp=0.3)'''),

    ("T", "Acid 303 only",    130, "A minor", '''Clock.bpm = 130
Scale.default = "minor"
Root.default = "A"
b1 >> tb303([0,0,3,0,5,0,_,-2], dur=1/4, oct=4, cutoff=linvar([500,2400],16), res=0.7, amp=0.7)'''),

    ("T", "Hoover stab loop", 138, "E minor", '''Clock.bpm = 138
Scale.default = "minor"
Root.default = "E"
c1 >> hoover([(0,3,7)], dur=PDur(3,8), sus=0.3, amp=0.7, drive=0.3)'''),

    ("T", "Reese bass",       170, "B minor", '''Clock.bpm = 170
Scale.default = "minor"
Root.default = "B"
b1 >> dbass([0,0,3,0,5,0], dur=1/4, oct=3, sus=0.2, drive=0.4, chorus=0.3, amp=0.8)'''),

    ("T", "Breakbeat alone",  140, "G minor", '''Clock.bpm = 140
Scale.default = "minor"
Root.default = "G"
s1 >> loop("amen8", dur=8, sample=PRand(8), chop=4, amp=0.7)'''),

    ("T", "Pad swell only",   72, "F# minor", '''Clock.bpm = 72
Scale.default = "minor"
Root.default = "F#"
p1 >> sinepad([(0,3,7),(2,5,9),(5,9,0)], dur=16, sus=16, amp=linvar([0,0.6],32), shimmer=0.4, cheapverb=0.5)'''),

    ("T", "Plaits FM lead",   100, "C major", '''Clock.bpm = 100
Scale.default = "major"
Root.default = "C"
l1 >> plaitsX(melody({0:[2,4], 2:[4,5], 4:[5,7], 5:[7,9], 7:[0,4]}), dur=1/4, oct=5, preset=3, amp=0.6)'''),
]


def main():
    merge = "--merge" in sys.argv

    existing = {}
    if CELLS_FILE.exists():
        existing = json.loads(CELLS_FILE.read_text())

    occupied = {"S": set(), "T": set()}
    for coord in existing:
        if len(coord) >= 2 and coord[0] in occupied and coord[1:].isdigit():
            occupied[coord[0]].add(int(coord[1:]))

    proposals = {}
    # Place starters in their target column starting from row 200 (the
    # original-cap watershed — keeps row 0–199 for existing scene cells)
    counters = {"S": 200, "T": 200}
    for col, label, tempo, key, code in STARTERS:
        # advance past occupied rows
        while counters[col] in occupied[col]:
            counters[col] += 1
        if counters[col] >= 400:
            print(f"WARN: col {col} row 400 reached, dropped: {label}")
            continue
        coord = f"{col}{counters[col]}"
        proposals[coord] = {
            "code": code,
            "label": f"starter: {label}",
            "type": "scene",
            "tempo": tempo,
            "key": key,
            "source": "composition-starters",
        }
        counters[col] += 1

    print(f"placed {len(proposals)} composition starters")
    GRID_DIR.joinpath("compositions_extracted.json").write_text(
        json.dumps({"_help": "curated composition starters (multi-line scenes)",
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
