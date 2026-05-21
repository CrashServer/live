SynthDef.new(\wavetable,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=1.0, buf=0, degree=0, sample=0, detune=0.2, wtpos=0, cutoff=8000, rq=0.8, wtdist=0, wtsync=0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = freq/2;
detune = 1 + (detune/100);
		osc = MultiWtOsc.arOscs(freq: freq, wtPos: Select.ar(K2A.ar((rate > 0)), [K2A.ar(wtpos), LFTri.ar(1 / (sus * rate) * 0.5, 0).range(wtpos,255)]), squeeze: wtdist, wtOffset: 0, bufnum: buf, wtSize: 2048, numTables: 8, ratio: 2, numOscs: 5, detune: detune, interpolation: 2, hardSync: 0, phaseMod: 0);
env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 2);
osc = osc * env * 0.5;
osc = HPF.ar(osc, 20);
osc = RLPF.ar(osc, cutoff, rq);
osc = LeakDC.ar(osc);
osc=(osc * amp);
osc = Splay.ar(osc, level:1,spread:wide, center:pan, levelComp: true);
	ReplaceOut.ar(bus, osc)},
metadata: (
credit: "CrashServer",
description: "",
category: \sample,
tags: []
)).add;
