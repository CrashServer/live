# svdk - Raw Rolling Bass Synth

Inspired by Daft Punk "Rollin' & Scratchin'" - Juno-106 + Boss MT-2 Metal Zone character.
With stereo drift, harmonic control, and solid low-end body.

## Sound Design

- **Oscillators**: 3 detuned saws (Juno-style) + white/pink noise
- **Harmonics**: Controllable upper partials (2nd, 3rd, 5th)
- **Sub layer**: Deep sine (2 oct down) + sine sub + pulse sub + triangle (parallel bass path)
- **Filter**: Resonant lowpass with envelope and keyboard tracking
- **Distortion**: 4-stage Boss MT-2 style (soft sat → hard clip → fold → tanh)
- **EQ**: Double bass shelf boost, slight mid cut, upper presence
- **Stereo**: Drift with independent L/R LFOs, pitch drift, subtle delay widening

## Parameters

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| grit | 0-1 | 0.5 | Distortion amount (clean → MT-2 cranked) |
| noise | 0-1 | 0.3 | White/pink noise mix |
| cutoff | 100-8000 | 800 | Filter cutoff frequency |
| res | 0-1 | 0.5 | Filter resonance |
| track | 0-2 | 1 | Keyboard tracking on filter |
| fenv | 0-1 | 0.3 | Filter envelope depth |
| slide | 0-0.5 | 0.05 | Portamento/glide time |
| body | 0-1 | 0.5 | Low-end weight/thickness |
| drift | 0-1 | 0.3 | Stereo movement (0=static, 1=wide) |
| harm | 0-1 | 0.2 | Upper harmonics (2nd, 3rd, 5th) |

---

## Usage Examples by Genre

### Daft Punk - Homework Era

```python
# === DA FUNK style ===
# Single root note pumping with kick, filter opens slowly
# Original: G minor, 303 through distortion
s1 >> svdk([0], dur=0.5, sus=0.4, oct=3, grit=0.7, res=0.4,
           cutoff=linvar([400, 1200], 16), body=0.8, noise=0.1)

# === ROLLIN' & SCRATCHIN' ===
# Sustained note, filter sweep IS the melody
# Max noise, high resonance, heavy distortion
s1 >> svdk([0], dur=8, sus=8, oct=3, grit=0.9, noise=0.8, res=0.7,
           cutoff=linvar([150, 4000], 8), body=0.7, drift=0.5, fenv=0)

# === REVOLUTION 909 ===
# Pumping bassline, tight and punchy
s1 >> svdk([0,0,0,[-2,0]], dur=0.5, sus=0.3, oct=3, grit=0.5,
           cutoff=600, res=0.3, body=0.9, slide=0.02)

# === AROUND THE WORLD ===
# Disco-funk bassline, slides between notes, ghost notes
# E minor, Dorian scale feel
s1 >> svdk([0,0,3,0, 5,0,3,0], dur=0.25, sus=[0.2,0.1,0.2,0.1], oct=4,
           grit=0.4, cutoff=900, res=0.2, body=0.7, slide=0.08,
           amp=[0.8,0.4,0.8,0.3, 0.8,0.4,0.8,0.3])
```

### Gesaffelstein - Dark Industrial

```python
# === PURSUIT style ===
# Slow, heavy, menacing - around 100 BPM
# MS-20 character: powerful filter, envelope shaping
Clock.bpm = 100
s1 >> svdk([0], dur=2, sus=1.8, oct=3, grit=0.8, res=0.6,
           cutoff=var([300, 600, 400, 800], 4), body=1,
           drift=0.4, harm=0.3, fenv=0.5)

# === OPR style ===
# Grinding, relentless, distorted
s1 >> svdk([0,0,-2,0], dur=0.5, sus=0.4, oct=3, grit=1, noise=0.3,
           cutoff=500, res=0.5, body=0.9, harm=0.4)

# === ALEPH texture ===
# Sine-based pump with long attack/release
s1 >> svdk([0], dur=4, sus=4, oct=3, grit=0.6, noise=0.1, res=0.3,
           cutoff=linvar([200, 800], 8), body=1, drift=0.6,
           atk=0.2, harm=0.2)

# === OBSESSION style ===
# Pumping sine bass, sidechain feel
s1 >> svdk([0,0,0,0], dur=0.5, sus=0.3, oct=3, grit=0.5, noise=0,
           cutoff=400, res=0.2, body=1, harm=0.1,
           amp=var([1,0.6,0.8,0.5], 0.5))

# === VIOL ===
# Dark stabs with silence
s1 >> svdk([0,rest,rest,-2, rest,rest,0,rest], dur=0.5, sus=0.3, oct=3,
           grit=0.9, cutoff=700, res=0.6, body=0.8, harm=0.5)
```

### Justice - Cross Era (Electro Punk)

```python
# === STRESS style ===
# Choppy, aggressive, bit-crushed feel
# Layer + detune + heavy limiting
s1 >> svdk([0,0,3,0, 5,5,3,0], dur=0.25, sus=0.15, oct=4, grit=1,
           cutoff=1200, res=0.4, body=0.6, harm=0.6, noise=0.2)

# === WATERS OF NAZARETH style ===
# Grinding, relentless, pitched chaos
s1 >> svdk([0,0,0,2, 0,0,0,-3], dur=0.25, sus=0.2, oct=4, grit=1,
           cutoff=var([600, 1500], 2), res=0.5, body=0.7,
           harm=0.7, slide=0.03)

# === D.A.N.C.E. bass ===
# Funky but distorted, bouncy
s1 >> svdk([0,0,5,0, 3,0,5,7], dur=0.25, sus=0.2, oct=4, grit=0.7,
           cutoff=1000, res=0.3, body=0.8, slide=0.05)

# === PHANTOM pt II ===
# Screaming lead-bass hybrid
s1 >> svdk([0,3,5,7], dur=1, sus=0.8, oct=4, grit=0.8, res=0.7,
           cutoff=linvar([500, 2500], 4), body=0.5, harm=0.8,
           drift=0.5)
```

### Boys Noize / SebastiAn (Dirty Electro)

```python
# === OH! style (Boys Noize) ===
# Distorted stabs, rat pedal character
s1 >> svdk([0,rest,0,rest, 0,0,rest,0], dur=0.25, sus=0.15, oct=4,
           grit=1, cutoff=800, res=0.5, body=0.6, harm=0.5)

# === & DOWN style ===
# Heavy sidechain pump, grinding
s1 >> svdk([0], dur=0.5, sus=0.3, oct=3, grit=0.9, noise=0.2,
           cutoff=600, res=0.4, body=1, amp=var([1,0.3], 0.25))

# === SEBASTIAN - EMBODY ===
# Brickwalled, aggressive, layered
s1 >> svdk([0,0,2,0, -2,0,2,3], dur=0.25, sus=0.2, oct=4, grit=1,
           cutoff=1000, res=0.6, body=0.7, harm=0.6).unison(2)

# === ROSS ROSS ROSS ===
# Raw acid screech
s1 >> svdk([0,0,0,2, 0,3,0,-2], dur=0.25, sus=0.3, oct=4, grit=0.8,
           cutoff=linvar([400, 2000], 2), res=0.7, body=0.5,
           harm=0.4, slide=0.1)
```

### Electro Punk / Noise

```python
# === FULL NOISE MODE ===
# Filter is the instrument
s1 >> svdk([0], dur=8, sus=8, oct=3, grit=1, noise=1, res=0.8,
           cutoff=linvar([100, 6000], 8), body=0.6, drift=0.8,
           harm=0.3, track=0.5)

# === INDUSTRIAL STUTTER ===
s1 >> svdk([0,0,0,0, 0,0,0,0], dur=[0.25,0.125,0.125,0.25, 0.5,0.25,0.125,0.375],
           sus=0.1, oct=4, grit=1, cutoff=var([400,1200], 0.5),
           res=0.6, body=0.7, noise=0.4)

# === DAF / NITZER EBB style ===
# Minimal EBM, driving, hypnotic
Clock.bpm = 120
s1 >> svdk([0,0,0,0], dur=0.25, sus=0.2, oct=3, grit=0.7,
           cutoff=500, res=0.4, body=0.9, harm=0.2)
s2 >> svdk([0,rest,-2,rest], dur=0.5, sus=0.4, oct=4, grit=0.6,
           cutoff=800, res=0.3, body=0.5, harm=0.4)

# === CHAOTIC SCREECH ===
s1 >> svdk([0,2,-3,5, -2,7,0,4], dur=0.125, sus=0.1, oct=4, grit=1,
           cutoff=PRand([400,800,1500,3000]), res=0.7, body=0.5,
           harm=0.8, noise=0.5, slide=0.02)
```

### Minimal / Hypnotic

```python
# === SINGLE NOTE MEDITATION ===
# Philip Glass meets industrial
s1 >> svdk([0], dur=4, sus=4, oct=3, grit=0.4, noise=0.1, res=0.3,
           cutoff=linvar([300, 1500], 16), body=0.9, drift=0.7,
           harm=0.5)

# === SLOW BUILD ===
s1 >> svdk([0,-2], dur=2, sus=1.8, oct=3,
           grit=linvar([0.3, 1], 32),
           cutoff=linvar([300, 2000], 32),
           res=linvar([0.2, 0.7], 32),
           body=0.9, drift=0.5, harm=0.3)

# === PULSING DRONE ===
s1 >> svdk([0], dur=0.5, sus=0.4, oct=3, grit=0.6, res=0.5,
           cutoff=400, body=1, harm=0.4, drift=0.6,
           amp=var([0.8,0.5,0.7,0.4], 0.5))
```

---

## SuperCollider Code

```supercollider
SynthDef.new(\svdk, {
    |bus=0, amp=1, sus=1, pan=0, freq=0, fmod=0,
     atk=0.01, rel=0.1, blur=1, beat_dur=1,
     grit=0.5, noise=0.3, cutoff=800, res=0.5,
     track=1, fenv=0.3, slide=0.05, body=0.5,
     drift=0.3, harm=0.2|

    var osc, nz, sub, subSine, subDeep, env, fltEnv, sig, freqSlide, fltFreq;
    var filtered, rq, bassPath, midPath, harmonics;
    var panMod, driftL, driftR, sigL, sigR;

    sus = sus * blur;
    freq = In.kr(bus, 1);
    freq = freq + fmod;

    // === PORTAMENTO ===
    freqSlide = Lag.kr(freq, slide);

    // === OSCILLATOR STACK ===
    osc = LFSaw.ar(freqSlide, 0, 0.5);
    osc = osc + LFSaw.ar(freqSlide * 1.006, 0.33, 0.4);
    osc = osc + LFSaw.ar(freqSlide * 0.998, 0.66, 0.3);

    // === HARMONICS LAYER ===
    harmonics = SinOsc.ar(freqSlide * 2, 0, 0.2 * harm);
    harmonics = harmonics + SinOsc.ar(freqSlide * 3, 0, 0.12 * harm);
    harmonics = harmonics + SinOsc.ar(freqSlide * 5, 0, 0.08 * harm);
    harmonics = harmonics + Pulse.ar(freqSlide * 2, 0.3, 0.1 * harm);

    // === SUB OSCILLATORS ===
    subDeep = SinOsc.ar(freqSlide * 0.25, 0, 0.4 * body);
    subSine = SinOsc.ar(freqSlide * 0.5, 0, 0.7 * body);
    sub = Pulse.ar(freqSlide * 0.5, 0.5, 0.4 * body);
    sub = sub + LFTri.ar(freqSlide, 0, 0.3 * body);

    // === NOISE ===
    nz = WhiteNoise.ar * noise * 0.5;
    nz = nz + (PinkNoise.ar * noise * 0.3);

    midPath = osc + harmonics + nz;

    // === FILTER ===
    fltEnv = EnvGen.kr(Env.perc(0.001, sus * 0.4, 1, -6), levelScale: fenv);
    fltFreq = cutoff + (freq * track * 0.25) + (fltEnv * cutoff * 2);
    fltFreq = fltFreq.clip(60, 6000);
    rq = (1 - res).linexp(0, 1, 0.05, 1);
    filtered = RLPF.ar(midPath, fltFreq, rq);
    filtered = filtered + (BPF.ar(midPath, fltFreq, 0.1) * res * 0.4);

    // === BASS PATH ===
    bassPath = subDeep + subSine + sub;
    bassPath = LPF.ar(bassPath, 300);
    bassPath = (bassPath * (1 + (grit * 0.6))).tanh;

    sig = filtered + bassPath;

    // === DISTORTION ===
    sig = sig * (1 + (grit * 3));
    sig = (sig * 1.5).tanh;
    sig = (sig * (1 + (grit * 2))).clip(-0.75, 0.75);
    sig = sig + ((sig * grit * 2).fold(-0.5, 0.5) * grit * 0.4);
    sig = (sig * (1 + grit)).tanh;

    // === EQ ===
    sig = BLowShelf.ar(sig, 80, 1, body * 5);
    sig = BLowShelf.ar(sig, 150, 1, body * 3);
    sig = BPeakEQ.ar(sig, 500, 1.5, grit * -3);
    sig = BPeakEQ.ar(sig, 2000, 0.8, grit * 3);
    sig = BHiShelf.ar(sig, 3500, 1, grit * res * 3);

    sig = HPF.ar(sig, 25);
    sig = LPF.ar(sig, 16000);
    sig = LeakDC.ar(sig);

    // === ENVELOPE ===
    env = EnvGen.ar(Env.linen(atk, sus, rel, 1, -2), doneAction: 2);
    sig = sig * env * amp * 0.35;

    // === STEREO DRIFT ===
    driftL = LFNoise2.kr(0.3 + (drift * 0.2)) * drift * 0.4;
    driftR = LFNoise2.kr(0.25 + (drift * 0.15)) * drift * 0.4;
    sigL = sig * (1 + (LFNoise2.kr(0.1) * drift * 0.003));
    sigR = sig * (1 + (LFNoise2.kr(0.12) * drift * 0.003));
    sigL = sigL * (1 - (pan + driftL).clip(-1, 1)).sqrt;
    sigR = sigR * (1 + (pan + driftR).clip(-1, 1)).sqrt;
    sigR = DelayC.ar(sigR, 0.02, drift * 0.008);

    ReplaceOut.ar(bus, [sigL, sigR]);
}).add;
```

---

## Research Sources

- [Attack Magazine - Daft Punk Basslines Guide](https://www.attackmagazine.com/technique/passing-notes/daft-punk-basslines-the-ultimate-guide/)
- [Reverb Machine - Homework Synth Sounds](https://reverbmachine.com/blog/daft-punk-homework-synth-sounds/)
- [Gearnews - How to Sound Like Gesaffelstein](https://www.gearnews.com/gesaffelstein/)
- [Gearnews - How to Sound Like Justice](https://www.gearnews.com/bear-the-cross-how-to-sound-like-justice/)
- [Gearspace - Boys Noize Bass](https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/167656-boys-noize-bass.html)
- [Matrixsynth - Juno 106 + Boss MT-2](https://www.matrixsynth.com/2009/01/juno-106-boss-mt-2-daft-punk-rollin.html)
- [Vintage Synth Forum](https://forum.vintagesynth.com/viewtopic.php?t=42612&start=15)

---

## Key Production Techniques

### Daft Punk (Homework)
- TB-303 through distortion pedal
- Juno-106 with noise maxed, high resonance
- Filter cutoff sweep as melody
- Sparse basslines, rhythmic interplay

### Gesaffelstein
- MS-20, MiniBrute monosynths
- ~100 BPM, dark and minimal
- Slow pumping bass with long attack/release
- Heavy but controlled distortion

### Justice
- "Juno-106 + distortion pedal"
- Choppy sample manipulation
- Heavy limiting and compression
- Bit-crushing, multiple distortion layers
- Treat synths like guitars

### Boys Noize / Ed Banger
- Rat distortion, Boss Turbo Distortion
- Layer and detune (3-4 layers)
- Heavy sidechain compression
- 303 through OTO pedals

---
CrashServer 2026
