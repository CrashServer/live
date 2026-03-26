# New FX Reference

## Sub Enhance (subenh)

Generates a sub-harmonic one octave below the low end. Adds weight to any sound.

| Param | Default | Description |
|-------|---------|-------------|
| subenh | 0 | Mix 0-1 |
| subhfreq | 100 | Crossover frequency — only content below this gets sub-octaved |
| subhgain | 1 | Sub level multiplier |

```
b1 >> dbass(dur=1, subenh=0.8)
b1 >> dbass(dur=1, subenh=0.6, subhfreq=80)
b1 >> dbass(dur=1, subenh=1, subhgain=1.5)
b1 >> pluck(dur=0.5, subenh=0.4, subhfreq=150)
```

---

## Spring Reverb (spring)

Physical spring tank character — dub, surf, lo-fi. Metallic "boing" quality none of the other reverbs have.

| Param | Default | Description |
|-------|---------|-------------|
| spring | 0 | Mix 0-1 |
| sprdecay | 1.5 | Decay time — how long the spring rings |
| sprdamp | 0.5 | High-frequency damping 0-1 |
| sprtens | 0.5 | Tension/brightness 0-1 — higher = brighter, more metallic |

```
p1 >> pluck(dur=0.5, spring=0.4)
p1 >> pluck(dur=0.5, spring=0.7, sprdecay=2.5)
p1 >> pluck(dur=0.5, spring=0.5, sprtens=0.8)
p1 >> pluck(dur=0.5, spring=0.6, sprdamp=0.9)
d1 >> play("X o x o", spring=0.3, sprdecay=0.8, sprtens=0.7)
s1 >> swell(dur=4, spring=linvar([0, 0.8], 32), sprdecay=2)
```

---

## Spectral Blur (sblur)

FFT-based frequency smearing. Turns anything into an evolving, washy texture. Like freeze but continuous and moving.

| Param | Default | Description |
|-------|---------|-------------|
| sblur | 0 | Mix 0-1 |
| sbluramt | 4 | Blur amount — how many bins to smear across. Higher = more wash |

```
s1 >> swell(dur=4, sblur=0.6)
s1 >> swell(dur=4, sblur=0.8, sbluramt=12)
s1 >> swell(dur=4, sblur=linvar([0, 1], 32))
p1 >> pads(dur=8, sblur=0.5, sbluramt=var([2, 8, 20], [16, 8, 8]))
b1 >> dbass(dur=1, sblur=0.3, sbluramt=3)
```

---

## Granular Delay (gdel)

Delay line where the echoes are granulated — each repeat fragments and scatters into texture.

| Param | Default | Description |
|-------|---------|-------------|
| gdel | 0 | Mix 0-1 |
| gdeltime | 0.5 | Delay time in beats |
| gdelsize | 0.1 | Grain size in seconds — smaller = more granular |
| gdelsprd | 0.5 | Pitch spread of grains — higher = more scattered |
| gdelfb | 0.3 | Feedback 0-1 — higher = more repeats, self-feeding |

```
p1 >> pluck(dur=1, gdel=0.5, gdeltime=0.75)
p1 >> pluck(gdel=0.6, gdelsize=0.2, gdelsprd=0.8)
p1 >> pluck(gdel=0.4, gdelfb=0.7)
s1 >> swell(dur=4, gdel=0.5, gdeltime=1, gdelsize=0.05, gdelsprd=1)
p1 >> pluck(gdel=0.6, gdeltime=var([0.25, 0.5, 1], 8), gdelfb=0.5)
d1 >> play("X..o..x.", gdel=0.3, gdeltime=0.5, gdelsize=0.08, gdelfb=0.4)
```

---

## Multiband Compressor (mbcomp)

3-band split compression. Tighten the low end without squashing highs, or glue a mix together.

| Param | Default | Description |
|-------|---------|-------------|
| mbcomp | 0 | Mix 0-1 |
| mbcxlo | 200 | Low/mid crossover frequency |
| mbcxhi | 3000 | Mid/high crossover frequency |
| mbcrat | 3 | Compression ratio — higher = more squash |
| mbcatk | 0.01 | Attack time in seconds |
| mbcrel | 0.1 | Release time in seconds |

```
d1 >> play("X o x o", mbcomp=0.8)
b1 >> dbass(dur=1, mbcomp=0.6, mbcrat=5)
s1 >> swell(mbcomp=0.5, mbcxhi=2000, mbcrel=0.3)
d1 >> play("X.o.x.o.", mbcomp=0.7, mbcxlo=120, mbcxhi=4000, mbcrat=4)
b1 >> dbass(dur=1, mbcomp=0.8, mbcxlo=80, mbcrat=6, mbcatk=0.005, mbcrel=0.05)
```

---

## Vocoder (vocod)

8-band analysis/resynthesis. Analyzes the input's spectral shape and applies it to a carrier signal — robotic, synthetic textures.

| Param | Default | Description |
|-------|---------|-------------|
| vocod | 0 | Mix 0-1 |
| voccarr | 0.5 | Carrier blend — 0=noise (breathy), 1=pulse (tonal/robotic) |
| vocbw | 0.3 | Band filter width — lower = sharper, more resonant |

```
s1 >> saw(dur=1, vocod=0.8)
s1 >> saw(dur=1, vocod=1, voccarr=1)
s1 >> saw(dur=1, vocod=0.7, voccarr=0, vocbw=0.1)
s1 >> saw(dur=1, vocod=0.8, voccarr=linvar([0, 1], 16))
p1 >> pluck(dur=0.5, vocod=0.6, voccarr=0.8, vocbw=0.2)
d1 >> play("X o x o", vocod=0.5, voccarr=0.3)
```

---

## Spectral Gate (sgate)

FFT threshold — keeps only the loudest (or quietest) frequency bins. Strips a sound to its skeleton or extracts hidden detail.

| Param | Default | Description |
|-------|---------|-------------|
| sgate | 0 | Mix 0-1 |
| sgthresh | 1 | Magnitude threshold — higher = fewer bins pass |
| sgmode | 0 | 0=keep loud bins (gate), 1=keep quiet bins (duck) |

```
s1 >> swell(dur=4, sgate=0.8, sgthresh=2)
s1 >> swell(dur=4, sgate=0.6, sgthresh=0.5, sgmode=1)
s1 >> swell(sgate=1, sgthresh=linvar([0.5, 5], 16))
p1 >> pluck(dur=0.5, sgate=0.7, sgthresh=3)
d1 >> play("X o x o", sgate=0.5, sgthresh=1.5, sgmode=0)
s1 >> swell(dur=4, sgate=0.8, sgthresh=var([1, 4, 0.5], [8, 4, 4]))
```

---

## Spectral Warp (spwarp)

Non-linear FFT bin shifting. Stretches or compresses the harmonic series — turns piano into bell, voice into alien.

| Param | Default | Description |
|-------|---------|-------------|
| spwarp | 0 | Mix 0-1 |
| spwstr | 1.5 | Stretch factor — 1=neutral, >1=spread harmonics apart, <1=compress |
| spwshift | 0 | Bin shift — moves all frequencies up (positive) or down (negative) |

```
s1 >> pluck(dur=0.5, spwarp=0.7, spwstr=2)
s1 >> pluck(dur=0.5, spwarp=0.5, spwstr=0.5)
s1 >> pluck(spwarp=0.8, spwstr=1, spwshift=4)
s1 >> pluck(spwarp=1, spwstr=linvar([0.5, 3], 32))
s1 >> saw(dur=1, spwarp=0.6, spwstr=var([1, 1.5, 2, 0.7], 8))
p1 >> pads(dur=4, spwarp=0.4, spwstr=1.2, spwshift=sinvar([0, 8], 16))
```

---

## Resonant Comb Sweep (csweep)

A comb filter with LFO-swept delay time. Karplus-Strong metallic resonance that moves — different from flanger (which is subtle), this rings.

| Param | Default | Description |
|-------|---------|-------------|
| csweep | 0 | Mix 0-1 |
| cswfreq | 200 | Base resonant frequency in Hz |
| cswdepth | 0.3 | Sweep depth 0-1 — how far the LFO moves the pitch |
| cswrate | 0.5 | LFO rate in Hz |
| cswdecay | 0.5 | Resonance decay time — higher = longer ring |

```
d1 >> play("X o x o", csweep=0.4, cswfreq=300)
s1 >> swell(csweep=0.5, cswfreq=150, cswrate=0.2, cswdecay=1)
s1 >> swell(csweep=0.6, cswfreq=linvar([100, 800], 16))
p1 >> pluck(dur=0.5, csweep=0.3, cswfreq=400, cswdepth=0.5, cswrate=2)
s1 >> saw(dur=1, csweep=0.5, cswfreq=var([150, 300, 600], 8), cswdecay=0.8)
d1 >> play("X..x..X.x.", csweep=0.4, cswfreq=500, cswrate=0.1, cswdecay=1.5)
```

---

## Doppler (doppler)

Simulates a sound source passing by. Combines pitch shift (via delay modulation), amplitude change, filter darkening, and stereo panning — all synced to circular motion.

| Param | Default | Description |
|-------|---------|-------------|
| doppler | 0 | Mix 0-1 |
| dopspd | 0.5 | Speed of the pass-by in Hz |
| dopdist | 1.0 | Distance — higher = more extreme pitch/volume/filter changes |

```
s1 >> pluck(dur=2, doppler=0.7, dopspd=0.3)
s1 >> pluck(dur=1, doppler=1, dopspd=2, dopdist=2)
p1 >> pads(dur=4, doppler=0.5, dopspd=sinvar([0.1, 1], 32))
s1 >> saw(dur=1, doppler=0.6, dopspd=0.5, dopdist=1.5)
d1 >> play("X o x o", doppler=0.4, dopspd=0.25, dopdist=0.8)
s1 >> swell(dur=8, doppler=0.8, dopspd=linvar([0.1, 3], 64), dopdist=2)
```

---

## Vowel Formant (vowel)

3-formant resonant filter that morphs between 5 vowels. Makes any sound "speak". Different from the existing `formant` effect (which is a single Formlet).

| Param | Default | Description |
|-------|---------|-------------|
| vowel | 0 | Mix 0-1 |
| vowelf | 0 | Vowel position — 0=a, 1=e, 2=i, 3=o, 4=u (sweeps continuously between them) |
| vowelq | 1 | Resonance sharpness — higher = more pronounced vowel character |

```
s1 >> saw(dur=1, vowel=0.8, vowelf=0)
s1 >> saw(dur=1, vowel=0.8, vowelf=2)
s1 >> saw(dur=1, vowel=1, vowelf=linvar([0, 4], 16))
s1 >> saw(dur=1, vowel=0.7, vowelf=[0, 2, 4], vowelq=3)
b1 >> dbass(dur=1, vowel=0.6, vowelf=sinvar([0, 4], 8), vowelq=2)
p1 >> pluck(dur=0.5, vowel=0.8, vowelf=var([0, 1, 2, 3, 4], 4), vowelq=1.5)
s1 >> saw(dur=1, vowel=0.7, vowelf=PLife(0.5, 0, 4), vowelq=2)
```
