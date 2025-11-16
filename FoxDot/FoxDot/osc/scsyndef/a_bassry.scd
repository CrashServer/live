SynthDef.new(\a_bassry,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1, bus=0, distortion=10, cutoff=700, resonance=0.6, pattern=0, swing=0.1|
		var osc, env, filter, dist, rhythmGate, rhythmEnv, patternTrig;
		freq = In.kr(bus, 1);

		freq = [freq, freq+fmod] * Line.ar(Rand(0.97,1.03),1,0.015);
		freq = freq / 4;

		// Rhythmic patterns - different triggers based on pattern parameter
		patternTrig = Select.kr(pattern, [
			// Pattern 0: Classic 4/4 with accents
			Impulse.kr(rate * [4, 4, 4, 4]) * [1, 0.3, 0.6, 0.8],

			// Pattern 1: Syncopated techno
			Impulse.kr(rate * [8, 8, 8, 8, 8, 8]) * [1, 0, 0.4, 0, 0.7, 0.3],

			// Pattern 2: Broken rhythm
			Impulse.kr(rate * [6, 6, 6]) * [1, 0.5, 0.8],

			// Pattern 3: Aggressive staccato
			Impulse.kr(rate * 16) * LFNoise0.kr(rate * 2).range(0, 1),

			// Pattern 4: French house style
			Impulse.kr(rate * [4, 4, 4, 4]) * [1, 0.2, 0.9, 0.4]
		]);

		// Add swing to the rhythm
		rhythmGate = Lag.kr(patternTrig.sum, swing);

		// Gate-controlled envelope that responds to rhythm
		rhythmEnv = EnvGen.kr(
			Env([0, 1, 0.7, 0], [0.01, 0.1, 0.3]),
			gate: rhythmGate > 0.1,
			levelScale: rhythmGate
		);

		// Main envelope
		env = EnvGen.ar(Env([0, 1, 0.8, 0.6, 0],
			[0.005, 0.03, sus * 0.4, sus * 0.6]), doneAction: 0);

		// Multi-oscillator with rhythmic modulation
		osc = Mix([
			VarSaw.ar(freq,
				width: LFTri.ar(rate * 0.25).range(0.1, 0.9) * rhythmEnv.lag(0.05),
				mul: 0.7),
			Pulse.ar(freq * 0.5,
				width: LFNoise1.kr(rate).range(0.2, 0.8),
				mul: 0.5 * rhythmEnv),
			SinOsc.ar(freq * 2, mul: 0.3 * rhythmEnv.pow(2))
		]);

		// Rhythmic filter modulation
		cutoff = cutoff * (1 + (rhythmEnv * 0.8));

		// Heavy distortion with rhythmic intensity
		dist = (osc * (distortion * (1 + rhythmEnv * 0.5))).tanh * 0.6;

		// Filtered with rhythmic resonance
		filter = RLPF.ar(dist,
			cutoff * env.pow(0.4),
			resonance * (1 + rhythmEnv * 0.3));

		// Additional rhythmic gating effect
		filter = filter * (0.3 + (rhythmEnv * 0.7));

		// Soft clipping and stereo processing
		osc = (filter * 1.4).softclip;
		osc = osc * env * amp * 0.25;

		// Rhythmic panning
		pan = pan + (LFNoise1.kr(rate * 0.5) * 0.15 * rhythmEnv);
		osc = Pan2.ar(osc, pan);

		ReplaceOut.ar(bus, osc)
	}
).add;
