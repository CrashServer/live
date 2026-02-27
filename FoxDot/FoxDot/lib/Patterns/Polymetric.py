"""
    Polymetric pattern tools for FoxDot.

    PMetric       -- N evenly-spaced pulses in M beats
    PTriplet      -- 3 notes in the space of dur
    PQuintuplet   -- 5 notes in the space of dur
    PPolymetric   -- Merge multiple metric divisions into a single timeline

"""

from __future__ import absolute_import, division, print_function

from .Main import Pattern, PGroup


def PMetric(pulses, period=1):
    """N evenly-spaced pulses in M beats.

        >>> PMetric(3, 2)
        P[0.667, 0.667, 0.667]
        >>> PMetric(7, 4)
        P[0.571, 0.571, 0.571, 0.571, 0.571, 0.571, 0.571]

    """
    dur = float(period) / pulses
    return Pattern([dur] * pulses)


def PTriplet(dur=1):
    """3 notes in the space of dur. Shorthand for PMetric(3, dur).

        >>> PTriplet(1)
        P[0.333, 0.333, 0.333]

    """
    return PMetric(3, dur)


def PQuintuplet(dur=1):
    """5 notes in the space of dur. Shorthand for PMetric(5, dur).

        >>> PQuintuplet(2)
        P[0.4, 0.4, 0.4, 0.4, 0.4]

    """
    return PMetric(5, dur)


def PPolymetric(*divisions, **kwargs):
    """Merge multiple (pulses, value) pairs into a single timeline.

    Each division is a (pulses, value) tuple. Events are placed at
    evenly-spaced times within `total` beats, sorted, and dur gaps
    between events are computed.

        >>> PPolymetric((3, 0), (4, 2), total=4)
        {'dur': P[...], 'degree': P[...]}

    """
    total = kwargs.get('total', 4)
    events = []
    for pulses, value in divisions:
        step = float(total) / pulses
        for i in range(pulses):
            events.append((i * step, value))
    events.sort(key=lambda e: e[0])

    durs = []
    degrees = []
    for i in range(len(events)):
        degrees.append(events[i][1])
        if i < len(events) - 1:
            durs.append(events[i + 1][0] - events[i][0])
        else:
            durs.append(total - events[i][0])

    return {'dur': Pattern(durs), 'degree': Pattern(degrees)}
