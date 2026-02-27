"""
    Sample slicing pattern helpers for FoxDot.

    PSlice    -- Equal-division slice positions as (start, end) PGroups
    slice_buf -- Normalized start positions for granular synth pos parameter

"""

from __future__ import absolute_import, division, print_function

from .Main import Pattern, PGroup


def PSlice(n_slices=8, pattern=None):
    """Equal-division slice positions as (start, end) PGroup tuples.

    Divides 0-1 into n_slices equal regions. If pattern is given,
    only those slice indices are selected.

        >>> PSlice(4)
        P[P(0.0, 0.25), P(0.25, 0.5), P(0.5, 0.75), P(0.75, 1.0)]

        >>> PSlice(4, [0, 2])
        P[P(0.0, 0.25), P(0.5, 0.75)]

    """
    step = 1.0 / n_slices
    slices = []
    indices = range(n_slices) if pattern is None else pattern
    for i in indices:
        start = round(i * step, 6)
        end = round((i + 1) * step, 6)
        slices.append(PGroup(start, end))
    return Pattern(slices)


def slice_buf(n_slices=8):
    """Normalized start positions for use with granular synth pos parameter.

        >>> slice_buf(4)
        P[0.0, 0.25, 0.5, 0.75]

    """
    step = 1.0 / n_slices
    return Pattern([round(i * step, 6) for i in range(n_slices)])
