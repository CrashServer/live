# WebFoxDot

A browser-based live coding environment that runs **scsynth** (SuperCollider's audio server) compiled to WebAssembly. Write FoxDot-style Python syntax in the browser — no SuperCollider installation required for the audience-facing version.

---

## How it works

```
Browser editor  →  JS transpiler  →  eval()  →  Player engine
                                                      ↓
                                              scsynth WASM  →  Web Audio API
```

- The editor transpiles FoxDot-like Python syntax to JavaScript in real time
- Players schedule notes via a JS clock and send OSC-style messages to scsynth
- scsynth runs as a WebAssembly + AudioWorklet module in the browser
- SynthDefs are precompiled to `.scsyndef` binary files and loaded at boot

---

## Requirements

| Tool | Version | Use |
|------|---------|-----|
| Python 3 | 3.8+ | dev server (`serve.py`) |
| SuperCollider | 3.12+ | compiling SynthDefs only |
| A modern browser | Chrome 90+ / Firefox 90+ | running the app |

> **Note:** SuperCollider (`sclang`) is only needed if you edit or add SynthDefs. The compiled `.scsyndef` files are checked in, so most users never need SC.

---

## Quick start (local dev)

```bash
# 1. Clone / enter the project
cd /path/to/supersonic-proto

# 2. Start the dev server
python3 serve.py

# 3. Open in browser
open http://127.0.0.1:8765
```

The dev server (`serve.py`) sets the required CORS headers (`Cross-Origin-Opener-Policy`, `Cross-Origin-Embedder-Policy`) that the WASM audio worklet needs. **You cannot open `index.html` directly as a `file://` URL** — it will fail to boot.

---

## Deploying to a server

### Nginx

```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com;

    root /var/www/webfoxdot;
    index index.html;

    # Required headers for SharedArrayBuffer / WASM threads
    add_header Cross-Origin-Opener-Policy   "same-origin"   always;
    add_header Cross-Origin-Embedder-Policy "require-corp"  always;
    add_header Cache-Control                "no-store"      always;

    location / {
        try_files $uri $uri/ =404;
    }

    # Serve .scsyndef as binary
    location ~* \.scsyndef$ {
        default_type application/octet-stream;
    }
}
```

### Apache

```apache
<VirtualHost *:443>
    DocumentRoot /var/www/webfoxdot

    Header always set Cross-Origin-Opener-Policy   "same-origin"
    Header always set Cross-Origin-Embedder-Policy "require-corp"
    Header always set Cache-Control                "no-store"

    AddType application/octet-stream .scsyndef .wasm
</VirtualHost>
```

### Caddy (simplest)

```caddyfile
yourdomain.com {
    root * /var/www/webfoxdot
    file_server

    header {
        Cross-Origin-Opener-Policy   "same-origin"
        Cross-Origin-Embedder-Policy "require-corp"
        Cache-Control                "no-store"
    }
}
```

### What to deploy

Copy the entire project directory. Nothing needs to be built for the JS side — it uses native ES modules. Only the `synthdefs/compiled/` binaries need to be up to date.

```
webfoxdot/
  index.html
  css/
  js/
  lib/           ← WASM + CodeMirror bundled here
  synthdefs/
    compiled/    ← precompiled .scsyndef binaries (must be present)
    src/         ← source .scd files (optional on server)
  scripts/       ← build tooling (optional on server)
  serve.py       ← only needed for local dev
```

---

## Project structure

```
supersonic-proto/
├── index.html                 Main app (thin bootstrap + eval context)
├── serve.py                   Local dev server (Python, sets CORS headers)
├── css/
│   └── style.css              All styles + 3 themes (dark / cyberpunk / synthwave)
├── js/
│   ├── engine/
│   │   ├── clock.js           BPM clock, player registry, beat scheduling
│   │   ├── player.js          Player class (>> operator, FX chain, methods)
│   │   └── scale.js           Scale/Root tables, degree → MIDI
│   ├── synths/
│   │   └── registry.js        SYNTH_DEFS: defaults, extraParams, buildParams()
│   ├── fx/
│   │   ├── registry.js        FX_REGISTRY: param name → SC param mapping
│   │   └── chain.js           Per-player FX chain SynthDef node management
│   ├── patterns/
│   │   ├── sequences.js       Pattern classes: PRand, PStutter, PEuclid, etc.
│   │   └── timevars.js        TimeVar interpolators: var, linvar, sinvar, expvar
│   ├── editor/
│   │   ├── foxdot_mode.js     CodeMirror syntax overlay (plain script, not module)
│   │   ├── transpiler.js      Python → JS transpiler (>> operator, kwargs, etc.)
│   │   ├── autocomplete.js    Ctrl+Space: synths, params, FX, methods
│   │   └── keybindings.js     Alt+Up/Down value nudge, Alt+X stop player
│   └── ui/
│       └── crashpanel.js      Right sidebar: clock display, players, tap tempo
├── lib/
│   ├── codemirror/            CodeMirror 5 + addons (bundled, no npm needed)
│   └── dist/
│       ├── supersonic.js      SuperSonic WASM wrapper
│       └── wasm/
│           └── scsynth-nrt.wasm   SuperCollider server (compiled to WASM)
├── synthdefs/
│   ├── src/
│   │   ├── synths/            One .scd file per synth
│   │   └── fx/                FX chain .scd
│   └── compiled/              Binary .scsyndef files (loaded at boot)
└── scripts/
    ├── build.sh               Compile SynthDefs via sclang
    └── compile.scd            sclang compile entry point
```

---

## Adding a synth

### 1. Write the SynthDef

Create `synthdefs/src/synths/mysynth.scd`:

```supercollider
// mysynth — short description
// Params: out, note, amp, sus, pan, attack, release, myParam1, myParam2
SynthDef(\fd_mysynth, {|out=0, note=60, amp=0.8, sus=1, pan=0,
                         attack=0.01, release=0.1,
                         myParam1=440, myParam2=0.5|
    var freq, sig, env;
    freq = note.midicps;
    env  = EnvGen.ar(Env.perc(attack, sus), doneAction: 2);
    sig  = SinOsc.ar(freq) * amp * env;
    Out.ar(out, Pan2.ar(sig, pan));
}).writeDefFile(~outDir);
"fd_mysynth done".postln;
```

The `~outDir` variable is set by the build script — do not hardcode a path.

### 2. Compile

```bash
./scripts/build.sh mysynth      # compile single synth
# or
./scripts/build.sh              # compile everything
```

This requires `sclang` in `PATH`.

### 3. Register in JS

Add to `synthdefs/src/synths/` list in `scripts/compile.scd`, then add to `js/synths/registry.js`:

```javascript
mysynth: {
    scName:      'fd_mysynth',
    defaults:    { oct: 4, amp: 0.7, dur: 1, pan: 0, attack: 0.01, release: 0.1,
                   myParam1: 440, myParam2: 0.5 },
    extraParams: ['myParam1', 'myParam2'],
},
```

### 4. Load at boot

Add `'fd_mysynth'` to the `SYNTHDEFS_TO_LOAD` array in `index.html`:

```javascript
const SYNTHDEFS_TO_LOAD = [
    'fd_dbass', 'fd_saw', 'fd_sine', 'fd_rsin', 'fd_donk',
    'fd_fx_chain',
    'fd_mysynth',   // ← add here
];
```

### 5. Expose in eval context

In `index.html`, the eval context automatically includes all synths from `SYNTH_DEFS` — no extra step needed.

---

## Adding an FX

### 1. Add a section to `synthdefs/src/fx/fx_chain.scd`

The FX chain is a single per-player SynthDef. Each FX is a wet/dry section:

```supercollider
// Chorus
wet = ... ;
sig = XFade2.ar(sig, wet, chorus * 2 - 1);   // chorus=0 → bypass, chorus=1 → full
```

### 2. Recompile

```bash
./scripts/build.sh fx_chain
```

### 3. Register in `js/fx/registry.js`

```javascript
chorus:       { scParam: 'chorus',      default: 0,   desc: 'Chorus mix' },
chorus_depth: { scParam: 'chorus_depth',default: 0.3, desc: 'Modulation depth' },
chorus_rate:  { scParam: 'chorus_rate', default: 0.5, desc: 'Modulation rate Hz' },
```

Any key in `FX_REGISTRY` is automatically:
- Routed to the FX chain (not the synth)
- Updated on every beat step (supports TimeVars)
- Available in autocomplete

---

## Keyboard shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` | Run block at cursor (or selection) |
| `Alt+X` | Stop player on current line |
| `Ctrl+Space` | Autocomplete (empty line → new player) |
| `Alt+↑ / ↓` | Nudge number under cursor ±1 (or ±0.1 for floats) |
| `Shift+Alt+↑ / ↓` | Nudge ×10 |
| `Ctrl+/` | Toggle line comment |

---

## Syntax reference

WebFoxDot uses a Python-like syntax that is transpiled to JavaScript.

### Players

```python
# p1 >> synth(degree, key=value, ...)
p1 >> dbass([0, -3, 0, 4], oct=3, amp=0.9, dur=1)
p1 >> saw([0, 4, 7], oct=4, cutoff=2000, reverb=0.3)

# Stop a player
p1 >> rest()    # or Alt+X on the line
```

### Clock & Scale

```python
Clock.bpm = 140
Scale.default = "dorian"
Root.default = 2       # D
```

### Patterns

```python
PRand([0, 2, 4, 7])          # random pick from list
PWalk(max=5, step=2)         # random walk
PDur(3, 8)                   # Euclidean: 3 pulses in 8 steps
PPing([0, 2, 4, 7])          # ping-pong
PStutter([0, 2, 4], 2)       # [0,0,2,2,4,4]
PAlt([0,4], [7,5])           # alternate between two lists
PShuf([0,2,4,7])             # shuffle once, cycle
PBern(0.7)                   # 1 with prob 0.7, else 0
PEuclid(8, 3)                # Euclidean rhythm 3-in-8
PRange(0, 8, 2)              # [0,2,4,6]
PSine(0, 7, 16)              # sine sweep 0→7 over 16 steps
PTri(0, 12, 8)               # triangle sweep
PChain({0:[2,4], 2:[0,7], 4:[0,2,5]})   # Markov chain
```

### TimeVars

```python
# var([values], [durations_in_beats])  — step-hold
cutoff=var([400, 2000], [8, 8])

# linvar([values], [durations])  — linear interpolation
amp=linvar([0.3, 1.0], [16, 16])

# sinvar — sine-eased
drive=sinvar([0, 1], [32, 32])

# expvar — exponential (good for frequency sweeps)
cutoff=expvar([200, 8000], [16, 16])
```

### FX params

All FX params can be TimeVars or plain values:

| Param | Range | Description |
|-------|-------|-------------|
| `reverb` | 0–1 | Reverb mix |
| `room` | 0–1 | Room size |
| `damp` | 0–1 | High-freq damping |
| `lpf` | 0–1 | Low-pass mix |
| `lpf_freq` | 20–20000 | LPF cutoff Hz |
| `lpf_rq` | 0.01–1 | LPF resonance |
| `hpf` | 0–1 | High-pass mix |
| `hpf_freq` | 20–20000 | HPF cutoff Hz |
| `tanh` | 0–1 | Soft saturation mix |
| `drive` | 0.01–100 | Drive amount |
| `echo` | 0–1 | Echo mix |
| `echo_time` | 0.001–2 | Echo delay seconds |
| `echo_dec` | 0–8 | Echo feedback |

### Player methods

```python
p1.stop()                    # stop immediately
p1.solo()                    # stop all other players
p1.every(8, 'stutter', 4)   # stutter every 8 beats
p1.every(16, 'reverse')     # reverse degrees every 16 beats
p1.every(4, 'shuffle')      # shuffle every 4 beats
```

### Utility

```python
drop(14, 2)          # silence random players for 14b, restore over 2b
drop(8, 4, 2)        # 2 loops
```

---

## Available synths

| Name | Description | Extra params |
|------|-------------|--------------|
| `dbass` | Deep bass — detuned VarSaw + RLPF | `cutoff`, `rq`, `phase` |
| `saw` | Detuned sawtooth pair + RLPF | `cutoff`, `rq`, `rate` |
| `sine` | Sine with FM feedback | `cutoff`, `rq`, `rate` |
| `rsin` | Resonant sine — SinOscFB + narrow RLPF | `cutoff`, `rq`, `feedback` |
| `donk` | Ringz resonator (raw decay time) | *(none — uses `dur` as Ringz decay)* |

---

## Troubleshooting

**"Boot failed" on first load**
The WASM module requires `SharedArrayBuffer`, which needs HTTPS or `localhost` with the `COOP/COEP` headers. Make sure you're using `http://127.0.0.1:8765` (not `file://`).

**No sound after booting**
Browsers block audio until a user gesture. Click the "boot" button directly — don't trigger it programmatically on page load.

**SynthDef load fails**
Check that `synthdefs/compiled/fd_<name>.scsyndef` exists. Run `./scripts/build.sh` to recompile.

**Player never fires**
If a player is assigned but silent, check the log panel for JS errors. A common cause is a transpiler failure — look for `transpiled:` in the browser console.

**`sclang` not found when compiling**
On Arch Linux: `sudo pacman -S supercollider`  
On Ubuntu/Debian: `sudo apt install supercollider`  
On macOS: install SuperCollider app, then `export PATH="/Applications/SuperCollider.app/Contents/MacOS:$PATH"`

---

## CORS headers — why they're required

The SuperCollider WASM module uses `SharedArrayBuffer` for the audio worklet communication, which requires the page to be in a [secure context](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts) with cross-origin isolation:

```
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
```

Without these, `SharedArrayBuffer` is disabled by the browser and scsynth will refuse to start. All the server configs above include them.
