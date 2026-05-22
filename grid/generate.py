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

# Arc: (section_name, bars, active_columns | None=endfade)
# Each section is a DELTA — generator emits only changes vs previous section.
# Columns not listed → players silenced. Columns added → new cell picked.
# Columns continuing → kept (or optionally swapped for variety).
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
# Default total: 208 bars = 832 beats

# Column priority for max_players trimming (lower = kept longer)
COL_PRIORITY = {
    "C": 1, "B": 2, "D": 3, "E": 4, "G": 5,
    "H": 6, "I": 7, "A": 8, "J": 9, "K": 10,
    "F": 11, "M": 12, "N": 13, "L": 14,
}

def _top_cols(cols, n):
    """Return up to n columns sorted by COL_PRIORITY (keep highest-priority)."""
    return sorted(cols, key=lambda c: COL_PRIORITY.get(c, 99))[:n]

# Extension cycle inserted before outro for longer tracks
_EXTEND_CYCLE = [
    ("break_x",  16, ["C", "B"]),
    ("drop_x",   32, ["C", "B", "D", "E", "G", "I"]),
    ("peak_x",   32, ["C", "B", "D", "E", "G", "A", "I", "K"]),
]

# Key relationship maps
_REL_MIN = {
    "C":"A","G":"E","D":"B","A":"F#","E":"C#","B":"G#","F#":"D#",
    "F":"D","Bb":"G","Eb":"C","Ab":"F","Db":"Bb","Gb":"Eb",
}
_REL_MAJ = {v: k for k, v in _REL_MIN.items()}

# Break root shifts: up a 4th (lifts the energy)
_FOURTH_UP = {
    "C":"F","F":"Bb","Bb":"Eb","Eb":"Ab","Ab":"Db","Db":"F#",
    "G":"C","D":"G","A":"D","E":"A","B":"E","F#":"B","C#":"F#",
}

PLAYER_RE = re.compile(r'^([a-z][a-z]?\d+)\s*>>', re.MULTILINE)


# ── key / tempo helpers ──────────────────────────────────────────────────────

def parse_key(s):
    """'D minor' → ('D', 'minor'). Returns (None, None) on failure."""
    if not s:
        return None, None
    p = s.strip().split()
    return (p[0], p[1].lower()) if len(p) >= 2 else (p[0], "minor")

def key_score(k1, k2):
    """Compatibility 0.0–1.0 between two (root, scale) pairs."""
    if None in k1 or None in k2:
        return 0.5
    r1, s1 = k1
    r2, s2 = k2
    if r1 == r2 and s1 == s2:
        return 1.0
    if r1 == r2:
        return 0.6  # same root, parallel mode
    if s1 == "minor" and s2 == "major" and _REL_MAJ.get(r1) == r2:
        return 0.9
    if s1 == "major" and s2 == "minor" and _REL_MIN.get(r1) == r2:
        return 0.9
    return 0.0

def tempo_score(t1, t2):
    """Compatibility 0.0–1.0 between two BPM values."""
    if not t1 or not t2:
        return 0.5
    d = abs(t1 - t2)
    if d == 0:    return 1.0
    if d <= 5:    return 0.9
    if d <= 10:   return 0.7
    if d <= 20:   return 0.4
    return 0.0


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
    """Strip indentation, drop blank lines, return list of non-empty lines."""
    return [l.strip() for l in code.splitlines() if l.strip()]


# ── cell selection ────────────────────────────────────────────────────────────

def find_cell(cells, col, key, tempo, used, rng, avoid_types=("starter",)):
    """Pick best compatible cell for (col, key, tempo). Returns (coord, cell) or (None, None)."""
    cands = []
    for coord, cell in cells.items():
        if coord[0] != col:
            continue
        if coord in used:
            continue
        if cell.get("type") in avoid_types:
            continue
        if not cell.get("code", "").strip():
            continue
        ks = key_score(key, parse_key(cell.get("key", "")))
        ts = tempo_score(tempo, cell.get("tempo"))
        if ks == 0.0:
            continue
        cands.append((ks * 0.65 + ts * 0.35, rng.random(), coord, cell))

    if not cands:
        return None, None

    cands.sort(reverse=True)
    best_score = cands[0][0]
    top_tier = [c for c in cands if c[0] >= best_score - 0.15]
    _, _, coord, cell = rng.choice(top_tier)
    return coord, cell


# ── main generator ────────────────────────────────────────────────────────────

def generate(cells, seed_coord=None, bars=None, rng_seed=None, swap_prob=0.28, max_players=5):
    """
    Generate a #@-sectioned CrashServer attack from grid cells.

    Returns (code_string, meta_dict).
    code_string: storageAttack.add("gen_...", \"\"\"...\"\"\") + compo.play(...)
    """
    rng = random.Random(rng_seed)
    # Filter to usable cells only
    cells = {
        k: v for k, v in cells.items()
        if not k.startswith("_") and v.get("code", "").strip()
    }

    # Seed: determine initial key + tempo
    if seed_coord and seed_coord in cells:
        seed = cells[seed_coord]
    else:
        anchors = [v for v in cells.values() if v.get("tempo") and v.get("key")]
        if not anchors:
            return "# generate: no cells with key+tempo metadata found", {}
        seed = rng.choice(anchors)

    cur_key   = parse_key(seed.get("key", ""))
    cur_tempo = seed.get("tempo") or 130

    # Build arc (extend if longer track requested)
    arc = list(ARC_DEFAULT)
    if bars and bars > 208:
        extra = bars - 208
        reps  = max(1, extra // 80)
        outro_idx = next(i for i, s in enumerate(arc) if s[0] == "outro1")
        for _ in range(reps):
            arc[outro_idx:outro_idx] = _EXTEND_CYCLE

    # ── Section loop ──
    sections = []   # [(name, bars, [code_lines])]
    active   = {}   # {col: {"coord": str, "players": [str]}}
    used     = set()
    did_root_shift = False
    first_section  = True
    root_str, scale_str = cur_key[0] or "C", cur_key[1] or "minor"

    for (sec_name, sec_bars, target_cols) in arc:
        code_lines = []

        # endfade: FoxDot handles fade+clear — just emit the tag with no code
        if target_cols is None:
            sections.append((sec_name, sec_bars, []))
            break

        # Root shift at first break section
        if "break" in sec_name and not did_root_shift:
            new_root = _FOURTH_UP.get(cur_key[0], cur_key[0])
            if new_root != cur_key[0]:
                cur_key    = (new_root, cur_key[1])
                root_str   = new_root
                code_lines.append(f'Root.default = "{root_str}"')
                did_root_shift = True
                # Force melodic/harmonic cols to swap to fit new root
                for col in active:
                    if col in ("G", "H", "A", "I"):
                        active[col]["_force_swap"] = True

        # Apply max_players: keep only the highest-priority columns
        effective = _top_cols(target_cols, max_players) if max_players else list(target_cols)

        cols_remove = [c for c in active if c not in effective]
        cols_add    = [c for c in effective if c not in active]
        cols_swap   = [
            c for c in effective if c in active and (
                active[c].pop("_force_swap", False) or (
                    c != "C" and rng.random() < swap_prob
                )
            )
        ]
        cols_swap = [c for c in cols_swap if c not in cols_add]

        # Stop removed players — all on one line, using .stop()
        stops = []
        for col in cols_remove:
            stops.extend(active[col]["players"])
            del active[col]
        if stops:
            code_lines.append("; ".join(f"{p}.stop()" for p in stops))

        # Emit new or swapped cells
        for col in cols_add + cols_swap:
            coord, cell = find_cell(cells, col, cur_key, cur_tempo, used, rng)
            if coord is None:
                continue

            code    = simplify(cell.get("code", "").strip())
            players = extract_players(code) or [COL_PLAYER.get(col, "x1")]

            # Remap primary player name to canonical convention for this column.
            canonical = COL_PLAYER.get(col)
            if canonical and players and players[0] != canonical:
                old_name = players[0]
                code = re.sub(r'\b' + re.escape(old_name) + r'\b', canonical, code)
                players = [canonical] + players[1:]

            # Stop any displaced players on swap
            if col in active:
                displaced = set(active[col]["players"]) - set(players)
                if displaced:
                    code_lines.append("; ".join(f"{p}.stop()" for p in displaced))

            code_lines.extend(clean_lines(code))
            used.add(coord)
            active[col] = {"coord": coord, "players": players}

        # Prepend Clock/Root/Scale to first non-empty section
        if first_section and code_lines:
            code_lines = [
                f"Clock.bpm = {cur_tempo}",
                f'Root.default = "{root_str}"',
                f'Scale.default = "{scale_str}"',
            ] + code_lines
            first_section = False

        sections.append((sec_name, sec_bars, code_lines))

    # ── Assemble output ──
    ts    = datetime.now().strftime("%Y%m%d_%H%M")
    name  = f"gen_{ts}"
    total_bars  = sum(s[1] for s in sections)
    total_beats = total_bars * BEATS_PER_BAR

    out = [f'storageAttack.add("{name}", """']
    for (sec_name, sec_bars, code_lines) in sections:
        out.append(f"#@{sec_name}({sec_bars * BEATS_PER_BAR})")
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
        "cells_used":  len(used),
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
    args = ap.parse_args()

    cells = json.loads(CELLS_FILE.read_text())
    code, meta = generate(cells, seed_coord=args.seed, bars=args.bars, rng_seed=args.rng)

    if args.out:
        Path(args.out).write_text(code)
        print(f"→ {args.out}  ({meta['bars']} bars | {meta['cells_used']} cells | {meta['sections']} sections | {meta['line_count']} lines)")
    else:
        print(code)


if __name__ == "__main__":
    main()
