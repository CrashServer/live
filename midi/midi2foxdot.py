#!/usr/bin/env python3
"""
midi2foxdot.py — Convert MIDI files to FoxDot live coding patterns.

Usage:
    python midi2foxdot.py file.mid
    python midi2foxdot.py file.mid --scale minor --root D
    python midi2foxdot.py file.mid --tracks 0,1,3
    python midi2foxdot.py file.mid --bars 1-8
"""

import struct
import sys
import os
from collections import defaultdict, Counter
from fractions import Fraction
from math import gcd

# --- MIDI binary parser (no dependencies) ---

def read_varlen(data, pos):
    """Read MIDI variable-length quantity."""
    result = 0
    while True:
        byte = data[pos]
        result = (result << 7) | (byte & 0x7F)
        pos += 1
        if not (byte & 0x80):
            break
    return result, pos

def parse_midi(filepath):
    """Parse a MIDI file into tracks with note events."""
    with open(filepath, 'rb') as f:
        data = f.read()

    pos = 0
    assert data[pos:pos+4] == b'MThd', "Not a MIDI file"
    pos += 4
    header_len = struct.unpack('>I', data[pos:pos+4])[0]
    pos += 4
    fmt = struct.unpack('>H', data[pos:pos+2])[0]
    num_tracks = struct.unpack('>H', data[pos+2:pos+4])[0]
    ticks_per_beat = struct.unpack('>H', data[pos+4:pos+6])[0]
    pos += header_len

    tracks = []
    for t in range(num_tracks):
        assert data[pos:pos+4] == b'MTrk', f"Expected MTrk at {pos}"
        pos += 4
        track_len = struct.unpack('>I', data[pos:pos+4])[0]
        pos += 4
        track_end = pos + track_len

        events = []
        tick = 0
        running_status = 0
        track_name = f"Track {t}"

        while pos < track_end:
            delta, pos = read_varlen(data, pos)
            tick += delta

            byte = data[pos]

            if byte == 0xFF:
                pos += 1
                meta_type = data[pos]
                pos += 1
                meta_len, pos = read_varlen(data, pos)
                meta_data = data[pos:pos+meta_len]
                pos += meta_len
                if meta_type == 0x03:
                    track_name = meta_data.decode('ascii', errors='replace').strip()
                elif meta_type == 0x51:
                    tempo = struct.unpack('>I', b'\x00' + meta_data[:3])[0]
                    events.append({'type': 'tempo', 'tick': tick, 'bpm': 60000000 / tempo})
                continue

            if byte == 0xF0 or byte == 0xF7:
                pos += 1
                sysex_len, pos = read_varlen(data, pos)
                pos += sysex_len
                continue

            if byte & 0x80:
                status = byte
                pos += 1
                running_status = status
            else:
                status = running_status

            msg_type = status & 0xF0
            channel = status & 0x0F

            if msg_type in (0x80, 0x90, 0xA0, 0xB0, 0xE0):
                d1 = data[pos]
                pos += 1
                d2 = data[pos]
                pos += 1
                if msg_type == 0x90 and d2 > 0:
                    events.append({'type': 'note_on', 'tick': tick, 'note': d1, 'vel': d2, 'ch': channel})
                elif msg_type == 0x80 or (msg_type == 0x90 and d2 == 0):
                    events.append({'type': 'note_off', 'tick': tick, 'note': d1, 'ch': channel})
            elif msg_type in (0xC0, 0xD0):
                pos += 1
            else:
                if pos < track_end:
                    pos += 1

        tracks.append({'name': track_name, 'events': events})

    return {'format': fmt, 'ticks_per_beat': ticks_per_beat, 'tracks': tracks}


# --- Scale/Note analysis ---

SCALE_TEMPLATES = {
    'major':            [0, 2, 4, 5, 7, 9, 11],
    'minor':            [0, 2, 3, 5, 7, 8, 10],
    'phrygian':         [0, 1, 3, 5, 7, 8, 10],
    'dorian':           [0, 2, 3, 5, 7, 9, 10],
    'mixolydian':       [0, 2, 4, 5, 7, 9, 10],
    'harmonicMinor':    [0, 2, 3, 5, 7, 8, 11],
    'minorPentatonic':  [0, 3, 5, 7, 10],
    'majorPentatonic':  [0, 2, 4, 7, 9],
    'blues':            [0, 3, 5, 6, 7, 10],
    'chromatic':        list(range(12)),
}

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def detect_scale(notes):
    """Detect best scale and root from MIDI note numbers."""
    pitch_classes = set(n % 12 for n in notes)
    best_score = -1
    best_root = 0
    best_scale = 'chromatic'

    for root in range(12):
        for name, template in SCALE_TEMPLATES.items():
            if name == 'chromatic':
                continue
            shifted = set((s + root) % 12 for s in template)
            overlap = len(pitch_classes & shifted)
            outside = len(pitch_classes - shifted)
            score = overlap * 2 - outside * 3
            if score > best_score:
                best_score = score
                best_root = root
                best_scale = name

    return best_root, best_scale


def midi_to_degree(note, root, scale_template):
    """Convert MIDI note to FoxDot degree + octave."""
    midi_octave = note // 12
    foxdot_oct = midi_octave
    pc = (note - root) % 12

    if pc in scale_template:
        degree = scale_template.index(pc)
    else:
        dists = [(min(abs(pc - s), 12 - abs(pc - s)), i)
                 for i, s in enumerate(scale_template)]
        degree = min(dists)[1]

    return degree, foxdot_oct


# --- Duration quantization ---

GRID_VALUES = [
    Fraction(4),      # whole
    Fraction(3),      # dotted half
    Fraction(2),      # half
    Fraction(3, 2),   # dotted quarter
    Fraction(1),      # quarter
    Fraction(3, 4),   # dotted eighth
    Fraction(1, 2),   # eighth
    Fraction(1, 3),   # triplet quarter
    Fraction(3, 8),   # dotted sixteenth
    Fraction(1, 4),   # sixteenth
    Fraction(1, 6),   # triplet eighth
    Fraction(1, 8),   # thirty-second
]


def ticks_to_dur(ticks, tpb):
    """Convert tick duration to nearest musical grid value."""
    if ticks <= 0:
        return Fraction(1, 8)
    raw = Fraction(ticks, tpb)
    best = min(GRID_VALUES, key=lambda g: abs(float(raw) - float(g)))
    if abs(float(raw) - float(best)) / max(float(best), 0.01) < 0.35:
        return best
    if float(raw) > 4:
        return Fraction(round(float(raw) * 2), 2)
    return best


def simplify_dur(dur):
    """Format a Fraction as FoxDot duration string."""
    if dur == 0:
        return 'rest'
    if dur.denominator == 1:
        return str(dur.numerator)
    nice = {
        Fraction(3, 2): '3/2', Fraction(3, 4): '3/4', Fraction(3, 8): '3/8',
        Fraction(1, 2): '1/2', Fraction(1, 3): '1/3', Fraction(1, 4): '1/4',
        Fraction(1, 6): '1/6', Fraction(1, 8): '1/8', Fraction(2, 3): '2/3',
    }
    if dur in nice:
        return nice[dur]
    return f'{dur.numerator}/{dur.denominator}'


# --- Pattern compression engine ---

def format_val(v):
    """Format a single value for FoxDot output."""
    if isinstance(v, tuple):
        # PGroup: (0,2,4) → "(0,2,4)"
        inner = ','.join(format_val(x) for x in v)
        return f'({inner})'
    if isinstance(v, Fraction):
        return simplify_dur(v)
    if v == 'rest':
        return 'rest(0)'
    return str(v)


def find_repeating_unit(values):
    """Find shortest repeating sub-pattern. Returns (unit, reps).
    Allows fuzzy last repetition (truncated or slightly different)."""
    n = len(values)
    # First try exact divisors
    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue
        unit = values[:size]
        if all(values[i:i+size] == unit for i in range(0, n, size)):
            return unit, n // size

    # Try non-exact: allow truncated last repetition
    for size in range(2, n // 2 + 1):
        unit = values[:size]
        full_reps = n // size
        if full_reps < 2:
            continue
        remainder = n % size
        match = True
        for i in range(size, full_reps * size, size):
            if values[i:i+size] != unit:
                match = False
                break
        if not match:
            continue
        if remainder > 0 and values[full_reps * size:] != unit[:remainder]:
            continue
        return unit, full_reps

    # Fuzzy: allow last full repetition to differ (1 mismatch tolerance)
    for size in range(2, n // 2 + 1):
        if n % size != 0:
            continue
        unit = values[:size]
        reps = n // size
        if reps < 3:
            continue
        mismatch_count = 0
        for i in range(size, n, size):
            if values[i:i+size] != unit:
                mismatch_count += 1
        if mismatch_count <= 1:
            return unit, reps

    return values, 1


def find_near_repeating(values, tolerance=0.15):
    """Find repeating unit allowing small variations (for amp/vel)."""
    n = len(values)
    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue
        unit = values[:size]
        match = True
        for i in range(size, n, size):
            chunk = values[i:i+size]
            for a, b in zip(unit, chunk):
                try:
                    if abs(float(a) - float(b)) > tolerance:
                        match = False
                        break
                except (ValueError, TypeError):
                    if str(a) != str(b):
                        match = False
                        break
            if not match:
                break
        if match:
            return unit, n // size
    return values, 1


def run_length_encode(strs):
    """Group consecutive identical values: [0,0,0,1,1] -> [(0,3),(1,2)]."""
    if not strs:
        return []
    runs = []
    current = strs[0]
    count = 1
    for v in strs[1:]:
        if v == current:
            count += 1
        else:
            runs.append((current, count))
            current = v
            count = 1
    runs.append((current, count))
    return runs


def try_pstutter(strs):
    """Try PStutter compression. Only use if result is shorter than raw list."""
    runs = run_length_encode(strs)
    has_repeats = any(c > 1 for _, c in runs)
    if not has_repeats:
        return None

    vals = [r[0] for r in runs]
    counts = [r[1] for r in runs]

    if all(c == counts[0] for c in counts):
        candidate = f'PStutter([{",".join(vals)}],{counts[0]})'
    else:
        candidate = f'PStutter([{",".join(vals)}],[{",".join(str(c) for c in counts)}])'

    raw = '[' + ','.join(strs) + ']'
    # Allow PStutter if it's within 10% of raw length — readability > saving 2 chars
    if len(candidate) > len(raw) * 1.1:
        return None
    # But only use if it actually compresses (has repeats worth showing)
    if max(counts) < 2:
        return None

    return candidate


def try_pdur(values):
    """Detect if a duration pattern matches PDur(n, k) — Euclidean rhythm.
    Very common in electronic/dance music. PDur(3,8), PDur(5,8) etc."""
    if not all(isinstance(v, Fraction) for v in values):
        return None
    n_events = len(values)
    if n_events < 2 or n_events > 16:
        return None

    total = sum(values)
    # PDur sums to a whole number of beats (typically 1, 2, or 4)
    if total.denominator not in (1, 2):
        return None

    # PDur has exactly 2 unique durations: short and long, where long = 2*short
    unique = sorted(set(values))
    if len(unique) != 2:
        return None
    short, long = unique
    if long != 2 * short:
        return None

    # Count pulses (short notes) and total steps
    # In PDur(n,k): k = total_steps, n = number of pulses
    # Each short = 1 step, each long = 2 steps
    n_short = sum(1 for v in values if v == short)
    n_long = sum(1 for v in values if v == long)
    k = n_short + n_long * 2  # total grid steps

    # Verify with Bjorklund: distribute n_events pulses over k steps
    # The number of long gaps = k - n_events
    if n_long != k - n_events:
        return None

    # Check if dur value matches: short should be total/k or a multiple
    expected_short = total / k
    if short != expected_short:
        return None

    # Build PDur string — use standard FoxDot PDur(n, k) form
    # dur=0.25 is the default, so PDur(n,k) works if short=0.25
    if short == Fraction(1, 4):
        return f'PDur({n_events},{k})'
    elif short == Fraction(1, 2):
        return f'PDur({n_events},{k})*2'
    elif short == Fraction(1, 8):
        return f'PDur({n_events},{k})/2'
    else:
        return f'PDur({n_events},{k},dur={format_val(short)})'


def try_prange(values):
    """Detect ascending/descending integer runs → PRange(start, stop, step)."""
    if len(values) < 4:
        return None
    if not all(isinstance(v, int) for v in values):
        return None
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    if len(set(diffs)) != 1:
        return None
    step = diffs[0]
    if step == 0:
        return None
    if step == 1:
        return f'PRange({values[0]},{values[-1]+1})'
    if step == -1:
        return f'PRange({values[0]},{values[-1]-1},-1)'
    return f'PRange({values[0]},{values[-1]+step},{step})'


def try_ptri(values):
    """Detect triangle patterns (up then down) → PTri(start, stop)."""
    if len(values) < 5:
        return None
    if not all(isinstance(v, int) for v in values):
        return None
    # Find the peak
    peak_idx = values.index(max(values))
    if peak_idx == 0 or peak_idx == len(values) - 1:
        return None
    up = values[:peak_idx+1]
    down = values[peak_idx:]
    # Check ascending part
    up_diffs = [up[i+1] - up[i] for i in range(len(up)-1)]
    if not up_diffs or len(set(up_diffs)) != 1 or up_diffs[0] != 1:
        return None
    # Check descending part
    down_diffs = [down[i+1] - down[i] for i in range(len(down)-1)]
    if not down_diffs or len(set(down_diffs)) != 1 or down_diffs[0] != -1:
        return None
    # Verify it's symmetric (PTri goes up and back down to start)
    if values[0] == values[-1]:
        return f'PTri({values[0]},{values[peak_idx]+1})'
    return None


def try_alternating(strs):
    """Detect short cycling patterns that FoxDot auto-repeats.
    [0,5,0,5,0,5] → [0,5] since FoxDot cycles lists."""
    n = len(strs)
    if n < 4:
        return None
    for cycle_len in [2, 3, 4]:
        if n < cycle_len * 2:
            continue
        cycle = strs[:cycle_len]
        # Cycle must have >1 unique value (otherwise compress_pattern scalar handles it)
        if len(set(cycle)) <= 1:
            continue
        # Check how many full cycles match
        full_cycles = n // cycle_len
        match_count = 0
        for i in range(0, full_cycles * cycle_len, cycle_len):
            if strs[i:i+cycle_len] == cycle:
                match_count += 1
        # Require >80% match rate
        if match_count >= max(full_cycles - 1, full_cycles * 4 // 5) and match_count >= 3:
            return '[' + ','.join(cycle) + ']'
    return None


def try_pstep(strs, values):
    """Detect sparse patterns → PStep(n, value, default).
    [0,0,0,1,0,0,0,1] → PStep(4,1)"""
    if len(values) < 4:
        return None
    counts = Counter(strs)
    if len(counts) != 2:
        return None
    (default_val, default_count), (step_val, step_count) = counts.most_common(2)
    if step_count >= default_count:
        return None
    # Check if step_val appears at regular intervals
    positions = [i for i, s in enumerate(strs) if s == step_val]
    if len(positions) < 2:
        return None
    gaps = [positions[i+1] - positions[i] for i in range(len(positions)-1)]
    if len(set(gaps)) == 1:
        interval = gaps[0]
        offset = positions[0]
        if default_val == '0':
            if offset == 0:
                return f'PStep({interval},{step_val})'
            else:
                return f'PStep({interval},{step_val},0,{offset})'
    return None


def detect_var_sections(values, durs):
    """Detect sectional patterns expressible as var() or Pvar().
    Greedy scanner: for each motif length, scans forward finding consecutive
    runs of the same motif, building sections. Picks the best compression.
    Returns var/Pvar string or None."""
    n = len(values)
    if n < 8:
        return None

    strs = [format_val(v) for v in values]
    raw = '[' + ','.join(strs) + ']'
    raw_len = len(raw)

    best_result = None
    best_score = raw_len  # lower is better

    # Try all reasonable motif lengths — greedy scan is O(N) per length
    max_motif = min(128, n // 2)
    motif_lengths = list(range(2, max_motif + 1))

    for motif_len in motif_lengths:
        sections = []  # [(motif_strs, count_of_cycles)]
        i = 0

        while i < n:
            if i + motif_len > n:
                # Remaining tail — ignore
                break

            motif = strs[i:i+motif_len]
            count = 0
            j = i
            while j + motif_len <= n and strs[j:j+motif_len] == motif:
                count += 1
                j += motif_len

            sections.append((motif, count))
            i = j

        if not sections or len(sections) < 2:
            continue

        # Calculate coverage: what % of values are in repeating sections?
        repeating_values = sum(c * motif_len for _, c in sections if c >= 2)
        total_values = sum(c * motif_len for _, c in sections)
        if total_values == 0:
            continue
        coverage = repeating_values / total_values
        # Need at least 20% of values in repeating sections to be worthwhile
        if coverage < 0.2:
            continue

        # Identify unique motifs and build section sequence
        unique_motifs = []
        motif_index = {}
        for motif, count in sections:
            key = tuple(motif)
            if key not in motif_index:
                motif_index[key] = len(unique_motifs)
                unique_motifs.append(motif)

        if len(unique_motifs) > 12:
            continue

        # Merge consecutive single-occurrence sections into one combined section
        merged = []
        i_s = 0
        while i_s < len(sections):
            motif, count = sections[i_s]
            if count >= 2:
                merged.append((motif, count))
                i_s += 1
            else:
                # Collect consecutive singles into one combined section
                combined = list(motif)
                i_s += 1
                while i_s < len(sections) and sections[i_s][1] == 1:
                    combined.extend(sections[i_s][0])
                    i_s += 1
                merged.append((combined, 1))
        sections = merged

        # Calculate beats per section
        beat_sections = []
        dur_idx = 0
        for motif, count in sections:
            section_beats = Fraction(0)
            events_in_section = count * len(motif) if count >= 2 else len(motif)
            for k in range(events_in_section):
                if dur_idx + k < len(durs):
                    section_beats += durs[dur_idx + k]
            dur_idx += events_in_section
            beat_sections.append((motif, count, float(section_beats)))

        # Check for repeating section pattern (ABAB, AABBAABB, etc.)
        sec_keys = [tuple(s[0]) for s in beat_sections]
        for sec_size in range(2, len(beat_sections) // 2 + 1):
            sec_unit = sec_keys[:sec_size]
            sec_reps = len(beat_sections) // sec_size
            if sec_reps < 2:
                continue
            is_repeating = all(
                sec_keys[r*sec_size:(r+1)*sec_size] == sec_unit
                for r in range(1, sec_reps)
            )
            if is_repeating:
                beat_sections = beat_sections[:sec_size]
                break

        # Build var() or Pvar() string
        # Use Pvar when motifs are lists (patterns), var when scalar
        motif_parts = []
        beat_parts = []
        for motif, count, beats in beat_sections:
            compressed = compress_motif(motif)
            motif_parts.append(compressed)
            if beats == int(beats):
                beat_parts.append(str(int(beats)))
            else:
                beat_parts.append(str(beats))

        # Choose Pvar (for pattern values) vs var
        has_lists = any('[' in p for p in motif_parts)
        func = 'Pvar' if has_lists else 'var'
        var_str = f'{func}([{",".join(motif_parts)}],[{",".join(beat_parts)}])'

        # Score: shorter is better
        if len(var_str) < best_score and len(var_str) < raw_len * 0.8:
            best_result = var_str
            best_score = len(var_str)

    # Fallback: dominant block detector for mixed-length sections
    # (e.g. AB AB AB C AB AB AB C where AB and C have different lengths)
    if best_result is None and n >= 24:
        dom = find_dominant_block(strs, durs, n)
        if dom and len(dom) < raw_len * 0.8:
            if best_result is None or len(dom) < best_score:
                best_result = dom

    return best_result


def find_dominant_block(strs, durs, n):
    """Find the most frequently occurring block of any length and segment around it.
    Handles patterns like (AB)×3 C (AB)×3 C where AB and C have different lengths.
    Returns Pvar string or None."""
    if n < 16:
        return None

    raw = '[' + ','.join(strs) + ']'
    raw_len = len(raw)

    # Try block sizes from 8 to n//3 — look for blocks that appear 3+ times
    best = None
    best_score = raw_len

    for bsize in range(8, min(n // 3 + 1, 65)):
        # Hash all possible blocks of this size
        block_positions = {}  # tuple(block) → [start_positions]
        for i in range(0, n - bsize + 1):
            block = tuple(strs[i:i + bsize])
            if block not in block_positions:
                block_positions[block] = []
            block_positions[block].append(i)

        # Find the most common block (non-overlapping occurrences)
        for block, positions in block_positions.items():
            # Filter to non-overlapping positions
            non_overlap = [positions[0]]
            for p in positions[1:]:
                if p >= non_overlap[-1] + bsize:
                    non_overlap.append(p)
            if len(non_overlap) < 3:
                continue

            # Segment the pattern: mark which positions belong to the dominant block
            covered = set()
            for p in non_overlap:
                for j in range(p, p + bsize):
                    covered.add(j)

            coverage = len(covered) / n
            if coverage < 0.4:
                continue

            # Build sections: dominant block occurrences + bridge sections
            sections = []  # [(strs_list, is_dominant)]
            i = 0
            while i < n:
                if i in covered and i in non_overlap:
                    sections.append((list(block), True))
                    i += bsize
                else:
                    # Bridge: collect until next dominant block
                    bridge = []
                    while i < n and i not in non_overlap:
                        bridge.append(strs[i])
                        i += 1
                    if bridge:
                        sections.append((bridge, False))

            if len(sections) < 2:
                continue

            # Calculate beats per section
            beat_sections = []
            dur_idx = 0
            for sec_strs, is_dom in sections:
                sec_beats = Fraction(0)
                for k in range(len(sec_strs)):
                    if dur_idx + k < len(durs):
                        sec_beats += durs[dur_idx + k]
                dur_idx += len(sec_strs)
                beat_sections.append((sec_strs, is_dom, float(sec_beats)))

            # Check if section sequence itself repeats
            sec_types = [s[1] for s in beat_sections]
            for ss in range(2, len(beat_sections) // 2 + 1):
                unit = sec_types[:ss]
                reps = len(sec_types) // ss
                if reps >= 2 and all(
                    sec_types[r*ss:(r+1)*ss] == unit
                    for r in range(1, reps)
                ):
                    beat_sections = beat_sections[:ss]
                    break

            # Build Pvar string
            parts = []
            beats = []
            for sec_strs_inner, is_dom, sec_beats in beat_sections:
                compressed = compress_motif(sec_strs_inner)
                parts.append(compressed)
                if sec_beats == int(sec_beats):
                    beats.append(str(int(sec_beats)))
                else:
                    beats.append(str(sec_beats))

            has_lists = any('[' in p for p in parts)
            func = 'Pvar' if has_lists else 'var'
            var_str = f'{func}([{",".join(parts)}],[{",".join(beats)}])'

            if len(var_str) < best_score and len(var_str) < raw_len * 0.8:
                best = var_str
                best_score = len(var_str)

        # Early exit if we found something good at this block size
        if best and best_score < raw_len * 0.5:
            break

    return best


def compress_motif(motif_strs):
    """Compress a single motif (section of a var) into the shortest form."""
    if len(motif_strs) == 1:
        return motif_strs[0]
    # Check if all same
    if len(set(motif_strs)) == 1:
        return motif_strs[0]
    # Check for inner alternating
    for cycle_len in [2, 3]:
        if len(motif_strs) >= cycle_len * 2 and len(motif_strs) % cycle_len == 0:
            cycle = motif_strs[:cycle_len]
            if all(motif_strs[i:i+cycle_len] == cycle
                   for i in range(0, len(motif_strs), cycle_len)):
                return 'P[' + ','.join(cycle) + ']'
    return 'P[' + ','.join(motif_strs) + ']'


def compress_pattern(values, allow_near=False, tolerance=0.15, durs=None):
    """Compress a list into the shortest FoxDot expression."""
    if len(values) == 0:
        return '[]'

    strs = [format_val(v) for v in values]
    unique = set(strs)

    # All same value → scalar
    if len(unique) == 1:
        return strs[0]

    # Short lists — just return as-is
    if len(strs) <= 3:
        return '[' + ','.join(strs) + ']'

    # --- Smart pattern detection ---

    # PDur: Euclidean rhythm (very common in electronic music)
    pd = try_pdur(values)
    if pd:
        return pd

    # PRange: ascending/descending runs
    pr = try_prange(values)
    if pr:
        return pr

    # PTri: triangle patterns
    pt = try_ptri(values)
    if pt:
        return pt

    # Alternating short cycles: [0,5,0,5,0,5] → [0,5]
    alt = try_alternating(strs)
    if alt:
        return alt

    # PStep: sparse regular patterns
    ps = try_pstep(strs, values)
    if ps:
        return ps

    # --- Existing compression strategies ---

    # Find exact repeating unit (including truncated + fuzzy last)
    unit, reps = find_repeating_unit(strs)
    if reps > 1:
        if len(set(unit)) == 1:
            return unit[0]
        # Try alternating on the unit itself
        alt = try_alternating(unit)
        if alt:
            return alt
        inner = try_pstutter(unit)
        if inner:
            return inner
        return '[' + ','.join(unit) + ']'

    # Near-repeating (for amp patterns)
    if allow_near and all(isinstance(v, (int, float)) for v in values):
        near_unit, near_reps = find_near_repeating(values, tolerance)
        if near_reps > 1:
            near_strs = [format_val(v) for v in near_unit]
            if len(set(near_strs)) == 1:
                return near_strs[0]
            inner = try_pstutter(near_strs)
            if inner:
                return inner
            return '[' + ','.join(near_strs) + ']'

    # var() for sectional patterns (e.g. AABB where A and B are different motifs)
    if durs and len(strs) >= 8:
        var_str = detect_var_sections(values, durs)
        if var_str:
            return var_str

    # Try PStutter on full list
    ps = try_pstutter(strs)
    if ps:
        return ps

    # Try splitting into halves
    for divisor in [2, 3, 4]:
        if len(strs) >= divisor * 2 and len(strs) % divisor == 0:
            chunk_size = len(strs) // divisor
            chunks = [strs[i:i+chunk_size] for i in range(0, len(strs), chunk_size)]
            if all(c == chunks[0] for c in chunks):
                inner = try_pstutter(chunks[0])
                if inner:
                    return inner
                return '[' + ','.join(chunks[0]) + ']'

    # For long lists: try to find any reasonable sub-pattern
    if len(strs) > 20 and len(unique) <= 4:
        ps = try_pstutter(strs)
        if ps:
            return ps

    return '[' + ','.join(strs) + ']'


def quantize_amp(values, levels=4):
    """Quantize amp values to N discrete levels."""
    if not values:
        return values
    step = 1.0 / levels
    quantized = []
    for v in values:
        if v == 0 or v == 'rest':
            quantized.append(0)
        else:
            fv = float(v)
            q = round(fv / step) * step
            q = max(step, min(1.0, q))
            quantized.append(round(q, 2))
    return quantized


# --- Chord grouping ---

def group_simultaneous_notes(notes, ticks_per_beat):
    """Group notes starting at the same tick into chord events.
    Returns list of events where simultaneous notes become tuples."""
    if not notes:
        return notes

    threshold = ticks_per_beat // 16  # ~32nd note tolerance

    groups = []
    current_group = [notes[0]]

    for n in notes[1:]:
        if abs(n['start'] - current_group[0]['start']) <= threshold:
            current_group.append(n)
        else:
            groups.append(current_group)
            current_group = [n]
    groups.append(current_group)

    result = []
    for group in groups:
        if len(group) == 1:
            result.append(group[0])
        else:
            # Sort by pitch (low to high) for consistent PGroup ordering
            group.sort(key=lambda n: n['note'])
            # Use earliest start, longest duration, average velocity
            result.append({
                'notes': [n['note'] for n in group],  # multiple notes
                'note': group[0]['note'],  # lowest for fallback
                'vel': max(n['vel'] for n in group),
                'start': group[0]['start'],
                'dur_ticks': max(n['dur_ticks'] for n in group),
                'ch': group[0]['ch'],
            })
    return result


# --- Note extraction and conversion ---

def extract_notes(track, ticks_per_beat, bar_range=None):
    """Extract note events with durations from a track."""
    notes_on = {}
    result = []

    for event in track['events']:
        if event['type'] == 'note_on':
            key = (event['note'], event['ch'])
            notes_on[key] = event
        elif event['type'] == 'note_off':
            key = (event['note'], event['ch'])
            if key in notes_on:
                on_event = notes_on.pop(key)
                result.append({
                    'note': on_event['note'],
                    'vel': on_event['vel'],
                    'start': on_event['tick'],
                    'dur_ticks': event['tick'] - on_event['tick'],
                    'ch': on_event['ch'],
                })

    result.sort(key=lambda x: x['start'])

    if bar_range:
        bar_start, bar_end = bar_range
        tick_start = bar_start * ticks_per_beat * 4
        tick_end = bar_end * ticks_per_beat * 4
        result = [n for n in result if tick_start <= n['start'] < tick_end]

    return result


def is_drum_track(notes):
    """Check if track is drums (channel 9)."""
    if not notes:
        return False
    return 9 in set(n['ch'] for n in notes)


def notes_to_foxdot(notes, ticks_per_beat, root, scale_name, amp_levels=4):
    """Convert note list to FoxDot patterns using onset-based timing.

    Uses inter-onset intervals for dur (no explicit rests in degree list).
    Adds sus when note duration differs from dur.
    Handles chords as PGroup tuples.
    """
    if not notes:
        return None

    # Group simultaneous notes into chords
    notes = group_simultaneous_notes(notes, ticks_per_beat)

    scale_template = SCALE_TEMPLATES[scale_name]
    degrees = []
    durs = []       # inter-onset intervals
    sus_vals = []   # actual note sound durations
    octs = []
    amps = []

    for i, n in enumerate(notes):
        # Handle chord (multiple simultaneous notes)
        if 'notes' in n:
            chord_degrees = []
            chord_octs = []
            for midi_note in n['notes']:
                deg, octv = midi_to_degree(midi_note, root, scale_template)
                chord_degrees.append(deg)
                chord_octs.append(octv)
            # Use tuple for PGroup
            if len(set(chord_octs)) == 1:
                # All same octave: simple degree PGroup
                degrees.append(tuple(chord_degrees))
                octs.append(chord_octs[0])
            else:
                # Different octaves: just use degrees, pick lowest oct
                degrees.append(tuple(chord_degrees))
                octs.append(min(chord_octs))
        else:
            degree, octave = midi_to_degree(n['note'], root, scale_template)
            degrees.append(degree)
            octs.append(octave)

        note_dur = ticks_to_dur(n['dur_ticks'], ticks_per_beat)

        # Inter-onset interval: time until next note starts
        if i < len(notes) - 1:
            onset_gap_ticks = notes[i+1]['start'] - n['start']
            if onset_gap_ticks > 0:
                ioi = ticks_to_dur(onset_gap_ticks, ticks_per_beat)
            else:
                ioi = note_dur
        else:
            ioi = note_dur  # last note

        durs.append(ioi)
        sus_vals.append(note_dur)
        amps.append(round(n['vel'] / 127, 2))

    # Quantize amp
    amps = quantize_amp(amps, amp_levels)

    # Determine if sus is needed (differs from dur significantly)
    needs_sus = False
    sus_diff_count = 0
    for d, s in zip(durs, sus_vals):
        if abs(float(d) - float(s)) > 0.1:
            sus_diff_count += 1
    needs_sus = sus_diff_count > len(durs) * 0.3  # >30% differ

    result = {'degree': degrees, 'dur': durs, 'oct': octs, 'amp': amps}
    if needs_sus:
        result['sus'] = sus_vals

    return result


def split_into_bars(converted, ticks_per_beat=None):
    """Split converted patterns into bar-sized chunks for motif detection."""
    durs = converted['dur']
    positions = []
    beat = 0
    for d in durs:
        positions.append(beat)
        beat += float(d)

    bar_len = 4  # assume 4/4

    bars = []
    bar_idx = 0
    keys = list(converted.keys())
    current_bar = {k: [] for k in keys}

    for i, pos in enumerate(positions):
        target_bar = int(pos / bar_len)
        while target_bar > bar_idx:
            bars.append(current_bar)
            bar_idx += 1
            current_bar = {k: [] for k in keys}

        for key in keys:
            current_bar[key].append(converted[key][i])

    if any(current_bar[k] for k in current_bar):
        bars.append(current_bar)

    return bars


def bars_equal(bar_a, bar_b, fuzzy=False):
    """Check if two bars have identical (or near-identical) patterns."""
    if bar_a['degree'] != bar_b['degree']:
        return False
    if bar_a['dur'] == bar_b['dur']:
        return True
    if fuzzy and len(bar_a['dur']) == len(bar_b['dur']):
        for a, b in zip(bar_a['dur'], bar_b['dur']):
            if abs(float(a) - float(b)) > 0.15:
                return False
        return True
    return False


def find_bar_motif(bars):
    """Find shortest repeating group of bars."""
    n = len(bars)
    if n <= 1:
        return bars, 1

    for fuzzy in [False, True]:
        for size in range(1, n // 2 + 1):
            if n % size != 0:
                continue
            motif = bars[:size]
            match = True
            for i in range(size, n, size):
                for j in range(size):
                    if i + j >= n or not bars_equal(motif[j], bars[i + j], fuzzy):
                        match = False
                        break
                if not match:
                    break
            if match:
                return motif, n // size

    return bars, 1


def find_note_motif(converted):
    """Find repeating motif at the note level (degree+dur tuples)."""
    deg = converted['degree']
    dur = converted['dur']
    n = len(deg)
    if n < 4:
        return converted, 1

    tuples = list(zip([str(d) for d in deg], [str(d) for d in dur]))

    for size in range(2, n // 2 + 1):
        unit = tuples[:size]
        full_reps = n // size
        if full_reps < 2:
            continue

        remainder = n % size
        match = True
        for i in range(size, full_reps * size, size):
            if tuples[i:i+size] != unit:
                match = False
                break
        if not match:
            continue
        if remainder > 0 and tuples[full_reps * size:] != unit[:remainder]:
            continue

        keys = list(converted.keys())
        result = {key: converted[key][:size] for key in keys}
        return result, full_reps

    # Fuzzy: allow 1 mismatched repetition out of many (degree+dur tuples)
    for size in range(2, n // 2 + 1):
        full_reps = n // size
        if full_reps < 3:
            continue
        unit = tuples[:size]
        mismatch = 0
        for i in range(size, full_reps * size, size):
            if tuples[i:i+size] != unit:
                mismatch += 1
        if mismatch <= 1:
            keys = list(converted.keys())
            result = {key: converted[key][:size] for key in keys}
            return result, full_reps

    # Degree-only motif: if degree repeats but dur has micro-variations,
    # match on degree alone and truncate all params to motif length.
    # FoxDot auto-cycles all lists independently, so this works.
    deg_strs = [str(d) for d in deg]
    for size in range(2, n // 2 + 1):
        deg_unit = deg_strs[:size]
        full_reps = n // size
        if full_reps < 2:
            continue

        # Exact degree match
        deg_match = True
        for i in range(size, full_reps * size, size):
            if deg_strs[i:i+size] != deg_unit:
                deg_match = False
                break
        if not deg_match:
            continue
        # Allow truncated last rep
        remainder = n % size
        if remainder > 0 and deg_strs[full_reps * size:] != deg_unit[:remainder]:
            continue

        # Degree repeats! Truncate all params to first cycle.
        # For dur: take the mode of each position across all cycles
        # to smooth out timing jitter.
        keys = list(converted.keys())
        result = {}
        for key in keys:
            vals = converted[key]
            if key == 'dur':
                # Average/mode each position across repetitions
                best_dur = []
                for pos in range(size):
                    position_vals = []
                    for rep in range(full_reps):
                        idx = rep * size + pos
                        if idx < len(vals):
                            position_vals.append(vals[idx])
                    if position_vals:
                        # Use the most common value (mode)
                        val_strs = [str(v) for v in position_vals]
                        from collections import Counter as Ctr
                        mode_str = Ctr(val_strs).most_common(1)[0][0]
                        # Find original value matching the mode
                        for v in position_vals:
                            if str(v) == mode_str:
                                best_dur.append(v)
                                break
                result[key] = best_dur
            else:
                result[key] = vals[:size]
        return result, full_reps

    # Fuzzy degree-only (allow 1 mismatch)
    for size in range(2, n // 2 + 1):
        full_reps = n // size
        if full_reps < 3:
            continue
        deg_unit = deg_strs[:size]
        mismatch = 0
        for i in range(size, full_reps * size, size):
            if deg_strs[i:i+size] != deg_unit:
                mismatch += 1
        if mismatch <= 1:
            keys = list(converted.keys())
            result = {key: converted[key][:size] for key in keys}
            return result, full_reps

    return converted, 1


def merge_bars(bars):
    """Merge a list of bar dicts into a single converted dict."""
    keys = list(bars[0].keys())
    result = {k: [] for k in keys}
    for bar in bars:
        for key in result:
            result[key].extend(bar[key])
    return result


# --- Output formatting ---

def format_output(converted, synth, player, track_name):
    """Format a converted track as a FoxDot player line."""
    deg = converted['degree']
    dur = converted['dur']
    oct_vals = converted['oct']
    amp_vals = converted['amp']
    sus_vals = converted.get('sus')

    # --- Check if track is too complex for literal output → use summary mode ---
    # Summary mode uses generative patterns (PRand, PWalk, PwRand) to capture
    # the feel of the track rather than every note.
    deg_str = compress_pattern(deg, durs=dur)
    dur_str = compress_pattern(dur)
    sus_str = None
    if sus_vals:
        sus_str = compress_pattern(sus_vals)
        if sus_str == dur_str:
            sus_str = None

    total_len = len(deg_str) + len(dur_str) + (len(sus_str) if sus_str else 0)
    if total_len > 600 and len(deg) > 40:
        summary = _summarize_track(deg, dur, oct_vals, amp_vals, sus_vals)
        if summary:
            deg_str, dur_str, sus_str, oct_str, amp_str = summary
            params = [f'dur={dur_str}']
            if sus_str:
                params.append(f'sus={sus_str}')
            if oct_str != '5':
                params.append(f'oct={oct_str}')
            if amp_str not in ('1', '1.0', '0.75', '1.00'):
                params.append(f'amp={amp_str}')
            line = f'{player} >> {synth}({deg_str}, {", ".join(params)})'
            return line

    # --- Standard compression path ---
    oct_str = compress_pattern(oct_vals)

    non_zero_amps = [a for a in amp_vals if a > 0]
    if non_zero_amps:
        amp_counts = Counter(non_zero_amps)
        most_common_amp, amc = amp_counts.most_common(1)[0]
        amp_variation = max(non_zero_amps) - min(non_zero_amps) if non_zero_amps else 0
        if amp_variation <= 0.3:
            amp_str = str(most_common_amp)
        else:
            amp_str = compress_pattern(amp_vals, allow_near=True, tolerance=0.15)
    else:
        amp_str = '1'

    params = [f'dur={dur_str}']
    if sus_str:
        params.append(f'sus={sus_str}')
    if oct_str != '5':
        params.append(f'oct={oct_str}')
    if amp_str not in ('1', '1.0', '0.75', '1.00'):
        params.append(f'amp={amp_str}')

    line = f'{player} >> {synth}({deg_str}, {", ".join(params)})'
    return line


def _summarize_track(deg, dur, oct_vals, amp_vals, sus_vals):
    """Generate a summary using generative FoxDot patterns instead of literal lists.
    Analyzes the statistical properties and melodic motion to pick the right generator.
    Returns (deg_str, dur_str, sus_str, oct_str, amp_str) or None."""
    n = len(deg)
    if n < 20:
        return None

    # --- Analyze degrees ---
    # Filter out tuples (chords) for motion analysis
    scalar_degs = [d for d in deg if isinstance(d, int)]
    deg_strs = [format_val(d) for d in deg]
    deg_counts = Counter(deg_strs)
    unique_degs = len(deg_counts)

    # Analyze melodic motion: intervals between consecutive scalar degrees
    intervals = []
    for i in range(len(scalar_degs) - 1):
        intervals.append(abs(scalar_degs[i+1] - scalar_degs[i]))

    avg_interval = sum(intervals) / max(len(intervals), 1) if intervals else 0
    max_degree = max(scalar_degs) if scalar_degs else 7
    min_degree = min(scalar_degs) if scalar_degs else 0

    # Decide degree generator based on motion analysis
    if avg_interval <= 1.5 and unique_degs > 4:
        # Stepwise motion → PWalk
        walk_range = max_degree - min_degree + 1
        if min_degree == 0:
            deg_str = f'PWalk(max={walk_range})'
        else:
            deg_str = f'PWalk(max={walk_range},start={min_degree})'
    elif unique_degs <= 6:
        # Few unique values → PwRand with weights
        top = deg_counts.most_common(6)
        vals = [v for v, c in top]
        weights = [c for v, c in top]
        # Simplify weights by dividing by GCD
        from math import gcd
        from functools import reduce
        g = reduce(gcd, weights)
        weights = [w // g for w in weights]
        if all(w == weights[0] for w in weights):
            deg_str = f'PRand([{",".join(vals)}])'
        else:
            deg_str = f'PwRand([{",".join(vals)}],[{",".join(str(w) for w in weights)}])'
    else:
        # Many unique values, larger intervals → PRand of common values
        top = deg_counts.most_common(8)
        vals = sorted([v for v, c in top], key=lambda x: int(x) if x.lstrip('-').isdigit() else 0)
        deg_str = f'PRand([{",".join(vals)}])'

    # --- Analyze durations ---
    dur_strs = [format_val(d) for d in dur]
    dur_counts = Counter(dur_strs)
    top_durs = dur_counts.most_common(5)
    # Keep durs that cover 90%+ of events
    total_dur_events = sum(c for v, c in dur_counts.items())
    kept_durs = []
    cumulative = 0
    for v, c in sorted(dur_counts.items(), key=lambda x: -x[1]):
        kept_durs.append(v)
        cumulative += c
        if cumulative >= total_dur_events * 0.9:
            break

    if len(kept_durs) == 1:
        dur_str = kept_durs[0]
    elif len(kept_durs) <= 4:
        # Check if they match a PDur
        pd = try_pdur(dur[:min(len(dur), 32)])
        if pd:
            dur_str = pd
        else:
            dur_str = f'PRand([{",".join(sorted(kept_durs))}])'
    else:
        dur_str = f'PRand([{",".join(sorted(kept_durs)[:5])}])'

    # --- Analyze sus ---
    sus_str = None
    if sus_vals:
        sus_strs = [format_val(s) for s in sus_vals]
        sus_counts = Counter(sus_strs)
        top_sus = sus_counts.most_common(3)
        if len(top_sus) == 1 or top_sus[0][1] > len(sus_vals) * 0.7:
            sus_str = top_sus[0][0]
        else:
            kept_sus = [v for v, c in top_sus]
            sus_str = f'PRand([{",".join(sorted(kept_sus))}])'
        if sus_str == dur_str:
            sus_str = None

    # --- Analyze octaves ---
    oct_counts = Counter(oct_vals)
    if len(oct_counts) == 1:
        oct_str = str(oct_vals[0])
    elif len(oct_counts) == 2:
        vals = sorted(oct_counts.keys())
        oct_str = f'[{vals[0]},{vals[1]}]'
    else:
        top_oct = oct_counts.most_common(1)[0]
        if top_oct[1] > len(oct_vals) * 0.7:
            oct_str = str(top_oct[0])
        else:
            vals = sorted(oct_counts.keys())
            oct_str = f'PRand([{",".join(str(v) for v in vals)}])'

    # --- Analyze amp ---
    non_zero = [a for a in amp_vals if a > 0]
    if non_zero:
        amp_range = max(non_zero) - min(non_zero)
        if amp_range <= 0.3:
            amp_str = str(Counter(non_zero).most_common(1)[0][0])
        else:
            amp_str = f'PWhite({min(non_zero)},{max(non_zero)})'
    else:
        amp_str = '1'

    return deg_str, dur_str, sus_str, oct_str, amp_str


def guess_synth(track_name):
    """Pick FoxDot synth based on track name."""
    name = track_name.lower()
    if 'bass' in name:
        return 'dbass'
    if 'guitar' in name or 'gtr' in name:
        return 'faim'
    if 'vocal' in name or 'voice' in name or 'sing' in name:
        return 'soprano'
    if 'piano' in name or 'key' in name:
        return 'pianovel'
    if 'pad' in name or 'string' in name or 'synth' in name:
        return 'cs80'
    if 'lead' in name or 'solo' in name:
        return 'lazer'
    if 'organ' in name:
        return 'organ'
    if 'bell' in name:
        return 'bell'
    return 'pluck'


# --- Drum mapping ---

GM_DRUM_MAP = {
    35: 'x', 36: 'x',  # Bass drum
    37: 't', 38: 'o', 40: 'o',  # Snare / rimshot
    39: '+',  # Clap
    41: 'v', 43: 'v', 45: 'v', 47: 'v', 48: 'v', 50: 'v',  # Toms
    42: '-', 44: '-',  # Closed hihat
    46: '=',  # Open hihat
    49: '#', 57: '#',  # Crash
    51: '~', 53: '~', 59: '~',  # Ride
    52: '*',  # China
    54: 't',  # Tambourine
    56: '+',  # Cowbell
}


def compress_drum_string(pat_str, bar_chars):
    """Compress a long drum pattern string using sectional detection.
    Returns the shortest representation: raw string, or var() of bar patterns."""
    n = len(pat_str)
    if n <= bar_chars * 4:
        return f'"{pat_str}"'

    # Split into bars
    bars = []
    for i in range(0, n, bar_chars):
        bar = pat_str[i:i+bar_chars]
        if len(bar) == bar_chars:
            bars.append(bar)

    if not bars:
        return f'"{pat_str}"'

    # Simple case: all bars identical
    unique_bars = list(dict.fromkeys(bars))
    if len(unique_bars) == 1:
        return f'"{unique_bars[0]}"'

    # Count unique bars (excluding silence)
    silence = '.' * bar_chars
    non_silent_unique = [b for b in unique_bars if b != silence]

    # Try 2-bar and 4-bar grouping for the repeat unit
    for group_size in [1, 2, 4]:
        if len(bars) < group_size * 2:
            continue
        grouped = []
        for i in range(0, len(bars) - group_size + 1, group_size):
            grouped.append(''.join(bars[i:i+group_size]))
        unique_grouped = list(dict.fromkeys(grouped))
        if len(unique_grouped) == 1:
            return f'"{unique_grouped[0]}"'

    # Section detection: find runs of identical bars, build var()
    sections = []  # [(bar_pattern, count)]
    i = 0
    while i < len(bars):
        current_bar = bars[i]
        count = 0
        j = i
        while j < len(bars) and bars[j] == current_bar:
            count += 1
            j += 1
        sections.append((current_bar, count))
        i = j

    # Also try 2-bar units as sections
    best_sections = sections
    if len(bars) >= 4:
        sections_2bar = []
        i = 0
        while i + 1 < len(bars):
            unit = bars[i] + bars[i+1]
            count = 0
            j = i
            while j + 1 < len(bars) and bars[j] + bars[j+1] == unit:
                count += 1
                j += 2
            if count >= 1:
                sections_2bar.append((unit, count))
                i = j
            else:
                sections_2bar = None
                break
        if sections_2bar and len(sections_2bar) < len(best_sections):
            best_sections = sections_2bar

    sections = best_sections

    # Skip if too many unique sections (not compressible)
    unique_section_patterns = list(dict.fromkeys(s[0] for s in sections))
    if len(unique_section_patterns) > 8:
        # Fall back: try fuzzy matching — group bars that are >80% similar
        sections = _fuzzy_drum_sections(bars, bar_chars)
        unique_section_patterns = list(dict.fromkeys(s[0] for s in sections))
        if len(unique_section_patterns) > 8:
            return f'"{pat_str}"'

    # Filter out silent sections
    non_silent_sections = [(p, c) for p, c in sections if p.replace('.', '') != '']
    if not non_silent_sections:
        return None

    # Check if sections themselves repeat (ABABAB)
    sec_keys = [s[0] for s in non_silent_sections]
    for sec_size in range(2, len(non_silent_sections) // 2 + 1):
        sec_unit = sec_keys[:sec_size]
        sec_reps = len(non_silent_sections) // sec_size
        if sec_reps >= 2 and all(
            sec_keys[r*sec_size:(r+1)*sec_size] == sec_unit
            for r in range(1, sec_reps)
        ):
            non_silent_sections = non_silent_sections[:sec_size]
            break

    # If only 1 unique pattern remains after dedup, just use it
    if len(set(s[0] for s in non_silent_sections)) == 1:
        return f'"{non_silent_sections[0][0]}"'

    # Build var() string
    parts = []
    beats = []
    for pattern, count in non_silent_sections:
        parts.append(f'"{pattern}"')
        bar_count = count * (len(pattern) // bar_chars)
        beats.append(str(bar_count * 4))

    var_str = f'var([{",".join(parts)}],[{",".join(beats)}])'

    # Quality gate
    raw_str = f'"{pat_str}"'
    if len(var_str) < len(raw_str) * 0.8:
        return var_str

    return f'"{pat_str}"'


def _fuzzy_drum_sections(bars, bar_chars):
    """Group bars by similarity (>80% chars match) into sections."""
    if not bars:
        return []

    def similarity(a, b):
        if len(a) != len(b):
            return 0
        return sum(1 for x, y in zip(a, b) if x == y) / len(a)

    sections = []
    i = 0
    while i < len(bars):
        ref = bars[i]
        count = 1
        j = i + 1
        while j < len(bars) and similarity(ref, bars[j]) > 0.8:
            count += 1
            j += 1
        sections.append((ref, count))
        i = j

    return sections


def drum_track_to_foxdot(notes, ticks_per_beat, resolution=16):
    """Convert drum notes to play() patterns — onset-based like codeBank style.
    Uses short strings + dur patterns instead of huge grid strings."""
    groups = defaultdict(list)
    for n in notes:
        char = GM_DRUM_MAP.get(n['note'], None)
        if char:
            groups[char].append(n)

    if not groups:
        return []

    all_starts = [n['start'] for n in notes]
    bar_ticks = ticks_per_beat * 4
    min_tick = (min(all_starts) // bar_ticks) * bar_ticks

    lines = []
    priority = ['x', 'o', '-', '=', '#', '~', 'v', '+', 't', '*']
    sorted_chars = sorted(groups.keys(), key=lambda c: priority.index(c) if c in priority else 99)

    for char in sorted_chars:
        char_notes = sorted(groups[char], key=lambda n: n['start'])
        if not char_notes:
            continue

        result = _drum_onset_pattern(char, char_notes, ticks_per_beat, min_tick)
        if result:
            lines.append(result)

    return lines


def _drum_onset_pattern(char, notes, ticks_per_beat, min_tick):
    """Convert a single drum instrument's hits to compact FoxDot play() line.
    Returns string like: play("x", dur=[1,1/2,1/2]) or play("x.x.", dur=1/4)"""
    bar_ticks = ticks_per_beat * 4

    # Calculate onset times in beats from song start
    onsets = [(n['start'] - min_tick) / ticks_per_beat for n in notes]
    if not onsets:
        return None

    # Calculate inter-onset intervals (IOI)
    iois = []
    for i in range(len(onsets) - 1):
        ioi = onsets[i + 1] - onsets[i]
        if ioi > 0:
            iois.append(ioi)
    if not iois:
        # Single hit — not worth a player
        return None

    # Quantize IOIs to musical grid
    quantized_iois = [ticks_to_dur(round(ioi * ticks_per_beat), ticks_per_beat) for ioi in iois]
    # Add final IOI: snap to bar boundary
    last_onset_beats = onsets[-1]
    last_bar_end = (int(last_onset_beats / 4) + 1) * 4
    final_ioi = last_bar_end - last_onset_beats
    if final_ioi > 0:
        quantized_iois.append(ticks_to_dur(round(final_ioi * ticks_per_beat), ticks_per_beat))

    # Delay: first onset offset from bar start
    first_beat_in_bar = onsets[0] % 4
    delay_frac = ticks_to_dur(round(first_beat_in_bar * ticks_per_beat), ticks_per_beat)

    # Try to find repeating motif in the IOI sequence
    motif_iois, motif_reps = _find_ioi_motif(quantized_iois)

    # Format the dur pattern
    dur_str = compress_pattern(motif_iois)

    # Build the line
    parts = [f'dur={dur_str}']
    if float(delay_frac) > 0.05:
        parts.append(f'delay={simplify_dur(delay_frac)}')

    # For very simple patterns (constant dur), try grid string approach
    # e.g. "x..x.x.." at dur=1/4 is more readable than "x" with dur=[1,3/4,1/4]
    grid_str = _try_grid_string(char, motif_iois)
    if grid_str and len(grid_str) <= 24:
        grid_parts = [f'dur=1/4']
        if float(delay_frac) > 0.05:
            grid_parts.append(f'delay={simplify_dur(delay_frac)}')
        return f'play("{grid_str}", {", ".join(grid_parts)})'

    return f'play("{char}", {", ".join(parts)})'


def _find_ioi_motif(iois):
    """Find shortest repeating motif in an IOI sequence."""
    n = len(iois)
    if n <= 1:
        return iois, 1

    strs = [simplify_dur(d) for d in iois]

    # Try exact repeating unit
    for size in range(1, n // 2 + 1):
        unit = strs[:size]
        full_reps = n // size
        if full_reps < 2:
            continue
        remainder = n % size
        match = True
        for i in range(size, full_reps * size, size):
            if strs[i:i+size] != unit:
                match = False
                break
        if not match:
            continue
        # Allow truncated last rep
        if remainder > 0 and strs[full_reps * size:] != unit[:remainder]:
            continue
        return iois[:size], full_reps

    # Fuzzy: allow 1 mismatch
    for size in range(2, n // 2 + 1):
        full_reps = n // size
        if full_reps < 3:
            continue
        unit = strs[:size]
        mismatches = sum(1 for i in range(size, full_reps * size, size)
                         if strs[i:i+size] != unit)
        if mismatches <= 1:
            return iois[:size], full_reps

    return iois, 1


def _try_grid_string(char, iois):
    """Try to express IOIs as a grid string (like "x..x.x..") at 16th resolution.
    Returns string or None if too complex."""
    # Check if all IOIs are multiples of 1/4 beat (16th note)
    grid = Fraction(1, 4)
    steps = []
    for ioi in iois:
        ratio = ioi / grid
        if ratio.denominator != 1:
            return None  # not on 16th grid
        steps.append(int(ratio))

    total_steps = sum(steps)
    if total_steps > 16:
        return None  # more than 1 bar — too long for grid

    # Build the grid string
    result = []
    for s in steps:
        result.append(char)
        result.extend(['.'] * (s - 1))

    pat = ''.join(result)

    # Trim trailing dots (FoxDot loops)
    pat = pat.rstrip('.')

    return pat if pat else None


# --- Main generation ---

def generate_foxdot_code(midi_data, track_indices=None, bar_range=None,
                         force_root=None, force_scale=None):
    """Generate FoxDot code from parsed MIDI data."""
    tpb = midi_data['ticks_per_beat']
    tracks = midi_data['tracks']

    # Detect tempo
    bpm = 120
    for track in tracks:
        for event in track['events']:
            if event['type'] == 'tempo':
                bpm = round(event['bpm'])
                break

    # Collect all notes
    all_notes = []
    track_notes = {}
    indices = track_indices or range(len(tracks))

    for i in indices:
        if i >= len(tracks):
            continue
        notes = extract_notes(tracks[i], tpb, bar_range)
        if notes:
            track_notes[i] = notes
            all_notes.extend(notes)

    if not all_notes:
        return "# No notes found in selected tracks"

    # Scale detection
    note_values = [n['note'] for n in all_notes if not is_drum_track([n])]
    if force_root is not None and force_scale is not None:
        root = force_root
        scale_name = force_scale
    elif note_values:
        root, scale_name = detect_scale(note_values)
    else:
        root, scale_name = 0, 'chromatic'

    # Generate output
    lines = []
    lines.append(f'Clock.bpm = {bpm}')
    lines.append(f'Scale.default = Scale.{scale_name}')
    lines.append(f'Root.default = "{NOTE_NAMES[root]}"')
    lines.append('')

    player_names = ['d1', 'd2', 'd3', 'd4', 'b1', 'b2', 'p1', 'p2', 'p3',
                    'a1', 'a2', 'a3', 'l1', 'l2', 's1', 's2']
    player_idx = 0

    for i, notes in track_notes.items():
        if player_idx >= len(player_names):
            break

        track_name = tracks[i]['name']
        is_drums = is_drum_track(notes)

        if is_drums:
            lines.append(f'# {track_name} (drums)')
            drum_lines = drum_track_to_foxdot(notes, tpb)
            for dl in drum_lines:
                if player_idx >= len(player_names):
                    break
                pname = player_names[player_idx]
                player_idx += 1
                lines.append(f'{pname} >> {dl}')
            lines.append('')
        else:
            pname = player_names[player_idx]
            player_idx += 1

            converted = notes_to_foxdot(notes, tpb, root, scale_name)
            if not converted:
                continue

            # --- Motif detection (note-level first, then bar-level) ---
            motif_found = False
            note_motif, note_reps = find_note_motif(converted)
            if note_reps > 1:
                converted = note_motif
                motif_found = True

            if not motif_found:
                bars = split_into_bars(converted, tpb)
                if len(bars) >= 2:
                    motif_bars, motif_reps = find_bar_motif(bars)
                    if motif_reps > 1:
                        converted = merge_bars(motif_bars)

            synth = guess_synth(track_name)
            line = format_output(converted, synth, pname, track_name)

            lines.append(f'# {track_name}')
            lines.append(line)
            lines.append('')

    return '\n'.join(lines)


# --- CLI ---

def print_track_info(midi_data):
    """Print summary of tracks."""
    tpb = midi_data['ticks_per_beat']
    print(f"\nTicks per beat: {tpb}")
    print(f"Tracks: {len(midi_data['tracks'])}\n")

    for i, track in enumerate(midi_data['tracks']):
        note_ons = [e for e in track['events'] if e['type'] == 'note_on']
        tempos = [e for e in track['events'] if e['type'] == 'tempo']
        channels = set(e.get('ch', -1) for e in track['events'] if 'ch' in e)

        info = f"  [{i}] {track['name']:30s}  notes: {len(note_ons):5d}"
        if channels:
            info += f"  ch: {','.join(str(c) for c in sorted(channels))}"
        if tempos:
            info += f"  bpm: {tempos[0]['bpm']:.0f}"
        print(info)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Convert MIDI to FoxDot code')
    parser.add_argument('file', help='MIDI file path')
    parser.add_argument('--scale', help='Force scale (e.g. minor, phrygian)')
    parser.add_argument('--root', help='Force root note (e.g. D, C#)')
    parser.add_argument('--tracks', help='Track indices (e.g. 0,1,3)')
    parser.add_argument('--bars', help='Bar range (e.g. 1-8)')
    parser.add_argument('--info', action='store_true', help='Print track info only')
    parser.add_argument('-o', '--output', help='Save FoxDot code to file')
    args = parser.parse_args()

    midi_data = parse_midi(args.file)

    if args.info:
        print_track_info(midi_data)
        return

    track_indices = None
    if args.tracks:
        track_indices = [int(x) for x in args.tracks.split(',')]

    bar_range = None
    if args.bars:
        parts = args.bars.split('-')
        bar_range = (int(parts[0]) - 1, int(parts[1]))

    force_root = None
    if args.root:
        root_name = args.root.upper()
        if root_name in NOTE_NAMES:
            force_root = NOTE_NAMES.index(root_name)

    force_scale = None
    if args.scale:
        force_scale = args.scale

    print_track_info(midi_data)

    code = generate_foxdot_code(midi_data, track_indices, bar_range,
                                force_root, force_scale)

    out_path = args.output
    if not out_path:
        base = os.path.splitext(os.path.basename(args.file))[0]
        out_path = os.path.join(os.path.dirname(args.file) or '.', base + '_foxdot.py')

    with open(out_path, 'w') as f:
        f.write(code + '\n')

    print(f"\nSaved to: {out_path}")
    print("\n" + "=" * 60)
    print(code)


if __name__ == '__main__':
    main()
