# WaveTable player and howto use wavetable files

## Pre-requisites
- wavetable files
- waetable quarks (ddwWaveTableSynth) available in supercollider

## Download wavetable files

usefull links:
- [carvetoy](https://www.carvetoy.online/q?sort=relevance)
-

Download as a single file.

## Convert wave

Use the wavetable quark to convert the wavetable file to a format that can be used in supercollider.

```C
w = WavetablePrep("/path/to/the/sample/mywavetable.wav".standardizePath);

w.read(action: { "done".postln });

w.tables.size

w.write("/path/to/loop/WT_Bass/test-wt.wav");
```

Make sure to save to the sample librairy folder and start the folder with `WT_`.


## use in Foxdot

```python
j8 >> wavetable("WT_Bass",degree=P[-2,2,4], oct=4, rate=0.10, wtpos=0, sample=0, detune=0.1, dur=8, cutoff=1800, rq=0.5, wtdist=0).unison(3)
```
