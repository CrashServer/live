#!/usr/bin/env python3
"""Multi-source extractor — atoms + scenes + tracks from 3 directories.

LAYOUT (cells.json grid):
  A-P  atoms (single-player snippets)  by role/tempo from ANY source
  Q    tracks from codeBank             (100 max)
  R    tracks from Téléchargements      (jam sessions, 100 max)
  S    scenes from any source           (first 100 by source/name)
  T    scenes overflow                  (next 100)
  U    tracks from Musique              (small set, plenty of headroom)
  V-Z  user-reserved

Atom extraction is union — every source contributes proposals; empty
coords get filled, populated ones are enriched with metadata if missing.

USAGE
    python3 grid/extract_all.py              # write *_extracted.json files
    python3 grid/extract_all.py --merge      # also merge into cells.json
"""
import json
import os
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

GRID_DIR = Path(__file__).resolve().parent
CELLS_FILE = GRID_DIR / "cells.json"

SOURCES = [
    {"name": "codeBank",        "dir": Path.home() / "live" / "codeBank",   "tracks_cols": ["Q"]},
    {"name": "Téléchargements", "dir": Path.home() / "Téléchargements",     "tracks_cols": ["R"]},
    {"name": "Musique",         "dir": Path.home() / "Musique",             "tracks_cols": ["U"]},
    {"name": "DriveCodebase",   "dir": Path("/run/media/svdk/storage/DRIVE/300_CrashServer/39_CODEBASE/391_FOXDOT"),
                                                                            "tracks_cols": ["V", "W", "X", "Y", "Z"]},
]

# --- regex + classifier (mirrored from extract_from_codebank.py) ---

PLAYER_RE = re.compile(r'^([a-z]\d+)\s*>>\s*([a-zA-Z_]+)\s*\(')
BPM_RE = re.compile(r'Clock\.bpm\s*=\s*(?:lininf\s*\(\s*)?([0-9]+)')
SCALE_RE = re.compile(r'Scale\.default\s*=\s*["\']([^"\']+)')
ROOT_RE = re.compile(r'Root\.default\s*=\s*["\']?([A-Za-z#b0-9]+)')
SECTION_RE = re.compile(r"^\s*#@\s*([a-zA-Z_]\w*)\s*\((\d+)b?\)\s*")

SYNTH_TO_COL = {
    # pad A
    "pianovel": "A", "varsaw": "A", "sinepad": "A", "ethpad": "A",
    "darkpad": "A", "pad2": "A", "soprano": "A", "choir": "A",
    "viola": "A", "varicelle": "A", "keys": "A", "a_vpad": "A",
    "a_poly": "A",
    # bass B
    "dbass": "B", "lbass": "B", "cbass": "B", "ebass": "B",
    "sawbass": "B", "subbass": "B", "fbass": "B", "pumpbass": "B",
    "superbass": "B", "abass": "B", "bbass": "B", "pbass": "B",
    "glitchbass": "B", "acidbass": "B", "wobble": "B",
    "bass": "B", "jbass": "B", "dafbass": "B", "dbss": "B",
    "a_xbass": "B", "a_bassry": "B",
    # kick C
    "compkick": "C", "prodrums": "C", "a_bd": "C",
    # snare D
    "industrialsnare": "D", "a_sn": "D", "a_cy": "D",
    # hat E
    "click": "E", "pumphihat": "E", "a_hhat": "E",
    # lead 1 G
    "faim": "G", "alva": "G", "darklead": "G", "prof": "G",
    "creep": "G", "lapin": "G", "vati": "G",
    "dab": "G", "swiss": "G", "ssaw": "G", "karp": "G",
    "guit": "G", "fmsynth": "G", "supersaw": "G",
    "pluck": "G", "mpluck": "G", "saw": "G", "sine": "G",
    "soft": "G", "svdk": "G", "a_glead": "G", "a_vlead": "G",
    "a_daftlead": "G", "a_daft": "G", "a_wave": "G",
    "donorgan": "G", "donorganpat": "G",
    # lead 2 H
    "plaitsX": "H", "plaits": "H", "cs80": "H", "braids": "H",
    "rave": "H", "rsin": "H", "four": "H", "donk": "H",
    "a_gesa": "H", "a_gesa2": "H", "a_gesa3": "H", "a_fantom": "H",
    "ews": "H",
    # chord stab I
    "hardstab": "I", "hoover": "I", "klank": "I", "organ": "I",
    "stress": "I", "a_stress": "I", "a_stab": "I", "stab": "I",
    # acid J
    "tb303": "J", "tb304": "J", "tb305": "J", "acidline": "J",
    "tekno": "J",
    # texture K
    "industrialdrone": "K", "noise": "K", "brown": "K", "drone": "K",
    "ambi": "K", "drift": "K", "angst": "K",
    # bell M
    "bell": "M", "bell2": "M", "gong": "M", "glass": "M",
    "charm": "M", "marimba": "M", "compperc": "M", "noisehit": "M",
    "crackle": "M", "blip": "M", "space": "M", "spaceMmm": "M",
    "dopple": "M", "cluster": "M", "foghorn": "M", "horn": "M",
    "zap": "M", "growl": "M", "gsynth": "M", "dub": "M",
    # vocal L
    "radio": "L",
    # loop F (special)
    "breakcore": "F",
}


def classify_sample_player(code, synth_kind):
    pattern_match = re.search(r'play\(\s*[r]?["\']([^"\']*)["\']', code)
    if pattern_match:
        pat = pattern_match.group(1)[:4].lower()
        if any(c in pat for c in "xk"): return "C"
        if any(c in pat for c in "os"): return "D"
        if any(c in pat for c in "-h=:"): return "E"
        if any(c in pat for c in "u"): return "D"
        return "F"
    if synth_kind == "loop":
        sample_name = re.search(r'loop\(\s*["\']([^"\']+)', code)
        if sample_name:
            name = sample_name.group(1).lower()
            if any(t in name for t in ("drum", "break", "beat", "rage", "psy",
                                       "house", "fill", "core", "junglemix",
                                       "ragedrum", "amen", "circle")):
                return "F"
            if any(t in name for t in ("atmo", "drone", "screech", "wind",
                                       "spheric", "sundrone", "whitedwarf",
                                       "gscreech")):
                return "N"
            if any(t in name for t in ("vocal", "voice", "oldies", "ahh", "growl")):
                return "L"
            return "F"
    if synth_kind == "noloop":
        sample_name = re.search(r'noloop\(\s*["\']([^"\']+)', code)
        if sample_name:
            name = sample_name.group(1).lower()
            if "vocal" in name or "oldies" in name or "voice" in name:
                return "L"
        return "L"
    if synth_kind == "stretch":
        return "N"
    return None


def bpm_to_row(bpm):
    if bpm is None:
        return 35
    if bpm < 80: return min(9, max(0, int((bpm - 60) / 2)))
    if bpm < 100: return 10 + min(9, max(0, int((bpm - 80) / 2)))
    if bpm < 120: return 20 + min(9, max(0, int((bpm - 100) / 2)))
    if bpm < 140: return 30 + min(9, max(0, int((bpm - 120) / 2)))
    if bpm < 160: return 40 + min(9, max(0, int((bpm - 140) / 2)))
    if bpm < 180: return 50 + min(9, max(0, int((bpm - 160) / 2)))
    return 60 + min(9, max(0, int((bpm - 180) / 2)))


def extract_atoms(path, source_name):
    cells = []
    try:
        text = path.read_text(errors="replace")
    except Exception:
        return cells
    current_bpm = None
    current_scale = None
    current_root = None
    for lineno, line in enumerate(text.splitlines(), 1):
        m = BPM_RE.search(line)
        if m:
            current_bpm = int(m.group(1))
            continue
        sm = SCALE_RE.search(line)
        if sm:
            current_scale = sm.group(1)
        rm = ROOT_RE.search(line)
        if rm:
            current_root = rm.group(1).strip('"\'')
        stripped = line.split('#', 1)[0].strip()
        if not stripped or stripped.startswith('~'):
            continue
        pm = PLAYER_RE.match(stripped)
        if not pm:
            continue
        synth = pm.group(2)
        col = SYNTH_TO_COL.get(synth)
        if col is None:
            if synth in ("play", "loop", "noloop", "stretch"):
                col = classify_sample_player(stripped, synth)
            if col is None:
                continue  # skip truly unknown
        row = bpm_to_row(current_bpm)
        coord = f"{col}{row}"
        key = None
        if current_root and current_scale: key = f"{current_root} {current_scale}"
        elif current_root: key = current_root
        elif current_scale: key = current_scale
        label = f"{synth} from {path.stem}"
        if current_bpm:
            label += f" @ {current_bpm}"
        cells.append({
            "coord": coord, "code": stripped, "label": label,
            "type": "atom", "tempo": current_bpm, "scale": current_scale,
            "root": current_root, "key": key, "instrument": synth,
            "source": source_name,
        })
    return cells


def extract_scenes(path, source_name):
    out = []
    try:
        text = path.read_text(errors="replace")
    except Exception:
        return out
    current = None
    current_bpm = None
    current_scale = None
    current_root = None
    for line in text.splitlines():
        m = BPM_RE.search(line)
        if m: current_bpm = int(m.group(1))
        sm_ = SCALE_RE.search(line)
        if sm_: current_scale = sm_.group(1)
        rm = ROOT_RE.search(line)
        if rm: current_root = rm.group(1).strip('"\'')
        sm = SECTION_RE.match(line)
        if sm:
            if current and current["lines"]:
                out.append(_finalize_scene(current))
            current = {
                "name": sm.group(1), "beats": int(sm.group(2)),
                "lines": [], "source_file": path.name, "source_name": source_name,
                "tempo": current_bpm, "scale": current_scale, "root": current_root,
            }
            continue
        if current is not None:
            current["lines"].append(line)
    if current and current["lines"]:
        out.append(_finalize_scene(current))
    # Filter trivially small
    return [s for s in out if _scene_non_trivial(s)]


def _finalize_scene(sec):
    code = "\n".join(sec["lines"]).strip()
    return {
        "name": sec["name"], "beats": sec["beats"], "code": code,
        "source_file": sec["source_file"], "source_name": sec["source_name"],
        "tempo": sec["tempo"], "scale": sec["scale"], "root": sec["root"],
    }


def _scene_non_trivial(s):
    non_trivial = [ln for ln in s["code"].splitlines()
                   if ln.strip() and not ln.strip().startswith("#")]
    return len(non_trivial) >= 2


def analyze_track(path, source_name):
    try:
        text = path.read_text(errors="replace")
    except Exception:
        return None
    bpms = BPM_RE.findall(text)
    scales = SCALE_RE.findall(text)
    roots = ROOT_RE.findall(text)
    tempo = int(bpms[0]) if bpms else None
    scale = scales[0] if scales else None
    root = roots[0].strip('"\'') if roots else None
    key = None
    if root and scale: key = f"{root} {scale}"
    elif root: key = root
    elif scale: key = scale
    return {
        "code": text, "tempo": tempo, "scale": scale, "root": root,
        "key": key, "name": path.stem, "source_file": path.name,
        "source_name": source_name,
        "lines": text.count("\n") + 1,
    }


def main():
    merge = "--merge" in sys.argv

    # ---- gather ----
    all_atoms = []
    all_scenes = []
    tracks_by_col = {}  # col -> [track_dict, ...]

    for src in SOURCES:
        d = src["dir"]
        if not d.exists():
            print(f"  skip {src['name']}: {d} not found")
            continue
        files = sorted(d.glob("*.py"))
        print(f"  {src['name']} ({d}): {len(files)} .py files")

        # atoms (union from all sources)
        for p in files:
            all_atoms.extend(extract_atoms(p, src["name"]))

        # scenes
        for p in files:
            all_scenes.extend(extract_scenes(p, src["name"]))

        # tracks (per source, into assigned column(s), 200 per col)
        src_tracks = []
        for p in files:
            t = analyze_track(p, src["name"])
            if t and t["lines"] > 5:
                src_tracks.append(t)
        src_tracks.sort(key=lambda t: t["name"].lower())
        for col in src["tracks_cols"]:
            tracks_by_col.setdefault(col, [])
        # paginate across the source's columns, 200 per col
        for i, t in enumerate(src_tracks):
            col_idx = i // 200
            if col_idx >= len(src["tracks_cols"]):
                break
            col = src["tracks_cols"][col_idx]
            tracks_by_col[col].append(t)

    print()
    print(f"total atoms found:  {len(all_atoms)}")
    print(f"total scenes found: {len(all_scenes)}")
    for col, ts in tracks_by_col.items():
        # find which source owns this column
        src_name = None
        for s in SOURCES:
            if col in s["tracks_cols"]:
                src_name = s["name"]
                break
        print(f"tracks for col {col} ({src_name}): {len(ts)}")

    # ---- Atoms: spread variants across the 10 rows of each (col, decade) ----
    # Each (col, decade) tempo-band holds up to 10 distinct atom variants.
    # First-precise-row wins for the cell at its computed row; remaining
    # variants fill empty rows in the decade in deterministic order.
    atoms_by_decade = defaultdict(list)
    for a in all_atoms:
        col = a["coord"][0]
        row = int(a["coord"][1:])
        decade = row // 10
        sig = a["code"][:160]
        if not any(x["code"][:160] == sig for x in atoms_by_decade[(col, decade)]):
            atoms_by_decade[(col, decade)].append(a)

    atom_proposals = {}
    for (col, decade), group in sorted(atoms_by_decade.items()):
        # Stable order: by (source, then alphabetical source-file label)
        group.sort(key=lambda x: (x.get("source", ""), x.get("label", "")))
        # Distribute up to 10 across rows decade*10 .. decade*10+9
        for i, a in enumerate(group[:10]):
            row = decade * 10 + i
            coord = f"{col}{row}"
            body = {
                "code": a["code"],
                "label": a["label"],
                "type": "atom",
                "tempo": a.get("tempo"),
                "key": a.get("key"),
                "scale": a.get("scale"),
                "root": a.get("root"),
                "instrument": a.get("instrument"),
                "source": a.get("source"),
            }
            atom_proposals[coord] = {k: v for k, v in body.items() if v is not None}

    # Scenes: 400-cell capacity across S0..S199 + T0..T199 (2 cols × 200 rows)
    all_scenes.sort(key=lambda s: (s["source_name"], s["source_file"], s["name"]))
    scene_proposals = {}
    for i, s in enumerate(all_scenes):
        if i >= 400: break
        col = "S" if i < 200 else "T"
        row = i if i < 200 else i - 200
        coord = f"{col}{row}"
        track_name = Path(s["source_file"]).stem
        key = None
        if s["root"] and s["scale"]: key = f"{s['root']} {s['scale']}"
        elif s["root"]: key = s["root"]
        elif s["scale"]: key = s["scale"]
        label = f"{s['name']} from {track_name}"
        if s["tempo"]: label += f" @ {s['tempo']}"
        label += f" ({s['beats']}b)"
        body = {
            "code": s["code"],
            "label": label,
            "type": "scene",
            "tempo": s["tempo"],
            "key": key,
            "source": s["source_name"],
        }
        scene_proposals[coord] = {k: v for k, v in body.items() if v is not None}

    # Tracks: per-column, up to 200 per column (rows 0-199)
    track_proposals = {}
    for col, ts in tracks_by_col.items():
        for i, t in enumerate(ts):
            if i >= 200: break
            coord = f"{col}{i}"
            label = t["name"]
            if t["tempo"]: label += f" @ {t['tempo']}"
            if t["key"]: label += f" {t['key']}"
            label += f" ({t['lines']}L)"
            body = {
                "code": t["code"],
                "label": label,
                "type": "track",
                "tempo": t["tempo"],
                "key": t["key"],
                "source": t["source_name"],
            }
            track_proposals[coord] = {k: v for k, v in body.items() if v is not None}

    # Write per-extractor proposals JSONs for review
    (GRID_DIR / "atoms_extracted.json").write_text(
        json.dumps({"proposed": atom_proposals}, indent=2, ensure_ascii=False))
    (GRID_DIR / "scenes_extracted.json").write_text(
        json.dumps({"proposed": scene_proposals}, indent=2, ensure_ascii=False))
    (GRID_DIR / "tracks_extracted.json").write_text(
        json.dumps({"proposed": track_proposals}, indent=2, ensure_ascii=False))

    print()
    print(f"proposals written: atoms={len(atom_proposals)}, "
          f"scenes={len(scene_proposals)}, tracks={len(track_proposals)}")

    if not merge:
        print("\n(dry-run — no merge into cells.json. Re-run with --merge to fill grid.)")
        return

    # ---- merge ----
    existing = {}
    if CELLS_FILE.exists():
        existing = json.loads(CELLS_FILE.read_text())

    stats = {"atoms_new": 0, "atoms_enriched": 0, "atoms_kept": 0,
             "scenes_new": 0, "scenes_kept": 0,
             "tracks_new": 0, "tracks_kept": 0}

    def merge_proposal(coord, body, kind):
        if coord in existing:
            cur = existing[coord]
            changed = False
            for k, v in body.items():
                if k in ("code", "label"):
                    continue
                if k not in cur:
                    cur[k] = v
                    changed = True
            if changed:
                stats[f"{kind}_enriched" if kind == "atoms" else f"{kind}_kept"] += 1
            else:
                stats[f"{kind}_kept"] += 1
        else:
            existing[coord] = body
            stats[f"{kind}_new"] += 1

    for coord, body in atom_proposals.items():
        merge_proposal(coord, body, "atoms")
    for coord, body in scene_proposals.items():
        merge_proposal(coord, body, "scenes")
    for coord, body in track_proposals.items():
        merge_proposal(coord, body, "tracks")

    # Atomic write
    with tempfile.NamedTemporaryFile("w", dir=str(GRID_DIR), delete=False,
                                     suffix=".json") as tf:
        json.dump(existing, tf, indent=2, ensure_ascii=False)
        tmp = tf.name
    os.replace(tmp, CELLS_FILE)

    print()
    print(f"merged into cells.json:")
    print(f"  atoms:  +{stats['atoms_new']} new, "
          f"{stats['atoms_enriched']} enriched, {stats['atoms_kept']} kept")
    print(f"  scenes: +{stats['scenes_new']} new, {stats['scenes_kept']} kept")
    print(f"  tracks: +{stats['tracks_new']} new, {stats['tracks_kept']} kept")
    total = len([k for k in existing if not k.startswith("_")])
    print(f"  cells.json total: {total} cells")
    print("  -> run `compo.cell_reload()` in your FoxDot session")


if __name__ == "__main__":
    main()
