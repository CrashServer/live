SynthDef.new(\brown,
	{|amp=1, sus=1, pan=0, freq=440, vib=0, fmod=0, rate=0, bus=0, cutoff=2800, rq=0.8|
		var osc, env;
		freq = In.kr(bus, 1);
		freq = [freq, freq+fmod];
		osc = BrownNoise.ar();
		env=EnvGen.ar(Env.new([1, 1], [1, 1]), doneAction:1);
		osc=(osc * env);
		osc = RLPF.ar(osc, cutoff,rq);
		osc = Mix(osc) * 0.1;
		osc = Pan2.ar(osc * amp, pan);
		ReplaceOut.ar(bus, osc)}
	).add;
