# Stem recording for adaptive game audio

Video-game audio system: live-coded FoxDot players captured as
independent .wav stems for vertical-remix layering in a game engine.

## Architecture

```
FoxDot players (live coding in webTroop)
   │  p1.output = 16        ┐
   │  b1.output = 18        │
   │  k1.output = 20        ├──► SC private busses
   │  ...                   ┘
   │
SC side: per-bus synth pair
   ├─ \stemTap     (bus → master 0/1, so user still hears)
   └─ \stemDiskOut (bus → DiskOut.ar → file)
   │
   ▼
./stems/{session}__{player}__{variation}.wav
   (one file per player, all same wallclock length)
```

## Usage

```python
# Live-code your scene as normal
p1 >> pianovel([0, 2, 5, 7], dur=1, oct=5, amp=0.6)
b1 >> dbass([0, 0, -2, 0], dur=2, oct=4, sus=1.5, amp=0.8)
k1 >> compkick(0, dur=1, oct=3, amp=1.0)
s1 >> play("..o.", dur=1/2, sample=3, amp=0.7)
h1 >> click(0, dur=1/4, amp=Pacc(6, 4), rate=18, hpf=5200)

# Record all five as separate stems, 16 bars long
compo.rec_stems(bars=16, session="forest", variation="calm")
# Files: ./stems/forest__p1__calm.wav  (and b1, k1, s1, h1 too)

# Wait for the recording to finish (auto-stops after 16 bars).
# Then mutate intensity and record a new variation:
p1 >> pianovel([0, 2, 5, 7, 9, 12], dur=1/2, oct=5, amp=0.8)
b1 >> dbass([0, 0, -2, 0, -3, 0], dur=1, oct=4, sus=0.5, amp=1.0, dist2=0.6)
k1 >> compkick(0, dur=1/2, oct=3, amp=1.2, click=0.8)
# ... etc

compo.rec_stems(bars=16, session="forest", variation="combat")
# Files: ./stems/forest__p1__combat.wav (etc.)
```

Game side loads `calm.wav` and `combat.wav` for each layer and
crossfades between them based on game state.

## API

```python
compo.rec_stems(
    bars=16,                # loop length in bars (4 beats/bar)
    session="scene",        # scene/track identifier
    variation="v1",         # intensity/state tag
    players=None,           # None=autodiscover; or list of names/refs
    output_dir=None,        # default './stems/'
    tail_bars=0,            # extra bars past loop for tail-fold (V2)
)

compo.stem_stop()           # force-stop active session
```

`players` accepts:
- `None` → autodiscover all 2-char player names in globals (`p1, b1, k1, ...`)
- `['p1', 'b1', 'k1']` → explicit names (looked up in globals)
- `[p1, b1, k1]` → explicit references

## Timing

`rec_stems()` defers actual start to the **next bar boundary** so
all stems begin at musical beat 1. After `(bars + tail_bars) * 4`
beats, it auto-stops and restores each player's `output` attribute.

All files end up exactly the same wallclock length regardless of
internal cycle lengths (e.g. `PDur(5, 8)` won't repeat cleanly in
16 bars but the file is still 16 bars long — just with a
non-aligned cycle within it).

## Loop-seamless authoring

For stems that loop cleanly when the game engine repeats them:

1. **Short tails** — keep `cvdecay < 2`, avoid `fbdelay` with `fbfeed > 0.5`.
   Avoid `jpverb`/`mverb` (already on the no-list anyway).
2. **Divisor cycles** — pattern length should divide loop length.
   8-step pattern at `dur=1` = 8 beats → divides 16 bars (64 beats) ✓.
   `PDur(5, 8)` cycle = 40 beats → does NOT divide 64 beats ✗.
3. **Tail-fold** (V2, when `tail_bars > 0`) — record `bars + tail_bars`,
   then fold the overflow back onto bars 0..tail_bars. Not yet wired.

## Variations workflow

Record multiple "intensity layers" of the same scene by re-evaluating
players between takes:

```python
# Take 1: calm
compo.rec_stems(bars=16, session="forest", variation="calm")
# (wait for it to finish...)

# Take 2: tense — add a counter-melody and detune
m1 >> faim(P[0, 2, 5, 7, 5, 2], dur=1/2, oct=6, amp=0.4, dist2=0.3)
b1 >> dbass([0, 0, -2, 0, -3, -5], dur=1, oct=4, sus=0.7, amp=0.9, dist2=0.4)
compo.rec_stems(bars=16, session="forest", variation="tense")

# Take 3: combat — full mix, drums double-time
k1 >> compkick(0, dur=1/2, oct=3, amp=1.3, click=0.9, comp=18, tape=0.7, tapedrive=2)
h1 >> play("-(--)-(--)-(--)-([--])", dur=1/4, sample=PStep(16, 1, 3), amp=PWhite(0.3, 0.55))
compo.rec_stems(bars=16, session="forest", variation="combat")
```

Each take produces the same set of `.wav` filenames with the variation
tag swapped — game-side trivially crossfades matching pairs.

## Game-engine integration

### Unity / Unreal / Godot pattern

```
// Per scene: load all stems for all variations
AudioSource layerCalm_p1   = Load("forest__p1__calm.wav");
AudioSource layerCombat_p1 = Load("forest__p1__combat.wav");
// ... and for b1, k1, s1, h1

// All play simultaneously from sample 0, looped
// Volume controlled per-layer:
layerCalm_p1.volume   = 1.0 - intensity;
layerCombat_p1.volume = intensity;        // crossfade based on game state
```

### FMOD / Wwise pattern

- Each `playername` becomes an event with multiple states
- State drives layer volumes via game parameters
- Music transitions happen at bar boundaries (FMOD's `MUSICALBAR`
  parameter, or Wwise's "wait until next bar" sync point)

## Limitations (V1)

- **No tail-fold yet** — `tail_bars` param accepts a value but post-
  process to fold the tail back into the loop start isn't wired.
  Workaround: record with short tails (see §Loop-seamless authoring).
- **Synth-internal randomness** — `PRand`, `PWhite`, `LFNoise.*`
  give different results per take. For deterministic stems, seed
  the RNG before recording or accept variance as a feature
  (round-robin stem variants).
- **Master FX baked in** — if `Server.addFx(...)` is active, those
  effects DON'T get printed onto each stem (they live on the master
  bus, downstream of `\stemTap`). Only the player's own inline FX
  (`tubedrive`, `fbdelay`, `dist2`, `tape`, etc.) are captured.
- **No re-route during recording** — if you re-evaluate a player
  during an active stem session (e.g. `p1 >> pianovel(...)`), the
  new `output` attribute may revert to default unless you ensure
  the call carries `output=` explicitly. Cleanest: complete the
  16-bar window, then mutate.

## Implementation files

- `/home/svdk/live/FoxDot.sc` — SC-side `\stemDiskOut`+`\stemTap`
  SynthDefs and `/foxdot_stems_start`/`/foxdot_stems_stop` OSC handlers
- `/home/svdk/live/FoxDot/FoxDot/lib/Crashserver/startup_live.py` —
  Python-side `Compo.rec_stems()` method (lines around 2066 onwards)
- `/home/svdk/live/codeBank/stems_demo.py` — minimal worked example
