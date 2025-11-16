SynthDef.new(\a_daft,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, cutoff=300, resonance=0.8, punch=1.2|
		var osc, env, filtered;
		freq = In.kr(bus, 1);

		freq = [freq, freq+fmod] * Line.ar(Rand(0.99,1.01),1,0.01);
		freq = freq / 4; // Sub bass range

		// Punchy bass oscillators
		osc = Mix([
			VarSaw.ar(freq, width: 0.0, mul: 0.6),
			VarSaw.ar(freq * 1.005, width: 0.2, mul: 0.4),
			Pulse.ar(freq * 2, width: 0.5, mul: 0.2)
		]);

		// Punchy envelope with quick attack
		env = EnvGen.ar(Env([0, 1, 0.8, 0.6, 0],
			[0.005, 0.02, sus * 0.3, sus * 0.7]), doneAction: 0);

		// Signature filter funk
		osc = (osc * punch).softclip;
		filtered = RLPF.ar(osc,
			cutoff * (1 + (env.pow(3) * 2)) *
			(1 + (LFTri.ar(rate * 0.5) * 0.3)),
			resonance);

		osc = filtered * env * amp * 0.4;
		osc = Pan2.ar(osc, pan);

		ReplaceOut.ar(bus, osc)
	}
).add;
