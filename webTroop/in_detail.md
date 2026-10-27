# WebTroop Visual Mode - Technical Documentation

## Overview

Visual Mode transforms WebTroop into a reactive coding interface that visualizes FoxDot patterns in real-time. It highlights currently playing values in the code editor and provides specialized visualizations for dynamic pattern generators.

---

## Features

### 1. Pattern Highlighting

Highlights the currently playing value in static patterns directly in the code editor.

**Static patterns** (arrays, strings):
```python
d1 >> bass([0, 2, 4, 7], dur=1/4)
           ↑
        highlighted in yellow as it plays
```

- **Degree patterns**: Yellow highlight with glow
- **Other parameters** (dur, amp, pan): Cyan highlight

### 2. Generator Visualizations

Dynamic patterns like `PWhite`, `linvar`, `var` get inline widget visualizations below the code line.

**Supported generators:**

| Generator | Visualization |
|-----------|---------------|
| `PWhite(lo, hi)` | Range bar with marker showing current value position |
| `PRand(lo, hi)` | Range bar with marker |
| `PRand([values])` | List with current pick highlighted |
| `PWalk(max, step)` | Range bar showing walk position |
| `PwRand(vals, weights)` | Weighted options with opacity based on weight |
| `linvar([vals], times)` | Progress bar with gradient fill |
| `var([vals], times)` | Segmented timeline with active segment highlighted |
| `Pvar` | Progress indicator |

**Example visualization:**
```
d1 >> bass(PWhite(0, 7), amp=linvar([0, 1], 16))
┌─────────────────────────────────────────────────────┐
│ deg  PWhite  [0|░░░░●░░░░|7]  5                     │
│ amp  linvar  [0 ▓▓▓▓▓▓░░░░░ 1]  0.52               │
└─────────────────────────────────────────────────────┘
```

### 3. Mini Piano Roll

Bottom-right floating panel showing pattern shapes and current position for all active players.

```
┌─────────────────────────────────┐
│ d1  ▁ ▃ ▅ █ ▁ ▃ ▅ █   7        │
│      ↑ active                   │
│ b1  █ ▃ ▁ ▅ █ ▃ ▁ ▅   2        │
└─────────────────────────────────┘
```

---

## Architecture

### Data Flow

```
FoxDot (Python)
    │
    ├── sendBeat() ──────────────────┐
    │   - beat position               │
    │   - playerSteps {id: step}      │  every 0.1s
    │                                 │
    ├── sendPlayer() ────────────────┤
    │   - player info                 │  every 1.0s
    │   - current values              │
    │   - patterns (static)           │
    │   - generators (metadata)       │
    │                                 ▼
    └──────────────────────────> WebSocket (port 20000)
                                      │
                                      ▼
                               crashpanel.js
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
                    ▼                 ▼                 ▼
             visualMode          visualMode        visualMode
             .setBeat()         .setPlayers()    .setPlayerSteps()
                    │                 │                 │
                    └─────────────────┼─────────────────┘
                                      │
                                      ▼
                              scheduleUpdate()
                                      │
                                      ▼
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
                    ▼                 ▼                 ▼
           highlightNotes()   renderWidgets()    updateRolls()
```

### Server-Side (FoxDot)

#### File: `FoxDot/lib/Crashserver/crash_generator/startup_live.py`

**sendBeat()** (lines 602-621)
- Sends beat position every 0.1 seconds
- Includes real-time step count for each player
- Enables smooth, accurate highlighting

```python
def sendBeat(self):
    while self.isrunning:
        playerSteps = {}
        for player in Clock.playing:
            playerSteps[player.name] = getattr(player, 'event_n', 0)
        msg = json.dumps({
            "type": "beat",
            "beat": Clock.beat,
            "playerSteps": playerSteps
        })
        asyncio.run(wsServer.sendWebsocket(msg))
        sleep(self.beatTime)  # 0.1s
```

**getGeneratorMeta()** (lines 623-714)
- Detects pattern type using `isinstance()`
- Extracts metadata specific to each generator type
- Returns JSON-serializable dictionary

```python
def getGeneratorMeta(self, pat):
    from FoxDot.lib.Patterns.Generators import GeneratorPattern, PWhite, PRand, ...
    from FoxDot.lib.TimeVar import TimeVar, linvar, Pvar

    if isinstance(pat, PWhite):
        return {
            "type": "PWhite",
            "lo": float(pat.low),
            "hi": float(pat.high),
            "current": float(pat.last_value)
        }
    elif isinstance(pat, linvar):
        return {
            "type": "linvar",
            "values": [...],
            "durs": [...],
            "progress": float(pat.proportion),
            "current": float(pat.now())
        }
    # ... etc
```

**sendPlayer()** (lines 716-786)
- Sends comprehensive player data every 1 second
- Includes patterns, generators, and current values

```python
playerListCount.append(json.dumps({
    "player": player,
    "name": name,
    "duration": duration,
    "solo": player in soloPlayers,
    "step": step,
    "current": current_values,
    "patterns": patterns,      # Static pattern arrays
    "generators": generators   # Generator metadata
}))
```

### Client-Side (WebTroop)

#### File: `src/js/visualMode.js`

**Class: VisualMode**

Properties:
- `enabled` - Visual mode on/off
- `editor` - CodeMirror instance
- `players` - Player data from server
- `playerSteps` - Real-time steps from beat messages
- `markers` - CodeMirror text markers for highlights
- `widgets` - CodeMirror line widgets for generators
- `updateInterval` - Throttle rate (80ms)

Key Methods:

| Method | Purpose |
|--------|---------|
| `setPlayerSteps()` | Receives real-time step data, triggers update |
| `setPlayers()` | Receives full player data with generators |
| `highlightCurrentNotes()` | Creates text markers for static patterns |
| `renderGeneratorWidgets()` | Creates line widgets for generators |
| `updatePianoRolls()` | Updates mini piano roll display |

**Step Timing Fix:**
```javascript
// FoxDot increments event_n after note starts
// So we subtract 1 to show currently PLAYING note
const step = rawStep > 0 ? rawStep - 1 : 0;
const currentIndex = step % patternLength;
```

**Generator Widget Rendering:**
```javascript
renderGenerator(gen, attr) {
    switch (gen.type) {
        case 'PWhite':
        case 'PRand':
        case 'PWalk':
            return this.renderRangeGenerator(gen, label);
        case 'linvar':
            return this.renderLinvarGenerator(gen, label);
        case 'var':
            return this.renderVarGenerator(gen, label);
        case 'PwRand':
            return this.renderWeightedGenerator(gen, label);
        default:
            return this.renderGenericGenerator(gen, label);
    }
}
```

#### File: `src/js/crashpanel.js`

Receives WebSocket messages and forwards to visualMode:

```javascript
case 'beat':
    updateBeat(data.beat);
    visualMode.setBeat(data.beat);
    if (data.playerSteps) {
        visualMode.setPlayerSteps(data.playerSteps);
    }
    break;

case 'players':
    formatPlayers(data.players);
    const playerData = data.players.map(ply => JSON.parse(ply));
    visualMode.setPlayers(playerData);
    break;
```

#### File: `src/css/visualMode.css`

**Pattern Highlights:**
```css
.playing-note {
    background: rgba(255, 255, 0, 0.5) !important;
    box-shadow: 0 0 8px rgba(255, 255, 0, 0.6);
}

.playing-param {
    background: rgba(0, 200, 255, 0.35) !important;
    box-shadow: 0 0 6px rgba(0, 200, 255, 0.5);
}
```

**Generator Widgets:**
```css
.gen-widget-line {
    display: flex;
    padding: 4px 8px 4px 40px;
    background: rgba(30, 30, 40, 0.6);
    border-left: 2px solid rgba(255, 255, 0, 0.3);
}

.gen-track {
    position: relative;
    width: 60px;
    height: 6px;
    background: rgba(80, 80, 100, 0.6);
}

.gen-marker {
    position: absolute;
    width: 8px;
    height: 8px;
    background: rgba(255, 255, 0, 0.9);
    border-radius: 50%;
    box-shadow: 0 0 6px rgba(255, 255, 0, 0.8);
}
```

---

## Message Formats

### Beat Message (every 0.1s)
```json
{
    "type": "beat",
    "beat": 42.5,
    "playerSteps": {
        "d1": 170,
        "b1": 85
    }
}
```

### Player Message (every 1.0s)
```json
{
    "type": "players",
    "players": [
        {
            "player": "d1",
            "name": "bass",
            "duration": "02:34",
            "solo": false,
            "step": 170,
            "current": {
                "degree": 5,
                "dur": 0.25,
                "amp": 0.8
            },
            "patterns": {
                "dur": [0.25, 0.5, 0.25, 0.25]
            },
            "generators": {
                "degree": {
                    "type": "PWhite",
                    "lo": 0,
                    "hi": 7,
                    "current": 5
                },
                "amp": {
                    "type": "linvar",
                    "values": [0, 1],
                    "durs": [16],
                    "progress": 0.52,
                    "current": 0.52
                }
            }
        }
    ]
}
```

---

## Generator Metadata Reference

### PWhite
```json
{
    "type": "PWhite",
    "lo": 0,
    "hi": 7,
    "current": 4.23
}
```

### PRand (range)
```json
{
    "type": "PRand",
    "lo": 0,
    "hi": 7,
    "current": 3
}
```

### PRand (list)
```json
{
    "type": "PRand",
    "values": [0, 2, 4, 7],
    "current": 4
}
```

### PwRand
```json
{
    "type": "PwRand",
    "values": [0, 2, 4, 7],
    "weights": [1, 2, 1, 3],
    "current": 7
}
```

### PWalk
```json
{
    "type": "PWalk",
    "lo": -7,
    "hi": 7,
    "step": 1,
    "current": 3
}
```

### linvar
```json
{
    "type": "linvar",
    "values": [0, 7],
    "durs": [8],
    "progress": 0.625,
    "current": 4.375
}
```

### var
```json
{
    "type": "var",
    "values": [0, 4, 7],
    "durs": [4, 4, 8],
    "progress": 0.5,
    "index": 1,
    "current": 4
}
```

### Pvar
```json
{
    "type": "Pvar",
    "progress": 0.75,
    "current": "[0, 2, 4]"
}
```

---

## Usage

### Enabling Visual Mode

1. Open WebTroop settings panel
2. Toggle "Visual Mode (highlight notes)" ON

### Example Patterns

**Static pattern with highlighting:**
```python
d1 >> bass([0, 2, 4, 7], dur=[1, 1/2, 1/4])
```

**Random generator with range visualization:**
```python
d1 >> bass(PWhite(0, 7), dur=1/4)
```

**Time-varying with progress bar:**
```python
d1 >> bass(linvar([0, 7], 8), dur=1/4)
```

**Stepped changes with segment display:**
```python
d1 >> bass(var([0, 4, 7], [4, 4, 8]), dur=1/4)
```

**Weighted random with option display:**
```python
d1 >> bass(PwRand([0, 2, 4, 7], [1, 2, 1, 3]), dur=1/4)
```

---

## Performance Considerations

1. **Throttled updates**: Visual updates limited to ~12fps (80ms interval)
2. **Data-driven**: No continuous animation loop - updates only on new data
3. **Efficient markers**: CodeMirror markers cleared and recreated only when needed
4. **Widget reuse**: Line widgets cleared before recreation to prevent accumulation

---

## Files Modified

| File | Changes |
|------|---------|
| `FoxDot/.../startup_live.py` | Added `getGeneratorMeta()`, modified `sendBeat()` and `sendPlayer()` |
| `webTroop/src/js/visualMode.js` | Complete visual mode implementation |
| `webTroop/src/css/visualMode.css` | Styles for highlights, widgets, piano roll |
| `webTroop/src/js/crashpanel.js` | Forward beat/player data to visualMode |
| `webTroop/src/js/main.js` | Import and initialize visualMode |
| `webTroop/src/js/configPanel.js` | Toggle handler for visual mode |
| `webTroop/index.html` | Visual mode toggle checkbox |

---

## Future Enhancements

- [ ] History trail for random generators (show last N values)
- [ ] Click on generator widget to modify parameters
- [ ] Color themes for visualizations
- [ ] Nested pattern visualization (PGroups, chords)
- [ ] Player method visualization (stutter, every, sometimes)
- [ ] BPM-synced animations
- [ ] Export visualization as video/GIF
