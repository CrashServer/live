# Adding an FX to FoxDot (CrashServer)

## Overview

FX are SuperCollider SynthDefs that sit on an audio bus between a player's output
and the master output. FoxDot instantiates them automatically when you set a named
parameter on a player (`p1.room=0.5`, `p1.myeff=0.8`).

---

## 1. Write the FX SynthDef

Create `FoxDot/FoxDot/osc/sceffects/myeff.scd`:

```supercollider
SynthDef(\fd_myeff, {
    |bus=0, myeff=0, myeff_depth=0.5|
    var sig = In.ar(bus, 2);
    var wet = /* your processing */;
    // XFade2: mix -1 = dry, +1 = wet
    ReplaceOut.ar(bus, XFade2.ar(sig, wet, myeff * 2 - 1));
}).add;
```

Rules:
- First arg must be `bus` — FoxDot assigns the player's audio bus
- The "amount" param has the **same name** as the SynthDef (minus `fd_`) → `myeff`
- Use `ReplaceOut` not `Out` — replaces the bus signal in-place
- Set to dry (`XFade2 mix = -1`) when amount is 0
- Any extra params are named `myeff_paramname` (prefixed)

---

## 2. Register in Python

Open `FoxDot/FoxDot/osc/sceffects/myeff.py`:

```python
from . import *

class myeff(dyn):
    """One-line description."""
    
    def __init__(self):
        dyn.__init__(self)
        self.myeff       = 0      # amount (0 = off, 1 = full wet)
        self.myeff_depth = 0.5    # secondary param
        self.func = "myeff"       # matches SynthDef name (minus fd_)
```

Export in `FoxDot/FoxDot/osc/sceffects/__init__.py`:

```python
from .myeff import myeff
```

---

## 3. Use it

```python
p1 >> pluck([0, 2, 4], myeff=0.6, myeff_depth=0.8)
# or modify live
p1.myeff = var([0, 0.6, 0, 1], [8, 4, 12, 4])   # breathing
```

---

## FX parameter naming patterns

```
myeff           → wet/dry amount (0–1)
myeff_mix       → alias for amount
myeff_freq      → frequency parameter
myeff_time      → time / delay parameter
myeff_rate      → LFO rate
myeff_depth     → modulation depth
myeff_damp      → damping / tone
myeff_feed      → feedback
```

---

## Common FX patterns to copy from

| Pattern | SynthDef to reference |
|---|---|
| Simple reverb | `room.scd` |
| Delay/echo | `echo.scd` |
| Distortion + wet/dry | `dist2.scd` |
| Filter sweep | `lpf.scd` |
| Modulation (chorus/flanger) | `vibrato.scd` |
| Custom breathing pattern | `dynfuzz.scd` (svdk custom) |

---

## Paths quick reference

```
SynthDef (.scd):   FoxDot/FoxDot/osc/sceffects/myeff.scd
Python class:      FoxDot/FoxDot/osc/sceffects/myeff.py
__init__ export:   FoxDot/FoxDot/osc/sceffects/__init__.py
122 existing FX:   docs/new-fx.md
```
