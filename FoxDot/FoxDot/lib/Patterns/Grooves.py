"""
Grooves.py
----------
Swing and accent pattern factories.

PSwing -- Swing delay pattern
Pacc   -- Accent patterns by type number

"""

from __future__ import absolute_import, division, print_function

from .Main import Pattern


def PSwing(amount=0.1, steps=8):
    ''' Alternating high/low swing pattern — works on any param.
        On-beats get 1.0, off-beats get (1 - amount), with subtle variation.
        `amount`: swing depth 0.0 (flat) to 1.0 (maximum contrast)
        `steps`: pattern length (default 8)
        e.g. `delay=PSwing(0.15)`    — offbeats slightly delayed
             `amplify=PSwing(0.3)`   — offbeats softer
             `sus=PSwing(0.2)`       — offbeats shorter
             `dur=0.5*PSwing(0.25)`  — shuffle feel '''
    data = []
    variation = [1.0, 0.85, 0.95, 0.75]
    for i in range(steps // 2):
        v = amount * variation[i % 4]
        data.extend([1.0, 1.0 - v])
    return Pattern(data)


# Accent templates: values are relative (1.0 = full accent, 0.0 = silent)
_accent_types = {
    # 0 / "backbeat": accents on 2 and 4
    0: [0.6, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4,
        0.6, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4],

    # 1 / "fourfloor": four on the floor
    1: [1.0, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4,
        1.0, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4],

    # 2 / "offbeat": accents on the and
    2: [0.4, 0.4, 1.0, 0.4, 0.4, 0.4, 1.0, 0.4,
        0.4, 0.4, 1.0, 0.4, 0.4, 0.4, 1.0, 0.4],

    # 3 / "ghost": ghost notes with strong downbeats
    3: [1.0, 0.25, 0.3, 0.25, 0.7, 0.25, 0.3, 0.25,
        1.0, 0.25, 0.3, 0.25, 0.7, 0.25, 0.3, 0.25],

    # 4 / "synco": syncopated — accents off the grid
    4: [0.4, 0.4, 1.0, 0.4, 0.4, 1.0, 0.4, 0.4,
        1.0, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 1.0],

    # 5 / "tresillo": 3+3+2 grouping
    5: [1.0, 0.3, 0.3, 1.0, 0.3, 0.3, 1.0, 0.3,
        1.0, 0.3, 0.3, 1.0, 0.3, 0.3, 1.0, 0.3],

    # 6 / "halftime": accent every other bar
    6: [1.0, 0.3, 0.5, 0.3, 0.7, 0.3, 0.5, 0.3,
        0.5, 0.3, 0.4, 0.3, 0.6, 0.3, 0.4, 0.3],
}

_accent_names = {
    "backbeat": 0, "fourfloor": 1, "offbeat": 2, "ghost": 3,
    "synco": 4, "tresillo": 5, "halftime": 6,
}

def Pacc(ptype=0, steps=16, intensity=1.0):
    ''' Accent pattern for amplify/amp.
        `ptype`: 0-6 or name: backbeat, fourfloor, offbeat,
                 ghost, synco, tresillo, halftime
        `steps`: pattern length (default 16)
        `intensity`: 0.0 (flat) to 1.0 (full contrast)
        e.g. `amp=Pacc("ghost")`
             `amp=Pacc("tresillo", 8)`
             `amp=Pacc(3, intensity=0.5)` — subtle ghost '''
    if isinstance(ptype, str):
        ptype = _accent_names.get(ptype.lower(), 0)
    if ptype not in _accent_types:
        ptype = 0
    template = _accent_types[ptype]
    if intensity >= 1.0:
        data = [template[i % len(template)] for i in range(steps)]
    else:
        # Blend toward flat (all 0.7) based on intensity
        flat = 0.7
        data = [flat + (template[i % len(template)] - flat) * intensity
                for i in range(steps)]
    return Pattern(data)
