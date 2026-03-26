"""
DrumPatterns.py
---------------
Genre-aware drum pattern generator for live coding.

pbuild(genre, **kwargs) — generate drum patterns by genre
pat(code)               — get a specific named pattern

Usage:
    d1 >> play(pbuild("techno"), dur=0.25)
    d1 >> play(pbuild("techno", evolve=8, fill=4, swing=0.1), dur=0.25)
    d1 >> play(pbuild("techno").kick, dur=0.25)
    d1 >> play(pat("t1"), dur=0.25)
"""

from __future__ import absolute_import, division, print_function
import random
from copy import copy, deepcopy

# ============================================================
# GENRE DEFINITIONS
# ============================================================
# Each genre defines layers with multiple variations.
# Characters follow FoxDot's sample mapping:
#   X/x=kick  o/O=snare  -=closed hat  ==open hat
#   *=clap  s=shaker  t=rimshot  #=crash  ~=ride
#   v=soft kick  u=soft snare  +=clicks  :=hi-hats

_genres = {
    "techno": {
        "kick": [
            "X   X   X   X   ",
            "X   X   X  XX   ",
            "X     X X   X   ",
            "X   X   X   X X ",
            "X  X  X X  X  X ",
            "X   X    X  X   ",
            "X  X    X   X   ",
            "X   X   X X X   ",
            "X     X X     X ",
            "X   X  XX   X  X",
            "X  XX   X   X   ",
            "X   X X   X X   ",
        ],
        "snare": [
            "    o       o   ",
            "    *       *   ",
            "    o     o o   ",
            "    *   o   *   ",
            "    o      oo   ",
            "  o     o   o   ",
            "    o  o    o   ",
            "    *     * *   ",
            "    o   o   o   ",
            "  o o       o   ",
            "    *  o    *  o",
            "    o       o  o",
        ],
        "hat": [
            "-.-.-.-.-.-.-.--",
            "----------------",
            "-.-.--=--.-.--=-",
            "--.--.---.------",
            "-.---.-.-.---.--",
            "--=---=---=---=-",
            "-.-.-.---.-.-.--",
            "---.-.-----.-.--",
            "-.--=-.--.--=-.-",
            "-.-.-.-.-.-=-.--",
            "=.-.=.-.=.-.=.--",
            "-...-..-...-..-.",
        ],
        "perc": [
            "                ",
            "  t   t   t   t ",
            "s   s   s   s   ",
            "    +     + +   ",
            "  :   :   :  :  ",
            "t     t     t   ",
            "  s     s     s ",
            "+   + +   +   + ",
            "  : :   : :   : ",
            "    t       t   ",
        ],
    },
    "ebm": {
        "kick": [
            "X   X   X   X   ",
            "X X X X X X X X ",
            "X  XX   X  XX   ",
            "X X X   X X X   ",
            "X   X X X   X X ",
            "X X   X X X   X ",
            "XX  X   XX  X   ",
            "X  XX  XX  XX   ",
            "X X X X   X X X ",
            "X   XX  X   XX  ",
            "XX  XX    XX  XX",
            "X X   X X   X X ",
        ],
        "snare": [
            "    O       O   ",
            "    *       *   ",
            "    O     O O   ",
            "   oO      oO   ",
            "    O  o    O  o",
            "    *  *    *   ",
            "    O   *   O   ",
            "  o O   o   O   ",
            "    O o     O o ",
            "    *   o  o*   ",
            "   oO  o   oO   ",
            "    O     o O  o",
        ],
        "hat": [
            "-.-.-.-.-.-.-.--",
            "----------------",
            "-.--.---.-.--.--",
            "-.-.-=-.-.-.-=-.",
            "-.---.---.---.--",
            "---.---.-.--.---",
            "-.-.-.-.---.-.--",
            "--=--.----=--.--",
        ],
        "perc": [
            "                ",
            "  t   t   t   t ",
            "+  + +  +  + +  ",
            "  r   r   r   r ",
            "+   +   +   + + ",
            "t t   t t t   t ",
        ],
    },
    "dnb": {
        "kick": [
            "X     X   X     ",
            "X       X   X   ",
            "X     X    X    ",
            "X  X      X     ",
            "X       X     X ",
            "X   X     X     ",
            "X      X  X     ",
            "X  X       X    ",
            "X     X       X ",
            "X        X  X   ",
            "X   X       X   ",
            "X  X    X       ",
        ],
        "snare": [
            "    o       o   ",
            "    o       o o ",
            "    o     o o   ",
            "   uo      uo   ",
            "    o  u    o u ",
            "    o       o  u",
            "    o  o    o   ",
            "   uo       o o ",
            "    o u     o   ",
            "    o     u o   ",
            "    o  u   uo   ",
            "    o   u   o u ",
        ],
        "hat": [
            "-.-.-.-.-.-.-.--",
            "-.---.-.-.---.--",
            "--=---=---=---=-",
            "-.-.=.-.-.-.=.--",
            "-.--.-=--.--.-=-",
            "=.-.-.=.-.-.-.=-",
            "-.-.-.---.-.-.--",
            "-.--=.-.-.--=.--",
        ],
        "perc": [
            "                ",
            "  ~   ~   ~   ~ ",
            "    s     s s   ",
            "~     ~     ~   ",
            "  s   s       s ",
            "  ~ ~   ~ ~   ~ ",
        ],
    },
    "house": {
        "kick": [
            "X   X   X   X   ",
            "X   X   X   X X ",
            "X   X  XX   X   ",
            "X   X   X  XX   ",
            "X   X X X   X   ",
            "X  XX   X   X   ",
            "X   X   X   XX  ",
            "X   X  XX   X X ",
        ],
        "snare": [
            "    *       *   ",
            "    H       H   ",
            "    *   *   *   ",
            "    *       * * ",
            "    H   *   H   ",
            "    *  *    *   ",
            "    H     * H   ",
            "    *   H   *   ",
        ],
        "hat": [
            "-.-.-.-.-.-.-.--",
            "--=---=---=---=-",
            "================",
            "-.--.-=--.--.-=-",
            "-.-.=.-.-.-.=.--",
            "=-.-=-=-.-.-=-=-",
            "-=.-=.-=-=.-=.--",
            "-.-.-.-=-.-.-.=-",
        ],
        "perc": [
            "                ",
            "s s s s s s s s ",
            "  +   +   +   + ",
            "s   s   s   s   ",
            "  + + +   + + + ",
            "s     s s     s ",
            "  +   + +   +   ",
        ],
    },
    "breaks": {
        "kick": [
            "X  X    X  X    ",
            "X     X  X      ",
            "X  X      X   X ",
            "X       X  X    ",
            "X    X  X       ",
            "X  X  X     X   ",
            "X       X X     ",
            "X  X       X  X ",
            "X     X     X   ",
            "X  X    X    X  ",
        ],
        "snare": [
            "    o  o    o   ",
            "    o   o  oo   ",
            "   oo       o o ",
            "    o o     o o ",
            "    o  o   oo   ",
            "   oo  o    o   ",
            "    o o  o  o   ",
            "    o  oo   o o ",
            "   oo   o   o   ",
            "    o o     oo  ",
        ],
        "hat": [
            "-.-.-.-.-.-.-.--",
            "-.---.-.-.---.--",
            "--=--.-.--=--.--",
            "-.-.-.---.-.-.--",
            "-.--=-.--.--=-.-",
            "-.---.---.---.--",
            "--.--.-.--.--.--",
        ],
        "perc": [
            "                ",
            "  t     t   t   ",
            "  ~ ~ ~   ~ ~ ~ ",
            "t   t   t     t ",
            "  ~     ~   ~   ",
            "  t ~ t   t ~ t ",
        ],
    },
    "halftime": {
        "kick": [
            "X       X       ",
            "X         X     ",
            "X       X    X  ",
            "X           X   ",
            "X     X         ",
            "X       X     X ",
            "X          X    ",
            "X   X           ",
        ],
        "snare": [
            "        o       ",
            "        o     o ",
            "    u   o       ",
            "        o   u   ",
            "        o  o    ",
            "    u   o     u ",
            "        *       ",
            "        o u     ",
        ],
        "hat": [
            "-.-.-.-.-.-.-.--",
            "-.--.--.-.--.---",
            "-.-.-=-.-.-.-=-.",
            "-.---.-.-.---.--",
            "-.--.-.--.--.---",
            "-.-.-.---.-.-.--",
        ],
        "perc": [
            "                ",
            "  s   s   s   s ",
            "s       s       ",
            "    ~       ~   ",
            "  s     s     s ",
        ],
    },
    "industrial": {
        "kick": [
            "X X X X X X X X ",
            "X  XX  XX  XX  X",
            "X X X   X X X X ",
            "XX  XX  XX  XX  ",
            "XXX   XXX   XXX ",
            "X XX  X XX  X XX",
            "X X XX  X X XX  ",
            "XX XX XX XX XX X",
            "X  XX X X  XX X ",
            "X X   XXX X   XX",
            "XX  X X XX  X X ",
            "X XXX   X XXX   ",
        ],
        "snare": [
            "    O       O   ",
            "    *   O   *   ",
            "  o O     o O   ",
            "    O O     O O ",
            "    *  O    *  O",
            "  O *     O *   ",
            "    O   *  oO   ",
            "  o O  *  o O  *",
            "    O o   O O o ",
            "    * O o   * O ",
        ],
        "hat": [
            "----------------",
            "-.-.-.-.-.-.-.--",
            "---.---.---.---.",
            "-.---.---.---.--",
            "----.-----.--.--",
            "-.-.---.-.-.---.",
            "--.--.--.--.--..",
        ],
        "perc": [
            "                ",
            "r r r r r r r r ",
            "  +   + +   + + ",
            "K   K   K   K   ",
            "r   r r   r r r ",
            "+ + +   + + +   ",
            "K K   K K K   K ",
            "  r +   r +   r ",
        ],
    },
    "reggae": {
        "kick": [
            "X       X       ",
            "X  X    X       ",
            "X     X X       ",
            "X       X   X   ",
            "X  X        X   ",
            "X     X   X     ",
            "X       X  X    ",
            "X   X   X       ",
        ],
        "snare": [
            "   o       o    ",
            "   *       *    ",
            "   o     o o    ",
            "   o  o    o    ",
            "   *     * *    ",
            "   o       o  o ",
            "   o   o   o    ",
            "   *  o    *  o ",
        ],
        "hat": [
            " - - - - - - - -",
            " -=- -=- -=- -=-",
            " - -=- - - -=- -",
            " -=- - - -=- - -",
            " - - -=- - - -=-",
            " --=- --=- --=- ",
        ],
        "perc": [
            "                ",
            "  s   s   s   s ",
            "t   t   t   t   ",
            "s     s s     s ",
            "  t   t     t   ",
            "s   s     s   s ",
        ],
    },
    "afro": {
        "kick": [
            "X  X  X   X   X ",
            "X    XX  X    X ",
            "X  X   X  X  X  ",
            "X   X  X  X     ",
            "X  X    X   X   ",
            "X    X  X  X    ",
            "X  X  X     X  X",
            "X     X X  X    ",
            "X  X   X    X   ",
            "X    X    X  X  ",
        ],
        "snare": [
            "    o     o     ",
            "   o  o  o  o   ",
            "    o   o   o o ",
            "  o   o     o   ",
            "    o  o  o     ",
            "   o    o   o   ",
            "    o     o  o  ",
            "  o o   o   o   ",
            "    o  o    o o ",
            "   o  o   o   o ",
        ],
        "hat": [
            "-.-.-.-.-.-.-.--",
            "-.--.-.--.--.---",
            "-.---.-.-.---.--",
            "-.--.--.-.--.---",
            "-.-.---.-.-.---.",
            "-.--.-.-.--.-.-.",
        ],
        "perc": [
            "s  s  s  s  s  s",
            " t t  t  t t  t ",
            ":  :  :  :  :  :",
            "s  s    s  s    ",
            " t   t t   t t  ",
            ":    ::    ::   ",
            "s t s   s t s   ",
            " : t :   : t :  ",
        ],
    },
}

# ============================================================
# FILL DEFINITIONS — per genre
# ============================================================

_fills = {
    "techno": [
        "X X X X X X XXXX",
        "X  XX  XXXXXXX X",
        "X   X   XXXXXXXX",
        "XXXX    o o XXXX",
        "X X XXXX  XXXXXX",
        "X   X XXXXXXXXXX",
        "XX XX XX XXXXXXX",
        "X  X  X  X XXXXX",
    ],
    "ebm": [
        "X X X X XXXXXXXX",
        "X X XXXXX X XXXX",
        "XXXXXXXXX X X X ",
        "XX XX XXXXXXXXXX",
        "X XXXXX XXXXXXXX",
        "XXXX X XXXXXXXXX",
    ],
    "dnb": [
        "X  oo  oX oXoo o",
        "X  o  XXXX oo oo",
        "X     oooooooooo",
        "X oX oXo oo oooo",
        "X  oo X oooooo o",
        "X   oooX ooooooo",
    ],
    "house": [
        "X   X   XXXX*  *",
        "X   X X X X XXXX",
        "X   X   * * XXXX",
        "X X X   XXXX* * ",
        "X   X ***   XXXX",
    ],
    "breaks": [
        "X oXo oXXoXo oXo",
        "X  oo XoXo ooXXo",
        "XoXo oXoXoXo oXo",
        "X oo oo ooXoXo o",
        "X  oXoXo oo  oXo",
    ],
    "halftime": [
        "X       oooooooo",
        "X     X oooXXXXX",
        "X       ooooo oo",
        "X     oo  oooooo",
    ],
    "industrial": [
        "XXXXXXXXXXXXXXXX",
        "X X XXXXX X XXXX",
        "XX XXXXX XX XXXX",
        "XXXXXX XXXXXXXXX",
        "X XXXXXXX XXXXXX",
    ],
    "reggae": [
        "X  X  X  X ooooo",
        "X  X oo  X oo oo",
        "X    X X  ooo oo",
    ],
    "afro": [
        "X oXo X oXo X oX",
        "XoX oXoXo oXoX o",
        "X o oXo oXoXo oX",
    ],
}

# ============================================================
# MUTATION RULES — for evolve
# ============================================================

def _mutate_add_hit(layer, chars):
    """Add a hit at a random empty slot"""
    empties = [i for i, c in enumerate(layer) if c == ' ']
    if empties:
        pos = random.choice(empties)
        layer = layer[:pos] + random.choice(chars) + layer[pos+1:]
    return layer

def _mutate_remove_hit(layer, keep_chars=None):
    """Remove a random hit (replace with space)"""
    hits = [i for i, c in enumerate(layer) if c != ' ']
    if keep_chars:
        hits = [i for i in hits if layer[i] not in keep_chars]
    if hits:
        pos = random.choice(hits)
        layer = layer[:pos] + ' ' + layer[pos+1:]
    return layer

def _mutate_shift_hit(layer):
    """Shift a random hit one position left or right"""
    hits = [i for i, c in enumerate(layer) if c != ' ']
    if hits:
        pos = random.choice(hits)
        direction = random.choice([-1, 1])
        new_pos = (pos + direction) % len(layer)
        if layer[new_pos] == ' ':
            char = layer[pos]
            layer = layer[:pos] + ' ' + layer[pos+1:]
            layer = layer[:new_pos] + char + layer[new_pos+1:]
    return layer

def _mutate_swap_variation(genre, layer_name):
    """Swap to a different variation of the same layer"""
    variations = _genres.get(genre, {}).get(layer_name, [])
    if variations:
        return random.choice(variations)
    return None

# ============================================================
# DRUM KIT CLASS
# ============================================================

class DrumKit:
    """A drum pattern kit that merges layers into a play() string.

    Supports:
        str(kit)     — merged pattern for play()
        kit.kick     — single layer string
        kit["kick", "snare"] — subset of layers merged
        kit | other  — merge two kits (union of hits)
    """

    _layer_order = ["kick", "snare", "hat", "perc"]

    def __init__(self, genre="techno", layers=None, density=1.0, seed=None,
                 mute=None, steps=16, **overrides):
        self.genre = genre
        self.steps = steps
        self._density = density
        self.mute = set(mute.split(",") if isinstance(mute, str) else (mute or []))
        self._rng = random.Random(seed)

        # Build initial layers
        genre_def = _genres.get(genre, _genres["techno"])
        if layers:
            self._layers = dict(layers)
        else:
            self._layers = {}
            for name in self._layer_order:
                variations = genre_def.get(name, [" " * steps])
                self._layers[name] = self._rng.choice(variations)

        # Apply overrides (e.g. kick="X   X X X   X   ")
        for name in self._layer_order:
            if name in overrides:
                val = overrides[name]
                if isinstance(val, str) and val in _genres:
                    # Cross-genre: hat="dnb"
                    self._layers[name] = self._rng.choice(_genres[val].get(name, [" " * steps]))
                else:
                    self._layers[name] = val

        # Store fills
        self._fills = _fills.get(genre, _fills.get("techno"))

    # --- Layer access ---

    def __getattr__(self, name):
        if name.startswith('_') or name in ('genre', 'steps', 'fill_every', 'swing',
            'mute', 'evolve', 'arc', 'drift', '_rng', '_layers', '_fills',
            '_density', '_evolve_step', '_evolve_beat', '_bar_counter'):
            raise AttributeError(name)
        if name in self._layers:
            return self._layers[name]
        raise AttributeError(f"No layer '{name}'")

    def __getitem__(self, keys):
        """kit["kick", "snare"] — merge subset of layers"""
        if isinstance(keys, str):
            keys = (keys,)
        return self._merge({k: self._layers[k] for k in keys if k in self._layers})

    # --- Merging ---

    def _merge(self, layers=None):
        """Merge layers into a single play() string"""
        if layers is None:
            layers = self._layers
        result = [' '] * self.steps
        for name in self._layer_order:
            if name in layers and name not in self.mute:
                layer = layers[name]
                for i in range(min(len(layer), self.steps)):
                    if layer[i] != ' ':
                        if result[i] == ' ':
                            result[i] = layer[i]
                        else:
                            # Layer conflict — use angle brackets for simultaneous
                            pass  # keep first hit, priority by layer order
        return ''.join(result)

    # --- Density ---

    def _apply_density(self, pattern, density):
        """Remove hits based on density (1.0 = full, 0.0 = silent)"""
        if density >= 1.0:
            return pattern
        result = list(pattern)
        for i, c in enumerate(result):
            if c != ' ' and self._rng.random() > density:
                result[i] = ' '
        return ''.join(result)

    # --- Evolution ---

    def _apply_evolution(self, step):
        """Mutate layers — add, remove, shift, or swap one element"""
        _chars = {'kick': 'Xx', 'snare': 'oO*u', 'hat': '-=', 'perc': 'ts+:~'}
        layer = self._rng.choice(self._layer_order)
        if layer not in self._layers:
            return
        action = self._rng.choice(["add", "remove", "shift", "swap"])
        if action == "add":
            self._layers[layer] = _mutate_add_hit(self._layers[layer], _chars.get(layer, 'x'))
        elif action == "remove":
            self._layers[layer] = _mutate_remove_hit(self._layers[layer])
        elif action == "shift":
            self._layers[layer] = _mutate_shift_hit(self._layers[layer])
        elif action == "swap":
            new = _mutate_swap_variation(self.genre, layer)
            if new:
                self._layers[layer] = new

    # --- Fill ---

    def _get_fill(self):
        """Get a fill pattern"""
        return self._rng.choice(self._fills)

    # --- String output (for play()) ---

    def __str__(self):
        pattern = self._merge()
        # Apply density
        if self._density < 1.0:
            # Density can be a number or a TimeVar — handle both
            d = self._density
            if hasattr(d, 'now'):
                d = d.now()
            pattern = self._apply_density(pattern, float(d))
        return pattern

    def __repr__(self):
        return f'DrumKit("{self.genre}")'

    # --- Operators ---

    def __or__(self, other):
        """kit1 | kit2 — merge two kits (union of hits)"""
        merged = {}
        all_layers = set(list(self._layers.keys()) + list(other._layers.keys()))
        for name in all_layers:
            a = self._layers.get(name, ' ' * self.steps)
            b = other._layers.get(name, ' ' * self.steps)
            result = []
            for i in range(max(len(a), len(b))):
                ca = a[i] if i < len(a) else ' '
                cb = b[i] if i < len(b) else ' '
                result.append(ca if ca != ' ' else cb)
            merged[name] = ''.join(result)
        return DrumKit(self.genre, layers=merged, density=self._density,
                       mute=None, seed=None)

    def __rshift__(self, n):
        """kit >> 2 — rotate all layers by n steps"""
        new_layers = {}
        for name, layer in self._layers.items():
            new_layers[name] = layer[-n:] + layer[:-n]
        result = copy(self)
        result._layers = new_layers
        return result


# ============================================================
# DRUM STRING — str subclass with layer access
# ============================================================

class DrumString(str):
    """A string that also carries drum layer info.
    isinstance(DrumString, str) is True — works with play()."""

    def __new__(cls, merged, kit):
        obj = str.__new__(cls, merged)
        obj._kit = kit
        return obj

    def __getattr__(self, name):
        if name == '_kit':
            raise AttributeError(name)
        if name in self._kit._layers:
            return self._kit._layers[name]
        raise AttributeError(f"No layer '{name}'")


# ============================================================
# NAMED PATTERNS — pat("t1") style
# ============================================================

_named_patterns = {}

def _register_named():
    """Build named patterns from genre definitions"""
    _prefixes = {
        "techno": "t", "ebm": "e", "dnb": "d", "house": "h",
        "breaks": "b", "halftime": "hf", "industrial": "i",
        "reggae": "rg", "afro": "af",
    }
    for genre, prefix in _prefixes.items():
        genre_def = _genres.get(genre, {})
        kick_vars = genre_def.get("kick", [])
        snare_vars = genre_def.get("snare", [])
        hat_vars = genre_def.get("hat", [])
        perc_vars = genre_def.get("perc", [])
        # Create numbered patterns by combining variations
        for i in range(max(len(kick_vars), 1)):
            kit = DrumKit(genre, layers={
                "kick": kick_vars[i % len(kick_vars)] if kick_vars else " " * 16,
                "snare": snare_vars[i % len(snare_vars)] if snare_vars else " " * 16,
                "hat": hat_vars[i % len(hat_vars)] if hat_vars else " " * 16,
                "perc": perc_vars[0] if perc_vars else " " * 16,
            })
            _named_patterns[f"{prefix}{i+1}"] = kit

_register_named()


# ============================================================
# PUBLIC API
# ============================================================

def pat(code):
    """Get a named drum pattern.

    Codes: {genre_prefix}{number}
        t1-t6   = techno
        e1-e5   = ebm
        d1-d5   = dnb
        h1-h3   = house
        b1-b4   = breaks
        hf1-hf3 = halftime
        i1-i4   = industrial
        rg1-rg3 = reggae
        af1-af3 = afro

    Returns a string for play().
    e.g. d1 >> play(pat("t1"), dur=0.25)
    """
    if code in _named_patterns:
        return str(_named_patterns[code])
    # List available if not found
    available = sorted(_named_patterns.keys())
    print(f"Unknown pattern '{code}'. Available: {', '.join(available)}")
    return " " * 16


def pbuild(genre="techno", evolve=8, fill=0, density=1.0,
           mute=None, seed=None, **overrides):
    """Build a drum pattern by genre.

    Args:
        genre:    "techno"|"ebm"|"dnb"|"house"|"breaks"|"halftime"|"industrial"|"reggae"|"afro"
        evolve:   number of bars before the pattern loops (default 8).
                  Each bar is a mutation of the previous — the groove evolves.
                  Set to 1 for a static single-bar pattern.
        fill:     insert a drum fill every N bars (0=no fills)
        density:  0.0-1.0 how many hits play
        mute:     layer name(s) to silence: "hat" or "kick,snare"
        seed:     random seed for reproducibility
        **overrides: replace layers: kick="X   X X ", hat="dnb"

    Returns a string for play().
    e.g. d1 >> play(pbuild("techno"), dur=0.25)
         d1 >> play(pbuild("techno", 4), dur=0.25)
         d1 >> play(pbuild("techno", 16, fill=4), dur=0.25)
    """
    kit = DrumKit(
        genre=genre, density=density, mute=mute, seed=seed, **overrides
    )

    if evolve <= 1:
        return DrumString(str(kit), kit)

    # Evolve by concatenation: each bar is a mutation, play() cycles through
    parts = []
    for i in range(evolve):
        if fill > 0 and (i + 1) % fill == 0:
            parts.append(kit._get_fill())
        else:
            parts.append(str(kit))
        # Mutate for next bar
        kit._apply_evolution(i + 1)
        kit._apply_evolution(i + 1)

    return DrumString(''.join(parts), kit)


def pkit(genre="techno", **kwargs):
    """Same as pbuild but returns DrumKit for layer access.
    e.g. kit = pkit("techno")
         d1 >> play(kit.kick, dur=0.25)
         d2 >> play(kit.hat, dur=0.25)
    """
    return DrumKit(genre=genre, **kwargs)


def genres():
    """List available genres"""
    return list(_genres.keys())
