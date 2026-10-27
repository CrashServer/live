#!/usr/bin/env python3
"""Grid track generator.

Assembles cells.json atoms into a #@-sectioned attack for the CrashServer
composition system. Output wraps in storageAttack.add() + compo.play().

Usage:
  python3 grid/generate.py [--seed B14] [--bars 208] [--rng 42] [--out path.py]
Also callable as module:
  from grid.generate import generate
  code, meta = generate(cells, seed_coord="B14")
"""
import json, random, re, sys
from datetime import datetime
from pathlib import Path

GRID_DIR = Path(__file__).resolve().parent
CELLS_FILE = GRID_DIR / "cells.json"

BEATS_PER_BAR = 4

# Column → canonical player name fallback (when code can't be parsed)
COL_PLAYER = {
    "A": "p1", "B": "b1", "C": "k1", "D": "s1",
    "E": "h1", "F": "l1", "G": "n1", "H": "n2",
    "I": "m1", "J": "b2", "K": "t1", "L": "v1",
    "M": "m2", "N": "t2",
}

# Column → musical role label (for section annotations in output)
COL_ROLE = {
    "A": "pad", "B": "bass", "C": "kick", "D": "snare",
    "E": "hat", "F": "loop", "G": "lead1", "H": "lead2",
    "I": "stab", "J": "acid", "K": "texture", "L": "vocal",
    "M": "bell", "N": "atmo", "O": "fx", "P": "modular",
}

# Synth name → role column (used to classify atoms extracted from track cells)
_SYNTH_COL = {
    # Bass (B)
    "pumpbass":"B","dbass":"B","subbass":"B","ebass":"B","rsin":"B",
    "qbass":"B","reese":"B","hoover":"B","dirt":"B","bass":"B",
    "303bass":"B","moogbass":"B","fmbass":"B","cbass":"B","fbass":"B",
    # Kick / primary drum (C)
    "compkick":"C","kick808":"C","bdrum":"C","kick":"C","prodrums":"C",
    "compperc":"C","noisehit":"C",
    # Snare / secondary drum (D)
    "snare":"D","sdrum":"D","industrialsnare":"D",
    # Hat (E)
    "hat":"E","hihat":"E","pumphihat":"E","a_hhat":"E",
    # Loop (F)
    "loop":"F",
    # Lead / melody (G)
    "plaitsX":"G","plaits":"G","tb303":"G","braids":"G",
    "supersaw":"G","square":"G","sawtooth":"G","dopple":"G",
    "fmsynth":"G","prophet":"G",
    # Chord stab (I)
    "hardstab":"I","stab":"I","chords":"I","faim":"I",
    # Texture / drone (K)
    "industrialdrone":"K","granular":"K","noise":"K",
    # Pad (A)
    "ethpad":"A","darkpad":"A","stringpad":"A","juno":"A",
    "varsaw":"A","svdk":"A",
    # Bell / keys (M)
    "bell":"M","vibraphone":"M","marimba":"M","pluck":"M","gbell":"M",
    "pianovel":"M","ep":"M","piano":"M","viola":"M","soprano":"M",
    # Atmo (N)
    "a_poly":"N","a_stress":"N","a_gesa2":"N","a_wave":"N",
}

# Synth name substrings → column (for unknown synths not in _SYNTH_COL)
_SYNTH_SUBSTR_COL = [
    ("kick",   "C"), ("drum",  "C"), ("perc",  "D"),
    ("snare",  "D"), ("hat",   "E"), ("hihat", "E"),
    ("bass",   "B"), ("sub",   "B"),
    ("pad",    "A"), ("drone", "K"), ("string","A"),
    ("stab",   "I"), ("chord", "I"),
    ("bell",   "M"), ("piano", "M"),
    ("atmo",   "N"), ("ambi",  "N"),
]

# Player name prefix → fallback column (secondary classifier)
_PLAYER_PREFIX_COL = {
    "p": "A", "b": "B", "k": "C", "s": "D", "h": "E",
    "l": "F", "n": "G", "m": "I", "t": "K", "v": "L",
    "a": "N", "f": "O", "q": "P",
}

# Arc shapes: list of (section_name, bars, active_columns | None=endfade)
# Each section is a DELTA — emit only changes vs previous section.
ARC_DEFAULT = [
    ("intro",   16, ["C", "B"]),
    ("build",   16, ["C", "B", "D", "E"]),
    ("drop1",   32, ["C", "B", "D", "E", "G"]),
    ("peak1",   32, ["C", "B", "D", "E", "G", "A", "I"]),
    ("break",   16, ["C", "B"]),
    ("drop2",   32, ["C", "B", "D", "E", "G", "I"]),
    ("peak2",   32, ["C", "B", "D", "E", "G", "A", "I", "K"]),
    ("outro1",  16, ["C", "B", "D", "E"]),
    ("outro2",  16, ["C", "B"]),
    ("endfade", 16, None),
]

ARC_MINIMAL = [
    ("intro",   16, ["C", "B"]),
    ("build",   24, ["C", "B", "D", "E", "G"]),
    ("peak1",   32, ["C", "B", "D", "E", "G", "A", "I"]),
    ("break",   16, ["B", "N"]),
    ("peak2",   32, ["C", "B", "D", "E", "G", "A", "K"]),
    ("outro",   16, ["C", "B"]),
    ("endfade", 16, None),
]  # 152 bars

ARC_PEAK = [
    ("intro",   16, ["B", "N"]),
    ("buildup", 16, ["C", "B", "D", "E"]),
    ("drop1",   32, ["C", "B", "D", "E", "G", "I"]),
    ("peak1",   32, ["C", "B", "D", "E", "G", "A", "I", "K"]),
    ("riser",   8,  ["C", "B", "M"]),
    ("drop2",   32, ["C", "B", "D", "E", "G", "I"]),
    ("peak2",   40, ["C", "B", "D", "E", "G", "A", "I", "K", "H"]),
    ("break",   16, ["B", "N"]),
    ("finale",  24, ["C", "B", "D", "E", "G", "A", "I"]),
    ("outro",   16, ["C", "B"]),
    ("endfade", 16, None),
]  # 248 bars

# Extension cycle inserted before outro for longer targets
_EXTEND_CYCLE = [
    ("break_x",  16, ["C", "B"]),
    ("drop_x",   32, ["C", "B", "D", "E", "G", "I"]),
    ("peak_x",   32, ["C", "B", "D", "E", "G", "A", "I", "K"]),
]

# Key / root helpers
_NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

_REL_MIN = {
    "C":"A","G":"E","D":"B","A":"F#","E":"C#","B":"G#","F#":"D#",
    "F":"D","Bb":"G","Eb":"C","Ab":"F","Db":"Bb","Gb":"Eb",
}
_REL_MAJ = {v: k for k, v in _REL_MIN.items()}

# Scale aliases that are musically close to "minor"
_MINOR_FAMILY = {"minor","dorian","phrygian","aeolian","harmonicminor","melodicminor","locrian"}
_MAJOR_FAMILY = {"major","lydian","mixolydian","ionian"}

_FOURTH_UP = {
    "C":"F","F":"Bb","Bb":"Eb","Eb":"Ab","Ab":"Db","Db":"F#",
    "G":"C","D":"G","A":"D","E":"A","B":"E","F#":"B","C#":"F#",
}
_FIFTH_UP = {v: k for k, v in _FOURTH_UP.items()}

PLAYER_RE = re.compile(r'^([a-z][a-z]?\d+)\s*>>', re.MULTILINE)
_STOP_LINE_RE = re.compile(r'^[a-z][a-z]?\d+\s*>>\s*None\s*$')
_PLAYER_LINE_RE = re.compile(r'^([a-z][a-z]?\d+)\s*>>\s*(\w+)\s*\(')


# ── key / tempo helpers ──────────────────────────────────────────────────────

def _normalize_root(s):
    """Convert numeric or lowercase root to canonical form ('4' → 'E', 'd' → 'D')."""
    s = s.strip()
    try:
        return _NOTE_NAMES[int(s) % 12]
    except ValueError:
        return s[0].upper() + s[1:]

def normalize_key(s):
    """Return canonical 'Root scale' string or None for unknown/var."""
    if not s:
        return None
    s = s.strip()
    low = s.lower()
    if low in ("", "var", "none") or low.startswith("var "):
        return None
    parts = s.split(None, 1)
    root = _normalize_root(parts[0])
    scale = parts[1].lower() if len(parts) > 1 else "minor"
    return f"{root} {scale}"

def parse_key(s):
    """Return (root, scale) tuple. Both None on failure."""
    norm = normalize_key(s)
    if not norm:
        return None, None
    p = norm.split(None, 1)
    return (p[0], p[1]) if len(p) >= 2 else (p[0], "minor")

def key_score(k1, k2):
    """Compatibility 0.0–1.0 between two (root, scale) pairs."""
    if None in k1 or None in k2:
        return 0.4  # unknown key = soft accept
    r1, s1 = k1
    r2, s2 = k2
    # Chromatic scales mix with anything
    if "chromatic" in s1 or "chromatic" in s2:
        return 0.5
    if r1 == r2 and s1 == s2:
        return 1.0
    if r1 == r2:
        # Same root, different mode — check family proximity
        f1 = s1 in _MINOR_FAMILY
        f2 = s2 in _MINOR_FAMILY
        if f1 == f2:
            return 0.75  # same family (both minor-ish or both major-ish)
        return 0.5       # parallel mode (C major ↔ C minor)
    # Relative major/minor (same key signature)
    if s1 in _MINOR_FAMILY and s2 in _MAJOR_FAMILY and _REL_MAJ.get(r1) == r2:
        return 0.9
    if s1 in _MAJOR_FAMILY and s2 in _MINOR_FAMILY and _REL_MIN.get(r1) == r2:
        return 0.9
    # 4th / 5th relationship (common modulation targets)
    if _FOURTH_UP.get(r1) == r2 or _FIFTH_UP.get(r1) == r2:
        fam_match = (s1 in _MINOR_FAMILY) == (s2 in _MINOR_FAMILY)
        return 0.6 if fam_match else 0.35
    # Different key but same scale family — weakly compatible
    if (s1 in _MINOR_FAMILY and s2 in _MINOR_FAMILY) or \
       (s1 in _MAJOR_FAMILY and s2 in _MAJOR_FAMILY):
        return 0.2
    return 0.1  # different key + different family: still include at low weight

def tempo_score(t1, t2):
    """Compatibility 0.0–1.0 between two BPM values (includes half/double-time)."""
    if not t1 or not t2:
        return 0.4
    # Direct comparison
    d = abs(t1 - t2)
    if d == 0:    return 1.0
    if d <= 5:    return 0.9
    if d <= 10:   return 0.75
    if d <= 20:   return 0.5
    if d <= 30:   return 0.3
    # Half-time / double-time compatibility
    for ratio in (0.5, 2.0):
        d2 = abs(t1 * ratio - t2)
        if d2 == 0:   return 0.75
        if d2 <= 5:   return 0.6
        if d2 <= 10:  return 0.45
    return 0.1


# ── track atom extraction ────────────────────────────────────────────────────

def _player_col_from_synth_and_name(player, synth):
    """Guess grid column from synth name + player name prefix."""
    col = _SYNTH_COL.get(synth)
    if col:
        return col
    # Substring heuristics on synth name
    sl = synth.lower()
    for substr, c in _SYNTH_SUBSTR_COL:
        if substr in sl:
            return c
    # play() / loop() — use player name prefix to guess role
    if synth in ("play", "loop"):
        prefix = re.match(r'^([a-z]+)', player)
        if prefix:
            return _PLAYER_PREFIX_COL.get(prefix.group(1))
        return None
    # Fallback: player name prefix
    prefix = re.match(r'^([a-z]+)', player)
    if prefix:
        return _PLAYER_PREFIX_COL.get(prefix.group(1))
    return None


def extract_track_atoms(cells):
    """Extract individual player stanzas from track-type cells (Q, R, U-Z columns).

    Returns a list of virtual atom dicts, each with:
      _virtual_col, code, key, tempo, label, _source_coord
    """
    atoms = []
    track_coords = [
        k for k, v in cells.items()
        if isinstance(v, dict)
        and v.get("type") == "track"
        and v.get("code", "").strip()
        and k[0] in "QRUVWXYZ"
    ]

    for coord in track_coords:
        cell = cells[coord]
        code = cell.get("code", "")
        key  = cell.get("key", "")
        tempo = cell.get("tempo")

        # Split into lines and group into stanzas.
        # A stanza starts at a 'player >>' line. Within a stanza we track
        # open-parenthesis depth: continuation lines (paren depth > 0) are
        # joined, as are method-chain lines (starting with . or +).
        lines = code.splitlines()
        stanzas = []   # list of (player, synth, [lines])
        cur_player = cur_synth = None
        cur_lines  = []
        paren_depth = 0

        def _paren_delta(s):
            # Count unquoted ( vs ) — good enough for FoxDot code
            return s.count("(") - s.count(")")

        for line in lines:
            stripped = line.strip()
            m = _PLAYER_LINE_RE.match(stripped)

            if m and paren_depth == 0:
                # New top-level player definition — flush previous stanza
                if cur_player and cur_lines:
                    stanzas.append((cur_player, cur_synth, cur_lines))
                cur_player  = m.group(1)
                cur_synth   = m.group(2)
                cur_lines   = [stripped]
                paren_depth = max(0, _paren_delta(stripped))

            elif cur_player:
                if paren_depth > 0:
                    # Inside an open expression — always continue
                    cur_lines.append(stripped)
                    paren_depth = max(0, paren_depth + _paren_delta(stripped))
                elif stripped.startswith('.') or stripped.startswith('+'):
                    # Method chain continuation
                    cur_lines.append(stripped)
                elif not stripped:
                    # Blank line — flush stanza
                    stanzas.append((cur_player, cur_synth, cur_lines))
                    cur_player = cur_synth = None
                    cur_lines  = []
                    paren_depth = 0
                # All other non-blank lines: new statement in same player block
                # (e.g. second line using same player name) — skip silently.

        if cur_player and cur_lines:
            stanzas.append((cur_player, cur_synth, cur_lines))

        for player, synth, stanza_lines in stanzas:
            if not stanza_lines:
                continue
            col = _player_col_from_synth_and_name(player, synth)
            if not col:
                continue
            stanza_code = "\n".join(stanza_lines)
            # Drop stanzas that are malformed: unbalanced parens or too short
            if stanza_code.count("(") != stanza_code.count(")"):
                continue
            if len(stanza_code) < 30:
                continue
            atoms.append({
                "_virtual_col": col,
                "_source_coord": coord,
                "code":  stanza_code,
                "key":   key,
                "tempo": tempo,
                "label": f"{player} from {cell.get('label', coord)}",
                "type":  "atom",
            })

    return atoms


# ── code helpers ─────────────────────────────────────────────────────────────

def extract_players(code):
    """Return ordered list of player names found in code."""
    return list(dict.fromkeys(PLAYER_RE.findall(code)))

def _pick_val(vals):
    for v in vals[1:]:
        if isinstance(v, (int, float)) and v != 0:
            return v
    return max((v for v in vals if isinstance(v, (int, float))), default=vals[0])

def simplify(code):
    """Replace var()/linvar()/sinvar() with single representative values."""
    def sub_lin(m):
        try:
            a, _b = json.loads(m.group(1))
            return str(a)
        except Exception:
            return m.group(0)
    code = re.sub(r'linvar\(\s*(\[[^\]]+\])\s*,\s*[\d.]+\)', sub_lin, code)

    def sub_sin(m):
        try:
            a, b = json.loads(m.group(1))
            return str(round((a + b) / 2, 4))
        except Exception:
            return m.group(0)
    code = re.sub(r'sinvar\(\s*(\[[^\]]+\])\s*,\s*[\d.]+\)', sub_sin, code)

    def sub_var(m):
        try:
            vals = json.loads(m.group(1).replace("(", "[").replace(")", "]"))
            if isinstance(vals, list) and vals:
                return str(_pick_val(vals))
        except Exception:
            pass
        return m.group(0)
    code = re.sub(
        r'(?<!lin)(?<!sin)(?<!exp)var\(\s*(\[[^\]]+\])\s*,\s*[^)]+\)',
        sub_var, code
    )
    return code

def clean_lines(code):
    """Strip indentation, drop blank lines and bare stop-patterns from cell code."""
    lines = []
    for l in code.splitlines():
        l = l.strip()
        if l and not _STOP_LINE_RE.match(l):
            lines.append(l)
    return lines


# ── cell selection ────────────────────────────────────────────────────────────

# Column similarity groups: when primary col has no good match, try siblings
_COL_SIBLINGS = {
    "G": ["H"],        # lead1 ↔ lead2
    "H": ["G"],
    "I": ["J", "M"],   # stab ↔ acid ↔ bell
    "J": ["I"],
    "M": ["I"],
    "A": ["K", "N"],   # pad ↔ texture ↔ atmo
    "K": ["A", "N"],
    "N": ["A", "K"],
    "D": ["E"],        # snare ↔ hat
    "E": ["D"],
    "L": ["G", "H"],   # vocal ↔ lead
}


def find_cell(cells, col, key, tempo, used, rng, track_atoms=None,
              avoid_types=("starter",), allow_reuse_from=None,
              used_src_tracks=None):
    """Pick best compatible cell for (col, key, tempo).

    Searches:
    1. Native column atoms (cells with coord starting with col)
    2. Track-derived atoms matching col (if track_atoms provided)
    3. Sibling columns (softer match)

    allow_reuse_from: set of coords eligible for reuse (played in prior sections)
    used_src_tracks: set of track source coords already used in this section
                     (prevents two atoms from the same track in one section)

    Returns (coord_or_key, cell) or (None, None).
    """
    cur_key = parse_key(key) if isinstance(key, str) else key
    _used_src = used_src_tracks or set()

    def score_cell(cell, bonus=0.0):
        ks = key_score(cur_key, parse_key(cell.get("key", "")))
        ts = tempo_score(tempo, cell.get("tempo"))
        return ks * 0.65 + ts * 0.35 + bonus

    def search_native(target_col, col_bonus=0.0):
        cands = []
        for coord, cell in cells.items():
            if coord[0] != target_col:
                continue
            if coord in used and (allow_reuse_from is None or coord not in allow_reuse_from):
                continue
            if cell.get("type") in avoid_types:
                continue
            if not cell.get("code", "").strip():
                continue
            # Native cells get a small quality bonus over extracted atoms
            s = score_cell(cell, col_bonus + 0.05)
            if s < 0.1:
                continue
            cands.append((s, rng.random(), coord, cell))
        return cands

    def search_atoms(target_col, col_bonus=0.0):
        if not track_atoms:
            return []
        cands = []
        for i, atom in enumerate(track_atoms):
            if atom.get("_virtual_col") != target_col:
                continue
            src = atom.get("_source_coord", "")
            # One atom per source track per section
            if src in _used_src:
                continue
            key_id = f"_atom_{i}"
            if key_id in used:
                continue
            s = score_cell(atom, col_bonus)
            if s < 0.1:
                continue
            cands.append((s, rng.random(), key_id, atom))
        return cands

    # 1. Primary column — native atoms (preferred)
    cands = search_native(col)
    # 2. Primary column — track-derived atoms
    cands += search_atoms(col)

    # 3. Sibling columns (penalised)
    if not cands:
        for sib in _COL_SIBLINGS.get(col, []):
            cands += search_native(sib, col_bonus=-0.1)
            cands += search_atoms(sib, col_bonus=-0.1)

    if not cands:
        return None, None

    cands.sort(reverse=True)
    best_score = cands[0][0]
    top_tier = [c for c in cands if c[0] >= best_score - 0.15]
    _, _, coord, cell = rng.choice(top_tier)
    return coord, cell


# ── main generator ────────────────────────────────────────────────────────────

def generate(cells, seed_coord=None, bars=None, rng_seed=None, swap_prob=0.28,
             max_players=5):
    """Generate a #@-sectioned CrashServer attack from grid cells.

    Returns (code_string, meta_dict).
    """
    rng = random.Random(rng_seed)
    cells = {
        k: v for k, v in cells.items()
        if not k.startswith("_") and isinstance(v, dict) and v.get("code", "").strip()
    }

    # Pre-extract atoms from track-type cells
    track_atoms = extract_track_atoms(cells)

    # Seed: determine initial key + tempo
    if seed_coord and seed_coord in cells:
        seed = cells[seed_coord]
    else:
        anchors = [v for v in cells.values() if v.get("tempo") and normalize_key(v.get("key"))]
        if not anchors:
            # Looser fallback: any cell with tempo
            anchors = [v for v in cells.values() if v.get("tempo")]
        if not anchors:
            return "# generate: no cells with metadata found", {}
        seed = rng.choice(anchors)

    cur_key   = parse_key(seed.get("key", ""))
    cur_tempo = seed.get("tempo") or 130

    # Choose arc shape based on target bars
    target_bars = bars or 208
    if target_bars <= 160:
        arc = list(ARC_MINIMAL)
    elif target_bars >= 240:
        arc = list(ARC_PEAK)
    else:
        arc = list(ARC_DEFAULT)

    # Extend arc if more bars requested
    arc_base = sum(s[1] for s in arc if s[2] is not None) + 16  # +16 for endfade
    if target_bars > arc_base:
        extra = target_bars - arc_base
        reps  = max(1, extra // 80)
        outro_idx = next(
            (i for i, s in enumerate(arc) if "outro" in s[0] or s[2] is None),
            len(arc) - 1
        )
        for _ in range(reps):
            arc[outro_idx:outro_idx] = _EXTEND_CYCLE

    # col_freq: how many arc sections each column appears in (for eviction priority)
    col_freq = {}
    for _, _, t in arc:
        if t:
            for c in t:
                col_freq[c] = col_freq.get(c, 0) + 1

    # ── Section loop ──
    sections    = []    # [(name, bars, [code_lines], {col: (coord, label)})]
    active      = {}    # {col: {"coord": str, "players": [str], "bars_played": int}}
    used        = set() # coords/atom-keys already placed
    cold_used   = {}    # coord → bars_when_used (for reuse eligibility after gap)
    bars_so_far = 0
    did_root_shift    = False
    did_scale_shift   = False
    first_section     = True
    root_str, scale_str = cur_key[0] or "C", cur_key[1] or "minor"

    for (sec_name, sec_bars, target_cols) in arc:
        code_lines    = []
        cell_notes    = {}   # col → "coord: label" for the section comment
        sec_src_used  = set()  # source track coords used in this section (atom diversity)

        # endfade: FoxDot fade+clear — just emit the tag
        if target_cols is None:
            sections.append((sec_name, sec_bars, [], {}))
            break

        # Allow reuse of cells placed > 3 sections ago
        reuse_eligible = {
            coord for coord, bar in cold_used.items()
            if bars_so_far - bar >= 96  # ~3 sections
        }

        # Root shift at first break section
        if "break" in sec_name and not did_root_shift:
            # Prefer 4th up; occasionally try 5th
            new_root = (_FIFTH_UP if rng.random() < 0.25 else _FOURTH_UP).get(
                cur_key[0], cur_key[0]
            )
            if new_root != cur_key[0]:
                cur_key  = (new_root, cur_key[1])
                root_str = new_root
                code_lines.append(f'Root.default = "{root_str}"')
                did_root_shift = True
                for col in active:
                    if col in ("G", "H", "A", "I", "M"):
                        active[col]["_force_swap"] = True

        # Parallel mode shift at a peak section (occasional colour change)
        if "peak" in sec_name and not did_scale_shift and rng.random() < 0.35:
            new_scale = "major" if scale_str in _MINOR_FAMILY else "minor"
            cur_key    = (cur_key[0], new_scale)
            scale_str  = new_scale
            code_lines.append(f'Scale.default = "{scale_str}"')
            did_scale_shift = True
            for col in active:
                if col in ("G", "H"):
                    active[col]["_force_swap"] = True

        # Arc-driven removes: cols no longer in target
        cols_remove = [c for c in list(active) if c not in target_cols]
        cols_add    = [c for c in target_cols if c not in active]
        cols_swap   = [
            c for c in target_cols if c in active and (
                active[c].pop("_force_swap", False) or (
                    c not in ("C", "B") and rng.random() < swap_prob
                )
            )
        ]
        cols_swap = [c for c in cols_swap if c not in cols_add]

        stops = []
        for col in cols_remove:
            stops.extend(active[col]["players"])
            cold_used[active[col]["coord"]] = bars_so_far
            del active[col]

        # Organic eviction: respect max_players cap
        if max_players:
            for col in cols_add:
                if len(active) >= max_players:
                    victim = min(
                        active.keys(),
                        key=lambda c: (col_freq.get(c, 0), -active[c].get("bars_played", 0))
                    )
                    stops.extend(active[victim]["players"])
                    cold_used[active[victim]["coord"]] = bars_so_far
                    del active[victim]

        if stops:
            code_lines.append("; ".join(f"{p}.stop()" for p in stops))

        # Emit new or swapped cells
        for col in cols_add + cols_swap:
            coord, cell = find_cell(
                cells, col,
                f"{root_str} {scale_str}", cur_tempo,
                used, rng,
                track_atoms=track_atoms,
                allow_reuse_from=reuse_eligible,
                used_src_tracks=sec_src_used,
            )
            if coord is None:
                continue

            raw_code = simplify(cell.get("code", "").strip())
            players  = extract_players(raw_code) or [COL_PLAYER.get(col, "x1")]

            # Remap primary player to canonical convention for this column
            canonical = COL_PLAYER.get(col)
            if canonical and players and players[0] != canonical:
                old_name = players[0]
                raw_code = re.sub(r'\b' + re.escape(old_name) + r'\b', canonical, raw_code)
                players  = [canonical] + players[1:]

            # Stop displaced players on swap
            if col in active:
                displaced = set(active[col]["players"]) - set(players)
                if displaced:
                    code_lines.append("; ".join(f"{p}.stop()" for p in displaced))

            code_lines.extend(clean_lines(raw_code))
            used.add(coord)
            if coord.startswith("_atom_"):
                src = cell.get("_source_coord", "")
                if src:
                    sec_src_used.add(src)  # prevent multiple atoms from same track this section
                # Shorten label: strip long code-timestamp filenames
                lbl = cell.get("label", "?")
                lbl = re.sub(r'\bcode_\d{8}T\d+\b', '<track>', lbl)
                cell_notes[col] = f"{src}→{lbl}"
            else:
                cell_notes[col] = f"{coord}: {cell.get('label', '')}"
            active[col] = {"coord": coord, "players": players, "bars_played": bars_so_far}

        # Prepend Clock/Root/Scale to first non-empty section
        if first_section and code_lines:
            code_lines = [
                f"Clock.bpm = {cur_tempo}",
                f'Root.default = "{root_str}"',
                f'Scale.default = "{scale_str}"',
            ] + code_lines
            first_section = False

        sections.append((sec_name, sec_bars, code_lines, cell_notes))
        bars_so_far += sec_bars

    # ── Assemble output ──
    ts    = datetime.now().strftime("%Y%m%d_%H%M")
    name  = f"gen_{ts}"
    total_bars  = sum(s[1] for s in sections)
    total_beats = total_bars * BEATS_PER_BAR

    out = [f'storageAttack.add("{name}", """']
    for (sec_name, sec_bars, code_lines, cell_notes) in sections:
        out.append(f"#@{sec_name}({sec_bars * BEATS_PER_BAR})")
        # Annotation: which cells are active in this section
        if cell_notes:
            note_parts = [
                f"{COL_ROLE.get(col, col)}={info}" for col, info in sorted(cell_notes.items())
            ]
            out.append("# " + " | ".join(note_parts))
        out.extend(code_lines)
        out.append("")
    out.append('""")')
    out.append(f'compo.play("{name}", seq=True)')

    meta = {
        "name":        name,
        "bars":        total_bars,
        "beats":       total_beats,
        "tempo":       cur_tempo,
        "key":         f"{root_str} {scale_str}",
        "cells_used":  len([c for c in used if not c.startswith("_atom_")]),
        "atoms_used":  len([c for c in used if c.startswith("_atom_")]),
        "track_atoms": len(track_atoms),
        "sections":    len(sections),
        "line_count":  len(out),
    }
    return "\n".join(out), meta


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Generate a grid-based FoxDot attack")
    ap.add_argument("--seed",  default=None,  help="Seed cell coord (e.g. B14)")
    ap.add_argument("--bars",  type=int, default=None, help="Target bars (default 208)")
    ap.add_argument("--rng",   type=int, default=None, help="RNG seed for reproducibility")
    ap.add_argument("--out",   default=None,  help="Output file (default: stdout)")
    ap.add_argument("--info",  action="store_true", help="Show extraction stats and exit")
    args = ap.parse_args()

    cells = json.loads(CELLS_FILE.read_text())

    if args.info:
        atoms = extract_track_atoms({k: v for k, v in cells.items() if not k.startswith("_")})
        from collections import Counter
        col_ct = Counter(a["_virtual_col"] for a in atoms)
        print(f"Track atoms extracted: {len(atoms)}")
        for col in sorted(col_ct):
            print(f"  {col} ({COL_ROLE.get(col, '?')}): {col_ct[col]}")
        return

    code, meta = generate(cells, seed_coord=args.seed, bars=args.bars, rng_seed=args.rng)

    if args.out:
        Path(args.out).write_text(code)
        print(
            f"→ {args.out}  "
            f"({meta['bars']} bars | {meta['cells_used']} cells + {meta['atoms_used']} atoms"
            f" | {meta['sections']} sections | {meta['line_count']} lines)"
        )
    else:
        print(code)


if __name__ == "__main__":
    main()
