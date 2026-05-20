# live2027_grid — Changes since live2026

## Grid Registry
A 2D cell library built into webTroop: 26 columns × 400 rows of live coding atoms (loops, synths, FX chains, full tracks). Extracted from codeBank, log_sessions, and Musique — ~1800+ cells total.

- Visual editor served on port 1235, toggleable side panel inside webTroop
- One-click fire via iframe postMessage to FoxDot
- Multi-duration play buttons (8 / 16 / 32 / ∞ bars)
- Per-cell metadata: tempo, key, type, instrument, source
- Filter sidebar to browse by category
- Color-coded cells by role and tempo (HSL modulation)
- 4 sources: codeBank, log_sessions, Musique, external drive — paginated across columns V–Z
- Pattern recipes, composition starters, FX chain presets included
- `compo.cell_*` methods for programmatic cell access

## Recording

### Stems (per-player capture)
- `compo.rec_stems()` / `compo.rec_stems_stop()` — captures each FoxDot player to its own `.wav` stem, synced to bar boundary, equal wallclock length
- Uses `\stemDiskOut` + `\stemTap` SynthDefs in SuperCollider (runs after defaultGroup)
- OSC handlers: `/foxdot_stems_start`, `/foxdot_stems_stop`
- Output in `FoxDot/stems/`

### Code Recording
- `compo.rec()` / `compo.rec_stop()` — records evaluated code with timestamps

### UI Buttons
- Crashpanel: **Rec Code** and **Rec Stems** buttons alongside existing audio Record

## Auto-reload + Rec State Sync
- webTroop auto-reloads cells on file change
- Rec state (audio/code/stems) synced between FoxDot and the UI in real time

## Wavetable Synth (from wavetableTest)
- Updated `wavetable.scd` — MultiWtOsc engine, 5 oscillators, `wtpos` (wavetable position 0–254), `wtdist` (squeeze/distortion), `wide` (stereo spread), full ADSR envelope
- Sweepable `wtpos` via `rate` param (LFTri auto-scan)

## New codeBank Scripts
`dividing.py`, `unknownfate.py`, `halal.py`, `formypeople.py`, `sandinmyshoes.py`, `ambient.py`
