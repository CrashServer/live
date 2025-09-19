SynthDef.new(\daftLead,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,
	  cutoff=2000, resonance=0.6, filterEnv=0.8, drive=2|
		var osc, env, filter, filterFreq;
		freq = In.kr(bus, 1);

		freq = [freq, freq+fmod, freq*1.007] * Line.ar(Rand(0.99,1.01),1,0.01);

		// Classic sawtooth with slight detuning for width
		osc = Mix([
			VarSaw.ar(freq, width: 0.0, mul: 0.6),
			VarSaw.ar(freq * 1.005, width: 0.1, mul: 0.4),
			Pulse.ar(freq * 0.5, width: 0.5, mul: 0.2)
		]);

		// Punchy envelope
		env = EnvGen.ar(Env([0, 1, 0.7, 0.5, 0],
			[0.01, 0.1, sus * 0.3, sus * 0.6]), doneAction: 0);

		// Signature filter sweep
		filterFreq = cutoff * (1 + (filterEnv * env.pow(2))) *
			(1 + (LFTri.ar(rate * 0.3) * 0.4));

		// Warm drive before filtering
		osc = (osc * drive).tanh;
		filter = RLPF.ar(osc, filterFreq.clip(50, 8000), resonance);

		osc = filter * env * amp * 0.4;
		osc = Pan2.ar(osc, pan);

		ReplaceOut.ar(bus, osc)
	}
).add;
