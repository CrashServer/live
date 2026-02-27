"""
Envelopes.py
-------------
Envelope and LFO shape generators as Patterns.

PEnv   -- Multi-segment envelope with curve control
PLFO   -- LFO waveform as Pattern (sin, tri, saw, square, noise)
PRamp  -- Linear ramp from start to end
PStep  -- Step sequencer with hold times

"""

from __future__ import absolute_import, division, print_function

import math
import random

from .Main import Pattern


def _interp(a, b, t, curve):
    """Interpolate between a and b at position t (0-1) with curve shaping."""
    if curve == 'lin' or curve == 0:
        return a + (b - a) * t
    elif curve == 'exp':
        if a == 0:
            a = 0.001
        if b == 0:
            b = 0.001
        return a * ((b / a) ** t)
    elif curve == 'sin':
        return a + (b - a) * (math.sin(t * math.pi / 2))
    elif isinstance(curve, (int, float)):
        if abs(curve) < 0.001:
            return a + (b - a) * t
        # Attempt SC-style curved interpolation
        denom = 1.0 - math.exp(curve)
        numer = 1.0 - math.exp(t * curve)
        return a + (b - a) * (numer / denom)
    return a + (b - a) * t


def PEnv(levels, times=None, curve='lin', steps=16):
    """Multi-segment envelope as a Pattern.

    `levels` is a list of breakpoint values (e.g. [0, 1, 0.5, 0]).
    `times` is a list of relative segment durations (len = len(levels)-1).
        None means equal duration for all segments.
    `curve` controls interpolation: 'lin', 'exp', 'sin', or a numeric value.
    `steps` is the total number of output values.

        >>> PEnv([0, 1, 0.5, 0], [0.2, 0.5, 0.3], curve=-4, steps=32)

    """
    n_segs = len(levels) - 1
    if n_segs <= 0:
        return Pattern(levels)
    if times is None:
        times = [1.0] * n_segs
    # Normalize times
    total = sum(times)
    times = [t / total for t in times]
    # Allocate steps per segment
    seg_steps = []
    for i, t in enumerate(times):
        seg_steps.append(max(1, int(round(t * steps))))
    # Adjust to match exact step count
    diff = steps - sum(seg_steps)
    if diff > 0:
        # Add extra steps to the longest segment
        idx = seg_steps.index(max(seg_steps))
        seg_steps[idx] += diff
    elif diff < 0:
        # Remove from the longest segment
        idx = seg_steps.index(max(seg_steps))
        seg_steps[idx] = max(1, seg_steps[idx] + diff)

    result = []
    for i in range(n_segs):
        a = levels[i]
        b = levels[i + 1]
        n = seg_steps[i]
        for j in range(n):
            t = j / float(n) if n > 1 else 0.0
            result.append(_interp(a, b, t, curve))

    # Trim or pad to exact length
    result = result[:steps]
    while len(result) < steps:
        result.append(levels[-1])

    return Pattern(result)


def PLFO(shape='sin', rate=1, depth=1, center=0, steps=16):
    """LFO waveform as a Pattern.

    `shape`: 'sin', 'tri', 'saw', 'square', 'noise'
    `rate`: number of full cycles within `steps`
    `depth`: amplitude of the waveform
    `center`: DC offset added to output

        >>> PLFO('tri', rate=2, depth=1, steps=16)

    """
    result = []
    for i in range(steps):
        phase = (i / float(steps)) * rate * 2 * math.pi

        if shape == 'sin':
            val = math.sin(phase)
        elif shape == 'tri':
            # Triangle: map phase to [-1, 1] triangle
            t = ((i / float(steps)) * rate) % 1.0
            val = 4 * abs(t - 0.5) - 1
        elif shape == 'saw':
            t = ((i / float(steps)) * rate) % 1.0
            val = 2 * t - 1
        elif shape == 'square':
            t = ((i / float(steps)) * rate) % 1.0
            val = 1 if t < 0.5 else -1
        elif shape == 'noise':
            val = random.uniform(-1, 1)
        else:
            val = math.sin(phase)

        result.append(center + depth * val)

    return Pattern(result)


def PRamp(start=0, end=1, steps=16):
    """Linear ramp Pattern from start to end.

        >>> PRamp(200, 8000, 16)

    """
    if steps <= 1:
        return Pattern([start])
    result = []
    for i in range(steps):
        t = i / float(steps - 1)
        result.append(start + (end - start) * t)
    return Pattern(result)


def PStep(values, holds=None):
    """Step sequencer Pattern: each value repeated `hold` times.

    `values`: list of step values
    `holds`: list of hold counts per value (None = 1 each)

        >>> PStep([200, 800, 400, 1200], holds=[4, 4, 4, 4])

    """
    if holds is None:
        holds = [1] * len(values)
    result = []
    for val, hold in zip(values, holds):
        result.extend([val] * hold)
    return Pattern(result)
