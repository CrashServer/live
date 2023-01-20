# Changelog CrashServer 

## Functions


### Global
  - play a text2Speech using system sound synthesis (need espeak-ng and mbrola voices), can also record to `/loop/voicetxt/` dir 
`Voice(text="", rate=100, amp=1.0, lang="fr", voice=0, pitch=0, octave=0, gap=0, record = "")`
  - send OSC text 
  - `random_bpm_var()` : change bpm randomly with var
  -  

### Generator Pattern
  - Round generator pattern to the nearest value with `.rnd(0.5)` , ex: `PWhite(0,4).rnd(0.25)` [Pattern/Main.py]
  -  

### Player Method
  - `.unison(voices, detune, analog)` , analog to add more random detuning
  - `.human(velocity=20, humanize=5, swing=0)` // humanize the amp, delay (humanize or swing) in % (less to more)  
  - `.fill(mute_player=0, on=1)` // add fill to a player (like a drum fill). 1st parameter is the player you will mute during the fill (optional and can be a group like Group(p1,p2,p3)). 
    The `on` argument is the way 0: off, 1: random (dur & amp), 2: random dur & amp=1, 3: random amplify & dur=1/2
  - `.brk(multi=1, code="")` , break beat a loop by adding a second player called z* . multiply the duration with multi, you can also add parameters to the second player (the z*) with code="shape=.4, echo=[0,0.5]). Stop with `.brk(0)`

### Pattern Method
  - `renv(nbr=1)` : chord inversion, ex `P(0,2,4).renv(1)`
  
### Pattern Generator
  - `PBin(number=0)`: generate a list of binary based on number. If number=0, generate a random number
  - `PSaw(n=16, inverse=0)` : like PSine() but with a Saw wave, can be inverted
  - `PTime()` : generate a pattern from local machine time 
  - `PTimebin()` : same as PTime but in binary
  - `PFrac(a=0.63, b=0.0, size=16, mapl=0, maph=1)` : generate a `size` lenght pattern with fractional step based on `a` & `b`. Can be mapped between low and high with `mapl` and `maph.
  -   


## FX

## Synth

