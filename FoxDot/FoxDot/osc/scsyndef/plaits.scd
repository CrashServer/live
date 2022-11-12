SynthDef.new(\plaits,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.0001, decay=0.01, rel=0.01, peak=1, level=0.8, engine=0, harm=0.1, timbre=0.5, morph=0.5, cutoff=4800, rq=0.8, bright=0.8, trigger=1, porta=0, aux=0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);

		//env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
		env = EnvGen.ar(Env.adsr(atk, decay, 1, rel), timeScale: sus, doneAction: 2);
		osc = MiPlaits.ar(freq.cpsmidi, engine: engine.clip(0,15), harm: harm, timbre: timbre, trigger:env, morph: morph, fm_mod: porta, timb_mod: 0.5, morph_mod: 0.5, decay: sus, lpg_colour: bright);

osc=(osc * env);
		osc = RLPF.ar(osc, cutoff, rq);
		osc = Select.ar(aux, [osc, osc[0]!2, osc[1]!2]);
		osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
