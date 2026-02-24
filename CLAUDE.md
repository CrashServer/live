# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**CrashServer Ultimate** is a live-coding music production system combining:
- **FoxDot** (`FoxDot/`): Python live-coding framework (v0.8.11, fork) that controls SuperCollider for audio synthesis via OSC
- **WebTroop** (`webTroop/`): Node.js + Vite web frontend for collaborative live coding, built on CodeMirror 5 and Yjs
- **SuperCollider**: The audio engine, controlled via OSC messages from FoxDot

The primary language of documentation and comments is French.

## Architecture

```
Browser (port 3000)          Node.js server (port 1234)       FoxDot (Python)        SuperCollider
   CodeMirror editor  ──WS──►  server.js  ──stdin──►  FoxDot process  ──OSC──►  scsynth
   Yjs collab (port 4444)      (spawns FoxDot)        stdout ──►  server ──WS──► all clients
```

- **WebSocket (port 1234)**: Code execution, CPU data, YouTube control, log broadcast between browser clients and server.js
- **Yjs WebSocket (port 4444)**: Real-time collaborative document editing with persistence in `webTroop/dbDir/`
- **OSC (UDP)**: FoxDot sends synth triggers, parameter updates, and effect chains to SuperCollider
- **Serial (115200 baud)**: Optional Arduino hardware integration

### Key message types over WebSocket
- `evaluate_code` — client sends code to execute in FoxDot
- `foxdot_log` — server broadcasts FoxDot stdout to all clients
- `cpu_data` — CPU usage from SuperCollider (via OSC port 2887)
- `yt_*` — YouTube video control commands
- `save_file` — persist code to `codeBank/`

## Development Commands

### WebTroop (frontend + server)

```bash
cd webTroop
npm install                    # install dependencies

# Three processes needed for full system:
npm run db                     # Yjs sync server (port 4444)
node server.js                 # Node.js backend + spawns FoxDot (port 1234)
npm run dev                    # Vite dev server (port 3000)

# Or run frontend + backend together (still need db separately):
npm start                      # concurrently runs dev + server
```

### FoxDot (Python)

```bash
cd FoxDot
pip install -e .               # install in editable mode
```

### Tests

```bash
pytest FoxDot/tests/           # run all tests
pytest FoxDot/tests/test_patterns.py  # run specific test file
```

Test files: `test_patterns.py`, `test_generator_pattern.py`, `test_buffers.py`

## Configuration

Copy `webTroop/crash_config_sample.json` to `webTroop/crash_config.json` and set:
- `HOST_IP`: server IP
- `FOXDOT_PATH`: absolute path to `FoxDot/` directory
- `sample_path`: path to audio samples
- `RECORDING_PATH`: recording output directory
- `FOXDOT_WS_PORT`: WebSocket port for FoxDot communication (default 20000)
- `SC_CPU_PORT`: SuperCollider CPU OSC port (default 2887)

SuperCollider config: `config/FoxDot.sc` (memory, nodes, channels), `config/startuplive.scd` (startup)

## Code Structure

### FoxDot/FoxDot/lib/ — Python core

| Area | Key files |
|------|-----------|
| Player/Synth control | `Players.py`, `TempoClock.py`, `Scale.py` |
| Pattern system | `Patterns/Main.py`, `Patterns/Generators.py`, `Patterns/Sequences.py` |
| Drum/Synth patterns | `DrumPatterns.py`, `SynthPatterns.py` |
| Effects | `Effects/Util.py`, `Effects/NewEffects.py` |
| SuperCollider comms | `ServerManager.py`, `OSC3.py`, `SCLang/SynthDef.py` |
| CrashServer extensions | `Crashserver/crashSynthDefs.py`, `Crashserver/crashFX.py` |
| Server startup/attacks | `Crashserver/crash_generator/startup_live.py`, `weapons.py` |
| Code execution | `Code/main_lib.py` |
| Video control | `VideoControl.py` |

### FoxDot/FoxDot/osc/ — SuperCollider definitions (.scd files)

- `scsyndef/` — 100+ synth definitions (instruments)
- `sceffects/` — audio effects
- `scenvelopes/` — envelope shapes

### webTroop/src/ — Frontend

| Area | Key files |
|------|-----------|
| App entry / editor | `js/main.js` (CodeMirror + Yjs setup) |
| Code execution | `js/functionUtils.js` |
| Autocomplete | `js/foxdotAutocomplete.js` |
| Control panel (BPM, Scale) | `js/crashpanel.js` |
| Config UI | `js/configPanel.js` |
| Visual mode | `js/visualMode.js`, `js/patternViz.js` |
| Video player | `js/video.js` |
| Component messaging | `js/eventBus.js` (EventEmitter pattern) |
| Syntax highlighting | `js/foxdot_mode.js` |

### webTroop/server.js — Node.js backend

Spawns FoxDot as a child process, bridges WebSocket clients to FoxDot stdin/stdout, handles Arduino serial, relays YouTube commands.

## Git Branches

- `master` — production
- `Dev` — development
- Feature branches: `yt_patterns`, `multiScreen`, `midiTroopCtrl`, etc.

## SuperCollider Requirements

Quarks: BatLib, FeedBack, FoxDot, miSCellaneous_lib
Plugins: mi-UGens, PortedPlugins, Open303, SC3 plugins
