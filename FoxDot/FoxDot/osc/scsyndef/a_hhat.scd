SynthDef.new(\hhat,
	{|amp=1, pan=0, tone=8000, decay=0.1, metallic=1, distortion=2, open=0, bus=0|
		var hihat, env, noise, metallic_part, dist;

		// Envelope - sharp for closed, longer for open
		env = EnvGen.ar(Env([0, 1, 0.3, 0], [0.001, 0.01, decay + (open * 0.3)]), doneAction: 2);

		// Base noise components
		noise = Mix([
			BPF.ar(WhiteNoise.ar(), tone, 0.3, mul: env),
			BPF.ar(WhiteNoise.ar(), tone * 1.5, 0.2, mul: env * 0.7),
			HPF.ar(WhiteNoise.ar(), tone * 0.7, mul: env * 0.8)
		]);

		// Metallic component - ring modulation for that harsh metallic sound
		metallic_part = Mix([
			SinOsc.ar(tone * 0.8) * SinOsc.ar(tone * 1.1) * env * metallic * 0.4,
			SinOsc.ar(tone * 1.3) * SinOsc.ar(tone * 0.6) * env * metallic * 0.3,
			// Add some inharmonic frequencies for more metallic character
			SinOsc.ar(tone * 2.1) * env * metallic * 0.2
		]);

		// Combine components
		hihat = (noise + metallic_part) * 0.7;

		// Light distortion for grit
		dist = (hihat * distortion).tanh * 0.9;

		// EQ shaping
		dist = BPeakEQ.ar(dist, tone, 0.5, 2); // Emphasize main frequency
		dist = HPF.ar(dist, 4000); // Keep it bright

		// Add some saturation for French electro character
		hihat = (dist * 1.3).softclip * amp * 0.5;

		hihat = Pan2.ar(hihat, pan);
		ReplaceOut.ar(bus, hihat);
	}
).add;
