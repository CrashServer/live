SynthDef.new(\a_vpad,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,
	  texture=0.8, granularity=0.6, cutoff=1000|
		var osc, env, textured, granular, filtered;
		freq = In.kr(bus, 1);

		// Complex, evolving oscillators
		osc = Mix([
			VarSaw.ar(freq * [1, 1.007, 0.993] *
				(1 + (LFNoise1.ar([0.3, 0.7, 1.1]) * 0.02)),
				width: LFNoise1.ar([2.1, 3.7]).range(0.2, 0.8), mul: 0.4),
			Pulse.ar(freq * [0.5, 0.503] *
				(1 + (LFNoise0.ar([0.1, 0.13]) * 0.01)),
				width: LFNoise1.ar([1.3, 2.7]).range(0.3, 0.7), mul: 0.3),
			// Granular-like textures
			SinOsc.ar(freq * (1 + LFNoise1.ar([4.1, 6.7]) * 0.1),
				LFNoise1.ar([8.3, 12.1]) * texture, mul: 0.3)
		]);

		// Evolving envelope
		env = EnvGen.ar(Env([0, 1, 0.9, 0.85, 0.6, 0],
			[0.8, 0.5, sus * 0.3, sus * 0.4, sus * 0.3]), doneAction: 0);

		// Granular texturing
		granular = osc * LFNoise0.ar(
			LFNoise1.ar(rate * 0.1).range(20, 200)
		).range(1 - granularity, 1);

		// Complex filtering
		filtered = BPF.ar(granular,
			cutoff * (1 + (LFNoise1.ar([0.07, 0.11]) * 0.5)),
			LFNoise1.ar(0.03).range(0.1, 0.6), mul: 0.6);
		filtered = filtered + RLPF.ar(granular, cutoff * 0.7, 0.4, mul: 0.4);

		osc = filtered * env * amp * 0.3;
		osc = Pan2.ar(osc, pan + (LFNoise1.ar([0.17, 0.23]) * 0.2));

		ReplaceOut.ar(bus, osc)
	}
).add;
