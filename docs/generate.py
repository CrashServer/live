#!/usr/bin/env python3
"""
docs/generate.py — Auto-generate reference docs from source files.

Outputs to docs/generated/:
  synths.md          FoxDot synths (parsed from .scd files)
  fx.md              FoxDot FX (parsed from crashFX.py)
  attacks.md         Attacks (from cells.json, attack_category)
  cells.md           Grid cells by column (from cells.json)
  webfoxdot-synths.md  WebFoxDot synth registry (from js/synths/registry.js)
  webfoxdot-fx.md    WebFoxDot FX registry (from js/fx/registry.js)

Usage:
  python3 docs/generate.py [--force]
"""

import re, json, os, sys
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).parent.parent
OUT  = REPO / "docs" / "generated"
OUT.mkdir(parents=True, exist_ok=True)

FORCE = "--force" in sys.argv
NOW   = datetime.now().strftime("%Y-%m-%d %H:%M")

def newer(src_paths, out_path):
    """True if any source is newer than the output, or output missing."""
    if FORCE or not out_path.exists():
        return True
    out_mtime = out_path.stat().st_mtime
    for p in src_paths:
        if isinstance(p, Path) and p.exists() and p.stat().st_mtime > out_mtime:
            return True
    return False

def write(path, content):
    path.write_text(content)
    print(f"  wrote {path.relative_to(REPO)}")

# ─────────────────────────────────────────────────────────────────────────────
# 1. FoxDot synths — parse .scd files
# ─────────────────────────────────────────────────────────────────────────────

def parse_scd_params(text):
    """Extract param=default pairs from SynthDef arg list |...|"""
    m = re.search(r'\|([^|]+)\|', text, re.DOTALL)
    if not m:
        return {}
    params = {}
    for item in m.group(1).split(','):
        item = item.strip()
        if '=' in item:
            k, v = item.split('=', 1)
            params[k.strip()] = v.strip()
        elif item and not item.startswith('//'):
            params[item.strip()] = '—'
    return params

def parse_scd_category(text):
    m = re.search(r'category:\s*\\(\w+)', text)
    return m.group(1) if m else 'misc'

def parse_scd_description(text):
    m = re.search(r'description:\s*"([^"]*)"', text)
    return m.group(1).strip() if m else ''

def gen_synths():
    scd_dir  = REPO / "FoxDot/FoxDot/osc/scsyndef"
    out_path = OUT / "synths.md"
    scd_files = sorted(scd_dir.glob("*.scd")) if scd_dir.exists() else []
    if not scd_files:
        print("  [skip] no .scd synth files found"); return
    if not newer(scd_files, out_path):
        print(f"  [skip] synths.md up to date"); return

    synths = []
    for f in scd_files:
        text = f.read_text(errors='replace')
        # Find SynthDef name
        m = re.search(r'SynthDef(?:\.new)?\s*\(\s*\\(\w+)', text)
        if not m:
            continue
        name     = m.group(1)
        params   = parse_scd_params(text)
        category = parse_scd_category(text)
        desc     = parse_scd_description(text)
        synths.append((category, name, params, desc))

    # Group by category
    by_cat = {}
    for cat, name, params, desc in sorted(synths, key=lambda x: (x[0], x[1])):
        by_cat.setdefault(cat, []).append((name, params, desc))

    lines = [f"# FoxDot Synths Reference", f"_Generated {NOW} from FoxDot/FoxDot/osc/scsyndef/ ({len(synths)} synths)_\n"]

    # Summary table first
    lines += ["## Summary\n", "| Synth | Category | Key params |", "|---|---|---|"]
    for cat, name, params, desc in sorted(synths, key=lambda x: (x[0], x[1])):
        extra = [p for p in params if p not in ('amp','sus','pan','freq','vib','fmod','rate','bus','out')]
        lines.append(f"| `{name}` | {cat} | {', '.join(f'`{p}`' for p in extra[:5])} |")

    lines.append("")

    # Detail by category
    for cat in sorted(by_cat):
        lines += [f"\n## {cat.upper()}\n"]
        for name, params, desc in sorted(by_cat[cat], key=lambda x: x[0]):
            lines.append(f"### `{name}`")
            if desc:
                lines.append(f"_{desc}_\n")
            if params:
                lines.append("| Param | Default |")
                lines.append("|---|---|")
                for p, v in params.items():
                    lines.append(f"| `{p}` | `{v}` |")
            lines.append("")

    write(out_path, '\n'.join(lines))

# ─────────────────────────────────────────────────────────────────────────────
# 2. FoxDot FX — parse crashFX.py
# ─────────────────────────────────────────────────────────────────────────────

def parse_fx_entries(text):
    """Parse FxList.new('name','DisplayName',{params},order=N,tag='cat') blocks."""
    entries = []
    # Join continuation lines then find each FxList.new block
    # Strategy: find all FxList.new( start positions, grab until .save()
    blocks = re.split(r'(?=FxList\.new\()', text)
    for block in blocks:
        if not block.strip().startswith('FxList.new'):
            continue
        # Extract name, display, params dict, tag
        head = re.match(
            r"FxList\.new\s*\(\s*['\"](\w+)['\"],\s*['\"]([^'\"]+)['\"],\s*(\{[^}]*\})",
            block, re.DOTALL
        )
        if not head:
            continue
        name, display, params_raw = head.group(1), head.group(2), head.group(3)

        tag_m = re.search(r"tag\s*=\s*['\"]([^'\"]+)['\"]", block)
        tag   = tag_m.group(1) if tag_m else 'misc'

        doc_m = re.search(r'\.doc\s*\(\s*["\']([^"\']+)["\']', block)
        doc   = doc_m.group(1) if doc_m else ''

        # Parse params dict
        params = {}
        for item in re.finditer(r"['\"](\w+)['\"]\s*:\s*([^,}\n]+)", params_raw):
            params[item.group(1)] = item.group(2).strip().rstrip(',').strip()

        entries.append((tag, name, display, params, doc))
    return entries

def gen_fx():
    fx_file  = REPO / "FoxDot/FoxDot/lib/Crashserver/crashFX.py"
    out_path = OUT / "fx.md"
    if not fx_file.exists():
        print("  [skip] crashFX.py not found"); return
    if not newer([fx_file], out_path):
        print(f"  [skip] fx.md up to date"); return

    text    = fx_file.read_text(errors='replace')
    entries = parse_fx_entries(text)

    by_tag = {}
    for tag, name, display, params, doc in entries:
        by_tag.setdefault(tag, []).append((name, display, params, doc))

    lines = [f"# FoxDot FX Reference", f"_Generated {NOW} from crashFX.py ({len(entries)} effects)_\n"]

    # Summary
    lines += ["## Summary\n", "| FX | Category | Params |", "|---|---|---|"]
    for tag, name, display, params, doc in sorted(entries, key=lambda x: (x[0], x[1])):
        lines.append(f"| `{name}` | {tag} | {', '.join(f'`{p}`' for p in list(params)[:6])} |")
    lines.append("")

    for tag in sorted(by_tag):
        lines += [f"\n## {tag.upper()}\n"]
        for name, display, params, doc in sorted(by_tag[tag]):
            lines.append(f"### `{name}`  —  {display}")
            if doc:
                lines.append(f"_{doc}_\n")
            if params:
                lines.append("| Param | Default |")
                lines.append("|---|---|")
                for p, v in params.items():
                    lines.append(f"| `{p}` | `{v}` |")
            lines.append("")

    write(out_path, '\n'.join(lines))

# ─────────────────────────────────────────────────────────────────────────────
# 3. Attacks — from cells.json
# ─────────────────────────────────────────────────────────────────────────────

def gen_attacks():
    cells_file = REPO / "grid/cells.json"
    out_path   = OUT / "attacks.md"
    if not cells_file.exists():
        print("  [skip] cells.json not found"); return
    if not newer([cells_file], out_path):
        print(f"  [skip] attacks.md up to date"); return

    cells = json.loads(cells_file.read_text())

    # Collect attacks, normalize categories
    by_cat = {}
    for coord, cell in cells.items():
        if not isinstance(cell, dict) or not cell.get('attack_category'):
            continue
        raw_cat = cell['attack_category']
        # take first clean tag from comma-separated
        cat = raw_cat.split(',')[0].strip().lower()
        if cat in ('', '_help', 'proposed'):
            continue
        entry = {
            'coord': coord,
            'label': cell.get('label', coord),
            'tempo': cell.get('tempo', ''),
            'key':   cell.get('key', ''),
            'src':   cell.get('source_file', ''),
            'raw_cat': raw_cat,
        }
        by_cat.setdefault(cat, []).append(entry)

    total = sum(len(v) for v in by_cat.values())
    lines = [f"# Attacks Reference", f"_Generated {NOW} from cells.json ({total} attacks, {len(by_cat)} categories)_\n"]
    lines += ["## Categories\n"]
    for cat in sorted(by_cat):
        lines.append(f"- `{cat}` — {len(by_cat[cat])} attacks")
    lines.append("")

    for cat in sorted(by_cat):
        lines += [f"\n## {cat}  ({len(by_cat[cat])})\n"]
        lines += ["| Coord | Label | BPM | Key | Source |", "|---|---|---|---|---|"]
        for e in sorted(by_cat[cat], key=lambda x: x['coord']):
            src = Path(e['src']).name if e['src'] else '—'
            lines.append(f"| `{e['coord']}` | {e['label'][:40]} | {e['tempo']} | {e['key']} | {src} |")
        lines.append("")

    write(out_path, '\n'.join(lines))

# ─────────────────────────────────────────────────────────────────────────────
# 4. Grid cells by column
# ─────────────────────────────────────────────────────────────────────────────

COL_ROLE = {
    'A':'pad','B':'bass','C':'kick','D':'snare','E':'hihat',
    'F':'drum loop','G':'lead 1','H':'lead 2','I':'chord stab','J':'acid',
    'K':'texture','L':'vox','M':'bell','N':'atmosphere','O':'fx',
    'P':'misc','Q':'full track','R':'track','S':'track','T':'track',
    'U':'track','V':'track','W':'track','X':'track','Y':'track','Z':'track',
}

def gen_cells():
    cells_file = REPO / "grid/cells.json"
    out_path   = OUT / "cells.md"
    if not cells_file.exists():
        print("  [skip] cells.json not found"); return
    if not newer([cells_file], out_path):
        print(f"  [skip] cells.md up to date"); return

    cells = json.loads(cells_file.read_text())

    by_col = {}
    for coord, cell in cells.items():
        if not isinstance(cell, dict) or coord.startswith('_'):
            continue
        col = coord[0].upper()
        by_col.setdefault(col, []).append((coord, cell))

    total = sum(len(v) for v in by_col.values())
    lines = [f"# Grid Cells Reference", f"_Generated {NOW} from cells.json ({total} cells)_\n"]

    # Summary table
    lines += ["## Columns\n", "| Col | Role | Count | Types |", "|---|---|---|---|"]
    for col in sorted(by_col):
        items  = by_col[col]
        role   = COL_ROLE.get(col, '?')
        types  = {}
        for _, c in items:
            t = c.get('type', '?')
            types[t] = types.get(t, 0) + 1
        type_str = ', '.join(f"{t}:{n}" for t, n in sorted(types.items()))
        lines.append(f"| **{col}** | {role} | {len(items)} | {type_str} |")
    lines.append("")

    for col in sorted(by_col):
        role  = COL_ROLE.get(col, '?')
        items = sorted(by_col[col], key=lambda x: x[0])
        lines += [f"\n## {col} — {role}  ({len(items)})\n"]
        lines += ["| Coord | Label | BPM | Key | Type |", "|---|---|---|---|---|"]
        for coord, cell in items:
            label = (cell.get('label') or '')[:40]
            lines.append(
                f"| `{coord}` | {label} | {cell.get('tempo','')} "
                f"| {cell.get('key','')} | {cell.get('type','?')} |"
            )
        lines.append("")

    write(out_path, '\n'.join(lines))

# ─────────────────────────────────────────────────────────────────────────────
# 5. WebFoxDot synths — parse js/synths/registry.js
# ─────────────────────────────────────────────────────────────────────────────

def parse_js_object_keys(text, obj_name):
    """Naive but reliable: find 'key: {' blocks inside a named export const."""
    start = text.find(f'export const {obj_name}')
    if start == -1:
        return {}
    # Find the opening brace of the object
    brace_start = text.index('{', start)
    # Walk to find matching closing brace
    depth, i, obj_text = 0, brace_start, []
    while i < len(text):
        obj_text.append(text[i])
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                break
        i += 1
    return ''.join(obj_text)

def gen_webfoxdot_synths():
    reg_file = REPO / "supersonic-proto/js/synths/registry.js"
    out_path = OUT / "webfoxdot-synths.md"
    if not reg_file.exists():
        print("  [skip] WebFoxDot synths registry not found"); return
    if not newer([reg_file], out_path):
        print(f"  [skip] webfoxdot-synths.md up to date"); return

    text     = reg_file.read_text()
    obj_text = parse_js_object_keys(text, 'SYNTH_DEFS')

    # Extract each synth entry:  name: { scName: '...', defaults: {...}, extraParams: [...] }
    synths = []
    for m in re.finditer(r'(\w+)\s*:\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', obj_text):
        name   = m.group(1)
        body   = m.group(2)
        sc_m   = re.search(r"scName\s*:\s*['\"]([^'\"]+)['\"]", body)
        sc     = sc_m.group(1) if sc_m else name
        # Parse defaults object
        def_m  = re.search(r'defaults\s*:\s*\{([^}]+)\}', body)
        defaults = {}
        if def_m:
            for dm in re.finditer(r'(\w+)\s*:\s*([^,}\n]+)', def_m.group(1)):
                defaults[dm.group(1)] = dm.group(2).strip().rstrip(',')
        # Parse extraParams array
        ep_m   = re.search(r'extraParams\s*:\s*\[([^\]]*)\]', body)
        extra  = re.findall(r"['\"](\w+)['\"]", ep_m.group(1)) if ep_m else []
        raw_m  = re.search(r'rawSus\s*:\s*(true|false)', body)
        raw_sus = raw_m.group(1) if raw_m else 'false'
        synths.append((name, sc, defaults, extra, raw_sus))

    lines = [f"# WebFoxDot Synths", f"_Generated {NOW} from supersonic-proto/js/synths/registry.js ({len(synths)} synths)_\n"]
    lines += ["| Synth | SC name | Extra params |", "|---|---|---|"]
    for name, sc, defaults, extra, _ in synths:
        lines.append(f"| `{name}` | `{sc}` | {', '.join(f'`{e}`' for e in extra)} |")
    lines.append("")

    for name, sc, defaults, extra, raw_sus in synths:
        lines.append(f"## `{name}`")
        lines.append(f"SC SynthDef: `{sc}`  |  rawSus: {raw_sus}\n")
        if defaults:
            lines += ["| Param | Default |", "|---|---|"]
            for p, v in defaults.items():
                lines.append(f"| `{p}` | `{v}` |")
        if extra:
            lines.append(f"\nExtra params: {', '.join(f'`{e}`' for e in extra)}")
        lines.append("")

    write(out_path, '\n'.join(lines))

# ─────────────────────────────────────────────────────────────────────────────
# 6. WebFoxDot FX — parse js/fx/registry.js
# ─────────────────────────────────────────────────────────────────────────────

def gen_webfoxdot_fx():
    reg_file = REPO / "supersonic-proto/js/fx/registry.js"
    out_path = OUT / "webfoxdot-fx.md"
    if not reg_file.exists():
        print("  [skip] WebFoxDot FX registry not found"); return
    if not newer([reg_file], out_path):
        print(f"  [skip] webfoxdot-fx.md up to date"); return

    text = reg_file.read_text()

    # Parse each entry: name: { scParam: '...', default: ..., desc: '...' }
    entries = []
    for m in re.finditer(
        r"(\w+)\s*:\s*\{\s*scParam\s*:\s*['\"]([^'\"]+)['\"]\s*,\s*default\s*:\s*([^,]+),\s*desc\s*:\s*['\"]([^'\"]*)['\"]",
        text
    ):
        entries.append({
            'name':    m.group(1),
            'scParam': m.group(2),
            'default': m.group(3).strip(),
            'desc':    m.group(4),
        })

    # Group by comment-section headers (lines starting with //)
    # Simple approach: just list them
    lines = [f"# WebFoxDot FX Registry", f"_Generated {NOW} from supersonic-proto/js/fx/registry.js ({len(entries)} params)_\n"]
    lines += ["| Param | SC param | Default | Description |", "|---|---|---|---|"]
    for e in entries:
        lines.append(f"| `{e['name']}` | `{e['scParam']}` | `{e['default']}` | {e['desc']} |")
    lines.append("")

    # Also show how to add
    lines += [
        "## Adding a new FX param\n",
        "1. Add the processing to `synthdefs/src/fx/fx_chain.scd`",
        "2. Add entry here in `js/fx/registry.js`:",
        "```javascript",
        "myeff: { scParam: 'myeff', default: 0, desc: 'My effect (0=off, 1=full)' },",
        "```",
        "3. Run `scripts/build.sh` to recompile, reload browser",
    ]

    write(out_path, '\n'.join(lines))

# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print(f"Generating docs → {OUT.relative_to(REPO)}/\n")
    gen_synths()
    gen_fx()
    gen_attacks()
    gen_cells()
    gen_webfoxdot_synths()
    gen_webfoxdot_fx()
    print("\nDone.")
