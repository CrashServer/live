SynthDef.new(\latoo,
	{|amp=1, sus=1, pan=0, freq=440, vib=0, fmod=0, rate=0, bus=0|
		var osc, env;
		freq = In.kr(bus, 1);
		freq = [freq, freq+fmod];
		osc = Latoocarfian2DN.ar(SampleRate.ir/4,SampleRate.ir, LFNoise2.kr(2.dup, 1.5, 1.5), d:LFNoise2.kr(2.dup, 0.5, 1.5),  mul:0.2);
		env=EnvGen.ar(Env.new([1, 1], [1, 1]), doneAction:1);
		osc=(osc * env);
		osc = Mix(osc) * 0.5;
		osc = Pan2.ar(osc * amp, pan);
		
		ReplaceOut.ar(bus, osc)}
	).add;