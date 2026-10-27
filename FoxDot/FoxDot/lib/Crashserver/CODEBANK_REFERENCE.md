# FoxDot Complete Codebank Reference
## CrashServer 2026

---

## SCALES (47 available)

### Western Scales
- `major`, `minor`/`aeolian`, `melodicMinor`, `melodicMajor`, `harmonicMinor`, `harmonicMajor`
- `chromatic` - all 12 semitones

### Pentatonic
- `majorPentatonic`, `minorPentatonic`, `pentatonic` (Egyptian)

### Modes
- `dorian`, `dorian2`, `phrygian`, `lydian`, `lydianMinor`, `mixolydian`, `locrian`, `locrianMajor`

### Diminished/Whole Tone
- `diminished`, `halfWhole`, `wholeHalf`, `wholeTone`

### Bebop/Jazz
- `bebopMaj`, `bebopDorian`/`bebopMin`, `bebopDom`, `bebopMelMin`
- `minMaj`, `susb9`, `lydianAug`, `lydianDom`, `melMin5th`, `halfDim`, `altered`

### Exotic/World
- `blues`, `yu`, `zhi`, `chinese`, `indian`, `prometheus`, `hungarianMinor`, `romanianMinor`

### Just Intonation
- `justMajor`, `justMinor`

### Usage
```python
Scale.default.set("minor")
p1 >> pads([0,2,4], scale=Scale.dorian)
p1 >> pads([0,1,2,3,4], scale=Scale.major.pentatonic)
```

---

## PATTERN GENERATORS

### Random
- `PRand([0,1,2])` - random choice from list
- `PRand(0, 10)` - random int 0-10
- `PWhite(0, 1)` - random float 0-1
- `PxRand([0,1,2])` - no consecutive repeats
- `PwRand([0,2,4], [1,2,3])` - weighted random
- `PChain({0:[0,1], 1:[1,2]})` - Markov chain

### Deterministic
- `PDelta([1,2,-1])` - cumulative sum
- `PSquare()` - index squared
- `PIndex()` - returns index
- `PFibMod()` - Fibonacci sequence

### Walk
- `PWalk(7, 1, 0)` - random walk bounded -7 to +7

### Tree
- `PTree(0, lambda x: (x+1, x-1))` - binary tree walk

---

## TIME VARIABLES

### var - stepped changes
```python
var([0, 4, 2], 4)  # change every 4 beats
var([10, 20], [2, 4])  # 10 for 2 beats, 20 for 4 beats
```

### linvar - linear interpolation
```python
linvar([0, 1], 8)  # ramp 0->1 over 8 beats
linvar([0, 10, 0], [4, 4])  # triangle shape
```

### sinvar - sinusoidal
```python
sinvar([0, 1], 8)  # sine curve 0->1
```

### expvar - exponential
```python
expvar([0, 1], 8)  # exponential curve
```

### Pvar - pattern switching
```python
Pvar([[0,1,2], [0,2,4,6]], 8)  # switch patterns every 8 beats
```

---

## PLAYER METHODS

### Voice/Spread
- `.unison(n, detune)` - n voices with detune spread
- `.spread(on=0.125)` - stereo spread with pitch variation
- `.slider(start=0, on=1)` - glissando/portamento

### Scale
- `.penta()` - switch to pentatonic mode

### Timing
- `.seconds()` - durations in seconds (bpm=60)
- `.offbeat(dur)` - play on offbeat
- `.strum(dur)` - strum chords

### Pattern Manipulation
- `.reverse()` - reverse pattern
- `.shuffle()` - randomize order
- `.rotate(n)` - rotate pattern
- `.multiply(n)` - repeat pattern n times

### Scheduling
- `.every(n)` - do something every n beats
- `.often()` - random 0.5-4 beats
- `.sometimes()` - random 4-16 beats
- `.rarely()` - random 16-32 beats

### Effects on Methods
```python
p1 >> pads([0,2,4]).every(4).stutter(4)
p1 >> pads([0,2,4]).often().shuffle()
p1 >> pads([0,2,4]).sometimes().reverse()
```

### Playback Control
- `.stop(n)` - stop after n bars
- `.solo()` - solo this player
- `.only()` - stop all others

### Following
- `.follow(other)` - follow another player
- `.accompany(other, [0,2,4])` - accompany with chord

---

## SYNTHS BY CATEGORY

### Bass (40+)
`svdk`, `a_gesa`, `a_gesa2`, `a_gesa3`, `a_daft`, `a_xbass`, `abass`, `acidbass`, `acidline`, `bass`, `bbass`, `cbass`, `dafbass`, `dbass`, `dblbass`, `doom`, `dub`, `ebass`, `fbass`, `fuzz`, `glitchbass`, `growl`, `jbass`, `lbass`, `neuroreese`, `pbass`, `pumpbass`, `sawbass`, `subbass`, `subbass2`, `superbass`, `tb303`, `tb304`, `tb305`, `war`, `wobble`, `wobble2`

### Lead (30+)
`a_daftlead`, `a_glead`, `a_vlead`, `darklead`, `fmsynth`, `guit`, `hardstab`, `hoover`, `keys`, `lazer`, `plaits`, `plaitsX`, `prof`, `prophet`, `pulse`, `rave`, `razz`, `ripple`, `saw`, `scratch`, `sine`, `sitar`, `soprano`, `spark`, `ssaw`, `supersaw`, `swell`, `swiss`, `tritri`, `varicelle`, `varsaw`, `vati`, `viola`, `zap`

### Pad/Ambient (20+)
`a_vpad`, `ambi`, `angst`, `choir`, `cs80`, `darkpad`, `ethpad`, `four`, `industrialdrone`, `pad2`, `pads`, `pink`, `rsin`, `sinepad`, `soft`, `sos`, `space`, `stargazer`, `waves`

### Pluck/Keys (20+)
`bell`, `bell2`, `bellmod`, `charm`, `feel`, `glass`, `gong`, `karp`, `klank`, `lapin`, `marimba`, `mpluck`, `nylon`, `orient`, `orientmod`, `piano`, `pianovel`, `pluck`, `pluck2`, `rhodes`, `twang`

### Percussion/Drums (15+)
`a_bd`, `a_cy`, `a_hhat`, `a_sn`, `click`, `compkick`, `compperc`, `donk`, `industrialsnare`, `noisehit`, `prodrums`, `pumphihat`, `snick`, `spick`, `squish`, `subkick`

### Experimental/Noise (15+)
`bnoise`, `brown`, `bug`, `crackle`, `creep`, `dust`, `dustV`, `glitcher`, `gray`, `hnoise`, `latoo`, `lfnoise`, `noise`, `radio`, `total`, `virus`

### Organ (5+)
`donorgan`, `organ`, `organx`

---

## EFFECTS BY CATEGORY

### Filters (20+)
- `hpf/hpr` - highpass with resonance
- `lpf/lpr` - lowpass with resonance
- `bpf/bpr/bpnoise` - bandpass with modulation
- `swell` - filter swell (auto-wah)
- `ehpf/elpf` - envelope-controlled filters
- `djf/djfq` - DJ crossfader filter
- `MoogFF (mpf/mpr)` - Moog ladder filter
- `VALadder`, `VAKorg`, `VADiodeFilter` - analog modeled
- `SLPF` - sliding lowpass
- `resonz` - resonant peak
- `formant` - vowel formants
- `DafunkFilter (dafilter)` - acid filter

### Distortion (15+)
- `dist` - crossover distortion
- `triode` - tube saturation
- `tanh/tanhmix` - tanh saturation
- `fdist/fdistfreq` - filtered distortion
- `fdistc` - multiband distortion
- `wavefold/fold/symetry/smooth` - wave folding
- `waveshaper/wshape/wgain` - 12 algorithms
- `octafuz/octamix` - octave fuzz
- `idist` - inside-out distortion
- `dirt_krush (krush/kutoff)` - heavy crush

### Bit Crush/Digital (5+)
- `bits/crush` - bit reduction
- `crush2/bits2` - alternative crusher
- `bitrot` - complex degradation
- `lofi/lofiwow` - tape emulation
- `waveloss/drop` - sample dropout

### Delay/Reverb (10+)
- `room/mix` - FreeVerb
- `room2/mix2/damp2` - advanced reverb
- `jpverb/jpmix/jpdamp/jpsize` - JPverb
- `mverb/mverbmix/mverbfreeze` - MI reverb
- `shimmer/shimsize/shimpitch` - shimmer reverb
- `echo/echomix/echotime` - comb delay
- `dubdelay (dubd/dublen/dubfeed)` - dub delay
- `pingpong (pong/pongtime)` - stereo delay
- `feeddelay (feed/feedfreq)` - feedback delay
- `darkverb/dvdecay/dvdamp` - dark reverb

### Modulation (10+)
- `chorus/chorusrate` - 4-tap chorus
- `chorus2/chorus2rate/chorus2depth` - advanced chorus
- `flanger/fdecay/flangermix` - flanger
- `phaser/phaserdepth` - 4-stage phaser
- `tremolo/tremolomix` - amplitude mod
- `vib/vibdepth` - vibrato
- `spin` - spinning pan
- `autopan/awidth/apwave` - auto-pan
- `drift/driftspeed/driftdepth` - analog drift

### Pitch (5+)
- `pshift` - semitone shift
- `shift/shiftsize` - pitch shifter
- `bend/benddelay` - pitch bend
- `fshift/fphase` - frequency shift
- `slide/slidefrom/slidedelay` - glide

### Dynamics (3+)
- `comp/comp_down/comp_up` - compressor
- `drcomp` - drum compressor
- `leg` - note length

### Granular/Special (5+)
- `clouds` - MI Clouds granular
- `MiRings (mring)` - MI Rings resonator
- `MiBlow (blow)` - MI Blow
- `stutbreak/stutterfx` - stutter
- `gatecrush` - rhythmic gate
- `resample` - granular resample
- `chop/chopmix/chopwave` - amplitude chop

### EQ (3)
- `low/lowfreq` - low shelf
- `mid/midfreq/midq` - mid peak
- `high/highfreq` - high shelf

---

## DRUM PATTERNS (DrumPatterns.py)

### Usage
```python
from FoxDot.lib.DrumPatterns import pat, pbuild, ppat

d1 >> play(pat("t1"), dur=0.25)
d1 >> play(pbuild(["t1","t2","t1","t3"]), dur=0.25)
b1 >> bass([0,0,0,0], dur=ppat("tk1"))
```

### Key Patterns
- **Techno**: t1-t12, tk1-tk10, th1-th12, tc1-tc8
- **House**: h1-h10, hk1-hk4, hh1-hh6, hc1-hc4
- **Breaks**: b1-b10, bk1-bk8, bs1-bs8
- **DnB**: d1-d8, dk1-dk6, ds1-ds6, dh1-dh4
- **Hip-Hop**: hp1-hp8, hpk1-hpk6, hps1-hps6
- **EBM**: e1-e5, ek1-ek3, ec1-ec3
- **Gabber**: g1-g5, gk1-gk3
- **Fills**: fo1-fo4, fx1-fx3, ft1-ft4, fc1-fc3

### Groups
- tverse1, tchorus1, tbuild1, tdrop1
- hverse1, hchorus1, hbuild1
- bverse1, bchorus1, bbuild1
- dverse1, dchorus1, dbuild1

---

## PLAY STRING CHARACTERS

### Kicks
- `x` - standard kick
- `X` - heavy kick
- `v` - deep kick
- `k` - alt kick
- `g` - gabber kick
- `G` - distorted gabber

### Snares/Claps
- `o` - snare
- `O` - heavy snare
- `u` - acoustic snare
- `U` - break snare
- `c` - clap
- `C` - electro clap
- `r` - rim

### Hats
- `-` - closed hat
- `=` - open hat
- `:` - short hat
- `~` - ride

### Other
- `#` - crash
- `s` - shaker
- `S` - tambourine
- `e` - cowbell
- `t/m/M/T` - toms (low to high)
- ` ` - rest

---

## COMBINATION EXAMPLES

### Evolving Parameters
```python
p1 >> svdk([0,0,-2,0], dur=0.5,
    grit=linvar([0.3, 1], 16),
    cutoff=linvar([300, 2000], 8),
    res=sinvar([0.3, 0.8], 4),
    body=0.9, harm=var([0.2, 0.5], 8))
```

### Random Variations
```python
p1 >> plaits([0,2,4], dur=0.25,
    timbre=PWhite(0.2, 0.8),
    morph=PRand([0.1, 0.5, 0.9]),
    amp=PwRand([0.5, 0.8, 1], [1, 2, 1]))
```

### Pattern Operations
```python
p1 >> pads(var([[0,2,4], [0,3,5], [0,4,6]], 8),
    dur=Pvar([[0.5,0.5,1], [0.25]*8], 8),
    scale=var([Scale.minor, Scale.dorian], 16))
```

### Method Chaining
```python
p1 >> supersaw([0,2,4,5,7]).unison(4, 0.3).every(8).stutter(4).sometimes().reverse()
```

### Multi-Effect Processing
```python
p1 >> neuroreese([0], dur=2, oct=3,
    morph=linvar([0.3, 0.9], 8),
    lpf=linvar([400, 4000], 16), lpr=0.3,
    triode=0.4,
    room=0.3, mix=0.2,
    chorus=0.5, chorusrate=0.3)
```

### Complex Drum Programming
```python
d1 >> play(pbuild(["t1","t1","t2","t8"]), dur=0.25,
    amp=var([0.9, 1], 8),
    triode=linvar([0, 0.5], 32),
    hpf=var([0, 200], 16))
```

---

## RECOMMENDED COMBINATIONS

### Dark Industrial
- Synths: `svdk`, `a_gesa`, `doom`, `neuroreese`, `darklead`, `darkpad`
- Effects: `triode`, `wavefold`, `darkverb`, `gatecrush`
- Drums: EBM patterns (e1-e5)
- Tempo: 90-110 BPM
- Scales: `minor`, `phrygian`, `locrian`

### Acid Techno
- Synths: `tb303`, `tb304`, `tb305`, `acidbass`, `acidline`
- Effects: `DafunkFilter`, `dist`, `echo`
- Drums: Techno patterns (t1-t12)
- Tempo: 130-145 BPM
- Scales: `minor`, `blues`

### Rave/Hardcore
- Synths: `hoover`, `rave`, `supersaw`, `hardstab`
- Effects: `chorus`, `room`, `dist`
- Drums: House/Gabber patterns
- Tempo: 140-170 BPM
- Scales: `minor`, `dorian`

### Experimental/Noise
- Synths: `virus`, `angst`, `doom`, `glitcher`, `hnoise`
- Effects: `clouds`, `bitrot`, `wavefold`, `resample`
- Drums: Experimental patterns (x1-x8)
- Tempo: Variable
- Scales: `chromatic`

### DnB/Jungle
- Synths: `neuroreese`, `subbass`, `darklead`
- Effects: `comp`, `room`, `hpf`
- Drums: DnB patterns (d1-d8)
- Tempo: 170-180 BPM
- Scales: `minor`, `dorian`

---
