"""
MelodyPatterns.py
-----------------
Genre-aware melody/bass/pad/arp pattern generator.

gen("genre", "role")  — degree pattern with rests
gp("code")            — specific named pattern
.gen("genre", "role") — player method, sets degree + sus + amp

Usage:
    d1 >> blip(dur=0.5, oct=3).gen("techno", "bass")
    d1 >> blip(gp("tb3"), dur=0.5, oct=3)
    d1 >> blip(gen("techno", "bass"), dur=0.5, oct=3)
"""

from __future__ import absolute_import, division, print_function
import random

# _ = None is the rest symbol in FoxDot
_ = None

# ============================================================
# PATTERN LIBRARY
# ============================================================
# Each pattern: {"degree": [...], "sus": [...], "amp": [...]}
# _ (None) = rest. sus/amp at rest positions should be 0.

_patterns = {

    # ========== TECHNO ==========
    # Inspired by: Jeff Mills, Surgeon, Robert Hood, Derrick May
    "techno": {
        "bass": [
            # Jeff Mills "The Bells" — root-only, filter does the work
            {"degree": [0, 0, 0, 0, 0, 0, 0, 0], "sus": [0.2, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1], "amp": [0.9, 0.6, 0.6, 0.6, 0.8, 0.6, 0.6, 0.6]},
            # Surgeon "Magnese" — rhythmic single-note
            {"degree": [0, _, 0, _, 0, 0, _, 0], "sus": [0.15, 0, 0.15, 0, 0.15, 0.15, 0, 0.15], "amp": [0.9, 0, 0.7, 0, 0.8, 0.7, 0, 0.8]},
            # Robert Hood "Minimal Nation" — syncopated sparse
            {"degree": [0, _, _, 0, _, 0, _, _], "sus": [0.3, 0, 0, 0.2, 0, 0.15, 0, 0], "amp": [0.8, 0, 0, 0.6, 0, 0.5, 0, 0]},
            # Classic techno movement — root + 4th + 5th
            {"degree": [0, 0, _, 3, 0, _, 4, 0], "sus": [0.4, 0.3, 0, 0.3, 0.3, 0, 0.2, 0.4], "amp": [0.8, 0.6, 0, 0.7, 0.6, 0, 0.5, 0.8]},
            # Derrick May — arpegiated bass
            {"degree": [0, 3, 5, 3, 0, 3, 7, 5], "sus": [0.45, 0.35, 0.35, 0.3, 0.45, 0.35, 0.35, 0.35], "amp": [0.8, 0.6, 0.7, 0.6, 0.8, 0.6, 0.7, 0.6]},
            # Driving 16th — root with offbeat 5th
            {"degree": [0, 0, 0, _, 0, 4, 0, _], "sus": [0.2, 0.15, 0.2, 0, 0.2, 0.3, 0.2, 0], "amp": [0.9, 0.7, 0.7, 0, 0.8, 0.7, 0.6, 0]},
            # Percussive staccato — all root
            {"degree": [0, _, 0, 0, _, 0, _, 0], "sus": [0.1, 0, 0.1, 0.1, 0, 0.1, 0, 0.15], "amp": [0.9, 0, 0.7, 0.8, 0, 0.7, 0, 0.8]},
            # Sub bass — long root notes
            {"degree": [0, _, _, _, 0, _, _, _], "sus": [1.5, 0, 0, 0, 1.0, 0, 0, 0], "amp": [0.8, 0, 0, 0, 0.6, 0, 0, 0]},
            # Syncopated with minor 7th
            {"degree": [0, _, 0, _, 6, _, 0, _], "sus": [0.3, 0, 0.2, 0, 0.4, 0, 0.3, 0], "amp": [0.8, 0, 0.6, 0, 0.7, 0, 0.7, 0]},
            # Rolling — even 16ths with subtle pitch
            {"degree": [0, 0, 3, 0, 0, 0, 4, 0], "sus": [0.15, 0.12, 0.2, 0.12, 0.15, 0.12, 0.2, 0.15], "amp": [0.8, 0.6, 0.7, 0.6, 0.8, 0.6, 0.7, 0.6]},
        ],
        "lead": [
            # Underworld "Born Slippy" — pedal root with decoration
            {"degree": [0, 0, 4, 0, 3, 0, 4, 0], "sus": [0.2, 0.15, 0.3, 0.15, 0.3, 0.15, 0.3, 0.15], "amp": [0.7, 0.5, 0.7, 0.5, 0.7, 0.5, 0.7, 0.5]},
            # Recondite — sparse descending, long notes
            {"degree": [7, _, 5, _, 4, _, _, 2], "sus": [0.7, 0, 0.5, 0, 0.4, 0, 0, 0.6], "amp": [0.6, 0, 0.5, 0, 0.5, 0, 0, 0.6]},
            # Moderat — emotive dotted rhythm
            {"degree": [4, 5, 7, 5, 4, 2, 0, 2], "sus": [0.35, 0.15, 0.3, 0.3, 0.35, 0.15, 0.3, 0.3], "amp": [0.6, 0.5, 0.7, 0.6, 0.6, 0.5, 0.6, 0.5]},
            # Orbital "Halcyon" — flowing scalar
            {"degree": [0, 2, 4, 7, 4, 2, 0, -1], "sus": [0.2, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.3], "amp": [0.6, 0.5, 0.6, 0.8, 0.6, 0.5, 0.6, 0.5]},
            # Ascending tension
            {"degree": [0, _, 2, 3, _, 5, 7, _], "sus": [0.3, 0, 0.2, 0.3, 0, 0.4, 0.5, 0], "amp": [0.6, 0, 0.5, 0.6, 0, 0.7, 0.8, 0]},
            # Sparse melancholic
            {"degree": [5, _, _, 3, 2, _, 0, _], "sus": [0.5, 0, 0, 0.4, 0.3, 0, 0.5, 0], "amp": [0.7, 0, 0, 0.6, 0.5, 0, 0.7, 0]},
            # Stepwise descent
            {"degree": [7, 5, 4, 3, 2, 0, _, 0], "sus": [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0, 0.3], "amp": [0.7, 0.6, 0.6, 0.6, 0.5, 0.7, 0, 0.6]},
            # Call and response
            {"degree": [0, 2, 4, _, 5, 4, 2, 0], "sus": [0.2, 0.2, 0.3, 0, 0.4, 0.3, 0.2, 0.3], "amp": [0.6, 0.5, 0.6, 0, 0.8, 0.6, 0.5, 0.7]},
        ],
        "pad": [
            # Static minor triad → 4th chord
            {"degree": [(0,2,4), (0,2,4), (0,2,4), (0,2,4), (3,5,7), (3,5,7), (3,5,7), (3,5,7)], "sus": [4, 4, 4, 4, 4, 4, 4, 4], "amp": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]},
            # Open voicing movement
            {"degree": [(0,4,7), (0,4,7), (0,4,7), (0,4,7), (2,5,9), (2,5,9), (2,5,9), (2,5,9)], "sus": [4, 4, 4, 4, 4, 4, 4, 4], "amp": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]},
            # Two-chord breathe
            {"degree": [(0,2,4), _, (3,5,7), _, (0,2,4), _, (4,6,8), _], "sus": [3, 0, 3, 0, 3, 0, 3, 0], "amp": [0.5, 0, 0.5, 0, 0.5, 0, 0.5, 0]},
            # Minor → diminished tension
            {"degree": [(0,3,7), (0,3,7), (2,5,9), (2,5,9), (4,7,11), (4,7,11), (0,3,7), (0,3,7)], "sus": [3, 3, 3, 3, 3, 3, 3, 3], "amp": [0.5, 0.45, 0.55, 0.5, 0.55, 0.5, 0.5, 0.45]},
            # Wide voicing
            {"degree": [(0,2,4), (0,2,4), (5,7,9), (5,7,9), (3,5,7), (3,5,7), (0,2,4), (0,2,4)], "sus": [3, 3, 3, 3, 3, 3, 3, 3], "amp": [0.5, 0.45, 0.55, 0.5, 0.5, 0.45, 0.5, 0.45]},
        ],
        "arp": [
            # Classic triad arp
            {"degree": [0, 2, 4, 7, 0, 2, 4, 7], "sus": [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15], "amp": [0.7, 0.5, 0.5, 0.6, 0.7, 0.5, 0.5, 0.6]},
            # Alternating cell
            {"degree": [0, 4, 2, 4, 3, 7, 5, 7], "sus": [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12], "amp": [0.7, 0.5, 0.6, 0.5, 0.7, 0.5, 0.6, 0.5]},
            # Descending mirror
            {"degree": [7, 4, 2, 0, 7, 4, 2, 0], "sus": [0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15], "amp": [0.7, 0.6, 0.5, 0.5, 0.7, 0.6, 0.5, 0.5]},
            # Pedal arp
            {"degree": [0, 2, 0, 4, 0, 5, 0, 7], "sus": [0.1, 0.15, 0.1, 0.15, 0.1, 0.15, 0.1, 0.15], "amp": [0.6, 0.7, 0.6, 0.7, 0.6, 0.7, 0.6, 0.8]},
            # Transposing cell
            {"degree": [0, 2, 4, 2, 3, 5, 7, 5], "sus": [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12], "amp": [0.7, 0.5, 0.5, 0.5, 0.7, 0.5, 0.5, 0.5]},
            # Wide intervals
            {"degree": [0, 7, 4, 2, 3, 7, 5, 3], "sus": [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12], "amp": [0.7, 0.5, 0.5, 0.6, 0.7, 0.5, 0.5, 0.6]},
        ],
        "stab": [
            # Offbeat chords
            {"degree": [(0,2,4), _, _, (0,2,4), _, _, (3,5,7), _], "sus": [0.08, 0, 0, 0.08, 0, 0, 0.08, 0], "amp": [0.9, 0, 0, 0.7, 0, 0, 0.8, 0]},
            # Syncopated
            {"degree": [_, (0,2,4), _, _, (0,2,4), _, (3,5,7), _], "sus": [0, 0.08, 0, 0, 0.08, 0, 0.08, 0], "amp": [0, 0.8, 0, 0, 0.7, 0, 0.9, 0]},
            # Power chords
            {"degree": [(0,4), _, (0,4), _, _, (3,7), _, _], "sus": [0.1, 0, 0.1, 0, 0, 0.1, 0, 0], "amp": [0.9, 0, 0.7, 0, 0, 0.8, 0, 0]},
            # Sparse hits
            {"degree": [_, _, (0,2,4), _, (3,5,7), _, _, (0,2,4)], "sus": [0, 0, 0.08, 0, 0.08, 0, 0, 0.08], "amp": [0, 0, 0.8, 0, 0.9, 0, 0, 0.7]},
        ],
    },

    # ========== GESAFFELSTEIN ==========
    # Inspired by: Pursuit, Viol, Hellifornia, Reset
    "gesaffelstein": {
        "bass": [
            # "Pursuit" — root + semitone below, menacing
            {"degree": [0, 0, _, 0, -1, -1, _, -1], "sus": [0.4, 0.2, 0, 0.4, 0.4, 0.2, 0, 0.4], "amp": [0.9, 0.8, 0, 0.9, 0.9, 0.8, 0, 1.0]},
            # "Viol" — dotted stab rhythm
            {"degree": [0, _, _, 0, _, _, 0, _], "sus": [0.1, 0, 0, 0.1, 0, 0, 0.1, 0], "amp": [1.0, 0, 0, 0.9, 0, 0, 1.0, 0]},
            # "Hellifornia" — chromatic descent
            {"degree": [0, 0, -1, -2, 0, 0, -1, -3], "sus": [0.4, 0.2, 0.4, 0.6, 0.4, 0.2, 0.4, 0.8], "amp": [0.9, 0.8, 0.9, 1.0, 0.9, 0.8, 0.9, 1.0]},
            # Relentless root
            {"degree": [0, 0, 0, _, 0, 0, _, 0], "sus": [0.3, 0.3, 0.3, 0, 0.3, 0.3, 0, 0.3], "amp": [0.9, 0.8, 0.8, 0, 0.9, 0.8, 0, 0.9]},
            # Mechanical — every hit same
            {"degree": [0, 0, 0, 0, 0, _, 0, 0], "sus": [0.3, 0.3, 0.3, 0.3, 0.3, 0, 0.3, 0.3], "amp": [0.9, 0.9, 0.9, 0.9, 0.9, 0, 0.9, 0.9]},
            # Dark drop
            {"degree": [0, _, 0, 0, _, 0, 0, -3], "sus": [0.3, 0, 0.3, 0.3, 0, 0.3, 0.3, 0.6], "amp": [0.9, 0, 0.8, 0.8, 0, 0.8, 0.8, 1.0]},
            # Semitone tension
            {"degree": [-1, _, 0, 0, 0, _, 0, -1], "sus": [0.4, 0, 0.3, 0.3, 0.3, 0, 0.3, 0.4], "amp": [1.0, 0, 0.8, 0.8, 0.8, 0, 0.8, 1.0]},
            # Sparse menace
            {"degree": [0, 0, _, _, 0, 0, 0, _], "sus": [0.3, 0.3, 0, 0, 0.4, 0.3, 0.3, 0], "amp": [0.9, 0.8, 0, 0, 1.0, 0.8, 0.8, 0]},
            # Alternating root/-2
            {"degree": [0, -2, 0, _, 0, -2, _, 0], "sus": [0.3, 0.3, 0.3, 0, 0.3, 0.3, 0, 0.4], "amp": [0.9, 0.8, 0.9, 0, 0.9, 0.8, 0, 1.0]},
            # Double-time burst
            {"degree": [0, 0, -1, 0, _, 0, -2, _], "sus": [0.2, 0.2, 0.2, 0.3, 0, 0.2, 0.3, 0], "amp": [0.9, 0.8, 0.9, 0.9, 0, 0.8, 1.0, 0]},
        ],
        "lead": [
            # Narrow, cold, dissonant
            {"degree": [0, _, 1, 0, _, _, 0, 1], "sus": [0.1, 0, 0.1, 0.15, 0, 0, 0.1, 0.1], "amp": [0.8, 0, 0.7, 0.8, 0, 0, 0.7, 0.7]},
            # Chromatic creep
            {"degree": [0, 1, _, 0, _, 2, 1, _], "sus": [0.12, 0.1, 0, 0.15, 0, 0.1, 0.1, 0], "amp": [0.8, 0.7, 0, 0.8, 0, 0.7, 0.7, 0]},
            # Minimal stabs
            {"degree": [_, 0, 0, _, 1, _, 0, _], "sus": [0, 0.1, 0.12, 0, 0.1, 0, 0.15, 0], "amp": [0, 0.7, 0.8, 0, 0.7, 0, 0.8, 0]},
            # Descending chromatic
            {"degree": [2, 1, 0, _, _, 0, 1, 2], "sus": [0.1, 0.1, 0.12, 0, 0, 0.12, 0.1, 0.1], "amp": [0.7, 0.7, 0.8, 0, 0, 0.8, 0.7, 0.7]},
            # Sparse cold
            {"degree": [0, _, _, 0, 1, 0, _, _], "sus": [0.15, 0, 0, 0.12, 0.1, 0.15, 0, 0], "amp": [0.9, 0, 0, 0.7, 0.7, 0.8, 0, 0]},
        ],
        "stab": [
            # Power stab — sparse
            {"degree": [(0,3), _, _, _, (0,3), _, _, _], "sus": [0.05, 0, 0, 0, 0.05, 0, 0, 0], "amp": [1.0, 0, 0, 0, 0.9, 0, 0, 0]},
            # Offbeat power
            {"degree": [_, (0,3), _, _, _, _, (0,3), _], "sus": [0, 0.05, 0, 0, 0, 0, 0.05, 0], "amp": [0, 1.0, 0, 0, 0, 0, 0.9, 0]},
            # Triple hit
            {"degree": [(0,3), _, (0,3), _, _, _, _, (0,3)], "sus": [0.05, 0, 0.05, 0, 0, 0, 0, 0.05], "amp": [1.0, 0, 0.8, 0, 0, 0, 0, 0.9]},
        ],
    },

    # ========== MINIMAL ==========
    # Inspired by: Plastikman, Ricardo Villalobos, Robert Hood "Minus"
    "minimal": {
        "bass": [
            # Plastikman "Spastik" — one note, all variation from filter/amp
            {"degree": [0, 0, 0, 0, 0, 0, 0, 0], "sus": [0.1, 0.3, 0.1, 0.05, 0.1, 0.3, 0.1, 0.05], "amp": [0.8, 0.6, 0.5, 0.4, 0.7, 0.6, 0.5, 0.4]},
            # Robert Hood — extremely sparse
            {"degree": [0, _, _, _, _, 0, _, _], "sus": [0.3, 0, 0, 0, 0, 0.15, 0, 0], "amp": [0.7, 0, 0, 0, 0, 0.5, 0, 0]},
            # Two notes max
            {"degree": [0, _, _, 4, _, _, 0, _], "sus": [0.5, 0, 0, 0.3, 0, 0, 0.4, 0], "amp": [0.7, 0, 0, 0.5, 0, 0, 0.6, 0]},
            # Ultra sparse — 2 hits per bar
            {"degree": [0, _, _, _, _, _, _, 0], "sus": [0.6, 0, 0, 0, 0, 0, 0, 0.4], "amp": [0.7, 0, 0, 0, 0, 0, 0, 0.6]},
            # Single sub hit
            {"degree": [0, _, _, _, 4, _, _, _], "sus": [0.6, 0, 0, 0, 0.4, 0, 0, 0], "amp": [0.7, 0, 0, 0, 0.6, 0, 0, 0]},
            # Villalobos — offbeat
            {"degree": [_, 0, _, _, 0, _, _, _], "sus": [0, 0.5, 0, 0, 0.4, 0, 0, 0], "amp": [0, 0.7, 0, 0, 0.6, 0, 0, 0]},
        ],
        "lead": [
            # One long note
            {"degree": [0, _, _, _, _, _, _, _], "sus": [1.5, 0, 0, 0, 0, 0, 0, 0], "amp": [0.5, 0, 0, 0, 0, 0, 0, 0]},
            # Two held notes
            {"degree": [0, _, _, _, 2, _, _, _], "sus": [1.0, 0, 0, 0, 1.0, 0, 0, 0], "amp": [0.5, 0, 0, 0, 0.5, 0, 0, 0]},
            # Wide interval
            {"degree": [_, _, 4, _, _, _, 2, _], "sus": [0, 0, 1.2, 0, 0, 0, 1.0, 0], "amp": [0, 0, 0.5, 0, 0, 0, 0.5, 0]},
            # Ghost melody
            {"degree": [_, _, _, 2, _, _, _, _], "sus": [0, 0, 0, 1.0, 0, 0, 0, 0], "amp": [0, 0, 0, 0.4, 0, 0, 0, 0]},
        ],
        "arp": [
            # Minimal 2-note
            {"degree": [0, _, 2, _, 0, _, 2, _], "sus": [0.1, 0, 0.1, 0, 0.1, 0, 0.1, 0], "amp": [0.5, 0, 0.4, 0, 0.5, 0, 0.4, 0]},
            # Paired hits
            {"degree": [0, 2, _, _, 0, 2, _, _], "sus": [0.1, 0.1, 0, 0, 0.1, 0.1, 0, 0], "amp": [0.5, 0.4, 0, 0, 0.5, 0.4, 0, 0]},
            # Sparse 3-note
            {"degree": [0, _, _, 4, _, _, 2, _], "sus": [0.12, 0, 0, 0.12, 0, 0, 0.12, 0], "amp": [0.5, 0, 0, 0.5, 0, 0, 0.5, 0]},
        ],
        "pad": [
            # Static single chord
            {"degree": [(0,4,7), (0,4,7), (0,4,7), (0,4,7), (0,4,7), (0,4,7), (0,4,7), (0,4,7)], "sus": [4, 4, 4, 4, 4, 4, 4, 4], "amp": [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35]},
            # Simple triad
            {"degree": [(0,2,4), (0,2,4), (0,2,4), (0,2,4), (0,2,4), (0,2,4), (0,2,4), (0,2,4)], "sus": [4, 4, 4, 4, 4, 4, 4, 4], "amp": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
        ],
    },

    # ========== METAL ==========
    # Inspired by: Meshuggah, Tool, Iron Maiden, djent
    "metal": {
        "bass": [
            # Meshuggah polyrhythmic — 3+3+3+3+4 grouping
            {"degree": [0, 0, _, 0, 0, 0, _, 0, _, 0, 0, _, 0, 0, 0, _], "sus": [0.1, 0.1, 0, 0.1, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0], "amp": [1.0, 0.8, 0, 0.9, 0.8, 0.9, 0, 1.0, 0, 0.9, 0.8, 0, 1.0, 0.8, 0.9, 0]},
            # Iron Maiden gallop — short-short-long
            {"degree": [0, 0, 0, _, 0, 0, 0, _], "sus": [0.1, 0.08, 0.08, 0, 0.1, 0.08, 0.08, 0], "amp": [1.0, 0.8, 0.7, 0, 1.0, 0.8, 0.7, 0]},
            # Djent breakdown — chromatic drops
            {"degree": [0, 0, 0, _, 0, -1, 0, _, 0, 0, -2, _, 0, -1, -3, 0], "sus": [0.1, 0.1, 0.1, 0, 0.1, 0.12, 0.1, 0, 0.1, 0.1, 0.12, 0, 0.1, 0.12, 0.15, 0.1], "amp": [1.0, 0.8, 0.7, 0, 1.0, 0.9, 0.8, 0, 1.0, 0.8, 0.9, 0, 1.0, 0.9, 1.0, 0.8]},
            # Tool "Schism" — alternating meter feel
            {"degree": [0, _, 0, 3, _, 0, 4, 0, 3, _, 0, _], "sus": [0.2, 0, 0.3, 0.2, 0, 0.15, 0.4, 0.2, 0.2, 0, 0.3, 0], "amp": [0.9, 0, 0.8, 0.7, 0, 0.7, 0.9, 0.8, 0.7, 0, 0.8, 0]},
            # Power chord pummel
            {"degree": [(0,4), _, (0,4), _, (0,4), (0,4), _, _], "sus": [0.2, 0, 0.2, 0, 0.2, 0.15, 0, 0], "amp": [1.0, 0, 0.9, 0, 1.0, 0.9, 0, 0]},
            # Chromatic riff
            {"degree": [0, 0, -1, 0, 0, 0, -1, 0], "sus": [0.12, 0.12, 0.15, 0.12, 0.12, 0.12, 0.15, 0.15], "amp": [0.9, 0.8, 1.0, 0.9, 0.9, 0.8, 1.0, 0.9]},
            # Heavy power chords
            {"degree": [(0,4), (0,4), _, (0,4), _, (3,7), (3,7), _], "sus": [0.18, 0.15, 0, 0.18, 0, 0.18, 0.15, 0], "amp": [1.0, 0.9, 0, 1.0, 0, 1.0, 0.9, 0]},
            # Palm mute root
            {"degree": [0, 0, 0, _, 0, 0, 0, _], "sus": [0.08, 0.08, 0.08, 0, 0.08, 0.08, 0.08, 0], "amp": [0.9, 0.7, 0.8, 0, 0.9, 0.7, 0.8, 0]},
        ],
        "lead": [
            # Fast scalar run
            {"degree": [0, 2, 3, 5, 7, 5, 3, 0], "sus": [0.15, 0.12, 0.12, 0.12, 0.2, 0.12, 0.12, 0.2], "amp": [0.8, 0.7, 0.7, 0.8, 0.9, 0.7, 0.7, 0.8]},
            # Descending shred
            {"degree": [12, 11, 9, 7, 5, 3, 2, 0], "sus": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.15], "amp": [0.8, 0.8, 0.8, 0.8, 0.7, 0.7, 0.7, 0.9]},
            # Wide leap melody
            {"degree": [0, _, 7, 5, 3, 0, _, 0], "sus": [0.15, 0, 0.15, 0.12, 0.12, 0.2, 0, 0.15], "amp": [0.8, 0, 0.8, 0.7, 0.7, 0.9, 0, 0.8]},
            # Full range ascending
            {"degree": [0, 3, 5, 7, 9, 7, 5, 3], "sus": [0.12, 0.12, 0.12, 0.12, 0.15, 0.12, 0.12, 0.12], "amp": [0.7, 0.7, 0.7, 0.8, 0.9, 0.8, 0.7, 0.7]},
            # Phrased with rests
            {"degree": [7, 5, 3, 2, 0, _, 0, 2], "sus": [0.15, 0.12, 0.12, 0.12, 0.2, 0, 0.15, 0.15], "amp": [0.8, 0.7, 0.7, 0.7, 0.8, 0, 0.7, 0.8]},
        ],
        "pad": [
            # Power chord drone
            {"degree": [(0,4), (0,4), (0,4), (0,4), (3,7), (3,7), (3,7), (3,7)], "sus": [3, 3, 3, 3, 3, 3, 3, 3], "amp": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]},
            # Dark progression
            {"degree": [(0,3,7), (0,3,7), (-1,3,6), (-1,3,6), (0,3,7), (0,3,7), (0,4,7), (0,4,7)], "sus": [3, 3, 3, 3, 3, 3, 3, 3], "amp": [0.55, 0.55, 0.6, 0.6, 0.55, 0.55, 0.55, 0.55]},
        ],
    },

    # ========== DNB ==========
    # Inspired by: Roni Size, Goldie, Noisia, Sub Focus
    "dnb": {
        "bass": [
            # Classic Reese — sparse, sustained
            {"degree": [0, _, _, _, _, _, 0, _], "sus": [1.5, 0, 0, 0, 0, 0, 0.8, 0], "amp": [0.8, 0, 0, 0, 0, 0, 0.6, 0]},
            # Sub drone — single note per bar
            {"degree": [0, _, _, _, _, _, _, _], "sus": [3.0, 0, 0, 0, 0, 0, 0, 0], "amp": [0.8, 0, 0, 0, 0, 0, 0, 0]},
            # Reese with 5th movement
            {"degree": [0, _, _, 4, _, _, 0, _], "sus": [0.8, 0, 0, 0.8, 0, 0, 1.0, 0], "amp": [0.8, 0, 0, 0.6, 0, 0, 0.7, 0]},
            # Neurofunk — choppy rhythmic
            {"degree": [0, 0, _, 0, -2, _, 0, 3], "sus": [0.2, 0.15, 0, 0.3, 0.2, 0, 0.15, 0.2], "amp": [0.9, 0.7, 0, 0.8, 0.7, 0, 0.7, 0.8]},
            # Sub Focus — bouncy minor triad
            {"degree": [0, 0, 0, 4, 3, 0, _, 0], "sus": [0.3, 0.15, 0.15, 0.4, 0.3, 0.2, 0, 0.15], "amp": [0.8, 0.6, 0.6, 0.7, 0.7, 0.6, 0, 0.6]},
            # Two-note sub
            {"degree": [0, _, _, _, 0, _, _, _], "sus": [1.2, 0, 0, 0, 0.8, 0, 0, 0], "amp": [0.8, 0, 0, 0, 0.6, 0, 0, 0]},
        ],
        "lead": [
            # Offbeat jazzy
            {"degree": [_, 2, 3, _, 5, _, 3, 2], "sus": [0, 0.2, 0.25, 0, 0.35, 0, 0.25, 0.2], "amp": [0, 0.5, 0.6, 0, 0.7, 0, 0.6, 0.5]},
            # Syncopated
            {"degree": [0, _, 4, 2, _, 5, _, 3], "sus": [0.25, 0, 0.2, 0.2, 0, 0.3, 0, 0.25], "amp": [0.6, 0, 0.5, 0.5, 0, 0.7, 0, 0.6]},
            # Descending
            {"degree": [5, 4, _, 2, 0, _, 2, _], "sus": [0.25, 0.2, 0, 0.2, 0.35, 0, 0.2, 0], "amp": [0.7, 0.6, 0, 0.5, 0.7, 0, 0.5, 0]},
            # Melodic run
            {"degree": [_, _, 0, 2, 4, 6, 4, 2], "sus": [0, 0, 0.2, 0.2, 0.2, 0.25, 0.2, 0.2], "amp": [0, 0, 0.5, 0.5, 0.6, 0.7, 0.6, 0.5]},
        ],
        "pad": [
            # 7th chord atmo
            {"degree": [(0,2,4), (0,2,4), (0,2,4), (0,2,4), (2,4,6), (2,4,6), (2,4,6), (2,4,6)], "sus": [4, 4, 4, 4, 4, 4, 4, 4], "amp": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]},
            # Open voicing
            {"degree": [(0,4,7), (0,4,7), (0,4,7), (0,4,7), (3,5,7), (3,5,7), (3,5,7), (3,5,7)], "sus": [4, 4, 4, 4, 4, 4, 4, 4], "amp": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]},
        ],
    },

    # ========== DUB ==========
    # Inspired by: Robbie Shakespeare, Lee Scratch Perry, King Tubby, Scientist
    "dub": {
        "bass": [
            # Roots — beat 1 + "and of 2"
            {"degree": [0, _, _, 4, _, 0, _, _], "sus": [1.5, 0, 0, 0.8, 0, 1.2, 0, 0], "amp": [0.9, 0, 0, 0.6, 0, 0.8, 0, 0]},
            # King Tubby — spacious, 3 notes max
            {"degree": [0, _, _, _, 4, _, _, 3], "sus": [2.0, 0, 0, 0, 1.5, 0, 0, 1.0], "amp": [0.9, 0, 0, 0, 0.7, 0, 0, 0.6]},
            # Sub drone
            {"degree": [0, _, _, _, _, _, _, _], "sus": [3.0, 0, 0, 0, 0, 0, 0, 0], "amp": [0.9, 0, 0, 0, 0, 0, 0, 0]},
            # Scientist — descending stepwise
            {"degree": [0, _, 5, _, 4, _, 3, _], "sus": [1.0, 0, 0.8, 0, 1.0, 0, 0.6, 0], "amp": [0.9, 0, 0.7, 0, 0.8, 0, 0.6, 0]},
            # Two-note bounce
            {"degree": [0, _, _, _, 0, _, _, _], "sus": [1.5, 0, 0, 0, 1.5, 0, 0, 0], "amp": [0.9, 0, 0, 0, 0.7, 0, 0, 0]},
            # Offbeat sub
            {"degree": [_, _, 0, _, _, _, _, _], "sus": [0, 0, 3.0, 0, 0, 0, 0, 0], "amp": [0, 0, 0.9, 0, 0, 0, 0, 0]},
            # With 5th
            {"degree": [0, _, _, _, _, 4, _, _], "sus": [2.0, 0, 0, 0, 0, 0.8, 0, 0], "amp": [0.9, 0, 0, 0, 0, 0.6, 0, 0]},
        ],
        "lead": [
            # Sparse melodic
            {"degree": [_, _, 0, _, _, _, 2, _], "sus": [0, 0, 0.6, 0, 0, 0, 0.5, 0], "amp": [0, 0, 0.5, 0, 0, 0, 0.5, 0]},
            # Single note
            {"degree": [0, _, _, _, _, _, _, _], "sus": [1.2, 0, 0, 0, 0, 0, 0, 0], "amp": [0.5, 0, 0, 0, 0, 0, 0, 0]},
            # Wide interval
            {"degree": [_, _, _, 4, _, _, _, 2], "sus": [0, 0, 0, 0.7, 0, 0, 0, 0.6], "amp": [0, 0, 0, 0.5, 0, 0, 0, 0.5]},
        ],
        "stab": [
            # Offbeat skank
            {"degree": [_, (0,2,4), _, _, _, (0,2,4), _, _], "sus": [0, 0.1, 0, 0, 0, 0.1, 0, 0], "amp": [0, 0.7, 0, 0, 0, 0.7, 0, 0]},
            # Reggae chop
            {"degree": [_, (0,4), _, (0,4), _, _, _, (0,4)], "sus": [0, 0.08, 0, 0.08, 0, 0, 0, 0.08], "amp": [0, 0.7, 0, 0.6, 0, 0, 0, 0.7]},
        ],
    },

    # ========== EBM ==========
    # Inspired by: DAF, Nitzer Ebb, Front 242
    "ebm": {
        "bass": [
            # DAF "Der Mussolini" — mechanical sequence
            {"degree": [0, 0, 0, 0, 3, 3, 0, 0], "sus": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "amp": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]},
            # Nitzer Ebb — rhythmic single note
            {"degree": [0, _, 0, 0, _, 0, _, 0], "sus": [0.15, 0, 0.15, 0.15, 0, 0.15, 0, 0.15], "amp": [0.9, 0, 0.8, 0.8, 0, 0.8, 0, 0.8]},
            # Front 242 — arpeggiated sequence
            {"degree": [0, 3, 5, 3, 0, 3, 7, 5], "sus": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "amp": [0.8, 0.7, 0.7, 0.7, 0.8, 0.7, 0.7, 0.7]},
            # Minor movement
            {"degree": [0, 1, 3, 4, 0, 1, 3, 4], "sus": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], "amp": [0.8, 0.7, 0.7, 0.8, 0.8, 0.7, 0.7, 0.8]},
            # Gapped sequence
            {"degree": [0, 0, 3, _, 0, 0, 4, _], "sus": [0.3, 0.3, 0.3, 0, 0.3, 0.3, 0.3, 0], "amp": [0.8, 0.7, 0.7, 0, 0.8, 0.7, 0.7, 0]},
            # Alternating
            {"degree": [0, 3, 0, 4, 0, 3, 0, 1], "sus": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], "amp": [0.8, 0.7, 0.8, 0.7, 0.8, 0.7, 0.8, 0.7]},
            # Author & Punisher — chromatic industrial
            {"degree": [0, 0, _, -1, 0, _, _, -3], "sus": [0.3, 0.15, 0, 0.4, 0.3, 0, 0, 0.6], "amp": [1.0, 0.8, 0, 0.9, 0.8, 0, 0, 1.0]},
        ],
        "lead": [
            # Robotic arp
            {"degree": [0, 3, 5, 7, 0, 3, 5, 7], "sus": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "amp": [0.7, 0.6, 0.6, 0.7, 0.7, 0.6, 0.6, 0.7]},
            # Gapped arp
            {"degree": [0, 3, 5, _, 0, 3, 7, _], "sus": [0.2, 0.2, 0.2, 0, 0.2, 0.2, 0.2, 0], "amp": [0.7, 0.6, 0.6, 0, 0.7, 0.6, 0.7, 0]},
            # Descending
            {"degree": [7, 5, 3, 0, 7, 5, 3, 0], "sus": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "amp": [0.7, 0.6, 0.6, 0.7, 0.7, 0.6, 0.6, 0.7]},
            # Spaced
            {"degree": [0, _, 3, _, 5, _, 7, _], "sus": [0.25, 0, 0.25, 0, 0.25, 0, 0.25, 0], "amp": [0.7, 0, 0.6, 0, 0.6, 0, 0.7, 0]},
        ],
        "stab": [
            # On-beat hits
            {"degree": [(0,3), _, _, (0,3), _, _, (0,3), _], "sus": [0.08, 0, 0, 0.08, 0, 0, 0.08, 0], "amp": [0.9, 0, 0, 0.8, 0, 0, 0.8, 0]},
            # Offbeat
            {"degree": [_, (0,4), _, _, (0,4), _, _, _], "sus": [0, 0.08, 0, 0, 0.08, 0, 0, 0], "amp": [0, 0.9, 0, 0, 0.8, 0, 0, 0]},
        ],
    },

    # ========== ACID ==========
    # Inspired by: Phuture, Hardfloor, DJ Pierre
    "acid": {
        "bass": [
            # Phuture "Acid Tracks" — with slide sustains
            {"degree": [0, 0, 3, 0, 5, _, 3, 0], "sus": [0.5, 0.15, 0.8, 0.15, 0.5, 0, 0.3, 0.15], "amp": [1.0, 0.5, 0.9, 0.5, 1.0, 0, 0.7, 0.5]},
            # Hardfloor "Acperience" — octave jump
            {"degree": [0, 0, 7, 0, 5, 3, 0, 5], "sus": [0.15, 0.15, 0.6, 0.15, 0.4, 0.3, 0.15, 0.5], "amp": [1.0, 0.5, 0.9, 0.5, 0.8, 0.7, 0.5, 0.8]},
            # Wild acid — wide range
            {"degree": [0, 7, 0, 5, 0, 3, 7, _], "sus": [0.15, 0.7, 0.15, 0.5, 0.15, 0.4, 0.8, 0], "amp": [0.8, 0.9, 0.7, 0.8, 0.7, 0.7, 0.9, 0]},
            # Bouncing — root + 3rd + 5th
            {"degree": [0, 3, 5, 3, 0, 3, 5, 7], "sus": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "amp": [0.8, 0.7, 0.7, 0.6, 0.8, 0.7, 0.7, 0.8]},
            # Squelch — filter does the work
            {"degree": [0, 0, 0, 5, 3, 0, 0, 7], "sus": [0.15, 0.15, 0.15, 0.3, 0.2, 0.15, 0.15, 0.3], "amp": [0.7, 0.6, 0.6, 0.8, 0.7, 0.6, 0.6, 0.8]},
            # Classic slide pattern
            {"degree": [0, _, 0, 3, _, 5, 0, _], "sus": [0.3, 0, 0.2, 0.2, 0, 0.3, 0.2, 0], "amp": [0.8, 0, 0.6, 0.7, 0, 0.8, 0.6, 0]},
            # DJ Pierre — chromatic
            {"degree": [0, 3, 0, 5, 7, 5, 3, 0], "sus": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "amp": [0.8, 0.7, 0.7, 0.7, 0.8, 0.7, 0.7, 0.7]},
            # With rests
            {"degree": [0, 0, _, 3, 5, 7, _, 0], "sus": [0.2, 0.2, 0, 0.2, 0.2, 0.3, 0, 0.2], "amp": [0.7, 0.6, 0, 0.7, 0.7, 0.8, 0, 0.7]},
        ],
    },

    # ========== AMBIENT ==========
    # Inspired by: Brian Eno, Stars of the Lid, Aphex Twin SAW2, Biosphere
    "ambient": {
        "pad": [
            # Eno "Music for Airports" — triads a third apart
            {"degree": [(0,2,4), (0,2,4), (0,2,4), (0,2,4), (2,4,6), (2,4,6), (2,4,6), (2,4,6)], "sus": [8, 8, 8, 8, 8, 8, 8, 8], "amp": [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35]},
            # Stars of the Lid — close voicing with one note shift
            {"degree": [(0,2,4,7), (0,2,4,7), (0,2,4,7), (0,2,4,7), (0,2,5,7), (0,2,5,7), (0,2,5,7), (0,2,5,7)], "sus": [8, 8, 8, 8, 8, 8, 8, 8], "amp": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
            # Aphex SAW2 — shifting chords
            {"degree": [(0,4,7), (0,4,7), (0,4,7), (0,4,7), (0,5,9), (0,5,9), (0,5,9), (0,5,9)], "sus": [6, 6, 6, 6, 6, 6, 6, 6], "amp": [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35]},
            # Biosphere — open 5ths, no thirds
            {"degree": [(0,4), _, _, (2,5), _, _, _, _], "sus": [6, 0, 0, 6, 0, 0, 0, 0], "amp": [0.35, 0, 0, 0.35, 0, 0, 0, 0]},
            # Deep 4-note chords
            {"degree": [(0,4,7,11), (0,4,7,11), (0,4,7,11), (0,4,7,11), (2,5,9,12), (2,5,9,12), (2,5,9,12), (2,5,9,12)], "sus": [8, 8, 8, 8, 8, 8, 8, 8], "amp": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
            # Wide voicing
            {"degree": [(0,2,7), (0,2,7), (0,2,7), (0,2,7), (2,5,9), (2,5,9), (2,5,9), (2,5,9)], "sus": [6, 6, 6, 6, 6, 6, 6, 6], "amp": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
        ],
        "lead": [
            # Single held note
            {"degree": [0, _, _, _, _, _, _, _], "sus": [3.0, 0, 0, 0, 0, 0, 0, 0], "amp": [0.4, 0, 0, 0, 0, 0, 0, 0]},
            # Wide interval pair
            {"degree": [7, _, _, _, _, _, _, 4], "sus": [2.0, 0, 0, 0, 0, 0, 0, 2.0], "amp": [0.35, 0, 0, 0, 0, 0, 0, 0.35]},
            # Ghost note
            {"degree": [_, _, _, _, 4, _, _, _], "sus": [0, 0, 0, 0, 2.0, 0, 0, 0], "amp": [0, 0, 0, 0, 0.4, 0, 0, 0]},
        ],
        "arp": [
            # Slow wide
            {"degree": [0, _, 4, _, 7, _, 4, _], "sus": [0.4, 0, 0.4, 0, 0.4, 0, 0.4, 0], "amp": [0.35, 0, 0.3, 0, 0.35, 0, 0.3, 0]},
            # With 11th
            {"degree": [0, 7, _, 4, _, 7, 11, _], "sus": [0.4, 0.4, 0, 0.4, 0, 0.4, 0.4, 0], "amp": [0.35, 0.3, 0, 0.3, 0, 0.3, 0.35, 0]},
        ],
    },

    # ========== INDUSTRIAL ==========
    # Inspired by: Author & Punisher, Godflesh, HEALTH
    "industrial": {
        "bass": [
            # Relentless root — no variation
            {"degree": [0, 0, 0, 0, 0, 0, 0, 0], "sus": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "amp": [1.0, 0.9, 1.0, 0.9, 1.0, 0.9, 1.0, 0.9]},
            # Gapped relentless
            {"degree": [0, 0, 0, _, 0, 0, 0, _], "sus": [0.2, 0.2, 0.2, 0, 0.2, 0.2, 0.2, 0], "amp": [1.0, 0.9, 1.0, 0, 1.0, 0.9, 1.0, 0]},
            # Chromatic crush
            {"degree": [0, 0, _, -1, 0, _, _, -3], "sus": [0.3, 0.15, 0, 0.4, 0.3, 0, 0, 0.6], "amp": [1.0, 0.8, 0, 0.9, 0.8, 0, 0, 1.0]},
            # Semitone alternation
            {"degree": [0, -1, 0, _, -1, 0, 0, _], "sus": [0.2, 0.2, 0.2, 0, 0.2, 0.2, 0.2, 0], "amp": [1.0, 0.9, 1.0, 0, 0.9, 1.0, 0.9, 0]},
            # Chromatic descent
            {"degree": [0, 0, -1, 0, 0, -1, 0, 0], "sus": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "amp": [1.0, 0.9, 0.9, 1.0, 0.9, 0.9, 1.0, 0.9]},
            # Syncopated
            {"degree": [0, _, 0, 0, _, 0, 0, 0], "sus": [0.25, 0, 0.2, 0.2, 0, 0.2, 0.2, 0.25], "amp": [1.0, 0, 0.9, 0.9, 0, 0.9, 0.9, 1.0]},
        ],
        "lead": [
            # Narrow chromatic
            {"degree": [0, 1, _, 0, _, _, 1, _], "sus": [0.12, 0.1, 0, 0.12, 0, 0, 0.1, 0], "amp": [0.8, 0.7, 0, 0.8, 0, 0, 0.7, 0]},
            # Offbeat stabs
            {"degree": [_, 0, 1, 0, _, 0, _, 1], "sus": [0, 0.12, 0.1, 0.12, 0, 0.12, 0, 0.1], "amp": [0, 0.8, 0.7, 0.8, 0, 0.8, 0, 0.7]},
            # Sparse
            {"degree": [0, _, 0, _, 1, _, 0, _], "sus": [0.15, 0, 0.15, 0, 0.12, 0, 0.15, 0], "amp": [0.8, 0, 0.7, 0, 0.7, 0, 0.8, 0]},
        ],
        "stab": [
            # Double hit
            {"degree": [(0,3), (0,3), _, _, (0,3), (0,3), _, _], "sus": [0.05, 0.05, 0, 0, 0.05, 0.05, 0, 0], "amp": [1.0, 0.9, 0, 0, 1.0, 0.9, 0, 0]},
            # Spaced power
            {"degree": [(0,4), _, _, (0,4), _, _, (0,4), _], "sus": [0.06, 0, 0, 0.06, 0, 0, 0.06, 0], "amp": [1.0, 0, 0, 0.9, 0, 0, 1.0, 0]},
        ],
    },

    # ========== IDM ==========
    # Inspired by: Autechre, Aphex Twin, Boards of Canada, Squarepusher
    "idm": {
        "bass": [
            # Autechre — irregular intervals
            {"degree": [0, _, 3, _, _, 2, _, 5], "sus": [0.4, 0, 0.3, 0, 0, 0.3, 0, 0.4], "amp": [0.7, 0, 0.5, 0, 0, 0.5, 0, 0.7]},
            # Squarepusher — jazz-influenced fast
            {"degree": [0, 3, 5, 7, 5, 0, -2, 0], "sus": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.12, 0.1], "amp": [0.7, 0.6, 0.6, 0.7, 0.6, 0.6, 0.7, 0.6]},
            # Irregular
            {"degree": [_, 0, _, 4, 2, _, _, 0], "sus": [0, 0.4, 0, 0.3, 0.3, 0, 0, 0.5], "amp": [0, 0.7, 0, 0.5, 0.5, 0, 0, 0.7]},
            # Broken
            {"degree": [_, _, 0, _, 3, 5, _, 2], "sus": [0, 0, 0.5, 0, 0.3, 0.3, 0, 0.3], "amp": [0, 0, 0.7, 0, 0.5, 0.6, 0, 0.5]},
        ],
        "lead": [
            # Aphex "Windowlicker" — scalar melodic
            {"degree": [0, 2, 4, 7, 5, 4, 2, 0], "sus": [0.3, 0.3, 0.3, 0.6, 0.3, 0.3, 0.3, 0.5], "amp": [0.6, 0.5, 0.6, 0.8, 0.6, 0.5, 0.5, 0.7]},
            # BoC — parallel thirds, nostalgic
            {"degree": [(0,2), (4,6), (2,4), (5,7), (0,2), (3,5), (2,4), _], "sus": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0], "amp": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0]},
            # Wide leaps
            {"degree": [7, _, 3, 5, _, 0, _, 9], "sus": [0.2, 0, 0.15, 0.2, 0, 0.3, 0, 0.2], "amp": [0.6, 0, 0.5, 0.6, 0, 0.7, 0, 0.6]},
            # Broken run
            {"degree": [_, 2, 5, _, 9, 7, 3, _], "sus": [0, 0.15, 0.2, 0, 0.2, 0.15, 0.15, 0], "amp": [0, 0.5, 0.6, 0, 0.7, 0.6, 0.5, 0]},
        ],
        "arp": [
            # Irregular cell
            {"degree": [0, 4, 7, 0, 2, 7, 4, 0], "sus": [0.1, 0.12, 0.1, 0.1, 0.12, 0.1, 0.12, 0.1], "amp": [0.6, 0.5, 0.5, 0.6, 0.5, 0.5, 0.5, 0.6]},
            # With rests
            {"degree": [0, _, 7, 4, _, 2, 0, _], "sus": [0.12, 0, 0.1, 0.12, 0, 0.12, 0.1, 0], "amp": [0.6, 0, 0.5, 0.6, 0, 0.5, 0.5, 0]},
        ],
    },
}


# ============================================================
# NAMED PATTERN CODES
# ============================================================

_named = {}
_prefixes = {
    "techno": "t", "gesaffelstein": "g", "minimal": "m", "metal": "mt",
    "dnb": "d", "dub": "du", "ebm": "e", "acid": "ac",
    "ambient": "am", "industrial": "i", "idm": "id",
}
_role_prefixes = {
    "bass": "b", "lead": "l", "pad": "p", "arp": "a", "stab": "s",
}

def _build_named():
    for genre, gprefix in _prefixes.items():
        for role, rprefix in _role_prefixes.items():
            patterns = _patterns.get(genre, {}).get(role, [])
            for i, pat in enumerate(patterns):
                code = f"{gprefix}{rprefix}{i+1}"
                _named[code] = pat

_build_named()


# ============================================================
# MELODY STRING — degree list with .sus and .amp access
# ============================================================

class MelodyPattern(list):
    """A list of degrees that also carries sus and amp patterns."""

    def __init__(self, degrees, sus=None, amp=None):
        super().__init__(degrees)
        self._sus = sus or [0.3] * len(degrees)
        self._amp = amp or [0.7] * len(degrees)

    @property
    def sus(self):
        return self._sus

    @property
    def amp(self):
        return self._amp


# ============================================================
# PUBLIC API
# ============================================================

def gen(genre="techno", role="bass", evolve=1, idx=None, seed=None):
    """Generate a melody/bass/pad/arp degree pattern.

    Args:
        genre:  techno, gesaffelstein, minimal, metal, dnb, dub, ebm, acid, ambient, industrial, idm
        role:   bass, lead, pad, arp, stab
        evolve: bars of evolution (1=static, default)
        idx:    specific pattern index (None=random)
        seed:   random seed for reproducibility

    Returns a MelodyPattern (list with .sus and .amp).
    e.g. b1 >> tekno(gen("techno", "bass"), dur=0.5, oct=3)
         b1 >> tekno(gen("techno", "bass"), dur=0.5, sus=gen("techno", "bass").sus)
    """
    rng = random.Random(seed)
    patterns = _patterns.get(genre, {}).get(role, [])
    if not patterns:
        return MelodyPattern([0], [0.3], [0.7])

    if idx is not None:
        pat = patterns[idx % len(patterns)]
    else:
        pat = rng.choice(patterns)

    degrees = list(pat["degree"])
    sus = list(pat["sus"])
    amp = list(pat["amp"])

    # Scale sus by role — stored values are normalized, multiply for musical range
    _sus_scale = {
        "bass": 2.5,   # bass needs weight: 0.3 → 0.75, 0.5 → 1.25
        "lead": 2.0,   # leads need breath: 0.2 → 0.4, 0.5 → 1.0
        "pad": 1.0,    # pads already have long sus values
        "arp": 1.5,    # arps slightly longer: 0.12 → 0.18
        "stab": 1.0,   # stabs should stay short
    }
    scale = _sus_scale.get(role, 1.5)
    sus = [s * scale if s > 0 else 0 for s in sus]

    if evolve <= 1:
        return MelodyPattern(degrees, sus, amp)

    # Evolve by concatenation — mutate per bar
    all_deg = list(degrees)
    all_sus = list(sus)
    all_amp = list(amp)
    step_len = len(degrees)

    for bar in range(1, evolve):
        # Mutate: small changes to the previous bar
        deg = list(degrees)
        s = list(sus)
        a = list(amp)
        for _ in range(2):
            pos = rng.randint(0, step_len - 1)
            action = rng.choice(["shift", "rest", "unrest", "swap"])
            if action == "shift" and deg[pos] is not None:
                deg[pos] = max(0, deg[pos] + rng.choice([-1, 1, -2, 2]))
            elif action == "rest" and deg[pos] is not None:
                deg[pos] = None
                s[pos] = 0
                a[pos] = 0
            elif action == "unrest" and deg[pos] is None:
                deg[pos] = rng.choice([0, 2, 3, 4, 5])
                s[pos] = rng.choice([0.2, 0.3, 0.4])
                a[pos] = rng.choice([0.5, 0.6, 0.7])
            elif action == "swap" and pos < step_len - 1:
                deg[pos], deg[pos+1] = deg[pos+1], deg[pos]
                s[pos], s[pos+1] = s[pos+1], s[pos]
                a[pos], a[pos+1] = a[pos+1], a[pos]
        degrees = deg
        all_deg.extend(deg)
        all_sus.extend(s)
        all_amp.extend(a)

    return MelodyPattern(all_deg, all_sus, all_amp)


def gp(code):
    """Get a specific named melody pattern.

    Codes: {genre}{role}{number}
        tb1  = techno bass 1
        tl3  = techno lead 3
        gb2  = gesaffelstein bass 2
        ml1  = metal lead 1
        db1  = dnb bass 1
        etc.

    e.g. b1 >> tekno(gp("tb3"), dur=0.5, oct=3)
    """
    if code in _named:
        pat = _named[code]
        return MelodyPattern(list(pat["degree"]), list(pat["sus"]), list(pat["amp"]))
    available = sorted(_named.keys())
    print(f"Unknown pattern '{code}'. Available: {', '.join(available[:20])}...")
    return MelodyPattern([0], [0.3], [0.7])


def gen_genres():
    """List available genres"""
    return list(_patterns.keys())

def gen_roles(genre="techno"):
    """List available roles for a genre"""
    return list(_patterns.get(genre, {}).keys())

def gen_show(genre="techno", role="bass"):
    """Print all patterns for a genre/role"""
    patterns = _patterns.get(genre, {}).get(role, [])
    gprefix = _prefixes.get(genre, "?")
    rprefix = _role_prefixes.get(role, "?")
    for i, pat in enumerate(patterns):
        code = f"{gprefix}{rprefix}{i+1}"
        print(f"{code}: degree={pat['degree']}")
        print(f"     sus={pat['sus']}")
        print(f"     amp={pat['amp']}")
