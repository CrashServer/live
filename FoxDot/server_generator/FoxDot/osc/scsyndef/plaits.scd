SynthDef.new(\plaits,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.0001, decay=0.01, rel=0.01, peak=1, level=0.8, engine=0, harm=0.1, timbre=0.5, morph=0.5|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
		osc = MiPlaits.ar(freq.cpsmidi, engine: engine.clip(0,15), harm: harm, timbre: timbre, morph: morph, fm_mod: fmod);
env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;