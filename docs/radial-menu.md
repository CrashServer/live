# Radial Menu — Adding & Managing Content

The radial menu (Ctrl+Shift+G) draws from three sources:
  - cells.json       → Cells domain (A-Z columns)
  - cells.json       → Attacks domain (attack_category field)
  - Editor content   → Parts domain (live-parsed #@ tags)

---

## Adding a Cell

Cells live in `grid/cells.json`. Each key is a coordinate (column + number).

```json
"B42": {
  "code": "b1 >> dbass([0, 7, 4], oct=4, dur=1/2, lpf=800)",
  "label": "dark sub 120",
  "type": "atom",
  "tempo": 120,
  "key": "E minor",
  "root": "E",
  "instrument": "dbass",
  "source": "manual"
}
```

### Column conventions

```
A  pad          B  bass         C  kick         D  snare
E  hihat        F  drum loop    G  lead 1        H  lead 2
I  chord stab   J  acid         K  texture       L  vox
M  bell         N  atmosphere   O  FX            P  misc
Q  full track   R-Z  track
```

### Cell types

```
atom      single player snippet (most cells)
track     full .py performance script (column Q)
scene     multi-player section
starter   template / starting point
```

### Adding via the Grid Editor

1. Open http://localhost:1235 (or Ctrl+Shift+Y in webTroop)
2. Click an empty coordinate
3. Paste code, fill label / key / tempo
4. Click Save — updates cells.json immediately
5. Radial menu picks up changes on next open (30s cache)

### Adding manually

Edit `grid/cells.json` directly. The coordinate determines the column.
Use `python3 grid/extract_tracks.py` to bulk-import from codeBank.

---

## Adding an Attack

Attacks are cells with an `attack_category` field. They appear in the Attacks domain
of the radial menu, grouped by genre tag.

```json
"Q47": {
  "code": "# banger 143\nClock.bpm=143\n...",
  "label": "banger 143 C# zhi",
  "type": "track",
  "tempo": 143,
  "key": "C# zhi",
  "attack_category": "banger",
  "source_file": "codeBank/s33d.py"
}
```

### attack_category values (normalized tags)

```
banger          techno          ambient         drums
drone           trance          experimental    algorave
dark            aggressive      chaosbits       recorded
WIP / todo      garbage         (empty = not an attack)
```

Comma-separated categories are allowed: `"banger, algorave"`.
The radial menu splits on comma and shows the first clean tag in the ring.

### Making a codeBank script into an attack

In cells.json, add `"attack_category": "banger"` (or whichever tag fits)
to a track-type cell. Or run:

```python
# grid/import_codebank_tracks.py — bulk import with category tagging
python3 grid/import_codebank_tracks.py --category banger codeBank/mytrack.py
```

---

## Adding Parts (#@ Sections)

Parts are read live from the current editor document — no file to edit.

In your `.py` script, add section tags:

```python
#@intro(32)
Clock.bpm = 120
p1 >> dbass([0], oct=4)

#@build(16)
p1.oct = 5

#@drop(32)
p2 >> lead([0, 4, 7], dur=1/4)

#@outro(8)
p2.stop()
```

### Syntax

```
#@name(beats)       section with beat count shown in radial menu
#@name              section without beat count
#@#@Track Name      track header (for folding, not a playable part)
```

### Reserved names (shown with distinct color in menu)

```
intro   build   peak   break   drop   outro
```

Custom names (`#@myriff(8)`) are shown as type `section`.

### Using parts from the radial menu

- Switch to Parts domain: press `p` or Tab to PARTS
- Press 1-9 to directly fire a section
- Enter on a focused section → jumps to that line + evaluates
- The ring shows segment sizes for intro/build/peak/break/drop/outro types

---

## cells.json format reference

```json
{
  "COORD": {
    "code":            "string  — FoxDot code to paste/eval",
    "label":           "string  — display name in radial menu",
    "type":            "atom | track | scene | starter",
    "tempo":           120,
    "key":             "E minor",
    "root":            "E",
    "instrument":      "dbass",
    "attack_category": "banger",
    "source_file":     "codeBank/mytrack.py",
    "source":          "manual | codeBank | log"
  }
}
```

All fields except `code` are optional (used for scoring and filtering).

---

## Paths

```
Cell data:          grid/cells.json
Grid editor:        http://localhost:1235
Extract from logs:  python3 grid/extract_logs.py
Extract from files: python3 grid/extract_tracks.py
Bulk import:        python3 grid/import_codebank_tracks.py
```
