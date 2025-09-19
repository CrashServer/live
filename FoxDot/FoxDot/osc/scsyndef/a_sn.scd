synthDef.new(\esn,
	{|amp=1, pan=0, freq=200, tone=1, snap=1, noise=1, distortion=4, bus=0|
		var snare, env, toneEnv, tonal, noisePart, dist;

		// Main envelope - sharp attack, medium decay
		env = EnvGen.ar(Env([0, 1, 0.6, 0.3, 0], [0.001, 0.01, 0.08, 0.15]), doneAction: 2);

		// Tone envelope for pitched component
		toneEnv = EnvGen.ar(Env([0, 1, 0.4, 0], [0.002, 0.03, 0.1]));

		// Tonal component
		tonal = Mix([
			SinOsc.ar(freq * EnvGen.ar(Env([2, 1, 0.8], [0.005, 0.02])), mul: toneEnv * tone),
			SinOsc.ar(freq * 1.6, mul: toneEnv * tone * 0.5),
			RLPF.ar(Saw.ar(freq * 0.5), freq * 4, 0.3, mul: toneEnv * 0.3)
		]);

		// Noise component - filtered for character
		noisePart = Mix([
			BPF.ar(WhiteNoise.ar(), 1200, 0.8, mul: noise * env),
			HPF.ar(WhiteNoise.ar(), 6000, mul: noise * env * 0.7),
			BPF.ar(PinkNoise.ar(), 400, 1.2, mul: noise * env * 0.6)
		]);

		// Snap/crack component
		noisePart = noisePart + (BPF.ar(WhiteNoise.ar(), 8000, 0.3) *
			EnvGen.ar(Env([0, 1, 0], [0.0005, 0.005])) * snap);

		// Combine components
		snare = (tonal + noisePart) * env;

		// Heavy distortion
		dist = (snare * distortion).fold(-0.7, 0.7) * 0.8;

		// EQ for punch
		dist = BPeakEQ.ar(dist, 200, 0.7, 2); // Body
		dist = BPeakEQ.ar(dist, 3000, 0.6, 3); // Crack
		dist = HPF.ar(dist, 60); // Clean up lows

		snare = dist * amp * 0.6;
		snare = Pan2.ar(snare, pan);
		ReplaceOut.ar(bus, snare);
	}
).add;
