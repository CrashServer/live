SynthDef(\fm, { arg bus = 0, freq = 440, index = 3, amp=1, pan=0, sus=0, level=1, atk=0.5, gate=1, fmod=0;
	var mod, car, env, osc;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod] * Line.ar(Rand(0.5,1.5),1,0.02);
	mod = SinOsc.ar(freq * 1,0,freq * index);
	osc = SinOsc.ar((freq * 2) + mod, 4);
	osc = osc + (Mix.arFill(7, { CombL.ar(osc, 0.005, 0.15, 0.15) })/2);
	env=EnvGen.ar(Env([0,1,0.8,0.8,0], [0.02, 0.01, sus/2, sus/2]), doneAction: 0);
	osc=(osc * env);
	osc = Mix(osc) * 1/32;
	osc = Pan2.ar(osc * amp, pan);
	ReplaceOut.ar(bus, osc)}).add;