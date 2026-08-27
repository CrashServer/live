"""
Advanced.py
-----------
Advanced pattern generators: growing arpeggios, polyrhythms, odd meters,
chord-aware melodies, groove templates and articulation.

PGrowArp      -- Arpeggio that gains a note every N beats
PPoly         -- Classic n-over-m polyrhythm durations
PPolyEuclid   -- Two Euclidean rhythms as a polyrhythm
PPolyPhase    -- Steve Reich style phase shifting
PAdditive     -- Additive / Balkan odd meters (7/8, 9/8, 11/8)
PMelody       -- Chord-aware melody generator
PCircle       -- Circle of fifths progression
PGroove       -- Genre groove templates
PClave        -- Traditional clave patterns
PSustain      -- Sustain derived from a duration pattern
PArticulation -- Standard musical articulations

"""

from __future__ import absolute_import, division, print_function

import random as _random

from .Main import Pattern
from .PGroups import PGroup
from .Sequences import PEuclid

__all__ = [
    "PGrowArp", "PPoly", "PPolyEuclid", "PPolyPhase", "PAdditive",
    "PMelody", "PCircle", "PGroove", "PClave", "PSustain", "PArticulation",
]


# --- helpers --------------------------------------------------------------

def _onsets(bits):
    """Indices of the 1s in a 1/0 list."""
    return [i for i, v in enumerate(bits) if v]


def _onsets_to_durs(onsets, steps, unit=0.25):
    """Gaps between onsets (wrapping at `steps`), scaled by `unit`."""
    if not onsets:
        return Pattern([steps * unit])
    durs = []
    for i, o in enumerate(onsets):
        nxt = onsets[i + 1] if i + 1 < len(onsets) else onsets[0] + steps
        durs.append((nxt - o) * unit)
    return Pattern(durs)


def _arp_notes(root, n, direction):
    """The first `n` notes of a growing arpeggio."""
    if direction == "down":
        return [root - i for i in range(n)]
    if direction == "diverge":
        out, step = [root], 1
        while len(out) < n:
            out.append(root + step)
            if len(out) < n:
                out.append(root - step)
            step += 1
        return out[:n]
    if direction == "random":
        pool = list(range(root - 3, root + 8))
        return [root] + [_random.choice(pool) for _ in range(n - 1)]
    return [root + i for i in range(n)]          # 'up' (default)


# --- growing patterns -----------------------------------------------------

def PGrowArp(root=0, max_notes=6, growth_rate=8, direction="up"):
    """ An arpeggio that gains one note every `growth_rate` BEATS, up to
        `max_notes`, then loops back to a single note.

        `root`        -- starting degree
        `max_notes`   -- notes in the final arpeggio (1-12)
        `growth_rate` -- beats each stage lasts before growing
        `direction`   -- 'up', 'down', 'diverge' or 'random'

        Growth is beat-accurate (built on Pvar), so it stays in step with the
        Clock no matter what `dur` the player uses.

        e.g. `p1 >> pluck(PGrowArp(0, max_notes=6, growth_rate=8), dur=1/2)`
             `p2 >> bass(PGrowArp(4, 5, 8, 'down'), dur=1/2, oct=4)`
             `p3 >> bell(PGrowArp(2, 7, 4, 'diverge'), dur=1/4, oct=6)` """
    from ..TimeVar import Pvar                    # lazy: TimeVar imports Patterns
    max_notes = max(1, int(max_notes))
    stages = [Pattern(_arp_notes(root, n, direction))
              for n in range(1, max_notes + 1)]
    return Pvar(stages, growth_rate)


# --- polyrhythm -----------------------------------------------------------

def PPoly(over, under, mode="duration"):
    """ Classic polyrhythm: play `over` notes evenly across `under` beats.

        `mode`: 'duration' -- durations for the `over` grid (default)
                'merged'   -- both grids merged into one onset pattern
                'delay'    -- onset offsets of the `over` grid

        e.g. `p1 >> pluck([0,2,4], dur=PPoly(3, 4))`      # 3 over 4
             `b1 >> bass([0,3,5], dur=PPoly(5, 4), oct=3)` """
    over, under = max(1, int(over)), float(under)
    if mode == "duration":
        return Pattern([round(under / over, 6)] * over)
    step = under / over
    if mode == "delay":
        return Pattern([round(i * step, 6) for i in range(over)])
    if mode == "merged":
        grid = sorted(set([round(i * step, 6) for i in range(over)]
                          + [float(i) for i in range(int(under))]))
        durs = [round(grid[i + 1] - grid[i], 6) for i in range(len(grid) - 1)]
        durs.append(round(under - grid[-1], 6))
        return Pattern([d for d in durs if d > 0])
    raise ValueError("PPoly: mode must be 'duration', 'merged' or 'delay'")


def PPolyEuclid(hits1, steps1, hits2, steps2, mode="dual", unit=0.25):
    """ Two Euclidean rhythms combined into a polyrhythm.

        `mode`: 'dual'      -- returns (durs1, durs2), one per player
                'merge'     -- union of both onset grids
                'offset'    -- second pattern rotated by half its length
                'alternate' -- one cycle of each, back to back

        e.g. `d1durs, d2durs = PPolyEuclid(3, 8, 5, 8)`
             `d1 >> play("x", dur=d1durs)`
             `d2 >> play("-", dur=d2durs)` """
    b1 = list(PEuclid(hits1, steps1))
    b2 = list(PEuclid(hits2, steps2))
    o1, o2 = _onsets(b1), _onsets(b2)

    if mode == "dual":
        return _onsets_to_durs(o1, steps1, unit), _onsets_to_durs(o2, steps2, unit)
    if mode == "alternate":
        return _onsets_to_durs(o1, steps1, unit) | _onsets_to_durs(o2, steps2, unit)
    if mode == "offset":
        shift = steps2 // 2
        o2 = sorted(((o + shift) % steps2) for o in o2)
        return _onsets_to_durs(o1, steps1, unit), _onsets_to_durs(o2, steps2, unit)
    if mode == "merge":
        steps = max(steps1, steps2)
        merged = sorted(set([o * steps / steps1 for o in o1]
                            + [o * steps / steps2 for o in o2]))
        return _onsets_to_durs([int(round(m)) for m in merged], steps, unit)
    raise ValueError("PPolyEuclid: mode must be 'dual', 'merge', 'offset' or 'alternate'")


def PPolyPhase(pattern, ratios=(1, 1.05), length=32):
    """ Steve Reich style phasing: the same pattern read at slightly different
        rates, stacked as PGroups so the voices drift against each other.

        `pattern` -- the material to phase
        `ratios`  -- read-rate per voice, e.g. [1, 1.05, 1.1]
        `length`  -- how many steps to generate

        e.g. `p1 >> pluck(PPolyPhase(P[0,2,4,7,4,2], [1, 1.05]), dur=1/4)` """
    src = list(pattern)
    if not src:
        return Pattern([])
    out = []
    for i in range(int(length)):
        voices = tuple(src[int(i * r) % len(src)] for r in ratios)
        out.append(voices[0] if len(voices) == 1 else PGroup(voices))
    return Pattern(out)


def PAdditive(*subdivisions, **kwargs):
    """ Additive (Balkan / odd) meters. Each argument is a group length in
        `unit` steps; the groups become durations.

        `unit` -- length of one step in beats (default 0.5, an eighth note)

        e.g. `PAdditive(2, 2, 3)`       # 7/8
             `PAdditive(2, 2, 2, 3)`    # 9/8
             `PAdditive(3, 3, 3, 2)`    # 11/8 Bulgarian
             `d1 >> play("x-o", dur=PAdditive(2, 2, 3))` """
    unit = kwargs.get("unit", 0.5)
    if len(subdivisions) == 1 and isinstance(subdivisions[0], (list, tuple)):
        subdivisions = tuple(subdivisions[0])
    if not subdivisions:
        subdivisions = (2, 2, 3)
    return Pattern([s * unit for s in subdivisions])


# --- melodic --------------------------------------------------------------

def PMelody(chord=None, style=0, length=16, seed=None):
    """ Generate a melody that leans on the notes of `chord`.

        `chord`  -- PGroup/list of scale degrees (default I, i.e. (0, 2, 4))
        `style`  -- 0 chord tones only        3 scalic motion
                    1 chord tones + passing   4 random walk favouring chord tones
                    2 chromatic approaches    5 broken chord
        `length` -- number of notes
        `seed`   -- optional int for a repeatable result

        e.g. `p1 >> pluck(PMelody(I, style=1, length=16), dur=1/4)`
             `p2 >> piano(PMelody([0,2,4], style=3), dur=1/2)` """
    rng = _random.Random(seed)
    if chord is None:
        chord = [0, 2, 4]
    tones = [int(t) for t in list(chord)]
    if not tones:
        tones = [0]
    lo, hi = min(tones), max(tones)
    out, cur = [], tones[0]

    for i in range(int(length)):
        if style == 0:
            out.append(tones[i % len(tones)])
        elif style == 1:
            out.append(tones[i % len(tones)] if i % 2 == 0
                       else rng.choice(tones) + rng.choice([-1, 1]))
        elif style == 2:
            t = tones[i % len(tones)]
            out.append(t if i % 2 == 0 else t - 0.5)
        elif style == 3:
            out.append(lo + (i % max(1, (hi - lo + 1))))
        elif style == 4:
            cur = cur + rng.choice([-2, -1, 1, 2])
            if rng.random() < 0.4:
                cur = min(tones, key=lambda t: abs(t - cur))
            out.append(cur)
        elif style == 5:
            order = [0, 2, 1] if len(tones) > 2 else list(range(len(tones)))
            out.append(tones[order[i % len(order)] % len(tones)])
        else:
            raise ValueError("PMelody: style must be 0-5")
    return Pattern(out)


def PCircle(start=0, steps=8, direction=1, wrap=True):
    """ Circle of fifths progression as scale degrees. Each step moves a fifth
        (4 degrees in a 7-note scale); `direction=-1` goes counter-clockwise
        (circle of fourths).

        `wrap` -- True (default) folds every root back into one octave, so the
                  progression circles as it should: 0, 4, 1, 5, 2, 6, 3, 0.
                  Set False to let it climb by a literal fifth each time.

        e.g. `p1 >> pads(PCircle(0, steps=8), dur=8, sus=7.5)`
             `p2 >> keys(PCircle(0, 4, direction=-1), dur=4)` """
    if isinstance(start, (list, tuple, PGroup)):
        start = int(list(start)[0])
    out = [int(start) + 4 * i * direction for i in range(int(steps))]
    if wrap:
        out = [v % 7 for v in out]
    return Pattern(out)


# --- groove & clave -------------------------------------------------------

_GROOVES = {
    "funk":      [1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0],
    "afrobeat":  [1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1],
    "breakbeat": [1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0],
    "techno":    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
    "dnb":       [1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0],
    "trap":      [1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0],
    "house":     [1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0],
}

_CLAVES = {
    "son":     [0, 3, 6, 10, 12],       # 3-2
    "reverse": [0, 4, 6, 9, 12],        # 2-3
    "rumba":   [0, 3, 7, 10, 12],
    "bossa":   [0, 3, 6, 10, 13],
}


def PGroove(style="funk", density=1.0, unit=0.25):
    """ Duration pattern from a genre groove template.

        `style`   -- 'funk', 'afrobeat', 'breakbeat', 'techno', 'dnb',
                     'trap' or 'house'
        `density` -- 0.0-1.0, thins the groove by dropping later onsets
        `unit`    -- length of one step in beats (default 0.25)

        e.g. `d1 >> play("-", dur=PGroove('funk', density=0.8))`
             `d2 >> play("x", dur=PGroove('dnb', 0.6))` """
    if style not in _GROOVES:
        raise ValueError("PGroove: style must be one of %s" % sorted(_GROOVES))
    bits = _GROOVES[style]
    onsets = _onsets(bits)
    density = max(0.0, min(1.0, density))
    keep = max(1, int(round(len(onsets) * density)))
    onsets = [onsets[0]] + sorted(_random.Random(0).sample(onsets[1:], keep - 1)) \
        if keep > 1 else [onsets[0]]
    return _onsets_to_durs(sorted(onsets), len(bits), unit)


def PClave(type="son", unit=0.25):
    """ Traditional Afro-Cuban / Latin clave as a duration pattern.

        `type` -- 'son' (3-2), 'reverse' (2-3), 'rumba' or 'bossa'

        e.g. `d1 >> play("x", dur=PClave('son'))`
             `d2 >> play("s", dur=PClave('rumba'))` """
    if type not in _CLAVES:
        raise ValueError("PClave: type must be one of %s" % sorted(_CLAVES))
    return _onsets_to_durs(_CLAVES[type], 16, unit)


# --- sustain & articulation ----------------------------------------------

def PSustain(durations, legato=1.0, style="normal"):
    """ Sustain values derived from a duration pattern.

        `legato` -- 1.0 notes touch, 0.5 staccato, 1.3 overlapping
        `style`  -- 'normal' proportional, 'decay' shortening,
                    'accent' alternating long/short

        e.g. `durs = PDur(5, 8)`
             `p1 >> pluck([0,2,4], dur=durs, sus=PSustain(durs, 0.5))` """
    durs = [float(d) for d in list(durations)]
    if not durs:
        return Pattern([])
    if style == "normal":
        out = [d * legato for d in durs]
    elif style == "decay":
        n = len(durs)
        out = [d * legato * (1.0 - 0.6 * (i / max(1, n - 1))) for i, d in enumerate(durs)]
    elif style == "accent":
        out = [d * legato * (1.0 if i % 2 == 0 else 0.5) for i, d in enumerate(durs)]
    else:
        raise ValueError("PSustain: style must be 'normal', 'decay' or 'accent'")
    return Pattern([round(v, 6) for v in out])


def PArticulation(type="legato", length=8):
    """ Sustain multipliers for a standard musical articulation.

        `type` -- 'legato' (1.0), 'staccato' (0.3), 'tenuto' (0.95),
                  'marcato' (accented, varied) or 'accent' (alternating)

        e.g. `p1 >> pluck([0,2,4,7], dur=1/2, sus=PArticulation('staccato'))` """
    table = {
        "legato":   [1.0],
        "staccato": [0.3],
        "tenuto":   [0.95],
        "marcato":  [1.0, 0.5, 0.7, 0.5],
        "accent":   [1.0, 0.6],
    }
    if type not in table:
        raise ValueError("PArticulation: type must be one of %s" % sorted(table))
    base = table[type]
    return Pattern([base[i % len(base)] for i in range(int(length))])
