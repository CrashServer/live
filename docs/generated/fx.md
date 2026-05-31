# FoxDot FX Reference
_Generated 2026-05-29 02:54 from crashFX.py (120 effects)_

## Summary

| FX | Category | Params |
|---|---|---|
| `bitrot` | distortion | `bitrot`, `rotbits`, `rotrate`, `rotjitter` |
| `crush2` | distortion | `crush2`, `bits2`, `crush2mix` |
| `decimate` | distortion | `decimate`, `decbits`, `decrate`, `decsmooth` |
| `dist2` | distortion | `dist2`, `dist2mix`, `dist2shape` |
| `disto` | distortion | `disto`, `smooth`, `distomix` |
| `drive` | distortion | `drive`, `drivemix` |
| `drop` | distortion | `drop`, `dropof` |
| `dynfuzz` | distortion | `dynfuzz`, `dfgain`, `dfatk`, `dfdec`, `dftone` |
| `envdist` | distortion | `envdist`, `envdistgain`, `envdistsens`, `envdistattack` |
| `fdist` | distortion | `fdist`, `fdistfreq` |
| `fdistc` | distortion | `fdistc`, `fdistcfreq1`, `fdistcfreq2`, `fdistcfreq3`, `fdistcfreq4`, `fdistcm1` |
| `fold` | distortion | `fold`, `symetry`, `smooth` |
| `fuzz` | distortion | `fuzz`, `fuzzgain`, `fuzztone`, `fuzzoctave` |
| `idist` | distortion | `idist` |
| `krush` | distortion | `krush`, `kutoff`, `krushmix` |
| `multicrush` | distortion | `multicrush`, `mclowdrive`, `mcmiddrive`, `mchighdrive`, `mclofreq`, `mchifreq` |
| `noiz` | distortion | `noiz`, `noizr`, `noizt`, `sus` |
| `octafuz` | distortion | `octafuz`, `octamix` |
| `shape` | distortion | `shape`, `shapemix` |
| `squiz` | distortion | `squiz` |
| `tanh` | distortion | `tanh`, `tanhmix` |
| `tape` | distortion | `tape`, `tapedrive`, `tapewarm`, `tapewobble` |
| `tek` | distortion | `tek`, `tekr`, `tekd` |
| `triode` | distortion | `triode` |
| `tube` | distortion | `tube`, `tubegain`, `tubewarm`, `tubebias` |
| `wshape` | distortion | `wshape`, `wgain`, `wmix` |
| `a` | envelope | `a`, `sus`, `ac` |
| `drift` | envelope | `drift`, `driftspeed`, `driftdepth`, `driftsmooth` |
| `leg` | envelope | `leg`, `sus` |
| `position` | envelope | `position`, `sus` |
| `r` | envelope | `r`, `sus`, `rc` |
| `transient` | envelope | `transient`, `transattack`, `transsustain`, `transtime` |
| `bell` | filter | `bell`, `bellf`, `bellq` |
| `combres` | filter | `combres`, `combfreq`, `combdecay`, `combspread` |
| `dafilter` | filter | `dafilter`, `dastart`, `darel`, `darq`, `datype`, `sus` |
| `dfm` | filter | `dfm`, `dfmr`, `dfmd` |
| `djf` | filter | `djf`, `djfq` |
| `ehpf` | filter | `ehpf`, `ehpr`, `ehpa`, `ehps`, `ehpc`, `sus` |
| `elpf` | filter | `elpf`, `elpr`, `elpa`, `elps`, `elpc`, `sus` |
| `formant` | filter | `formant`, `formantmix` |
| `high` | filter | `high`, `highfreq` |
| `hpf` | filter | `hpf`, `hpr` |
| `lofi` | filter | `lofi`, `lofiwow`, `lofiamp` |
| `low` | filter | `low`, `lowfreq` |
| `lpf` | filter | `lpf`, `lpr` |
| `mid` | filter | `mid`, `midfreq`, `midq` |
| `mpf` | filter | `mpf`, `mpr` |
| `resonz` | filter | `rfreq`, `resonz` |
| `sblur` | filter | `sblur`, `sbluramt` |
| `sgate` | filter | `sgate`, `sgthresh`, `sgmode` |
| `spf` | filter | `spf`, `spr`, `spfslide`, `spfend` |
| `subenh` | filter | `subenh`, `subhfreq`, `subhgain` |
| `vadiod` | filter | `vadiod`, `vadiodr`, `vadiodd`, `vadiodc` |
| `vakorg` | filter | `vakorg`, `vakorgr`, `vakorgd`, `vakorgt`, `vakorgc` |
| `valad` | filter | `valad`, `valadr`, `valadd`, `valadt`, `valadc` |
| `vowel` | filter | `vowel`, `vowelf`, `vowelq` |
| `tstretch` | granular | `tstretch`, `tstretchsize` |
| `apan` | misc | `apan`, `awidth`, `apwave`, `beat_dur` |
| `fshift` | misc | `fshift`, `fphase`, `fmix` |
| `shimmer` | misc | `shimmer`, `shimsize`, `shimpitch`, `shimmix` |
| `test` | misc | `test`, `testa`, `testb`, `testc`, `testd` |
| `chop` | modulation | `chop`, `sus`, `chopmix`, `chopwave`, `chopi` |
| `csweep` | modulation | `csweep`, `cswfreq`, `cswdepth`, `cswrate`, `cswdecay` |
| `doppler` | modulation | `doppler`, `dopspd`, `dopdist` |
| `fm_pulse` | modulation | `fm_pulse`, `fm_pulse_i` |
| `fm_saw` | modulation | `fm_saw`, `fm_saw_i` |
| `fm_sin` | modulation | `fm_sin`, `fm_sin_i` |
| `glitch` | modulation | `glitch`, `glitchrate`, `glitchdepth`, `glitchcrush`, `glitchchance`, `beat_dur` |
| `mring` | modulation | `mring`, `rstruct`, `rbright`, `rdamp`, `rpos`, `rmodel` |
| `phaser` | modulation | `phaser`, `phaserdepth` |
| `resonbank` | modulation | `resonbank`, `rbfreq`, `rbdecay`, `rbspread` |
| `ring` | modulation | `ring`, `ringl`, `ringh` |
| `ringz` | modulation | `ringzfreq`, `ringz` |
| `sbrk` | modulation | `sbrk`, `t_reset`, `sbrkdur`, `sbrkmix`, `sus` |
| `stut` | modulation | `stut`, `stutrate`, `stutlen`, `t_reset` |
| `tremolo` | modulation | `tremolo`, `beat_dur`, `tremolomix` |
| `vocod` | modulation | `vocod`, `voccarr`, `vocbw` |
| `apan` | panning | `apan`, `awidth`, `apwave`, `beat_dur` |
| `panR` | panning | `panR` |
| `stereowidth` | panning | `stereowidth`, `swfreq`, `swnarrow`, `swwide` |
| `blow` | pitch | `blow`, `bflow`, `bmodel`, `bpos`, `sus` |
| `fshift` | pitch | `fshift`, `fphase`, `fmix` |
| `glide` | pitch | `glide`, `glidedur` |
| `glide2` | pitch | `glide2`, `glide2dur`, `sus` |
| `octclean` | pitch | `octclean`, `ocsub`, `ocup` |
| `octer` | pitch | `octer`, `octersub`, `octersubsub` |
| `shift` | pitch | `shift`, `shiftsize` |
| `spwarp` | pitch | `spwarp`, `spwstr`, `spwshift` |
| `cheapverb` | reverb | `cheapverb`, `cvdecay`, `cvdamp` |
| `clouds` | reverb | `clouds`, `cpos`, `csize`, `cdens`, `ctex`, `cpitch` |
| `jpverb` | reverb | `jpverb`, `jpmix`, `jpdamp`, `jpsize` |
| `mverb` | reverb | `mverb`, `mverbmix`, `mverbdamp`, `mverbdiff`, `mverbfreeze` |
| `room2` | reverb | `room2`, `mix2`, `damp2`, `revatk`, `revsus` |
| `shimmer` | reverb | `shimmer`, `shimsize`, `shimpitch`, `shimmix` |
| `spring` | reverb | `spring`, `sprdecay`, `sprdamp`, `sprtens` |
| `chorus` | time | `chorus`, `chorusrate` |
| `chorus2` | time | `chorus2`, `chorus2rate`, `chorus2depth`, `chorus2mode` |
| `dubd` | time | `dubd`, `dublen`, `dubwidth`, `dubfeed` |
| `eb` | time | `eb`, `ebfeed`, `ebmix`, `ebmode`, `ebwow`, `ebflutter` |
| `echo` | time | `echo`, `echomix`, `beat_dur`, `echotime` |
| `fbdelay` | time | `fbdelay`, `fbtime`, `fbfeed`, `fbcutoff`, `fbspread`, `beat_dur` |
| `feed` | time | `feed`, `feedfreq` |
| `flanger` | time | `flanger`, `fdecay`, `flangermix` |
| `freeze` | time | `freeze`, `freezemix`, `freezerand` |
| `gdel` | time | `gdel`, `gdeltime`, `gdelsize`, `gdelsprd`, `gdelfb` |
| `pong` | time | `pong`, `beat_dur`, `pongtime` |
| `rgate` | time | `rgate`, `rgaterate`, `rgatewave`, `beat_dur` |
| `tstop` | time | `tstop`, `tstoptime`, `tstopcurve`, `tstopdir`, `sus` |
| `fx` | util | `fx`, `lpfx`, `hpfx`, `fxout`, `fxmix` |
| `fx1` | util | `fx1`, `lpfx1`, `hpfx1`, `fx1mix` |
| `fx2` | util | `fx2`, `lpfx2`, `hpfx2`, `fx2mix` |
| `mon` | util | `mon` |
| `output` | util | `output` |
| `comp` | volume | `comp`, `comp_down`, `comp_up` |
| `drcomp` | volume | `drcomp` |
| `mbcomp` | volume | `mbcomp`, `mbcxlo`, `mbcxhi`, `mbcrat`, `mbcatk`, `mbcrel` |
| `mu` | volume | `mu` |
| `pumper` | volume | `pumper`, `pumprate`, `pumpattack`, `pumprel`, `pumpcurve` |
| `sidechain` | volume | `sidechain`, `sidechain_atk`, `sidechain_rel`, `thresh` |
| `vol` | volume | `vol` |


## DISTORTION

### `bitrot`  —  bitrot
_Digital degradation - bit reduction with jitter and aliasing_

| Param | Default |
|---|---|
| `bitrot` | `0.5` |
| `rotbits` | `8` |
| `rotrate` | `0.5` |
| `rotjitter` | `0.1` |

### `crush2`  —  crush2
| Param | Default |
|---|---|
| `crush2` | `0` |
| `bits2` | `8` |
| `crush2mix` | `0.5` |

### `decimate`  —  decimate
_Extreme decimation - aggressive lo-fi destruction_

| Param | Default |
|---|---|
| `decimate` | `0.5` |
| `decbits` | `4` |
| `decrate` | `4000` |
| `decsmooth` | `0` |

### `dist2`  —  dist2
| Param | Default |
|---|---|
| `dist2` | `0` |
| `dist2mix` | `1` |
| `dist2shape` | `0.1` |

### `disto`  —  disto_mod
| Param | Default |
|---|---|
| `disto` | `0` |
| `smooth` | `0.3` |
| `distomix` | `1` |

### `drive`  —  overdriveDistortion
| Param | Default |
|---|---|
| `drive` | `0` |
| `drivemix` | `0.5` |

### `drop`  —  waveloss
| Param | Default |
|---|---|
| `drop` | `0` |
| `dropof` | `100` |

### `dynfuzz`  —  dynfuzz
_Fuzz with per-note envelope shaping - pumps on repetitive patterns_

| Param | Default |
|---|---|
| `dynfuzz` | `0` |
| `dfgain` | `1` |
| `dfatk` | `0.005` |
| `dfdec` | `0.3` |
| `dftone` | `0.6` |

### `envdist`  —  envdist
_Distortion amount follows signal amplitude - punchy dynamics_

| Param | Default |
|---|---|
| `envdist` | `0.5` |
| `envdistgain` | `2` |
| `envdistsens` | `1` |
| `envdistattack` | `0.01` |

### `fdist`  —  fdist
| Param | Default |
|---|---|
| `fdist` | `0` |
| `fdistfreq` | `1600` |

### `fdistc`  —  fdistc
| Param | Default |
|---|---|
| `fdistc` | `0` |
| `fdistcfreq1` | `1600` |
| `fdistcfreq2` | `1600` |
| `fdistcfreq3` | `1600` |
| `fdistcfreq4` | `1600` |
| `fdistcm1` | `1.1` |
| `fdistcm2` | `1.1` |
| `fdistcm3` | `1.4` |
| `fdistcm4` | `2` |
| `fdistcq1` | `1` |
| `fdistcq2` | `1` |
| `fdistcq3` | `1` |
| `fdistcq4` | `1` |

### `fold`  —  wavefold
| Param | Default |
|---|---|
| `fold` | `0` |
| `symetry` | `1` |
| `smooth` | `0.5` |

### `fuzz`  —  fuzz
_Asymmetric fuzz with octave-up artifacts_

| Param | Default |
|---|---|
| `fuzz` | `0.5` |
| `fuzzgain` | `2` |
| `fuzztone` | `0.5` |
| `fuzzoctave` | `0.3` |

### `idist`  —  idist
| Param | Default |
|---|---|
| `idist` | `0` |

### `krush`  —  dirt_krush
| Param | Default |
|---|---|
| `krush` | `0` |
| `kutoff` | `15000` |
| `krushmix` | `0.5` |

### `multicrush`  —  multicrush
_Multiband distortion - independent saturation per frequency band_

| Param | Default |
|---|---|
| `multicrush` | `0.5` |
| `mclowdrive` | `1.5` |
| `mcmiddrive` | `2` |
| `mchighdrive` | `1.8` |
| `mclofreq` | `200` |
| `mchifreq` | `3000` |

### `noiz`  —  noiz
_Noize Fx_

| Param | Default |
|---|---|
| `noiz` | `0` |
| `noizr` | `1` |
| `noizt` | `0` |
| `sus` | `1` |

### `octafuz`  —  octafuz
| Param | Default |
|---|---|
| `octafuz` | `0` |
| `octamix` | `0.5` |

### `shape`  —  wavesShapeDistortion
| Param | Default |
|---|---|
| `shape` | `0` |
| `shapemix` | `0.5` |

### `squiz`  —  squiz
| Param | Default |
|---|---|
| `squiz` | `0` |

### `tanh`  —  tanhDisto
| Param | Default |
|---|---|
| `tanh` | `0` |
| `tanhmix` | `0.5` |

### `tape`  —  tape
_Tape saturation with warmth, compression and subtle wobble_

| Param | Default |
|---|---|
| `tape` | `0.5` |
| `tapedrive` | `1.5` |
| `tapewarm` | `0.5` |
| `tapewobble` | `0.1` |

### `tek`  —  tek
| Param | Default |
|---|---|
| `tek` | `0` |
| `tekr` | `500` |
| `tekd` | `8` |

### `triode`  —  triode
| Param | Default |
|---|---|
| `triode` | `0` |

### `tube`  —  tubedrive
_Tube-style saturation with even harmonics and warmth_

| Param | Default |
|---|---|
| `tube` | `0.5` |
| `tubegain` | `1.5` |
| `tubewarm` | `0.6` |
| `tubebias` | `0.1` |

### `wshape`  —  waveshaper
_Waveshaper distortion whith different waveforms_

| Param | Default |
|---|---|
| `wshape` | `0` |
| `wgain` | `1` |
| `wmix` | `0.5` |


## ENVELOPE

### `a`  —  attack
_attack envelope_

| Param | Default |
|---|---|
| `a` | `0` |
| `sus` | `1` |
| `ac` | `0` |

### `drift`  —  drift
_Timing drift - adds subtle humanized timing variations_

| Param | Default |
|---|---|
| `drift` | `0.5` |
| `driftspeed` | `2` |
| `driftdepth` | `0.02` |
| `driftsmooth` | `0.5` |

### `leg`  —  leg
| Param | Default |
|---|---|
| `leg` | `0` |
| `sus` | `1` |

### `position`  —  trimPos
| Param | Default |
|---|---|
| `position` | `0` |
| `sus` | `1` |

### `r`  —  releas
_release envelope_

| Param | Default |
|---|---|
| `r` | `0` |
| `sus` | `1` |
| `rc` | `0` |

### `transient`  —  transient
_Transient shaper - control attack punch and sustain level_

| Param | Default |
|---|---|
| `transient` | `0.5` |
| `transattack` | `1` |
| `transsustain` | `1` |
| `transtime` | `0.02` |


## FILTER

### `bell`  —  Bell_Filter
_Bell Filter_

| Param | Default |
|---|---|
| `bell` | `0.5` |
| `bellf` | `3000` |
| `bellq` | `0.9` |

### `combres`  —  combres
_Comb resonator - metallic textures and pitched resonance_

| Param | Default |
|---|---|
| `combres` | `0.5` |
| `combfreq` | `200` |
| `combdecay` | `0.3` |
| `combspread` | `0.01` |

### `dafilter`  —  DafunkFilter
_Dafunk Filter_

| Param | Default |
|---|---|
| `dafilter` | `1200` |
| `dastart` | `250` |
| `darel` | `0.2` |
| `darq` | `0.5` |
| `datype` | `0` |
| `sus` | `1` |

### `dfm`  —  DFM1
_DFM1 filter_

| Param | Default |
|---|---|
| `dfm` | `1000` |
| `dfmr` | `0.1` |
| `dfmd` | `1` |

### `djf`  —  djFilter
_DJ Filter_

| Param | Default |
|---|---|
| `djf` | `0` |
| `djfq` | `0.3` |

### `ehpf`  —  envHPF
_ehpf_

| Param | Default |
|---|---|
| `ehpf` | `0` |
| `ehpr` | `0.7` |
| `ehpa` | `0.001` |
| `ehps` | `0.01` |
| `ehpc` | `-3` |
| `sus` | `1` |

### `elpf`  —  envLPF
_elpf_

| Param | Default |
|---|---|
| `elpf` | `0` |
| `elpr` | `0.7` |
| `elpa` | `0.001` |
| `elps` | `0.01` |
| `elpc` | `-3` |
| `sus` | `1` |

### `formant`  —  formantFilter
| Param | Default |
|---|---|
| `formant` | `0` |
| `formantmix` | `0.5` |

### `high`  —  H_Equalizer
_High shelf Equalizer_

| Param | Default |
|---|---|
| `high` | `1` |
| `highfreq` | `8000` |

### `hpf`  —  highPassFilter
_Highpass filter_

| Param | Default |
|---|---|
| `hpf` | `0` |
| `hpr` | `1` |

### `lofi`  —  lofi
| Param | Default |
|---|---|
| `lofi` | `0` |
| `lofiwow` | `0.5` |
| `lofiamp` | `0.5` |

### `low`  —  L_Equalizer
_Low shelf Equalizer_

| Param | Default |
|---|---|
| `low` | `1` |
| `lowfreq` | `80` |

### `lpf`  —  lowPassFilter
| Param | Default |
|---|---|
| `lpf` | `0` |
| `lpr` | `1` |

### `mid`  —  M_Equalizer
_Middle boost Equalizer_

| Param | Default |
|---|---|
| `mid` | `1` |
| `midfreq` | `1000` |
| `midq` | `1` |

### `mpf`  —  MoogFF
_MoogFF filter_

| Param | Default |
|---|---|
| `mpf` | `0` |
| `mpr` | `0` |

### `resonz`  —  resonz
_Resonz_

| Param | Default |
|---|---|
| `rfreq` | `50` |
| `resonz` | `0.1` |

### `sblur`  —  sblur
_Spectral blur - smears frequencies into evolving textures_

| Param | Default |
|---|---|
| `sblur` | `0` |
| `sbluramt` | `4` |

### `sgate`  —  sgate
_Spectral gate - strips sound to loudest partials (mode 0) or quietest (mode 1)_

| Param | Default |
|---|---|
| `sgate` | `0` |
| `sgthresh` | `1` |
| `sgmode` | `0` |

### `spf`  —  SLPF
| Param | Default |
|---|---|
| `spf` | `0` |
| `spr` | `1` |
| `spfslide` | `1` |
| `spfend` | `15000` |

### `subenh`  —  subenh
_Sub-harmonic enhancer - adds one octave below the low end_

| Param | Default |
|---|---|
| `subenh` | `0` |
| `subhfreq` | `100` |
| `subhgain` | `1` |

### `vadiod`  —  VADiodeFilter
_VADiode filter_

| Param | Default |
|---|---|
| `vadiod` | `500` |
| `vadiodr` | `0.5` |
| `vadiodd` | `0.5` |
| `vadiodc` | `0.3` |

### `vakorg`  —  VAKorg
_VAKorg filter_

| Param | Default |
|---|---|
| `vakorg` | `500` |
| `vakorgr` | `0.5` |
| `vakorgd` | `0.5` |
| `vakorgt` | `0` |
| `vakorgc` | `0.3` |

### `valad`  —  VALadder
_VALadder filter_

| Param | Default |
|---|---|
| `valad` | `500` |
| `valadr` | `0.3` |
| `valadd` | `5` |
| `valadt` | `0` |
| `valadc` | `0.2` |

### `vowel`  —  vowel
_Vowel formant filter - vowelf sweeps a(0) e(1) i(2) o(3) u(4), vowelq controls resonance_

| Param | Default |
|---|---|
| `vowel` | `0` |
| `vowelf` | `0` |
| `vowelq` | `1` |


## GRANULAR

### `tstretch`  —  timeStretchFx
_PitchShift-based time stretch on any signal, pitch preserved_

| Param | Default |
|---|---|
| `tstretch` | `1` |
| `tstretchsize` | `0.2` |


## MISC

### `apan`  —  autopan
_Rhythmic auto-panning with waveform selection (0=sine, 1=tri, 2=saw, 3=pulse)_

| Param | Default |
|---|---|
| `apan` | `0` |
| `awidth` | `1` |
| `apwave` | `0` |
| `beat_dur` | `1` |

### `fshift`  —  freqshift
_Frequency shifter - shifts all frequencies by a fixed Hz amount (creates metallic/robotic sounds)_

| Param | Default |
|---|---|
| `fshift` | `0` |
| `fphase` | `0` |
| `fmix` | `0.5` |

### `shimmer`  —  shimmer
_Shimmer reverb - octave-up pitch shift + reverb for ethereal sounds_

| Param | Default |
|---|---|
| `shimmer` | `0` |
| `shimsize` | `0.8` |
| `shimpitch` | `0.5` |
| `shimmix` | `0.5` |

### `test`  —  test
_Test Fx_

| Param | Default |
|---|---|
| `test` | `0` |
| `testa` | `0` |
| `testb` | `0` |
| `testc` | `0` |
| `testd` | `0` |


## MODULATION

### `chop`  —  chop
| Param | Default |
|---|---|
| `chop` | `0` |
| `sus` | `1` |
| `chopmix` | `1` |
| `chopwave` | `0` |
| `chopi` | `0` |

### `csweep`  —  csweep
_Resonant comb sweep - moving metallic resonance, cswfreq sets pitch_

| Param | Default |
|---|---|
| `csweep` | `0` |
| `cswfreq` | `200` |
| `cswdepth` | `0.3` |
| `cswrate` | `0.5` |
| `cswdecay` | `0.5` |

### `doppler`  —  doppler
_Doppler effect - sound passes by with pitch shift, volume and pan movement_

| Param | Default |
|---|---|
| `doppler` | `0` |
| `dopspd` | `0.5` |
| `dopdist` | `1.0` |

### `fm_pulse`  —  FrequencyModulationPulse
| Param | Default |
|---|---|
| `fm_pulse` | `0` |
| `fm_pulse_i` | `1` |

### `fm_saw`  —  FrequencyModulationSaw
| Param | Default |
|---|---|
| `fm_saw` | `0.5` |
| `fm_saw_i` | `0.7` |

### `fm_sin`  —  FrequencyModulationSine
| Param | Default |
|---|---|
| `fm_sin` | `0` |
| `fm_sin_i` | `1` |

### `glitch`  —  glitch
_Random glitch - combines crush, pitch shift, and stutters_

| Param | Default |
|---|---|
| `glitch` | `0.5` |
| `glitchrate` | `8` |
| `glitchdepth` | `0.5` |
| `glitchcrush` | `0.3` |
| `glitchchance` | `0.5` |
| `beat_dur` | `1` |

### `mring`  —  MiRings
_Mi Rings resonator_

| Param | Default |
|---|---|
| `mring` | `0` |
| `rstruct` | `0.1` |
| `rbright` | `0.8` |
| `rdamp` | `0.7` |
| `rpos` | `0` |
| `rmodel` | `1` |
| `rpoly` | `4` |
| `regg` | `0` |
| `sus` | `0` |
| `rsus` | `2` |

### `phaser`  —  phaser
| Param | Default |
|---|---|
| `phaser` | `0` |
| `phaserdepth` | `0.5` |

### `resonbank`  —  resonbank
_6-resonator bank (rbspread=1 harmonic, other = inharmonic)_

| Param | Default |
|---|---|
| `resonbank` | `0` |
| `rbfreq` | `200` |
| `rbdecay` | `0.5` |
| `rbspread` | `1.0` |

### `ring`  —  ring_modulation
| Param | Default |
|---|---|
| `ring` | `0` |
| `ringl` | `500` |
| `ringh` | `1500` |

### `ringz`  —  Ringmod
_Ringmodulation_

| Param | Default |
|---|---|
| `ringzfreq` | `50` |
| `ringz` | `0.1` |

### `sbrk`  —  stutbreak
| Param | Default |
|---|---|
| `sbrk` | `0.5` |
| `t_reset` | `0` |
| `sbrkdur` | `0.5` |
| `sbrkmix` | `1.0` |
| `sus` | `1` |

### `stut`  —  stutterfx
| Param | Default |
|---|---|
| `stut` | `1` |
| `stutrate` | `1` |
| `stutlen` | `0.02` |
| `t_reset` | `0` |

### `tremolo`  —  tremolo
| Param | Default |
|---|---|
| `tremolo` | `0` |
| `beat_dur` | `1` |
| `tremolomix` | `1` |

### `vocod`  —  vocod
_Vocoder - robotic spectral reshaping, voccarr blends noise(0) to pulse(1)_

| Param | Default |
|---|---|
| `vocod` | `0` |
| `voccarr` | `0.5` |
| `vocbw` | `0.3` |


## PANNING

### `apan`  —  autopan
_Rhythmic auto-panning with waveform selection (0=sine, 1=tri, 2=saw, 3=pulse)_

| Param | Default |
|---|---|
| `apan` | `0` |
| `awidth` | `1` |
| `apwave` | `0` |
| `beat_dur` | `1` |

### `panR`  —  panR
_Pan rear_

| Param | Default |
|---|---|
| `panR` | `1` |

### `stereowidth`  —  stereowidth
_Stereo imager - mono bass, adjustable width for highs_

| Param | Default |
|---|---|
| `stereowidth` | `0.5` |
| `swfreq` | `300` |
| `swnarrow` | `0` |
| `swwide` | `1.5` |


## PITCH

### `blow`  —  MiBlow
_Mi Blow resonator_

| Param | Default |
|---|---|
| `blow` | `0` |
| `bflow` | `0.3` |
| `bmodel` | `0` |
| `bpos` | `0.2` |
| `sus` | `0` |

### `fshift`  —  freqshift
_Frequency shifter - shifts all frequencies by a fixed Hz amount (creates metallic/robotic sounds)_

| Param | Default |
|---|---|
| `fshift` | `0` |
| `fphase` | `0` |
| `fmix` | `0.5` |

### `glide`  —  glide
| Param | Default |
|---|---|
| `glide` | `0` |
| `glidedur` | `0.05` |

### `glide2`  —  glissandoriginal
| Param | Default |
|---|---|
| `glide2` | `0` |
| `glide2dur` | `0.5` |
| `sus` | `1` |

### `octclean`  —  octclean
_Clean octaver via PitchShift (sub -1oct, up +1oct)_

| Param | Default |
|---|---|
| `octclean` | `0` |
| `ocsub` | `0.5` |
| `ocup` | `0.3` |

### `octer`  —  octer
| Param | Default |
|---|---|
| `octer` | `0` |
| `octersub` | `0` |
| `octersubsub` | `0` |

### `shift`  —  pitchshifter
| Param | Default |
|---|---|
| `shift` | `0` |
| `shiftsize` | `0.1` |

### `spwarp`  —  spwarp
_Spectral warp - stretch harmonics apart (>1) or compress (<1), shift bins up/down_

| Param | Default |
|---|---|
| `spwarp` | `0` |
| `spwstr` | `1.5` |
| `spwshift` | `0` |


## REVERB

### `cheapverb`  —  cheapverb
_CPU-light delay-based reverb (Schroeder topology)_

| Param | Default |
|---|---|
| `cheapverb` | `0` |
| `cvdecay` | `1.5` |
| `cvdamp` | `0.5` |

### `clouds`  —  clouds
_Clouds granulator_

| Param | Default |
|---|---|
| `clouds` | `0` |
| `cpos` | `0.5` |
| `csize` | `0.25` |
| `cdens` | `0.4` |
| `ctex` | `0.5` |
| `cpitch` | `0` |
| `cgain` | `2` |
| `cfb` | `0` |
| `cmode` | `0` |

### `jpverb`  —  jpVerb
| Param | Default |
|---|---|
| `jpverb` | `0` |
| `jpmix` | `0.5` |
| `jpdamp` | `0.0` |
| `jpsize` | `1.0` |

### `mverb`  —  miVerb
| Param | Default |
|---|---|
| `mverb` | `0` |
| `mverbmix` | `0.5` |
| `mverbdamp` | `0.8` |
| `mverbdiff` | `0.625` |
| `mverbfreeze` | `0` |

### `room2`  —  reverb_stereo
| Param | Default |
|---|---|
| `room2` | `0` |
| `mix2` | `0.2` |
| `damp2` | `0.8` |
| `revatk` | `0` |
| `revsus` | `1` |

### `shimmer`  —  shimmer
_Shimmer reverb - octave-up pitch shift + reverb for ethereal sounds_

| Param | Default |
|---|---|
| `shimmer` | `0` |
| `shimsize` | `0.8` |
| `shimpitch` | `0.5` |
| `shimmix` | `0.5` |

### `spring`  —  spring
_Spring reverb - dub/surf/lo-fi spring tank character_

| Param | Default |
|---|---|
| `spring` | `0` |
| `sprdecay` | `1.5` |
| `sprdamp` | `0.5` |
| `sprtens` | `0.5` |


## TIME

### `chorus`  —  chorus
| Param | Default |
|---|---|
| `chorus` | `0` |
| `chorusrate` | `0.5` |

### `chorus2`  —  chorus2
| Param | Default |
|---|---|
| `chorus2` | `0` |
| `chorus2rate` | `0.5` |
| `chorus2depth` | `1` |
| `chorus2mode` | `1` |

### `dubd`  —  dubdelay
| Param | Default |
|---|---|
| `dubd` | `0` |
| `dublen` | `0.1` |
| `dubwidth` | `0.12` |
| `dubfeed` | `0.8` |

### `eb`  —  echoBoy
_Echo Boy - Roland-style delay (ebmode: 0=Digital, 1=Analog, 2=Tape)_

| Param | Default |
|---|---|
| `eb` | `0.5` |
| `ebfeed` | `0.5` |
| `ebmix` | `0.3` |
| `ebmode` | `0` |
| `ebwow` | `0.1` |
| `ebflutter` | `0.15` |
| `ebsat` | `0.3` |
| `sus` | `1` |

### `echo`  —  combDelay
| Param | Default |
|---|---|
| `echo` | `0` |
| `echomix` | `0.5` |
| `beat_dur` | `1` |
| `echotime` | `1` |

### `fbdelay`  —  fbdelay
_Feedback delay with filtering - self-oscillating dub delays_

| Param | Default |
|---|---|
| `fbdelay` | `0.5` |
| `fbtime` | `0.25` |
| `fbfeed` | `0.7` |
| `fbcutoff` | `3000` |
| `fbspread` | `0.02` |
| `beat_dur` | `1` |

### `feed`  —  feeddelay
| Param | Default |
|---|---|
| `feed` | `0.7` |
| `feedfreq` | `50` |

### `flanger`  —  flanger
| Param | Default |
|---|---|
| `flanger` | `0` |
| `fdecay` | `0` |
| `flangermix` | `0.5` |

### `freeze`  —  spectralfreeze
_Spectral freeze - captures and holds spectrum for drones_

| Param | Default |
|---|---|
| `freeze` | `0.5` |
| `freezemix` | `0.5` |
| `freezerand` | `0` |

### `gdel`  —  gdel
_Granular delay - echoes fragment and scatter into texture_

| Param | Default |
|---|---|
| `gdel` | `0` |
| `gdeltime` | `0.5` |
| `gdelsize` | `0.1` |
| `gdelsprd` | `0.5` |
| `gdelfb` | `0.3` |

### `pong`  —  pingpong
| Param | Default |
|---|---|
| `pong` | `0` |
| `beat_dur` | `1` |
| `pongtime` | `1` |

### `rgate`  —  rhythmgate
_Rhythmic gate - choppy textures synced to beat (wave: 0=square, 1=saw, 2=sine)_

| Param | Default |
|---|---|
| `rgate` | `0.5` |
| `rgaterate` | `4` |
| `rgatewave` | `0` |
| `beat_dur` | `1` |

### `tstop`  —  tapestop
_Tape stop - pitch drops to zero (or speeds up) like stopping tape_

| Param | Default |
|---|---|
| `tstop` | `0.5` |
| `tstoptime` | `0.5` |
| `tstopcurve` | `-4` |
| `tstopdir` | `0` |
| `sus` | `1` |


## UTIL

### `fx`  —  fxout
_FX Bus_

| Param | Default |
|---|---|
| `fx` | `0` |
| `lpfx` | `22000` |
| `hpfx` | `0` |
| `fxout` | `2` |
| `fxmix` | `1` |

### `fx1`  —  fx1out
_FX1 Bus_

| Param | Default |
|---|---|
| `fx1` | `0` |
| `lpfx1` | `22000` |
| `hpfx1` | `0` |
| `fx1mix` | `1` |

### `fx2`  —  fx2out
_FX2 Bus_

| Param | Default |
|---|---|
| `fx2` | `0` |
| `lpfx2` | `22000` |
| `hpfx2` | `0` |
| `fx2mix` | `1` |

### `mon`  —  monitoring
_Monitoring Bus_

| Param | Default |
|---|---|
| `mon` | `0` |

### `output`  —  output
_Output select Bus_

| Param | Default |
|---|---|
| `output` | `0` |


## VOLUME

### `comp`  —  comp
| Param | Default |
|---|---|
| `comp` | `0` |
| `comp_down` | `1` |
| `comp_up` | `0.8` |

### `drcomp`  —  drcomp
| Param | Default |
|---|---|
| `drcomp` | `0` |

### `mbcomp`  —  mbcomp
_Multiband compressor - tighten lows without squashing highs_

| Param | Default |
|---|---|
| `mbcomp` | `0` |
| `mbcxlo` | `200` |
| `mbcxhi` | `3000` |
| `mbcrat` | `3` |
| `mbcatk` | `0.01` |
| `mbcrel` | `0.1` |

### `mu`  —  mimu
| Param | Default |
|---|---|
| `mu` | `0` |

### `pumper`  —  pumper
_Sidechain simulation - creates pumping effect synced to beat_

| Param | Default |
|---|---|
| `pumper` | `0.5` |
| `pumprate` | `4` |
| `pumpattack` | `0.005` |
| `pumprel` | `0.2` |
| `pumpcurve` | `-4` |

### `sidechain`  —  sidechain
| Param | Default |
|---|---|
| `sidechain` | `0` |
| `sidechain_atk` | `0.05` |
| `sidechain_rel` | `0.1` |
| `thresh` | `0.006` |

### `vol`  —  volume
_Volume_

| Param | Default |
|---|---|
| `vol` | `1` |
