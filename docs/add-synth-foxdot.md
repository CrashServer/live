# Adding a Synth to FoxDot (CrashServer)

## Overview

A synth lives in two places: an `.scd` SynthDef file compiled into SuperCollider, and a
Python entry in FoxDot's synth registry that maps parameters.

---

## 1. Write the SynthDef

Create `FoxDot/FoxDot/osc/scsyndef/mysynth.scd`:

```supercollider
SynthDef(\fd_mysynth, {
    |out=0, freq=440, amp=0.8, pan=0, sus=1, attack=0.01, release=0.1,
     cutoff=2000, rq=0.5|
    var env = EnvGen.ar(
        Env.linen(attack, (sus - attack - release).max(0.001), release, amp, \sin),
        doneAction: 2
    );
    var sig = Saw.ar(freq) * env;
    sig = RLPF.ar(sig, cutoff.clip(40, 20000), rq.clip(0.01, 1.0));
    Out.ar(out, Pan2.ar(sig, pan));
}).add;
```

Rules:
- Name must start with `fd_` → `fd_mysynth`
- Always include: `out, freq, amp, pan, sus, attack, release`
- `doneAction: 2` frees the synth node when envelope ends
- Use `freq` not `note` — FoxDot sends MIDI note numbers converted to Hz

---

## 2. Register in Python

Open `FoxDot/FoxDot/osc/scsyndef/mysynth.py` (or add to an existing file):

```python
from . import *

class mysynth(SynthDef):
    type = "pluck"   # bass / lead / pad / pluck / perc / noisy
    
    def __init__(self):
        SynthDef.__init__(self)
        self.cutoff  = 2000
        self.rq      = 0.5
        # any extra params you added to the SynthDef
```

Then register it in `FoxDot/FoxDot/osc/scsyndef/__init__.py` alongside other synths:

```python
from .mysynth import mysynth
```

---

## 3. Make it available at startup

In `FoxDot/FoxDot/lib/Custom/startup.py`, add to the synth list if you want it
pre-imported in the live coding namespace:

```python
mysynth = SynthDef("mysynth")
```

Or it's available automatically via `Player >> mysynth(...)` once registered.

---

## 4. Boot / reload

In SuperCollider IDE:
```supercollider
FoxDot.start;
// or if already running, just recompile:
SynthDescLib.read;
```

Then in FoxDot / webTroop:
```python
# Test it
p1 >> mysynth([0, 2, 4], oct=4, dur=1, cutoff=1200)
```

---

## Key conventions

| Convention | Detail |
|---|---|
| Player naming | `p1, p2` = pads · `b1` = bass · `m1` = lead · `k1` = kick |
| Default oct | pads/leads: 4–5 · bass: 3–4 |
| sus meaning | total duration in seconds passed to SC (attack + body + release) |
| Extra params | anything beyond the base set → add to `__init__` with default |

---

## Paths quick reference

```
SynthDef (.scd):     FoxDot/FoxDot/osc/scsyndef/mysynth.scd
Python class:        FoxDot/FoxDot/osc/scsyndef/mysynth.py
__init__ export:     FoxDot/FoxDot/osc/scsyndef/__init__.py
Custom startup:      FoxDot/FoxDot/lib/Custom/startup.py
CrashServer defs:    FoxDot/FoxDot/lib/Crashserver/crashSynthDefs.py
```

See also: `docs/cheatsheet_fonctions_crash.md` for the full synth list.
