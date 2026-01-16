// Acid line - 303 style, reliable
SynthDef.new(\acidline,
	{|bus=0, amp=1, pan=0, freq=440, fmod=0, sus=0.3, atk=0.001, rel=0.1,
	  cutoff=1000, res=0.6, drive=2, accent=0, slide=0|
		var sig, env, filterEnv, osc, filtered, final;

		freq = In.kr(bus, 1);
		freq = freq / 2;

		// Amp envelope
		env = EnvGen.ar(
			Env.perc(atk, sus + rel, 1, -6),
			doneAction: 2
		);

		// Filter envelope - accent affects intensity
		filterEnv = EnvGen.ar(Env.perc(0.001, sus * 0.5, 1 + accent, -8));

		// Saw oscillator
		osc = LFSaw.ar(freq);

		// Add some harmonics
		osc = osc + (LFPulse.ar(freq, width: 0.5).bipolar * 0.3);

		// Pre-filter drive
		osc = (osc * (1 + drive * 0.5)).tanh;

		// Resonant filter - the acid sound
		filtered = RLPF.ar(osc,
			(cutoff * (1 + (filterEnv * 3))).clip(50, 15000),
			res.clip(0.05, 0.95)
		);

		// Post-filter saturation
		filtered = (filtered * drive).tanh;

		// Compression
		filtered = Compander.ar(filtered, filtered,
			thresh: 0.1, slopeBelow: 1, slopeAbove: 0.3,
			clampTime: 0.001, relaxTime: 0.03, mul: 2
		);

		final = Limiter.ar(filtered, 0.9, 0.001);
		final = final * env * amp * 0.5;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
