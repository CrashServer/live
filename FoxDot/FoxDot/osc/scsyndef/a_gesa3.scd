SynthDef.new(\a_gesa3,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1, bus=0, distortion=8, cutoff=600, complexity=0.5, probability=0.8, shuffle=0.2|
		var osc, env, filter, dist, rhythmSeq, gateSeq, ampMod, filterMod;
		freq = In.kr(bus, 1);

		freq = [freq, freq+fmod] * Line.ar(Rand(0.98,1.02),1,0.01);
		freq = freq / 4;

		// Complex probabilistic rhythm generation
		rhythmSeq = Dseq([1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1] *
			LFNoise0.kr(rate * 0.125).range(0.3, 1), inf);

		gateSeq = Demand.kr(
			Impulse.kr(rate * 4), 0,
			rhythmSeq * (LFNoise0.kr(rate * 0.25) > (1 - probability))
		);

		// Shuffle/swing timing
		gateSeq = Lag.kr(gateSeq, shuffle * 0.1);

		// Amplitude modulation based on rhythm
		ampMod = gateSeq * (1 + (LFNoise1.kr(rate) * complexity));

		// Filter modulation with complexity
		filterMod = LFNoise1.kr(rate * [0.5, 0.25, 0.125]).range(0.5, 1.5);

		// Main envelope
		env = EnvGen.ar(Env([0, 1, 0.8, 0.5, 0],
			[0.002, 0.02, sus * 0.3, sus * 0.7]), doneAction: 0);

		// Rhythmically modulated oscillators
		osc = Mix([
			VarSaw.ar(freq * [1, 1.005],
				width: LFTri.ar(rate * 0.5 * complexity).range(0.05, 0.95),
				mul: ampMod * 0.6),
			Pulse.ar(freq * 0.5,
				width: LFNoise1.kr(rate * complexity).range(0.1, 0.9),
				mul: ampMod * 0.5),
			// Rhythmic sub harmonics
			SinOsc.ar(freq * [0.5, 2],
				mul: [ampMod * 0.4, ampMod * 0.2])
		]);

		// Dynamic distortion
		dist = (osc * distortion * (1 + ampMod * 0.5)).fold(-0.7, 0.7);

		// Multi-stage filtering with rhythmic modulation
		filter = RLPF.ar(dist,
			cutoff * filterMod.sum * env.pow(0.3) * (1 + gateSeq),
			0.7 * (1 + ampMod * 0.3));

		// Rhythmic gating
		filter = filter * (0.2 + (gateSeq * 0.8));

		osc = filter * env * amp * 0.2;
		osc = Pan2.ar(osc, pan + (LFNoise1.kr(rate * 0.3) * 0.1));

		ReplaceOut.ar(bus, osc)
	}
).add;
