SynthDef.new(\war,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, beef=8, cutoff=800, rq=0.7, attack=0.01|
		var osc, env, filter, dist;
		freq = In.kr(bus, 1);
		freq = [freq, freq+fmod, freq*1.005] * Line.ar(Rand(0.98,1.02),1,0.01);
		freq = freq / 4; 
		osc = Mix([
			VarSaw.ar(freq, width: LFNoise1.ar(2).range(0.1, 0.9), mul: 0.6),
			Pulse.ar(freq * 0.5, width: LFTri.ar(0.3).range(0.2, 0.8), mul: 0.4),
			SinOsc.ar(freq * 2, mul: 0.2) 
		]);
		env = EnvGen.ar(Env([0, 1, 0.9, 0.7, 0],
			[attack, 0.05, sus * 0.3, sus * 0.7]), doneAction: 0);
		dist = (osc * beef).tanh * 0.7;
		filter = RLPF.ar(dist,
			cutoff * (1 + (LFNoise1.ar(rate * 0.5) * 0.3)) * env.pow(0.5),
			rq);
		filter = (filter * 1.5).softclip;
		osc = filter * env * amp * 0.3;
		osc = Pan2.ar(osc, pan + (LFNoise1.ar(0.5) * 0.1));
		ReplaceOut.ar(bus, osc)
	}
).add;