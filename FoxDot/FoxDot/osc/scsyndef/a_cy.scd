SynthDef.new(\a_cy,
	{|amp=1, pan=0, decay=2, bright=1, distortion=1.5, bus=0|
		var crash, env, noise, metallic, dist;

		// Long decay envelope
		env = EnvGen.ar(Env([0, 1, 0.7, 0.3, 0], [0.01, 0.1, decay * 0.5, decay * 0.5]), doneAction: 2);

		// Complex noise structure
		noise = Mix([
			BPF.ar(WhiteNoise.ar(), 6000, 0.1, mul: env),
			BPF.ar(WhiteNoise.ar(), 12000, 0.2, mul: env * 0.8),
			HPF.ar(WhiteNoise.ar(), 8000, mul: env * bright)
		]);

		// Metallic resonances
		metallic = Mix([
			SinOsc.ar(1200) * SinOsc.ar(1800) * env * 0.3,
			SinOsc.ar(2400) * SinOsc.ar(3200) * env * 0.2,
			SinOsc.ar(4800) * SinOsc.ar(6400) * env * 0.15
		]);

		crash = (noise + metallic) * 0.6;

		// Gentle distortion
		dist = (crash * distortion).tanh;

		// EQ for sparkle
		dist = BPeakEQ.ar(dist, 10000, 0.3, bright * 2);
		dist = HPF.ar(dist, 3000);

		crash = dist * amp * 0.4;
		crash = Pan2.ar(crash, pan);
		ReplaceOut.ar(bus, crash);
	}
).add;
