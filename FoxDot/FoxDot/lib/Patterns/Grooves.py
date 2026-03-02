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
    ''' Returns alternating [0, amount] swing delay pattern.
        `amount`: swing offset (default 0.1)
        `steps`: pattern length (default 8)
        e.g. `delay=PSwing(0.4, 16)` '''
    return Pattern([0, amount] * (steps // 2))


# Accent type templates (indexed by number)
_accent_types = {
    # 0: Backbeat accents on 2 and 4
    0: [0.6, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4,
        0.6, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4],

    # 1: Four on the floor
    1: [1.0, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4,
        1.0, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4],

    # 2: Offbeat accents
    2: [0.4, 0.4, 1.0, 0.4, 0.4, 0.4, 1.0, 0.4,
        0.4, 0.4, 1.0, 0.4, 0.4, 0.4, 1.0, 0.4],

    # 3: Ghost notes
    3: [1.0, 0.25, 0.3, 0.25, 0.7, 0.25, 0.3, 0.25,
        1.0, 0.25, 0.3, 0.25, 0.7, 0.25, 0.3, 0.25],
}

def Pacc(ptype=0, steps=16):
    ''' Returns accent amplify values (0-1) for a given type.
        `ptype`: 0=backbeat, 1=four_floor, 2=offbeat, 3=ghost
        `steps`: pattern length (default 16)
        e.g. `amp=Pacc(0)` backbeat
             `amp=Pacc(3)` ghost notes
             `amplify=Pacc(2, 4)` offbeat, 4-step grid '''
    if ptype not in _accent_types:
        ptype = 0
    template = _accent_types[ptype]
    data = [template[i % len(template)] for i in range(steps)]
    return Pattern(data)
