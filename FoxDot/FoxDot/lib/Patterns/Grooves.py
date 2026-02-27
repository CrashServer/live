"""
Grooves.py
----------
Named groove/swing templates as Pattern factories.

PSwing  -- Basic swing delay pattern
PGroove -- Named groove delay templates (mpc60, tr808, etc.)
PAccent -- Named velocity accent patterns (backbeat, ghost, etc.)

"""

from __future__ import absolute_import, division, print_function

from .Main import Pattern


def PSwing(amount=0.1, steps=8):
    """Basic swing pattern — alternating delay offsets.

    Returns a Pattern of alternating [0, amount] for use with the `delay` attribute.
    Applies a swing feel by delaying every other step.

        >>> d1 >> pluck(delay=PSwing(0.08))

    """
    return Pattern([0, amount] * (steps // 2))


# Pre-measured groove delay templates (normalized to beat fractions)
_groove_templates = {
    "mpc60": [0, 0.04, 0, 0.06, 0, 0.03, 0, 0.07,
              0, 0.04, 0, 0.05, 0, 0.03, 0, 0.06],

    "tr808": [0, 0.02, 0, 0.03, 0, 0.01, 0, 0.04,
              0, 0.02, 0, 0.03, 0, 0.01, 0, 0.03],

    "sp1200": [0, 0.05, 0, 0.08, 0, 0.04, 0, 0.09,
               0, 0.05, 0, 0.07, 0, 0.04, 0, 0.08],

    "linn": [0, 0.03, 0, 0.05, 0, 0.02, 0, 0.06,
             0, 0.03, 0, 0.04, 0, 0.02, 0, 0.05],

    "shuffle": [0, 0.08, 0, 0.08, 0, 0.08, 0, 0.08,
                0, 0.08, 0, 0.08, 0, 0.08, 0, 0.08],

    "clave": [0, 0, 0.06, 0, 0, 0.04, 0, 0,
              0, 0, 0.06, 0, 0, 0, 0.04, 0],
}

def PGroove(name="mpc60", steps=16):
    """Named groove delay templates.

    Returns a Pattern of delay offsets per step, scaled and tiled to `steps`.
    Available templates: mpc60, tr808, sp1200, linn, shuffle, clave.

        >>> d1 >> play("x-o-x-o-", dur=0.25, delay=PGroove("mpc60"))

    """
    if name not in _groove_templates:
        raise ValueError("Unknown groove '{}'. Available: {}".format(
            name, list(_groove_templates.keys())))
    template = _groove_templates[name]
    # Tile template to fill requested steps
    data = [template[i % len(template)] for i in range(steps)]
    return Pattern(data)


# Named accent/velocity templates
_accent_templates = {
    # Backbeat: accents on beats 2 and 4 (in 16th-note grid)
    "backbeat": [0.6, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4,
                 0.6, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4],

    # Four on the floor: every beat accented
    "four_floor": [1.0, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4,
                   1.0, 0.4, 0.4, 0.4, 1.0, 0.4, 0.4, 0.4],

    # Offbeat: upbeats accented
    "offbeat": [0.4, 0.4, 1.0, 0.4, 0.4, 0.4, 1.0, 0.4,
                0.4, 0.4, 1.0, 0.4, 0.4, 0.4, 1.0, 0.4],

    # Ghost notes: quiet e-and-a ghost notes with normal downbeats
    "ghost": [1.0, 0.25, 0.3, 0.25, 0.7, 0.25, 0.3, 0.25,
              1.0, 0.25, 0.3, 0.25, 0.7, 0.25, 0.3, 0.25],
}

def PAccent(name="backbeat", steps=16):
    """Named velocity accent patterns.

    Returns a Pattern of amplify values (0-1) for use with `amplify`.
    Available templates: backbeat, four_floor, offbeat, ghost.

        >>> d1 >> play("x-o-x-o-", dur=0.25, amplify=PAccent("ghost"))

    """
    if name not in _accent_templates:
        raise ValueError("Unknown accent pattern '{}'. Available: {}".format(
            name, list(_accent_templates.keys())))
    template = _accent_templates[name]
    data = [template[i % len(template)] for i in range(steps)]
    return Pattern(data)
