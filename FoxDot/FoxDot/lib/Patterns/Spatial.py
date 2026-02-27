"""
    Spatial audio pattern helpers for FoxDot.

    POrbit   -- Pre-computed sine pan positions for orbital panning
    PStereo  -- Map values to stereo field positions

"""

from __future__ import absolute_import, division, print_function

import math
from .Main import Pattern


def POrbit(speed=0.25, width=1.0, steps=16):
    """Pre-computed sine pan positions for use with the pan attribute.

    Returns a Pattern of sin(phase) values scaled by width.

        >>> POrbit(0.5, 1.0, 8)
        P[0.0, 0.707, 1.0, 0.707, 0.0, -0.707, -1.0, -0.707]

    """
    values = []
    for i in range(steps):
        phase = 2 * math.pi * speed * i / steps
        values.append(round(math.sin(phase) * width, 6))
    return Pattern(values)


def PStereo(values, width=1.0):
    """Map values to stereo positions in [-width, width].

    Normalizes the input range to the stereo field.

        >>> PStereo([0, 1, 2, 3], width=1.0)
        P[-1.0, -0.333, 0.333, 1.0]

    """
    values = list(values)
    lo = min(values)
    hi = max(values)
    rng = hi - lo
    if rng == 0:
        return Pattern([0.0] * len(values))
    mapped = []
    for v in values:
        norm = (v - lo) / rng
        mapped.append(round(norm * 2 * width - width, 6))
    return Pattern(mapped)
