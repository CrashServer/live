# webTroop Keyboard Shortcuts

All shortcuts use the main editor (CodeMirror, sublime keymap base).

---

## Evaluate & Execute

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` | Evaluate current block (detect block from cursor position) |
| `Ctrl+Alt+Enter` | Evaluate current block with multi-player broadcast |
| `Ctrl+;` | **Stop all** — `Clock.clear()` + `soff()`, cancels any active sequence |

---

## Comment & Mute

| Shortcut | Action |
|----------|--------|
| `Alt+X` | Toggle comment on current line **and re-evaluate** the block (live mute/unmute) |
| `Ctrl+Alt+X` | Toggle comment on **entire block** and re-evaluate (mute/unmute whole player) |

---

## Player controls

| Shortcut | Action |
|----------|--------|
| `Alt+S` | Solo current player (`player.solo()`) |
| `Ctrl+Alt+S` | Unsolo all players (`unsolo()`) |
| `Alt+O` | Solo drop — solo player, schedule `unsolo()` at next bar-of-64 |
| `Alt+R` | Reset player — evaluates `~player_line` (sends stop event) |

---

## Number tweaking (live parameter editing)

| Shortcut | Action |
|----------|--------|
| `Alt+↑` | Increment number under cursor **+1** (integers) / **+0.1** (decimals), re-eval |
| `Alt+↓` | Decrement **−1** / **−0.1**, re-eval |
| `Ctrl+↑` | Increment **+10** (integers > 300 → +100), re-eval |
| `Ctrl+↓` | Decrement **−10**, re-eval |
| `Alt+A` | **Randomizer** — replace parameter value under cursor with a random alternative from the known range |

All increment/decrement also trigger `autoRecCapture` if automation recording is armed.

---

## Automation recorder

| Shortcut | Action |
|----------|--------|
| `Alt+T` | **Arm / Disarm** — arm: starts recording; disarm: converts recorded Alt+↑↓ tweaks into a `var([...], [...])` TimeVar and replaces the parameter in-place |
| `Esc` | **Cancel** recording (while armed) — restores original parameter values |

Use: arm with `Alt+T`, then tweak values with `Alt+↑/↓`, then disarm with `Alt+T` again. Produces a `var()` pattern automatically.

---

## Navigation

| Shortcut | Action |
|----------|--------|
| `Ctrl+Left` | Jump to previous comma (navigate function arguments) |
| `Ctrl+Right` | Jump to next comma |
| `Ctrl+Alt+Left` | Go to line start |
| `Ctrl+Alt+Right` | Go to line end |
| `Alt+J` | Jump to **other player's cursor** (collaborative — jumps to co-editor position) |
| `Ctrl+Alt+J` | Return to **previous position** (undo last jump) |
| `Ctrl+J` | Jump to **current section** in active sequence (if sequencer running) |

---

## Sequencer (#@ sections)

| Shortcut | Action |
|----------|--------|
| `Ctrl+;` | Cancel active sequence and stop all |
| `Ctrl+Shift+J` | Cancel sequence only (keeps clock running) |
| `Ctrl+J` | Scroll editor to the currently-playing section |

Sections are `#@name(bars)` tags. Evaluate the tag line with `Ctrl+Enter` to start sequencing.

---

## Folding

| Shortcut | Action |
|----------|--------|
| `Ctrl+Alt+U` | **Unfold all** — expand everything |
| Gutter arrow | Click fold gutter to fold/unfold individual `#@` or `#@#@` blocks |

`#@#@` = track header (folds entire track). `#@` = section (folds section block).

> Note: `Ctrl+Shift+F` (fold-all) may conflict with browser/system search on some setups — use gutter arrows instead. `Ctrl+Alt+F` was changed to `Ctrl+Alt+U` (unfold) to avoid the find-bar conflict.

---

## Search & Find

| Shortcut | Action |
|----------|--------|
| `Alt+F` | Open persistent find bar |
| `Ctrl+G` | Find next match |
| `Alt+I` | **Show definition** — tooltip with synth/function docs for word under cursor |
| `Ctrl+Space` | **Autocomplete** — FoxDot synths, effects, patterns, functions |

---

## Save & File

| Shortcut | Action |
|----------|--------|
| `Ctrl+S` | Save editor content (persists to server) |

---

## Panels & UI

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+G` | Open / close **Cell Dial** (radial cell picker) |
| `Ctrl+Shift+Y` | Toggle **Grid Panel** |
| `Alt+P` | Toggle **Piano Roll** panel |

### Cell Dial (`Ctrl+Shift+G`)

| Key | Action |
|-----|--------|
| `Tab` / `Shift+Tab` | Cycle domain: CELLS → ATTACKS → PARTS → ALL |
| `A`–`Z` | (CELLS domain, empty filter) jump to column |
| `1`–`9` | Pick Nth visible result directly |
| `↑` / `↓` | Navigate results |
| `Enter` | Paste cell code at cursor (PARTS: jump to section) |
| `Shift+Enter` | Paste + evaluate immediately |
| `Backspace` | Clear active column/category filter |
| `Esc` | Close |
| `~120` | Filter by BPM ±10 |
| `@em` | Filter by key (e.g. `@minor`, `@F#`) |

---

## Sublime keymap (base layer)

webTroop uses CodeMirror's `sublime` keymap as the base. Key inherited bindings:

| Shortcut | Action |
|----------|--------|
| `Ctrl+D` | Select next occurrence of word |
| `Ctrl+L` | Select entire line |
| `Ctrl+Shift+K` | Delete line |
| `Ctrl+/` | Toggle line comment (standard) |
| `Ctrl+Z` / `Ctrl+Y` | Undo / Redo |
| `Ctrl+F` | Find (CodeMirror default — use `Alt+F` for persistent) |
| `Home` / `End` | Line start / end |
| `Alt+Click` | Multiple cursors |

---

## Tip: live-mute pattern

Most common live-coding mute flow:
1. Put cursor on a player line
2. `Alt+X` → toggles comment + re-evals → player goes silent / comes back
3. Entire block: `Ctrl+Alt+X` → comments all lines in block + re-evals

## Tip: number tweak + autoRec

To capture a live tweak as a TimeVar:
1. `Alt+T` to arm (indicator appears)
2. Use `Alt+↑/↓` several times at different moments
3. `Alt+T` again → disarms, generates `var([val1, val2, ...], [t1, t2, ...])` in-place
4. `Esc` while armed → cancels and restores original values
