# =============================================================================
# SYNTHPATTERNS.PY - Envelope and Melodic Pattern Library
# =============================================================================
#
# Pre-defined patterns for synth parameters: sustain, amplitude, melodies, arps
#
# Usage:
#     s1 >> pluck([0,2,4], dur=1/4, sus=env("stab"))
#     b1 >> bass(mel("acid1"), dur=1/8)
#     a1 >> saw(arp("trance1"), dur=1/16)
#     c1 >> keys(chords("house1"), dur=4)
#
# =============================================================================

from .Patterns import Pattern, P, PGroup

# =============================================================================
# ENVELOPE PATTERNS
# =============================================================================
# Values for sus, amp, or any numeric parameter
# Designed for 4, 8, or 16 step patterns at dur=1/4

ENVELOPES = {
    # -------------------------------------------------------------------------
    # SUSTAIN PATTERNS (sus=)
    # -------------------------------------------------------------------------

    # Stabs - short hits
    "stab":      [0.1, 0.1, 0.1, 0.1],
    "stab2":     [0.15, 0.1, 0.15, 0.1],
    "stab8":     [0.1, 0.1, 0.1, 0.1, 0.15, 0.1, 0.1, 0.1],
    "stab16":    [0.1]*16,

    # Longer notes
    "hold":      [0.5, 0.5, 0.5, 0.5],
    "hold2":     [0.8, 0.4, 0.8, 0.4],
    "hold8":     [0.5, 0.3, 0.5, 0.3, 0.7, 0.3, 0.5, 0.3],

    # Sustained/legato
    "legato":    [0.9, 0.9, 0.9, 0.9],
    "legato8":   [0.95, 0.9, 0.95, 0.9, 0.95, 0.9, 0.95, 0.9],

    # Gated - on/off pattern
    "gate":      [0.4, 0, 0.4, 0],
    "gate2":     [0.5, 0, 0, 0.5, 0, 0, 0.5, 0],
    "gate3":     [0.3, 0, 0.3, 0, 0.3, 0, 0, 0],
    "gate16":    [0.4, 0, 0.4, 0, 0.4, 0, 0.4, 0, 0.4, 0, 0.4, 0, 0.4, 0, 0, 0],

    # Swell - building up
    "swell":     [0.2, 0.4, 0.6, 0.8],
    "swell8":    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
    "swell16":   [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.9],

    # Decay - fading out
    "decay":     [0.8, 0.6, 0.4, 0.2],
    "decay8":    [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],
    "decay16":   [1.0, 0.9, 0.85, 0.8, 0.7, 0.65, 0.6, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1],

    # Pump - sidechain style
    "pump":      [0.2, 0.5, 0.8, 0.6],
    "pump2":     [0.1, 0.4, 0.7, 0.9, 0.6, 0.4, 0.7, 0.5],
    "pump16":    [0.1, 0.3, 0.5, 0.7, 0.9, 0.7, 0.5, 0.3, 0.1, 0.3, 0.5, 0.7, 0.9, 0.7, 0.5, 0.3],

    # -------------------------------------------------------------------------
    # AMPLITUDE PATTERNS (amp=)
    # -------------------------------------------------------------------------

    # Accents
    "accent":    [1.0, 0.6, 0.8, 0.6],
    "accent2":   [1.0, 0.5, 0.7, 0.5, 0.9, 0.5, 0.7, 0.5],
    "accent3":   [1.0, 0.4, 0.6, 0.4, 0.8, 0.4, 0.6, 0.4],
    "accent16":  [1.0, 0.5, 0.7, 0.5, 0.9, 0.5, 0.7, 0.5, 1.0, 0.5, 0.7, 0.5, 0.9, 0.5, 0.8, 0.6],

    # Velocity curves
    "velocity":  [1.0, 0.7, 0.85, 0.7],
    "velocity8": [1.0, 0.6, 0.8, 0.6, 0.9, 0.6, 0.75, 0.6],
    "soft":      [0.5, 0.4, 0.45, 0.4],
    "soft8":     [0.5, 0.35, 0.45, 0.35, 0.5, 0.35, 0.4, 0.35],

    # Crescendo/decrescendo
    "cresc":     [0.3, 0.5, 0.7, 0.9],
    "cresc8":    [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    "decresc":   [0.9, 0.7, 0.5, 0.3],
    "decresc8":  [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2],

    # Builds
    "build8":    [0.3, 0.35, 0.4, 0.5, 0.6, 0.7, 0.85, 1.0],
    "build16":   [0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 1.0],

    # Sparse
    "sparse":    [1.0, 0, 0, 0],
    "sparse2":   [1.0, 0, 0, 0, 0.8, 0, 0, 0],
    "sparse3":   [1.0, 0, 0, 0, 0, 0, 0.7, 0],

    # Offbeat
    "offbeat":   [0, 0.8, 0, 0.8],
    "offbeat8":  [0, 0.7, 0, 0.7, 0, 0.8, 0, 0.7],

    # Syncopated
    "sync":      [1.0, 0, 0.7, 0, 0.8, 0, 0, 0.6],
    "sync2":     [1.0, 0, 0, 0.7, 0, 0.8, 0, 0],

    # -------------------------------------------------------------------------
    # FILTER PATTERNS (lpf=, hpf=)
    # -------------------------------------------------------------------------

    # Opening filter
    "open":      [500, 1000, 2000, 4000],
    "open8":     [400, 600, 900, 1200, 1800, 2500, 3500, 5000],
    "open16":    [300, 400, 500, 700, 900, 1100, 1400, 1800, 2200, 2800, 3500, 4200, 5000, 6000, 7000, 8000],

    # Closing filter
    "close":     [4000, 2000, 1000, 500],
    "close8":    [5000, 3500, 2500, 1800, 1200, 900, 600, 400],

    # Wobble filter
    "wobble":    [800, 2000, 800, 2000],
    "wobble2":   [500, 3000, 500, 3000, 700, 2500, 700, 2500],
    "wobble3":   [400, 1500, 600, 2000, 400, 1500, 800, 2500],

    # Stepped filter
    "step":      [500, 500, 1500, 1500, 3000, 3000, 1500, 1500],
    "step2":     [400, 800, 1200, 1600, 2000, 2400, 2800, 3200],

    # Resonant peaks
    "peak":      [500, 2000, 500, 4000],
    "peak8":     [400, 1500, 400, 3000, 400, 2000, 400, 5000],
}

# =============================================================================
# MELODIC PATTERNS
# =============================================================================
# Degree values for bass, lead, arp patterns

MELODIES = {
    # -------------------------------------------------------------------------
    # TECHNO BASSLINES
    # -------------------------------------------------------------------------

    # Minimal techno
    "tb1":       [0, 0, 0, 0],
    "tb2":       [0, 0, 0, -1],
    "tb3":       [0, 0, 3, 0],
    "tb4":       [0, 0, 0, 0, 0, 0, 3, 0],
    "tb5":       [0, 0, 0, 0, 0, 0, 0, 3],
    "tb6":       [0, 0, 3, 0, 0, 0, 5, 3],
    "tb7":       [0, 3, 5, 3, 0, 3, 5, 7],
    "tb8":       [0, 0, 0, 0, 3, 3, 0, 0],

    # Driving techno
    "tbdrive1":  [0, 0, 0, 0, 0, 0, 0, 0],
    "tbdrive2":  [0, 0, 0, 0, 0, 0, -2, 0],
    "tbdrive3":  [0, 0, 3, 0, 0, 0, 5, 0],

    # -------------------------------------------------------------------------
    # ACID BASSLINES (303 style)
    # -------------------------------------------------------------------------

    "acid1":     [0, 0, 12, 0, 3, 0, 7, 0],
    "acid2":     [0, 12, 0, 3, 7, 3, 0, 12],
    "acid3":     [0, 0, 0, 12, 0, 0, 7, 12],
    "acid4":     [0, 3, 5, 7, 12, 7, 5, 3],
    "acid5":     [0, 0, 7, 0, 0, 7, 12, 7],
    "acid6":     [0, 12, 0, 0, 3, 12, 7, 0],
    "acid7":     [0, 0, 3, 0, 5, 0, 7, 12, 0, 0, 3, 0, 5, 7, 5, 3],
    "acid8":     [0, 12, 0, 12, 0, 12, 7, 12, 0, 12, 0, 12, 3, 12, 5, 12],

    # -------------------------------------------------------------------------
    # HOUSE BASSLINES
    # -------------------------------------------------------------------------

    "hb1":       [0, 0, 0, 3, 0, 0, 5, 3],
    "hb2":       [0, 0, 3, 0, 5, 0, 3, 0],
    "hb3":       [0, 3, 5, 3, 0, 3, 5, 7],
    "hb4":       [0, 0, 0, 0, -2, -2, 0, 0],
    "hb5":       [0, 5, 0, 5, 3, 5, 3, 5],
    "hb6":       [0, 0, 7, 0, 5, 0, 3, 0],

    # Deep house
    "deep1":     [0, 0, 0, 0, 3, 0, 0, 0],
    "deep2":     [0, 0, 3, 0, 0, 0, 5, 0],
    "deep3":     [0, 3, 0, 5, 0, 3, 0, 0],

    # -------------------------------------------------------------------------
    # DnB BASSLINES
    # -------------------------------------------------------------------------

    "dnb1":      [0, 0, 0, 0, 0, 3, 0, 0],
    "dnb2":      [0, 0, 3, 0, 5, 0, 3, 0],
    "dnb3":      [0, 0, 0, 5, 0, 0, 3, 0],
    "dnb4":      [0, 5, 0, 3, 0, 5, 3, 0],

    # Reese movement
    "reese1":    [0, 0, 0, 0, 0, 0, 0, 3],
    "reese2":    [0, 0, 3, 0, 0, 0, 5, 3],
    "reese3":    [0, 3, 5, 3, 0, -2, 0, 3],

    # Jump up
    "jump1":     [0, 0, 5, 0, 0, 7, 5, 0],
    "jump2":     [0, 5, 7, 5, 0, 5, 7, 12],

    # -------------------------------------------------------------------------
    # HIP-HOP / TRAP
    # -------------------------------------------------------------------------

    "trap1":     [0, 0, 0, 0, 0, 0, 0, 0],
    "trap2":     [0, 0, 0, 3, 0, 0, 5, 0],
    "trap3":     [0, 0, 5, 0, 3, 0, 0, 0],
    "trap808":   [0, 0, 0, 0, 0, 0, -5, 0],

    "boom1":     [0, 0, 0, 0, 3, 0, 0, 0],
    "boom2":     [0, 0, 3, 0, 0, 5, 0, 0],

    # -------------------------------------------------------------------------
    # ARPEGGIOS
    # -------------------------------------------------------------------------

    # Basic arps
    "arp1":      [0, 2, 4, 2],
    "arp2":      [0, 2, 4, 7],
    "arp3":      [0, 4, 7, 4],
    "arp4":      [0, 2, 4, 7, 4, 2],
    "arp5":      [0, 4, 7, 12, 7, 4],

    # Trance arps
    "trance1":   [0, 4, 7, 12, 7, 4, 0, 4],
    "trance2":   [0, 7, 4, 7, 12, 7, 4, 7],
    "trance3":   [0, 4, 7, 4, 12, 7, 12, 7],
    "trance4":   [0, 2, 4, 7, 9, 7, 4, 2],
    "trance5":   [0, 4, 7, 11, 12, 11, 7, 4],

    # Extended arps
    "arp8":      [0, 2, 4, 7, 9, 7, 4, 2],
    "arp16":     [0, 2, 4, 2, 4, 7, 4, 7, 9, 7, 9, 12, 9, 7, 4, 2],

    # Broken arps
    "broken1":   [0, 4, 2, 7, 4, 9, 7, 4],
    "broken2":   [0, 7, 2, 4, 0, 9, 4, 7],

    # -------------------------------------------------------------------------
    # CHORD VOICINGS (as single values representing chord degrees)
    # -------------------------------------------------------------------------

    # Basic progressions
    "prog1":     [0, 3, 5, 4],           # I-IV-VI-V
    "prog2":     [0, 5, 3, 4],           # I-VI-IV-V
    "prog3":     [0, 4, 5, 3],           # I-V-VI-IV (pop)
    "prog4":     [0, 3, 4, 4],           # I-IV-V-V

    # Minor progressions
    "minor1":    [0, 3, 5, 4],
    "minor2":    [0, 5, 6, 4],
    "minor3":    [0, 2, 3, 5],

    # House progressions
    "hchord1":   [0, 0, 3, 3, 5, 5, 4, 4],
    "hchord2":   [0, 3, 5, 4],
    "hchord3":   [0, 5, 3, 4],

    # Dark progressions
    "dark1":     [0, 1, 3, 2],
    "dark2":     [0, 5, 1, 4],
    "dark3":     [0, 3, 1, 5],

    # -------------------------------------------------------------------------
    # LEAD MELODIES
    # -------------------------------------------------------------------------

    "lead1":     [0, 2, 4, 2, 0, -1, 0, 2],
    "lead2":     [0, 4, 7, 4, 2, 4, 0, 2],
    "lead3":     [7, 5, 4, 2, 0, 2, 4, 5],
    "lead4":     [0, 0, 4, 4, 7, 7, 4, 4],

    # Hooks
    "hook1":     [0, 2, 4, 7, 4, 2, 4, 0],
    "hook2":     [7, 7, 5, 4, 2, 2, 4, 5],
    "hook3":     [0, 4, 0, 4, 7, 4, 7, 9],

    # -------------------------------------------------------------------------
    # RIFFS
    # -------------------------------------------------------------------------

    "riff1":     [0, 0, 3, 0, 5, 3, 0, 0],
    "riff2":     [0, 3, 5, 3, 7, 5, 3, 0],
    "riff3":     [0, 0, 0, 3, 5, 3, 0, 0],

    # -------------------------------------------------------------------------
    # OCTAVE PATTERNS (for adding to melodies)
    # -------------------------------------------------------------------------

    "oct1":      [0, 0, 0, 12],
    "oct2":      [0, 0, 12, 0],
    "oct3":      [0, 12, 0, 12],
    "oct4":      [0, 0, 0, 0, 0, 0, 0, 12],
    "oct8":      [0, 0, 12, 0, 0, 12, 0, 0],

    # Sub octaves
    "sub1":      [0, 0, 0, -12],
    "sub2":      [0, -12, 0, 0],
    "sub3":      [0, 0, -12, 0, 0, 0, -12, 0],
}

# =============================================================================
# CHORD PATTERNS (as PGroups for polyphonic playing)
# =============================================================================

CHORDS = {
    # Basic triads
    "maj":       (0, 2, 4),
    "min":       (0, 2, 4),  # Scale handles minor
    "dim":       (0, 2, 4),
    "aug":       (0, 2, 4),

    # 7ths
    "maj7":      (0, 2, 4, 6),
    "min7":      (0, 2, 4, 6),
    "dom7":      (0, 2, 4, 6),

    # Extended
    "add9":      (0, 2, 4, 8),
    "sus2":      (0, 1, 4),
    "sus4":      (0, 3, 4),

    # Progressions as lists of PGroups
    "houseprog": [(0, 2, 4), (3, 5, 7), (5, 7, 9), (4, 6, 8)],
    "deeprog":   [(0, 2, 4), (5, 7, 9), (3, 5, 7), (4, 6, 8)],
    "darkprog":  [(0, 2, 4), (1, 3, 5), (3, 5, 7), (2, 4, 6)],
    "tranceprog": [(0, 2, 4), (4, 6, 8), (5, 7, 9), (3, 5, 7)],

    # Stab chords
    "stab1":     (0, 4, 7, 11),
    "stab2":     (0, 2, 4, 7),
    "stab3":     (0, 4, 7, 12),
}


# =============================================================================
# FUNCTIONS
# =============================================================================

def _resolve(name, lookup, dur=None):
    """ Name, number, list or var -> pattern data.
        "trance3" / 1         -> that pattern
        [1, "trance3"]        -> the patterns played one after the other
        [1, "trance3"], dur=8 -> switch whole patterns every 8 beats (Pvar; dur can be a list)
        var([1, 3], 8)        -> same, numbers only: FoxDot's var splits strings into letters """
    from .TimeVar import TimeVar, Pvar
    if dur is not None and isinstance(name, (list, tuple, Pattern)):
        return Pvar([_resolve(n, lookup) for n in name], dur)
    if isinstance(name, TimeVar):
        return Pvar([_resolve(v, lookup) for v in name.values], name.dur, start=name.start_time)
    if isinstance(name, (list, tuple, Pattern)):
        out = []
        for n in name:
            item = _resolve(n, lookup)
            out.extend(item if isinstance(item, list) else [item])
        return out
    return lookup(name)


def _numbered(table, name, default):
    """ Name lookup, or a number: n -> the n-th entry as listed by mels()/envs()
        (alphabetical, 1-based, wraps around so any integer works) """
    if isinstance(name, (int, float)) and not isinstance(name, bool):
        keys = sorted(table)
        return table[keys[(int(name) - 1) % len(keys)]]
    return table.get(name, default)


def env(name, dur=None):
    """
    Look up an envelope pattern by name.

    Args:
        name: Pattern name (e.g., "stab", "pump", "accent")

    Returns:
        List of values for use with sus=, amp=, lpf=, etc.

    Examples:
        s1 >> pluck([0,2,4], dur=1/4, sus=env("stab"))
        s1 >> saw([0], dur=1/4, amp=env("accent"))
        s1 >> bass([0], dur=1/4, lpf=env("wobble"))
        s1 >> pluck([0], dur=1/4, sus=env(["stab", "swell"]))       # one after the other
        s1 >> pluck([0], dur=1/4, sus=env(var([1, 4], 8)))          # numbers as listed by envs()
        s1 >> pluck([0], dur=1/4, sus=env(["stab", "pump"], 8))      # switch every 8 beats
    """
    return _resolve(name, lambda n: _numbered(ENVELOPES, n, [1]), dur)


def e(name, dur=None):
    """Short alias for env()"""
    return env(name, dur)


def mel(name, dur=None):
    """
    Look up a melodic pattern by name.

    Args:
        name: Pattern name (e.g., "acid1", "tb1", "arp1")

    Returns:
        List of degree values

    Examples:
        b1 >> bass(mel("acid1"), dur=1/8)
        a1 >> pluck(mel("trance1"), dur=1/16)
        p1 >> pads(mel("prog1"), dur=4)
        b1 >> bass(mel(["acid1", "acid2"]), dur=1/8)
        b1 >> bass(mel(3), dur=1/8)                         # 3rd melody as listed by mels()
        b1 >> bass(mel([1, 5], 8), dur=1/8)                 # switch every 8 beats
        b1 >> bass(mel(var([1, 5], 8)), dur=1/8)            # same, with a var
        b1 >> bass(mel(["tb1", "acid3"], 16), dur=1/8)          # switch every 16 beats
    """
    return _resolve(name, lambda n: _numbered(MELODIES, n, [0]), dur)


def m(name, dur=None):
    """Short alias for mel()"""
    return mel(name, dur)


def arp(name, dur=None):
    """
    Look up an arpeggio pattern by name.
    Searches both MELODIES (arp*, trance*) patterns.

    Args:
        name: Pattern name (e.g., "trance1", "arp1", "broken1")

    Returns:
        List of degree values

    Examples:
        a1 >> pluck(arp("trance1"), dur=1/16)
        a1 >> saw(arp("arp8"), dur=1/8)
        a1 >> pluck(arp(1), dur=1/4)                       # number -> arp1 (then trance1)
        a1 >> pluck(arp([1, 2, "trance3"]), dur=1/4)       # one after the other
        a1 >> pluck(arp([1, "trance3"], 8), dur=1/4)       # switch every 8 beats
        a1 >> pluck(arp([1, 3], [12, 4]), dur=1/4)         # 12 beats arp1, 4 beats arp3
        a1 >> pluck(arp(var([1, 3], 8)), dur=1/4)          # var works with numbers
    """
    return _resolve(name, _arp_one, dur)


def _arp_one(name):
    # Direct match, then "arp<name>", then "trance<name>"
    for key in (name, f"arp{name}", f"trance{name}"):
        if key in MELODIES:
            return MELODIES[key]
    return [0, 2, 4, 7]  # Default arp


def chord(name, dur=None):
    """
    Look up a chord or chord progression.

    Args:
        name: Chord name (e.g., "maj7", "houseprog")

    Returns:
        Tuple for single chord, or list of tuples for progression

    Examples:
        c1 >> keys(chord("maj7"), dur=4)
        c1 >> pads(chord("houseprog"), dur=4)
        c1 >> pads(chord(["houseprog", "darkprog"]), dur=4)
        c1 >> keys(chord(["maj7", "min7"], 8), dur=2)
    """
    return _resolve(name, _chord_one, dur)


def _chord_one(name):
    result = _numbered(CHORDS, name, (0, 2, 4))
    if isinstance(result, list):
        return [PGroup(c) for c in result]
    return PGroup(result)


def chords(name, dur=None):
    """Alias for chord(), typically used for progressions"""
    return chord(name, dur)


def envs():
    """Print all available envelope patterns"""
    print("\n=== ENVELOPE PATTERNS ===\n")

    categories = {
        'stab': 'Stabs (short)',
        'hold': 'Hold (medium)',
        'legato': 'Legato (long)',
        'gate': 'Gated',
        'swell': 'Swell (building)',
        'decay': 'Decay (fading)',
        'pump': 'Pump (sidechain)',
        'accent': 'Accents',
        'velocity': 'Velocity',
        'soft': 'Soft',
        'cresc': 'Crescendo',
        'decresc': 'Decrescendo',
        'build': 'Build',
        'sparse': 'Sparse',
        'offbeat': 'Offbeat',
        'sync': 'Syncopated',
        'open': 'Filter Open',
        'close': 'Filter Close',
        'wobble': 'Filter Wobble',
        'step': 'Filter Step',
        'peak': 'Filter Peak',
    }

    current_cat = None
    for key in sorted(ENVELOPES.keys()):
        # Find category
        cat = None
        for prefix, cat_name in categories.items():
            if key.startswith(prefix):
                cat = cat_name
                break

        if cat != current_cat:
            current_cat = cat
            print(f"\n{cat or 'Other'}:")

        vals = ENVELOPES[key]
        preview = str(vals[:6])
        if len(vals) > 6:
            preview = preview[:-1] + ", ...]"
        print(f"  {sorted(ENVELOPES).index(key) + 1:3}  {key:12} {preview}")


def mels():
    """Print all available melodic patterns"""
    print("\n=== MELODIC PATTERNS ===\n")

    categories = {
        'tb': 'Techno Bass',
        'tbdrive': 'Techno Driving',
        'acid': 'Acid',
        'hb': 'House Bass',
        'deep': 'Deep House',
        'dnb': 'DnB',
        'reese': 'Reese',
        'jump': 'Jump Up',
        'trap': 'Trap',
        'boom': 'Boom Bap',
        'arp': 'Arpeggios',
        'trance': 'Trance',
        'broken': 'Broken',
        'prog': 'Progressions',
        'minor': 'Minor',
        'hchord': 'House Chords',
        'dark': 'Dark',
        'lead': 'Leads',
        'hook': 'Hooks',
        'riff': 'Riffs',
        'oct': 'Octave',
        'sub': 'Sub Octave',
    }

    current_cat = None
    for key in sorted(MELODIES.keys()):
        # Find category
        cat = None
        for prefix, cat_name in sorted(categories.items(), key=lambda x: -len(x[0])):
            if key.startswith(prefix):
                cat = cat_name
                break

        if cat != current_cat:
            current_cat = cat
            print(f"\n{cat or 'Other'}:")

        vals = MELODIES[key]
        preview = str(vals[:8])
        if len(vals) > 8:
            preview = preview[:-1] + ", ...]"
        print(f"  {sorted(MELODIES).index(key) + 1:3}  {key:12} {preview}")


# =============================================================================
# JSON EXPORT (for webTroop autocomplete)
# =============================================================================

def get_env_category(key):
    """Determine category from envelope key"""
    prefixes = {
        'stab': 'Sustain Stab', 'hold': 'Sustain Hold', 'legato': 'Sustain Legato',
        'gate': 'Sustain Gate', 'swell': 'Sustain Swell', 'decay': 'Sustain Decay',
        'pump': 'Sustain Pump', 'accent': 'Amp Accent', 'velocity': 'Amp Velocity',
        'soft': 'Amp Soft', 'cresc': 'Amp Crescendo', 'decresc': 'Amp Decrescendo',
        'build': 'Amp Build', 'sparse': 'Amp Sparse', 'offbeat': 'Amp Offbeat',
        'sync': 'Amp Sync', 'open': 'Filter Open', 'close': 'Filter Close',
        'wobble': 'Filter Wobble', 'step': 'Filter Step', 'peak': 'Filter Peak',
    }
    for prefix, cat in sorted(prefixes.items(), key=lambda x: -len(x[0])):
        if key.startswith(prefix):
            return cat
    return 'Other'


def get_mel_category(key):
    """Determine category from melody key"""
    prefixes = {
        'tbdrive': 'Techno Drive', 'tb': 'Techno Bass', 'acid': 'Acid',
        'hchord': 'House Chords', 'hb': 'House Bass', 'deep': 'Deep House',
        'reese': 'DnB Reese', 'jump': 'DnB Jump', 'dnb': 'DnB',
        'trap808': 'Trap 808', 'trap': 'Trap', 'boom': 'Boom Bap',
        'trance': 'Trance Arp', 'broken': 'Broken Arp', 'arp': 'Arpeggio',
        'prog': 'Progression', 'minor': 'Minor Prog', 'dark': 'Dark Prog',
        'lead': 'Lead', 'hook': 'Hook', 'riff': 'Riff',
        'oct': 'Octave', 'sub': 'Sub Octave',
    }
    for prefix, cat in sorted(prefixes.items(), key=lambda x: -len(x[0])):
        if key.startswith(prefix):
            return cat
    return 'Other'


def export_json(filepath=None):
    """
    Export envelopes and melodies to JSON for webTroop autocomplete.

    Usage:
        export_json()  # prints to stdout
        export_json("/path/to/synthPatterns.json")
    """
    import json

    data = {
        "envelopes": [],
        "melodies": [],
        "chords": [],
        "categories": {}
    }

    # Export envelopes
    for key, value in sorted(ENVELOPES.items()):
        category = get_env_category(key)
        preview = str(value[:4]) + "..." if len(value) > 4 else str(value)

        entry = {
            "code": key,
            "values": value,
            "preview": preview,
            "category": category,
            "length": len(value)
        }
        data["envelopes"].append(entry)

        cat_key = f"env:{category}"
        if cat_key not in data["categories"]:
            data["categories"][cat_key] = []
        data["categories"][cat_key].append(key)

    # Export melodies
    for key, value in sorted(MELODIES.items()):
        category = get_mel_category(key)
        preview = str(value[:6]) + "..." if len(value) > 6 else str(value)

        entry = {
            "code": key,
            "values": value,
            "preview": preview,
            "category": category,
            "length": len(value)
        }
        data["melodies"].append(entry)

        cat_key = f"mel:{category}"
        if cat_key not in data["categories"]:
            data["categories"][cat_key] = []
        data["categories"][cat_key].append(key)

    # Export chords
    for key, value in sorted(CHORDS.items()):
        preview = str(value)[:20] + "..." if len(str(value)) > 20 else str(value)

        entry = {
            "code": key,
            "values": value if isinstance(value, tuple) else [v for v in value],
            "preview": preview,
            "category": "Chords"
        }
        data["chords"].append(entry)

    json_str = json.dumps(data, indent=2)

    if filepath:
        with open(filepath, 'w') as f:
            f.write(json_str)
        print(f"Exported to {filepath}")
    else:
        print(json_str)

    return data


# =============================================================================
# EXPORTS
# =============================================================================

__all__ = ['env', 'e', 'mel', 'm', 'arp', 'chord', 'chords',
           'envs', 'mels', 'export_json',
           'ENVELOPES', 'MELODIES', 'CHORDS']


# CLI support
if __name__ == "__main__":
    import sys
    output = sys.argv[1] if len(sys.argv) > 1 else None
    export_json(output)
