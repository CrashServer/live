# Changelog CrashServer 

## Functions


### Global
  - play a text2Speech using system sound synthesis (need espeak-ng and mbrola voices), can also record to `/loop/voicetxt/` dir 
`Voice(text="", rate=100, amp=1.0, lang="fr", voice=0, pitch=0, octave=0, gap=0, record = "")`
  - send OSC text 
  - `random_bpm_var()` : change bpm randomly with var
  - `PDrum(sytle, pat, listen, khsor, duree, spl, charPlayer)` : generate a drum pattern style. Select with style and pattern, listen to hear it, khsor can replace kick/hihat/snare/openhat/rim character, change the duration, sample player and player prefix(duree, spl, charPlayer)
  - `darker()` : change scale to more darker
  - `lighter()` : change scale to more lighter
  - chord dictionnary : I, II, III, IV, V, VI, VII
  - `drop(playtime=14, droptime=2, nbloop=1)` : make a drop every 'playtime', during 'droptime', 'nbloop' times.
  - `drop_bpm(duree=32, nbr=0, end=4)` : create a drop bpm effect. duree: how long total, nbr: how many parts, end: drop duration to the end.
  - `chaos(n=1)` : generate n random player lines and copy to clipboard
  - `ascii_gen(text="", font=0)` : generate ascii text
  - `lost()` : return all attacks available
  - `attack("name", printOut=0) : copy to clipboard the attack "name", print the attack if printOut != 0
  - `print_synth(synth="")` : print the argument of the synth or list of synth if no name
  - `print_fx(fx="")` : print the argument of the fx or list of fx if no name
  - `print_sample(sample="")` : print the description of the sample or find the letter
  - `print_loops(loop="")` : print the all available loop or list of loop for directory name
  - unsolo() : remove all solo on players
  
  - 

### Var
  - `lininf(start=0, finish=1, time=32)` : linvar but stay at finish
  - `expinf(start=0, finish=1, time=32)` : same but exponential 
  - `linbpm(endBpm=170, durBpm=128)` : linvar from actual bpm to endBpm in durBpm beats, use with `Clock.bpm = linbpm(220, 32)` 
  - 

### Player Method
  - `.unison(voices, detune, analog)` , analog to add more random detuning
  - `.human(velocity=20, humanize=5, swing=0)` // humanize the amp, delay (humanize or swing) in % (less to more)  
  - `.fill(mute_player=0, on=1)` // add fill to a player (like a drum fill). 1st parameter is the player you will mute during the fill (optional and can be a group like Group(p1,p2,p3)). The `on` argument is the way 0: off, 1: random (dur & amp), 2: random dur & amp=1, 3: random amplify & dur=1/2
  - `.brk(multi=1, code="")` , break beat a loop by adding a second player called z* . multiply the duration with multi, you can also add parameters to the second player (the z*) with code="shape=.4, echo=[0,0.5]). Stop with `.brk(0)`
  - `.switch(other, key, bypass)` : swith(exchange)  the attr of a player, ex: `b2 >> blip(-2, amp=1).switch(b1, "degree")`
  - `.clone(player)` : clone a player , all his attributes
  - `.once()` : play a player only once. 
  - `.drummer(duration=16, dur=1/2)` : turn a sample player to a human drummer. 'duration' is the time for a new drum pattern, `dur` is the duration of the player.
  - `basser(duration=64, markdur=2)`: turn a synth player to a bass player. 'duration' is the time for a new pattern, markdur is the length of the pattern
  -  `.gtr(string=1)` : set player to match guitar tabs
  -  `.chroma()` : set player to chromatic scale
  -  

### Pattern Method
  - `.renv(nbr=1)` : chord inversion, ex `P(0,2,4).renv(1)`
  - `.add(value)` : like '+', but can be used with .sometimes("degree.add", 2)
  - `.mul(value)` : like 'x', but can be used with .sometimes("degree.mul", 2)
  - `.norm(mult=1)` : normalize the pattern with all values between 0 and mult.
  - `.clamp(mini, maxi)` : return the pattern with all valuers clamped to min - max
  - `.lmap(min, max)` : remap the pattern to values between min - max
   
  
### Pattern Generator
  - `.rnd()` : Round generator pattern to the nearest value with `.rnd(0.5)` , ex: `PWhite(0,4).rnd(0.25)` [Pattern/Main.py modification]
  - `PBin(number=0)`: generate a list of binary based on number. If number=0, generate a random number
  - `PSaw(n=16, inverse=0)` : like PSine() but with a Saw wave, can be inverted
  - `PTime()` : generate a pattern from local machine time 
  - `PTimebin()` : same as PTime but in binary
  - `PFrac(a=0.63, b=0.0, size=16, mapl=0, maph=1)` : generate a `size` lenght pattern with fractional step based on `a` & `b`. Can be mapped between low and high with `mapl` and `maph.
  - `PChords()` : generate a chord sequence 
  - `PGauss(mean=0, deviation=1)` : generate random values using Gaussian distrib
  - `PLog(mean=0, deviation=1)` : generate random values using Logarithmic distrib
  - `PTrir(low=0, high=8, mode=None)` : generate random values using triangular distrib
  - `PCoin(low=0, high=1, proba=0.5)` : generate values low or high with proba (more proba = more high)
  - `PChar(case=2, alpha=2)` : generate random characters, case{0: lowercase, 1: uppercase, 2: both}, alpha{0: alpha, 1: nonalpha, 2: both}
  - `PMarkov()` : generate chords with a Markov chain 3rd order dictionnary based on most popular chords progression. 
  - `Pzero(size, offset)` : generate a pattern starting with 1 and (size-1) zero, the 1 can be offseted
  - `PBool(pat1, pat2, operator)` : binary operation between two patterns, operator{0: and, 1: or, 2: xor}
  - `melody(scale_melody, melody_dict)` : generate melody based on a markov chain dict of popular melodies
  - `PRy(duration=16, div=4, restprob=0.3)` : generate rythmique duration for a total time of 'duration' in 'div' parts with a probability to have a rest of 'restprob'.
  - `PArp(pattern, index)` : turn the pattern to arppegiator, index select the type of arp
  - `PMorse(text, point=1/4, tiret=3/4)` : convert a string to Morse code with values of point and tiret.
  - 

## FX

## Synth

