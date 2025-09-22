# Crash Server Functions Cheatsheet
## version 1.0 - 21 sept 2025

## Utility Classes

| Function Call | Argument Description | Function Description | Example |
|---------------|---------------------|---------------------|-----|
| `StorageAttack()` | - | Gets attacks from files and puts them in a dict |
| `MidiDwarf(ch=12)` | **ch**: MIDI channel (default: 12) | Controls dwarf recording with various commands |
| `voicecount.start(lang="fr", voice=2, dur=8, amp=1, pitch=0.0` | **lang**: select the language<br>**voice** : type of voice<br>**dur** : freq of the count<br>**voicecount.help()**  : show the help | Random voice counting recursively every 8 bars |
| `Variation(durTotal, durBreak)` | **durTotal**: total duration<br>**durBreak**: variation duration<br>**variation.help()** : show the help | Creates continuous master variations | `variation(16,4)` |

## Global Functions

| Function Call | Argument Description | Function Description | Example |
|---------------|---------------------|---------------------|---------------------|
| `random_bpm_var()` | - | Randomly changes the clock with random variables |
| `random_bpm()` | - | Changes the Clock to a random number |
| `setseed(seed=None)` | **seed**: seed for random generator (default: None) | Sets the seed for the random generator | <pre lang="python">setseed(1664)</pre> | 
| `darker()` | - | Changes the scale to a darker one | |
| `lighter()` | - | Changes the scale to a lighter one | |
| `lininf(start=0, finish=1, time=32)` | **start**: starting value (default: 0)<br>**finish**: ending value (default: 1)<br>**time**: duration in beats (default: 32) | Linvar from start to finish but stays at finish after time | `d1 >> blip(amp=lininf(0,1,32))`|
| `expinf(start=0, finish=1, time=32)` | **start**: starting value (default: 0)<br>**finish**: ending value (default: 1)<br>**time**: duration in beats (default: 32) | Expvar from start to finish but stays at finish after time | `d1 >> blip(amp=expinf(0,1,32))` |
| `linbpm(endBpm=170, durBpm=128)` | **endBpm**: target BPM (default: 170)<br>**durBpm**: duration to reach BPM (default: 128) | Changes current BPM to target BPM in x beats | `Clock.bpm = linbpm(192, 32)` |
| `linmod(start, end, duration, default=0)` | **start**: starting value<br>**end**: ending value<br>**duration**: duration<br>**default**: default value (default: 0) | Linvar from start to end during duration at next mod(duration) then returns to default | `d1 >> star(lpf=linmod(6000, 120, 8))` |
| `drop(playTime=14, dropTime=2, nbloop=1)` | **playTime**: play time (default: 14)<br>**dropTime**: drop time (default: 2)<br>**nbloop**: number of loops (default: 1) | Drops amplify to 0 for random players | `drop(12,4,3)` |
| `drop_bpm(duree=32, nbr=0, end=4)` | **duree**: total duration of the part (default: 32)<br>**nbr**: number of drop divisions (default: 0)<br>**end**: drop duration from the end (default: 4) | Creates a BPM drop effect (var bpm) | **Need a fix, not working**  |
| `melody()` | - | Generates a melody based on Markov chains |
| `reset()` | - | Emergency reset of everything |
| `PTuple(pattern, size=1)` | **pattern**: source pattern<br>**size**: group size (default: 1) | Returns a PGroup of size 'size' with the pattern | `PTuple(PWhite(-1,1), 3) = P(PWhite(-1.0, 1.0), PWhite(-1.0, 1.0), PWhite(-1.0, 1.0))` |

## Crash Server Live Functions

| Function Call | Argument Description | Function Description |
|---------------|---------------------|---------------------|
| `sendAttack(msg="")` | **msg**: message to send (default: "") | Sends an attack to webTroop |
| `ascii_gen(text="", font="")` | **text**: text to convert (default: "")<br>**font**: font to use (default: "") | Generates ASCII art from text |
| `connect()` | - | Complete reset and sets bpm, root, sos & video player |
| `attack(attackName, prntOut=0)` | **attackName**: attack name<br>**prntOut**: output display (default: 0)<br>**attack()** : return a random attack | Gets the attack code |
| `lost(attack=None)` | **attack**: attack name (default: None) <br>**lost()** : return a list of all attacks  | List of all attacks |
| `psynth(synth="")` | **synth**: synth name (default: "")<br>**psynth()** : return a list of all synth | Shows the name and arguments of a synth |
| `pfx(fx="")` | **fx**: effect name (default: "")<br>**pfx()** : return a list of all fx | Shows the name and arguments of an effect |
| `psample(sample="")` | **sample**: sample name (default: "")<br>**psample()** : return a list of all samples<br>**psample("kick")** : return a list of kick samples | Shows sample descriptions or finds corresponding letter |
| `ploops(loopName="")` | **loopName**: loop name (default: "")<br>**ploops()** : return a list of all loops<br>**ploop(4)** : return a list of 4 random loops<br>**ploop("break")** : return a list of all break loops  | Shows all available loop sample name for the given loop |
| `pfonk(fonk="")` | **fonk**: function name (default: "")<br>**pfonk()** : return a list of all functions<br>**pfonk(PBool)** : return the help for PBool   | Helper for functions |
| `pshort(short="")` | **short**: shortcut (default: "")<br>**pshort()** : return a list of all shortcuts  | Helper for shortcuts |
| `print_video()` | - | Helper for video player |
| `pgroup(pgroup="")` | **pgroup**: PGroup type (default: "") | Helper for PGroup |
| `chaos(chaosInt=1, plyrType=None)` | **chaosInt**: number of players (default: 1)<br>**plyrType**: player type (*synth*\|*loop*\|*drum*) (default: None) | Generates random players |
| `unsolo()` | - | Unsolos all solo players |
| `soloRnd(time=8, soloPlayer=None)` | **time**: modulo time (default: 8)<br>**soloPlayer**: player to solo (default: None) | Solo a random player at modulo time or can specify which one|
| `genArp(nbrseq=4, lengthseq=8)` | **nbrseq**: number of sequences (default: 4)<br>**lengthseq**: sequence length (default: 8) | Generates an arpeggio based on Markov chord progression |
| `masterAll(args=0, value=1)` | **args**: argument to modify (default: 0)<br>**value**: value to apply (default: 1)<br>**argsall**: additional arguments | Temporarily sets all player to specified FX, ex: `masterAll("lpf", 400)`, reset with `masterAll()` |
| `chrono()` | - | Initializes the crash panel chronometer |

## Pattern Functions (@loop_pattern_func)

| Function Call | Argument Description | Function Description | Example |
|---------------|---------------------|---------------------| --------------------|
| `PBin(number=0)` | **number**: number to convert (default: 0) | Returns a random binary pattern or converts number to binary pattern, if no number -> random | `d1 >> blip(dur=1/4, amp=PBin(909))` |
| `PSaw(n=16, inverse=0)` | **n**: number of parts (default: 16)<br>**inverse**: invert the wave (default: 0) | Returns values of one cycle of Saw wave split into 'n' parts | `d1 >> supersaw(oct=3, dur=1/4, lpf=200+PSaw(64)*3000)` |
| `PTime()` | - | Generates a pattern from the local machine time (number between 0 -9)| `d1 >> blip(PTime())` |
| `PTimebin()` | - | Generates a pattern of actual time converted to binary | `d1 >> blip(PTime(), amp=PTimebin())` |
| `PFrac(a=0.63, b=0.0, size=16, mapl=0, maph=1)` | **a**: fractional coefficient (default: 0.63)<br>**b**: fractional offset (default: 0.0)<br>**size**: pattern size (default: 16)<br>**mapl**: mapping min value (default: 0)<br>**maph**: mapping max value (default: 1) | Returns a pattern with fractional step | Better use Pfr() |
| `PFr(mapl=0, maph=1, seedFr=1664, size=16)` | **mapl**: mapping min value (default: 0)<br>**maph**: mapping max value (default: 1)<br>**seedFr**: random seed (default: 1664)<br>**size**: pattern size (default: 16) | Simplified version of PFrac | `s2 >> saw(dur=1/2, lpf=PFr(200, 4000, 404, 8), oct=3)` |
| `PDrum(style=None, pat='', listen=False, khsor='', duree=1/2, spl=0, charPlayer="d")` | **style**: drum style<br>**pat**: pattern (default: '')<br>**listen**: listen (default: False)<br>**khsor**: drum parameter (kickn, hihat, snare, openhat, rim) <br>**duree**: duration (default: 1/2)<br>**spl**: split (default: 0)<br>**charPlayer**: player character (default: "d") | Generates a drum pattern based on style | *Need a fix, not working* |
| `PBal(n, k, style=0, dur=0.25, start=0)` | **n**: number of pulses<br>**k**: total steps<br>**style**: rhythmic style variation (default: 0)<br>**dur**: base duration unit (default: 0.25)<br>**start**: rotation offset (default: 0) | Returns balanced rhythm durations | `j9 >> play("<x.><:>", dur=(1/2, PBal(5,16,2)))` |
| `PRy(total=16, div=4, restProb=0)` | **total**: total (default: 16)<br>**div**: division (default: 4)<br>**restProb**: rest probability (default: 0) | Generates a rhythm pattern | `j9 >> play("<x>", dur=PRy(8))` |

## Player Methods (@player_method)

| Method Call | Argument Description | Method Description | Example |
|-------------|---------------------|--------------------|---------------------|
| `.unison(unison=2, detune=0.125, analog=0)` | **unison**: number of voices (default: 2)<br>**detune**: detuning (default: 0.125)<br>**analog**: analog (default: 0) | Like spread(), but can specify number of voices | `s2 >> saw(dur=8, oct=3).unison(5, .25, 80)` |
| `.human(velocity=20, humanize=5, swing=0)` | **velocity**: velocity (default: 20)<br>**humanize**: humanization (default: 5)<br>**swing**: swing (default: 0) | Humanizes velocity, delay and adds swing in % | `j9 >> play("<x.><->").human(30, 20, 30)` |
| `.fill(mute_player=0, on=1)` | **mute_player**: player to mute (default: 0)<br>**on**: state (default: 1) | Adds a fill to a drum player | `w2 >> play("{tTmM}").fill()` |
| `.brk(multi=1, code="")` | **multi**: multiplier (default: 1)<br>**code**: additional code (default: "") | Turns loop into break beat (only with splitter player) | `j9 >> loop("break8", dur=8).brk(2, "hpf=400, room=0.7, mix=0.4")` |
| `.note(note=0)` | **note**: note (default: 0) | Sets the note of the player, useful for wavetable synth | `o4 >> wavetable("AKWF_0009", oct=3, dur=1/2, sample=8).note([var([0,-2],8),2,4,2])` |
| `.lclip(clip=0)` | **clip**: clip duration (default: 0) | Clips the loop player to a specific duration | `j9 >> loop("break8", dur=8).lclip([8, 4, 2, 1, 0.5, 0.25, 0.25])` |
| `.gtr(strings=1)` | **strings**: string number (default: 1) | Sets player to match guitar strings | `j2 >> pluck([0, 2, 3, [5,7]], dur=[1.5, 1/4, 1/4, 2], oct=4, drive=.5).gtr(1)` |
| `.chroma()` | - | Sets player to chromatic scale |
| `.porta(portDelay=0.5)` | **portDelay**: portamento delay (default: 0.5) | Adds a portamento effect |
| `.morph(other, prob=50)` | **other**: other player<br>**prob**: probability percentage (default: 50) | Randomly morphs some attributes between 2 players | `d1 >> blip(room=.9, mix=0.8, dur=4, rate=4, shape=.3)`<br>`d2 >> dbass(rate=.3, dur=1/2, room=.1, mix=.2, shape=.1).morph(d1)` |
| `.trim(length)` | **length**: length | Trims to length every pattern of player | `u2 >> pluck(P[0, 2, 4, 7, 7, 0, 0, 4], dur=[0.5,1,.5,2,4], oct=[3, 6, 3, 4, 4], ).unison(2).trim(2)` |
| `.end(length=8, duration=2)` | **length**: length (default: 8)<br>**duration**: duration (default: 2) | Amplifies at the end of length, for duration, play only at the end | `rk >> pluck(P[0, 2, 4, 7, 7, 0, 0], dur=1/4, oct=4).unison(2).end(8,2)` |
| `.switch(other, key, bypass=1)` | **other**: other player<br>**key**: attribute key<br>**bypass**: bypass (default: 1) | Switches the attribute of a player | `d1 >> blip(room=.9, mix=0.8, dur=4, rate=4, shape=.3)`<br>`d2 >> dbass(dur=1/2).switch(d1, "dur")` |
| `.clone(player)` | **player**: player to clone | Clones a player | `d1 >> blip(room=.9, mix=0.8, dur=4, rate=4, shape=.3)`<br>`d2 >> dbass(dur=1/2).clone(d1)` |
| `.once()` | - | Plays a player once and stops it | `j2 >> play("W").once()` |
| `.start(startBeat=8)` | **startBeat**: starting beat (default: 8) | Starts a player at a specific beat | `j2 >> play("W.").start(16)` |
| `.drummer(durloop=16, durPlyr=1/2)` | **durloop**: loop duration (default: 16)<br>**durPlyr**: player duration (default: 1/2) | Transforms the player into an automatic drummer | `j2 >> play().drummer()` |

## Pattern Methods (@PatternMethod)

| Method Call | Argument Description | Method Description | Example |
|-------------|---------------------|--------------------|---------------------|
| `.renv(nbr=1)` | **nbr**: number of inversions (default: 1) | Pattern chord inversion | `w2 >> pianovel([I, III.renv(1), IV.renv(2)], oct=5, dur=4)` |
| `.add(value)` | **value**: value to add | Pattern method add | `w2 >> pianovel([0,2,4,5], oct=4, dur=1/2).sometimes("degree.add", 4)` |
| `.mul(value)` | **value**: value to multiply | Pattern method mul | `w2 >> pianovel([0,2,4,5], oct=4, dur=1/2,lpf=400).sometimes("lpf.mul", 10)` |
| `.norm(mult=1)` | **mult**: multiplier (default: 1) | Returns the pattern with all values between 0 and 1*mult | `w2 >> pianovel(P[0,2,4,5].norm(), oct=4, dur=1/2)` |
| `.clamp(mini, maxi)` | **mini**: minimum value<br>**maxi**: maximum value | Returns the pattern with all values clamped to min-max |
| `.lmap(oMin, oMax)` | **oMin**: output min value<br>**oMax**: output max value | Returns the pattern mapped to min and max values | `w2 >> pianovel(P[0,.5, .8, 1].lmap(0,9), oct=4, dur=1/2)` |

## Pattern Generators

| Pattern | Description des arguments | Description de la classe |
|------------------|-----------|---------------------------|
| `PChain2(mapping)`  | **mapping** : mapping dictionary | Markov chain pattern generator |
| `PChords(chord=None)` | **chord** : chord (default: None) | Chords generator |
| `PGauss(mean=0, deviation=1)` | **mean** : mean (default: 0)<br>**deviation** : deviation (default: 1)| Return random values with Gaussian distribution |
| `PLog(mean=0, deviation=1)` | **mean** : mean (default: 0)<br>**deviation** : deviation (default: 1) | Return random values with Logarithmic distribution |
| `PTrir(low=0, high=8, mode=None)` | **low** : low value (default: 0)<br>**high** : high value (default: 8)<br>**mode** : mode (default: None) | Return random values with Triangular distribution|
| `PCoin(low=0, high=1, proba=0.5)` | **low** : low value (default: 0)<br>**high** : high value (default: 1)<br>**proba** : probability (default: 0.5)| Choose between 2 values with probability |
| `PChar(case=2, alpha=2)` | **case** : case type (default: 2)<br>**alpha** : alpha type (default: 2)| return random char |
| `PMarkov()` | - | PMarkov mod with probability |
| `PZero(size=2, offset=0)` | **size** : size of the pattern (default: 2)<br>**offset** : offset the 1 (défaut: 0) | Generate a pattern with a '1' and size-1 '0' |
| `PBool(pat1=P[0], pat2=P[0], operator=0)` | **pat1** : pattern 1 (default: P[0])<br>**pat2** : pattern 2 (default: P[0])<br>**operator** : 0 -> and, 1 -> or, 2 -> xor  (défaut: 0) | Binary operation between 2 patterns |
| `PMorse(text, point=1/4, tiret=3/4)` | text: text to convert<br>point: dot duration (default: 1/4)<br>tiret: dash duration (default: 3/4) | Converts a string to morse dot and dash values |

## Shortcut Variables (French Cut)

| Variable Name | Value | Description |
|---------------|-------|-------------|
| `é` | `linvar([0,1],[16,0])` | Linear rise over 16 beats |
| `é4` | `linvar([0,1],[4,0])` | Linear rise over 4 beats |
| `é8` | `linvar([0,1],[8,0])` | Linear rise over 8 beats |
| `é32` | `linvar([0,1],[32,0])` | Linear rise over 32 beats |
| `è` | `linvar([1,0],[16,0])` | Linear fall over 16 beats |
| `è4` | `linvar([1,0],[4,0])` | Linear fall over 4 beats |
| `è8` | `linvar([1,0],[8,0])` | Linear fall over 8 beats |
| `è32` | `linvar([1,0],[32,0])` | Linear fall over 32 beats |
| `ê` | `linvar([0,1],[16,16])` | Rise then fall over 32 beats |
| `ê4` | `linvar([0,1],[4,4])` | Rise then fall over 8 beats |
| `ê8` | `linvar([0,1],[8,8])` | Rise then fall over 16 beats |
| `ê32` | `linvar([0,1],[32,32])` | Rise then fall over 64 beats |
| `ù` | `PDur(var([4,PRand(8)],[6,2]), 8)` | Variable duration pattern |
| `ù3` | `PDur(var([3,PRand(8)],[6,2]), 8)` | Variable duration pattern on 3 |
| `ù5` | `PDur(var([5,PRand(8)],[6,2]), 8)` | Variable duration pattern on 5 |
| `à` | `PRand(10)` | Random number from 0 to 9 |
| `ç` | `PWhite(-1,1)` | Random float between -1 and 1 |
| `ç0` | `PWhite(0,1)` | Random float between 0 and 1 |

## Chord Variables

| Variable Name | Value | Description |
|---------------|-------|-------------|
| `circ5` | `(P[0:12]*7) % 12` | Circle of fifths |
| `circ5m` | `circ5.rotate(3)` | Minor circle of fifths |
| `Maj` | `P(0, 4, 7)` | Major chord |
| `Min` | `P(0, 3, 7)` | Minor chord |
| `Sus2` | `P(0, 2, 7)` | Sus2 chord |
| `Sus4` | `P(0, 5, 7)` | Sus4 chord |
| `Dim` | `P(0, 3, 6)` | Diminished chord |
| `Maj7` | `P(0, 4, 7, 11)` | Major 7 chord |
| `Aug` | `P(0, 4, 8)` | Augmented chord |
| `Six` | `P(0, 4, 7, 9)` | Sixth chord |

---