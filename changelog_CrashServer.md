# Changelog CrashServer 

## Functions


### Global
  - play a text2Speech using system sound synthesis (need espeak-ng and mbrola voices), can also record to `/loop/voicetxt/` dir 
`Voice(text="", rate=100, amp=1.0, lang="fr", voice=0, pitch=0, octave=0, gap=0, record = "")`

  - send OSC text 
  - `random_bpm_var()` : change bpm randomly with var
  - mod `.unison(voices, detune, analog)` to add more random detuning
  - `.human(velocity=20, humanize=5, swing=0)` 
  - 

### Generator Pattern
  - Round generator pattern to the nearest value with `.rnd(0.5)` , ex: `PWhite(0,4).rnd(0.25)` [Pattern/Main.py]
  -  

## FX

## Synth

