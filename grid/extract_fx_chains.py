#!/usr/bin/env python3
"""Curated FX chain presets — combinations that work together musically.

Each cell shows a known-good combination of 2–4 effects applied to a
carrier synth. These are recipes the user can apply by either:
  - playing the cell directly to hear the chain
  - copying the FX kwargs into their own player

Lives in column P (FX showcase column, currently has individual FX demos
at rows 0–128).

USAGE
    python3 grid/extract_fx_chains.py             # dry-run
    python3 grid/extract_fx_chains.py --merge     # fill column P
"""
import json
import os
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

GRID_DIR = Path.home() / "live" / "grid"
CELLS_FILE = GRID_DIR / "cells.json"

# Each chain = (label, code). Column hardcoded to P.
CHAINS = [
    ("shimmer bloom (shimmer+room+atk)",
        'p1 >> sinepad([0,3,5,7], dur=4, sus=4, amp=0.5, shimmer=0.4, room=0.6, atk=2)'),
    ("tape warmth (tape+drift+tape drive)",
        'p1 >> pianovel([(0,3,7),(2,5,9)], dur=2, sus=1.5, amp=0.5, tape=0.5, tapedrive=0.3, drift=0.2)'),
    ("distorted lead (dist2+lpf+chorus)",
        'p1 >> svdk([0,3,5,7], dur=1/4, sus=0.2, amp=0.6, dist2=0.3, lpf=1800, chorus=0.4)'),
    ("industrial fuzz (dynfuzz+crush+room)",
        'p1 >> war([0,3,5], dur=1/4, sus=0.2, amp=0.6, dynfuzz=0.4, crush=4, room=0.5)'),
    ("dub space (echo+room+lpf sweep)",
        'p1 >> klank([(0,3,7)], dur=2, sus=1.5, amp=0.5, echo=0.4, echotime=0.5, room=0.6, lpf=linvar([800,3200],8))'),
    ("vinyl lofi (tape+crush+lpf+bits)",
        'p1 >> pianovel([(0,3,7)], dur=2, sus=1.5, amp=0.5, tape=0.4, crush=6, lpf=1200, bits=10)'),
    ("granular cloud (timeStretchFx+chop+shimmer)",
        'l1 >> loop("choir16", dur=16, amp=0.5, timeStretchFx=0.5, chop=8, shimmer=0.3)'),
    ("acid wobble (lpf sweep+drive+chorus)",
        'b1 >> tb303([0,3,0,5], dur=1/4, oct=4, cutoff=linvar([400,2800],8), drive=0.3, chorus=0.4, amp=0.7)'),
    ("breathing dist (sinvar shape)",
        'p1 >> svdk([0,3,5,7], dur=1/4, sus=0.3, amp=0.6, shape=sinvar([0,0.4],8), drive=0.2)'),
    ("octclean shimmer (octclean+room)",
        'p1 >> sinepad([0,3,5,7], dur=4, sus=4, amp=0.5, octclean=1, room=0.5)'),
    ("conditional shape on root",
        'p1 >> svdk([0,3,5,7], dur=1/4, sus=0.3, amp=0.6, shape=(p1.degree==0)*0.5)'),
    ("pumping sidechain (amp linvar)",
        'b1 >> dbass([0,0,3,0], dur=1/2, oct=4, sus=0.4, amp=linvar([0.2,0.9],[3,1])*0.7)'),
    ("filter pingpong (sinvar lpf+hpf)",
        'p1 >> svdk([0,3,5,7], dur=1/4, sus=0.3, amp=0.6, lpf=sinvar([400,3200],8), hpf=sinvar([100,800],4))'),
    ("ringmod metallic (ring+lpf)",
        'p1 >> bell([0,3,5,7], dur=1/4, sus=0.4, amp=0.5, ring=0.6, lpf=2400)'),
    ("formant vowel (formant+chorus)",
        'p1 >> svdk([0,3,5,7], dur=1/2, sus=0.4, amp=0.6, formant=2, chorus=0.3)'),
    ("multistage drive (drive+shape+crush)",
        'p1 >> svdk([0,3,5,7], dur=1/4, sus=0.3, amp=0.5, drive=0.3, shape=0.2, crush=6)'),
    ("psy lead chain (lpf+res+drive+chorus)",
        'p1 >> dab([0,3,5,7,5,3], dur=1/4, oct=5, lpf=linvar([800,4000],8), res=0.7, drive=0.3, chorus=0.4, amp=0.6)'),
    ("ghostly verb (cheapverb high+lpf)",
        'p1 >> bell([0,4,7,11], dur=2, sus=1.5, amp=0.4, cheapverb=0.7, lpf=2400, oct=6)'),
    ("trance arp (lpf sweep+sidechain+pluck)",
        'p1 >> pluck([0,3,5,7,3,5,7,0], dur=1/8, sus=0.1, amp=linvar([0.3,0.7],[1,1]), lpf=linvar([1200,6000],32))'),
    ("vocal chop (chop+stretch+room)",
        'l1 >> loop("vocalcrash8", dur=8, sample=PRand(4), chop=PRand(2,8), amp=0.5, room=0.5)'),
    ("amen mangler (crush+chop+rate var)",
        's1 >> loop("amen8", dur=PDur(5,8), sample=PRand(4), chop=PRand(2,8), crush=PRand(2,8), amp=0.6)'),
    ("freeze drone (freeze+cheapverb)",
        'p1 >> ethpad([0,3,5,7], dur=16, sus=16, amp=0.4, freeze=1, cheapverb=0.5)'),
    ("doppler swoop (doppler+room)",
        'p1 >> svdk([0,3,5,7], dur=2, sus=1.5, amp=0.5, doppler=0.5, room=0.4)'),
    ("comb resonator (combs+pluck)",
        'p1 >> combs([0,3,5,7], dur=1/4, sus=0.4, vibrate=4, depth=0.6, regen=-2, amp=0.5)'),
    ("fbdelay self-osc (fbdelay+lpf)",
        'p1 >> pluck([0], dur=1/4, sus=0.2, amp=0.5, fbdelay=0.6, lpf=1800, oct=5)'),
    ("krush+lofi (krush+bits+coarse)",
        'p1 >> svdk([0,3,5,7], dur=1/4, sus=0.3, amp=0.5, krush=0.4, bits=8, coarse=4)'),
    ("MoogFF resonant (mpf+mpr)",
        'p1 >> sawbass([0,0,3,0], dur=1/4, oct=4, mpf=600, mpr=3.8, drive=0.2, amp=0.7)'),
    ("DFM1 filter (dfm)",
        'p1 >> sawbass([0,0,3,0], dur=1/4, oct=4, dfm=800, dfmr=0.2, dfmd=1.5, amp=0.7)'),
    ("striate sample (striate)",
        's1 >> play("X.o.", dur=1/4, striate=8, amp=0.7)'),
    ("pshift detune (pshift)",
        'p1 >> pluck([0,3,5,7], dur=1/4, sus=0.3, amp=0.6, pshift=7)'),
    ("glide portamento (glide+sus)",
        'b1 >> dbass([0,3,5,2], dur=1, oct=4, sus=0.8, glide=1, glidedur=0.2, amp=0.7)'),
    ("envdist envelope follower",
        'p1 >> svdk([0,3,5,7], dur=1/4, sus=0.3, amp=0.6, envdist=0.4, drive=0.2)'),
    ("formant filter sweep (formant linvar)",
        'p1 >> svdk([0,3,5,7], dur=1/2, sus=0.4, amp=0.6, formant=linvar([0,4],16))'),
    ("multicrush bit reduction",
        'p1 >> pluck([0,3,5,7], dur=1/4, sus=0.3, amp=0.6, multicrush=4)'),
    ("decimate harsh (decimate+drive)",
        'p1 >> svdk([0,3,5,7], dur=1/4, sus=0.3, amp=0.5, decimate=0.4, drive=0.3)'),
    ("drcomp pumping (drcomp)",
        'b1 >> dbass([0,0,3,0], dur=1/2, oct=4, sus=0.4, amp=0.7, drcomp=0.5)'),
    ("comp limiter (comp)",
        'l1 >> svdk([0,3,5,7], dur=1/4, sus=0.3, amp=0.8, comp=0.5)'),
]


def main():
    merge = "--merge" in sys.argv

    existing = {}
    if CELLS_FILE.exists():
        existing = json.loads(CELLS_FILE.read_text())

    occupied = set()
    for coord in existing:
        if coord.startswith("P") and coord[1:].isdigit():
            occupied.add(int(coord[1:]))

    row_iter = (r for r in range(400) if r not in occupied)
    proposals = {}
    for label, code in CHAINS:
        try:
            row = next(row_iter)
        except StopIteration:
            print(f"WARN: col P full, dropped: {label}")
            continue
        coord = f"P{row}"
        proposals[coord] = {
            "code": code,
            "label": f"chain: {label}",
            "type": "atom",
            "source": "fx-chains",
        }

    print(f"placed {len(proposals)} fx-chain cells in column P")

    GRID_DIR.joinpath("fx_chains_extracted.json").write_text(
        json.dumps({"_help": "curated fx-chain presets",
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
