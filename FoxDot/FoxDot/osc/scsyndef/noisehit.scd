// Industrial noise hit - brutal transient, texture tool
SynthDef.new(\noisehit,
	{|bus=0, amp=1, pan=0, freq=1000, decay=0.15, filter=4000, res=0.5,
	  comp=12, drive=5, type=0, sweep=0.5, crush=0|
		var sig, env, filterEnv, noises, filtered, compressed, final;

		// Envelopes
		env = EnvGen.ar(Env.perc(0.0002, decay, 1, -8), doneAction: 2);
		filterEnv = EnvGen.ar(Env.perc(0.0001, decay * sweep, 1, -6));

		// === NOISE SOURCES ===

		// Select noise type
		noises = Select.ar(type.round, [
			// Type 0: White noise burst
			WhiteNoise.ar,
			// Type 1: Pink noise - darker
			PinkNoise.ar * 1.5,
			// Type 2: Crackle - broken
			Crackle.ar(1.97),
			// Type 3: Dust - sparse
			Dust2.ar(20000) * 3
		]);

		// Add impulse for attack
		noises = noises + (Impulse.ar(0) * 5);

		// === FILTER ===

		// Sweeping filter
		filtered = RLPF.ar(noises,
			(filter * filterEnv + 200).clip(50, 18000),
			res.clip(0.1, 0.95)
		);

		// Parallel highpass for attack
		filtered = filtered + HPF.ar(noises * 0.5, 6000) * filterEnv;

		sig = filtered * env;

		// === DISTORTION ===

		// Bit crush if enabled
		sig = Select.ar(crush > 0, [
			sig,
			sig.round(2.pow(crush.neg * 4)) * 2
		]);

		// Multi-stage saturation
		sig = (sig * drive * 2).clip(-1, 1);
		sig = (sig * 1.5).tanh;
		sig = sig + ((sig * drive).fold(-0.8, 0.8) * 0.3);

		// === BRUTAL COMPRESSION ===

		compressed = Compander.ar(sig, sig,
			thresh: 0.01,
			slopeBelow: 2,
			slopeAbove: 1/comp,
			clampTime: 0.00001,
			relaxTime: 0.005,
			mul: comp * 2
		);

		// Second limiter
		compressed = Limiter.ar(compressed * 2, 0.95, 0.0002);

		// === EQ ===

		final = BPeakEQ.ar(compressed, freq, 0.5, 3);
		final = BHiShelf.ar(final, 8000, 1, 4);

		final = final * amp * 0.3;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
