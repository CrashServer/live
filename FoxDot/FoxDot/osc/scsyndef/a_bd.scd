SynthDef.new(\edb,
	{|amp=1, pan=0, freq=60, click=1, punch=1, sub=1, distortion=3, bus=0|
		var kick, env, clickEnv, subEnv, punchy, dist;

		// Main kick envelope - sharp attack, controlled decay
		env = EnvGen.ar(Env([0, 1, 0.7, 0.3, 0], [0.002, 0.01, 0.1, 0.3]), doneAction: 2);

		// Click envelope for attack transient
		clickEnv = EnvGen.ar(Env([0, 1, 0], [0.001, 0.01]));

		// Sub envelope for low-end thump
		subEnv = EnvGen.ar(Env([0, 1, 0.8, 0], [0.005, 0.05, 0.4]));

		// Multi-component kick
		kick = Mix([
			// Main body - pitch envelope
			SinOsc.ar(freq * EnvGen.ar(Env([3, 1, 0.7, 0.5], [0.002, 0.02, 0.2])), mul: env),

			// Click component for punch
			LPF.ar(WhiteNoise.ar(click * clickEnv), 3000) * 0.3,

			// Sub component
			SinOsc.ar(freq * 0.5 * EnvGen.ar(Env([2, 1], [0.01])), mul: subEnv * sub),

			// Punch/body resonance
			RLPF.ar(Impulse.ar(0), freq * 2, 0.5, mul: punch * env * 0.4)
		]);

		// Heavy distortion - signature of French electro
		dist = (kick * distortion).tanh * 0.8;

		// EQ shaping
		dist = BPeakEQ.ar(dist, 80, 0.8, 3); // Boost low-mids
		dist = BPeakEQ.ar(dist, 2000, 0.5, 2); // Slight high-mid boost

		// Soft limiting
		kick = (dist * 1.2).softclip * amp * 0.7;

		kick = Pan2.ar(kick, pan);
		ReplaceOut.ar(bus, kick);
	}
).add;
