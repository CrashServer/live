# Grid Registry — Cell Library

A 2D grid of role-focused FoxDot snippets addressable by coordinate
(`A0`..`Z99`). Each cell is a short, composable snippet — typically
one player declaration + a label.

## File

All cells live in `cells.json`. Single file, hand-editable for V1.
The `_meta` key documents the convention (column = role, row = tempo
band). Strip `_meta` before saving programmatically.

## Convention

```
Columns (role):                    Rows (tempo band):
  A — pad           (p1)             0-9    : 60-80 BPM
  B — bass          (b1)             10-19  : 80-100 BPM
  C — kick          (k1)             20-29  : 100-120 BPM
  D — snare/clap    (s1)             30-39  : 120-140 BPM
  E — hihat         (h1)             40-49  : 140-160 BPM
  F — drum loop     (l1)             50-59  : 160-180 BPM
  G — lead 1        (m1)             60-69  : 180-200 BPM
  H — lead 2        (n1)             70-89  : variations / alt scales
  I — chord stab    (c1)             90-99  : one-shots / fills
  J — acid          (t1)
  K — texture       (x1)
  L — vocal         (v1)
  M — bell          (e1)
  N — atmo loop     (a1)
  O — FX            (f1)
  P — modular       (q1)
  Q-Z — user-defined
```

Each cell's code SHOULD use the column-canonical player name so
calling cells from different columns stacks them without collisions
(e.g., `attack("B32")` updates `b1`, `attack("C32")` updates `k1` —
they coexist).

## Usage

In webTroop or any FoxDot session:

```python
compo.cells_list()              # all populated cells
compo.cells_list('B')           # all column-B (bass) cells
compo.cells_list('B3')          # B30..B39 (120-140 BPM basses)

compo.cell_display('B32')       # print the code for inspection
compo.cell_run('B32')           # fire it, runs forever
compo.cell_run('B32', 8)        # fire it, auto-stop after 8 beats

compo.cell_reload()             # re-read cells.json from disk
                                # (useful after external editing)

compo.cell_save('B32',          # save / overwrite a cell
                code='b1 >> dbass(...)',
                label='rolling sub-bass')

compo.cell_delete('B32')        # remove a cell
```

## Three actions in webTroop UI

When the grid is shown as a side panel, clicking a cell offers:

- **Display** (👁): `compo.cell_display(coord)` — prints the code, no
  execution. For inspection or copying.
- **Run** (▶): `compo.cell_run(coord)` — fires the code, players run
  until you stop them manually.
- **Run + auto-stop** (⏱ N): `compo.cell_run(coord, N)` — fires the
  code, auto-stops the players the cell created N beats later. N is
  one of 2, 4, 8, 16, 64.

## Adding cells

For V1, hand-edit `cells.json`:

```json
{
  "B32": {
    "code": "b1 >> dbass([0, 0, -2, 0], dur=1/2, oct=4, ...)",
    "label": "rolling sub-bass 120 BPM"
  }
}
```

Then `compo.cell_reload()` in the session — picks up the new cell
without restart.

Later (phase 2) a web-based editor will land at `/grid-editor` on
the webTroop server.

## Player-name conventions per column

Sticking to the per-column canonical player name is what makes the
grid composable. If you write a column-B cell that uses `b2` instead
of `b1`, you break the slot model — the next column-B cell you
fire won't replace it.

The editor (when built) will enforce this; for now, keep it tidy
manually.
