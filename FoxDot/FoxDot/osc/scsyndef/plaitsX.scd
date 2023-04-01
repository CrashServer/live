SynthDef.new(\plaitsX,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.0001, decay=0.01, rel=0.01, peak=1, level=0.8, cutoff=5800, rq=0.8, trigger=1,  bright=0.5, preset=0, porta=0, harm=0, timbre=0, morph=0, aux=1, fdecay=1|
var osc, env, engineArr, harmArr, timbreArr, morphArr, engine, harmP, timbreP, morphP, octArr, octdiv;
sus = sus * blur;
freq = In.kr(bus, 1);

		engineArr =
[0,1,0,2,2,0,2,4,5, 11, 8,8,8,8, 7];
		harmArr = [0.8,0.5,0.88,0.5,0.0,0.4,0,0.4,0.5, 0.3, 0.2,0.2,0.05,0.25, 0.5];
		timbreArr = [0.4,0.8,0.8,0.63,0.91,0.3,0.2,0.1,0, 0.5, 0.1,0.12,0.2,1.0, 0.5];
		morphArr = [0.2,0.5,0.85,0.8,0.91,0.75,1,0.6,0.45, 0.6, 1,0.67,0.7,1.0, 0.5];
		//octArr = [1,1,3,1,1,1,1,1,1];

		engine = Select.kr(preset, engineArr);
		harmP = Select.kr(preset, harmArr);
		timbreP = Select.kr(preset, timbreArr);
		morphP = Select.kr(preset, morphArr);
		//octdiv = Select.kr(preset, octArr);
//freq = freq/octdiv;
/*
		env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);*/
		env = EnvGen.ar(Env.adsr(atk, decay, 1, rel), timeScale: sus, doneAction: 2);
		osc = MiPlaits.ar(freq.cpsmidi, engine: engine, harm: harmP + harm, timbre: timbreP + timbre, morph: morphP + morph, fm_mod: porta, trigger: env, timb_mod: 0.5, morph_mod: 0.5, decay: sus*fdecay, lpg_colour: bright);

osc=(osc * env);
		osc = RLPF.ar(osc, cutoff, rq);
		osc = Select.ar(aux, [osc, osc[0]!2, osc[1]!2]);
		osc = Mix(osc*amp) * 0.2;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
