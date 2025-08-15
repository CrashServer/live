SynthDef.new(\guit,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.0001, decay=0.01, rel=0.01, peak=1, level=1, detune=0.01, tone=0.7, beef=0.7, fdecay=1, mod=0.2|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
		env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
		osc = MiPlaits.ar(freq.cpsmidi, engine: 11, harm: detune, timbre: tone, trigger:env, morph: beef, fm_mod: 0, timb_mod: mod, morph_mod: 1, decay: sus*fdecay, lpg_colour: 1.0);

		osc=(osc * env);
		osc = Mix(osc[0]!2)* amp * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
