# Changelog — since live2026 (2026-04-30)

Branch: `2027_radialgrid` · 97 commits + current session work

---

## [unreleased] — 2026-05-30 (branch: 2027_radialgrid)

### Radial Cell Dial (`Ctrl+Shift+G`)
- New floating overlay picker (`cellDial.js` + `cellDial.css`)
- **4 domains** cycled with `Tab`: CELLS / ATTACKS / PARTS / ALL
  - CELLS: A–Z ring, columns as slices, brightness = compat score
  - ATTACKS: genre ring (top 16 categories by count, from cells metadata)
  - PARTS: scrollable button list of `#@` sections — Enter jumps editor cursor, Shift+Enter pastes tag
  - ALL: flat search across everything
- **Context chips**: detects BPM and scale from editor text, renders as one-click filter buttons
- **Filter syntax**: bare number `122` or `~122` for BPM ±15, `@minor` / `@F#` for key
- Number shortcuts `1–9` pick Nth visible result; `A–Z` jump to column (CELLS domain)
- `Enter` = paste cell code at cursor · `Shift+Enter` = paste + evaluate
- Footer hint bar shows all active shortcuts

### Keyboard shortcuts
- Unfold all: **`Ctrl+Alt+U`** (was `Ctrl+Alt+F` — conflicted with find)
- Fold all `#@#@` headers: `Ctrl+Shift+F` (may conflict on some setups — use gutter arrows)
- Grid panel: `Ctrl+Shift+Y`
- Piano roll: `Alt+P`
- `docs/shortcuts.md` added — full reference for all Ctrl/Alt/Shift bindings

### Bug fixes
- `drop()`: fixed silent failure when only 1 player active (was `len > 1` guard, now `len > 0`)
- `drop()` intermediate loops: `randint(1, max(1, n-1))` handles n=1 safely
- Grid panel iframe: lazy-loaded on first open (saves ~15–20MB idle RAM)

---

## 2026-05-29

### SuperSonic WASM Proto (`supersonic-proto/`)
- Browser-based live coding environment running scsynth in WebAssembly
- FoxDot-style syntax transpiler, in-browser clock, player engine
- Compiled SynthDefs for WASM target

### Install
- Interactive setup script with path-agnostic build fixes
- SuperSonic WASM engine section in install docs

---

## 2026-05-28

### SuperSonic WASM
- Initial browser live coding env on scsynth WASM (`supersonic-proto/`)

---

## 2026-05-27

### Bug fixes
- `drop()`: timing + thread safety overhaul (originally stashed, now fully applied)
- `crashserver-reference.html`: full HTML reference doc for CrashServer API

---

## 2026-05-25

### CrashPanel & WebSocket stability
- Resilient WS threads: auto-reconnect on disconnect
- `wsServer` sentinel — prevents double-init on hot reload
- Fixed `attack()` NameError when crashpanel loads before FoxDot namespace is ready

---

## 2026-05-22

### Grid — Attacks panel
- Category tabs added to grid editor
- All 209 codeBank files indexed for attack metadata
- Lower line threshold for attack extraction (more cells matched)

### Grid — codeBank two-way sync
- Edit in codeBank → auto-reflected in grid editor
- Edit cell in grid → written back to `codeBank/` file
- Attacks panel tab in grid editor UI

### webTroop UI
- Grid panel layout push: main editor shrinks when panel is open
- Attack markers in grid cells
- WebSocket reconnect indicator
- `start.sh` consolidation

### Grid — Generate system
- `/api/generate` endpoint: produces a `#@`-sectioned track from selected cells
- `.stop()` instead of `>> None` in generated code
- `max_players` cap to avoid SC overload

### Synths
- `juno` SynthDef — Juno-106 style polysynth
- `reese` SynthDef — classic Reese bass (detuned saws + HPF)

### codeBank
- `lurch.py`, `chrome.py`, `redline.py` — trap / hip-hop trilogy
- `tabation.py` — D minor rock, 122 BPM, 7-section arc with Root shift D→F

---

## 2026-05-21

### codeBank
- `sediment.py`, `glycine.py`, `splinter.py`
- `ferment.py` — 170 BPM DnB, delays-as-rhythm; deduplication fix for `play()` loops

---

## 2026-05-20

### Install — full overhaul
- One-click installer for Linux + Windows (PowerShell + winget)
- Python venv support (fixes externally-managed-environment error)
- nvm integration for Node version management
- git-lfs setup
- HOST_IP auto-sync between FoxDot and webTroop config
- Post-install verifier (`verify.sh`)
- `start.sh` consolidated with all service launchers

### Live2027 grid merge
- Pulled `live2027_grid` branch content: pretexte rework, new synths, codeBank + sessions, hub, MIDI tools
- MIDI-to-FoxDot converter (`midi/midi2foxdot.py`)

---

## 2026-05-13

### Grid — major expansion
- **26×400 grid** (was 26×100)
- Extracted atoms from 354 gig log_session files → **+1598 cells**
- Added loop/synth/FX showcase atoms → **+605 cells**
- Pattern recipes, composition starters, FX chain presets → **+159 cells**
- Auto-reload: saving a cell triggers `compo.cell_reload()` in FoxDot automatically
- Per-cell color by tempo + source (HSL modulation in editor)
- Resolve ALL identifiers in cell code (not just synths/players)
- Atom variants spread across rows; larger scenes + tracks

### Recording — UI sync
- `rec_state` / `stems_state` EventBus events: UI buttons auto-reflect FoxDot-side recording state
- `__REC_START__` / `__REC_STOP__` / `__STEMS_START__` / `__STEMS_STOP__` markers parsed from stdout

### webTroop
- **Rec Code** + **Rec Stems** buttons in crashpanel (with bars/session/variation fields)
- Buttons auto-revert when FoxDot-side stop fires (no manual click needed)

---

## 2026-05-12

### Grid — editor features
- Filter sidebar with metadata fields (tempo / key / type / source)
- 4th source: external drive, paginated tracks across V–Z columns
- Custom synths resolved by scanning loaded modules
- All FoxDot symbols injected into `cell_run()` namespace
- Paste button + multi-duration play buttons (8 / 16 / 32 / ∞ bars)
- More robust namespace search for `cell_run`
- Rich metadata per cell (tempo / key / type / instrument)
- 100 full tracks in column Q

---

## 2026-05-11

### Grid — initial system
- `grid/` directory: 2D cell library with `compo.cell_*` methods
  - `compo.cell_run(coord)` — evaluate cell at coordinate
  - `compo.cell_reload()` — reload cells.json into FoxDot namespace
- Visual editor (`grid/editor.html`) served by `grid/serve.py` on port 1235
  - Color-coded cells by role
  - 26×100 standard layout
  - One-click test fire via iframe postMessage to webTroop
- Integrated as toggleable panel in webTroop (`Ctrl+Shift+Y`)
  - Drag-to-resize handle
  - Lazy iframe load on first open
  - Theme sync (webTroop theme forwarded to iframe)
- codeBank extractor (`grid/extract_tracks.py`) → 283 auto-extracted cells

### Stems system
- `compo.rec_stems(bars, session, variation)` — per-player `.wav` capture
- SuperCollider-side bus routing for isolated stem recording
- Designed for adaptive game audio export

---

## 2026-05-08

### codeBank
- `dividing.py`, `unknownfate.py`, `halal.py`, `formypeople.py` (updated)

---

## 2025-12-01

### FoxDot / CrashServer
- Fix: missing `addFx` and Server Global Fx
- Updated autocomplete interface for FX
- Merged `SetFx` branch

---

## 2025-11-08

### codeBank
- `crashpatterns.py` — pattern showcase / recipe collection

---

## 2025-10-14

### FoxDot
- `crashFX.py` updates
- New synths uploaded

---

## 2025-09-19

### Synths (SynthDef additions)
- `a_bd`, `a_sn`, `a_hhat`, `a_stab`, `a_fantom`, `a_bassry` — acoustic-style drums + bass
- `a_gesa`, `a_gesa2`, `a_gesa3` — generative/spectral
- `a_stress`, `a_cy` — cymbals + transient hits
- `a_vene`, `a_daft`, `a_daftlead`, `a_vpad`, `a_poly` — vintage poly/lead
- `a_glead`, `a_xbass` — aggressive lead + sub bass
- `gheavy.scd`, `xbass.scd` — heavy guitar + extended sub

---

## 2025-08-15

### webTroop
- Removed `masterFx` from webTroop UI and startup
- Removed per-player `addFx` calls (handled server-side now)

---

## 2025-06-27 – 2025-06-28

### codeBank
- `blaze.py`, `nowhere.py`, `filter2.py`, `random.py` — early session scripts

---

## Notes

- `drop()` — fixed twice: 2026-05-27 (thread safety), 2026-05-30 (n=1 guard)
- Fold shortcut history: started as `Ctrl+Shift+F` (fold) / `Ctrl+Alt+F` (unfold) → unfold moved to `Ctrl+Alt+U` on 2026-05-30 due to search conflict
- `jpverb` / `mverb` removed from recommended FX (CPU cost) — use `cheapverb` + `cvdecay`
- `prophet` / `xbass` synths not loaded in current startup configuration
