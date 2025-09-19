SynthDef.new(\xbass,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,
		distortion=8, cutoff=800, resonance=0.7, attack=0.01,
		rhythmType=0, tempo=120, accent=0.5|

		var osc, env, filter, dist, rhythmGate, accentMod;
		var punkRhythm, mathRhythm1, mathRhythm2, mathRhythm3;
		var selectedRhythm, beatRate;

		freq = In.kr(bus, 1);
		beatRate = tempo / 60; // Convert BPM to Hz

		// RHYTHMIC PATTERNS
		// Punk pattern - fast 8th notes with accents
		punkRhythm = Demand.kr(
			Impulse.kr(beatRate * 2), // 8th note trigger
			0,
			Dseq([1, 0.6, 0.8, 1, 0.7, 1, 0.6, 0.9], inf) // Accent pattern
		);

		// Math rock pattern 1 - 7/8 time with irregular accents
		mathRhythm1 = Demand.kr(
			Impulse.kr(beatRate * 2.286), // Slightly irregular timing
			0,
			Dseq([1, 0.5, 0.8, 0.3, 1, 0.6, 0.4], inf)
		);

		// Math rock pattern 2 - Complex polyrhythm
		mathRhythm2 = Demand.kr(
			Impulse.kr(beatRate * 1.6), // 5/4 feel
			0,
			Dseq([1, 0.4, 0.7, 0.6, 0.9, 0.3, 0.8, 0.5, 1, 0.4], inf)
		);

		// Math rock pattern 3 - Angular with odd groupings
		mathRhythm3 = Demand.kr(
			Impulse.kr(beatRate * 2.67), // Triplet-based
			0,
			Dseq([1, 0.8, 0.3, 0.6, 0.9, 0.4, 0.7, 0.5, 1, 0.3, 0.8], inf)
		);

		// Select rhythm pattern based on rhythmType parameter
		selectedRhythm = Select.kr(rhythmType, [
			punkRhythm,
			mathRhythm1,
			mathRhythm2,
			mathRhythm3
		]);

		// Create rhythmic gate with accents
		rhythmGate = selectedRhythm * (1 + (accent * LFNoise1.kr(beatRate * 0.5)));

		// Apply slight timing variations for humanization
		rhythmGate = rhythmGate * LFNoise1.kr(beatRate * 0.1).range(0.95, 1.05);

		// Frequency modulation and detuning
		freq = [freq, freq+fmod, freq*1.005] * Line.ar(Rand(0.98,1.02),1,0.01);
		freq = freq / 4; // Sub bass range

		// Multi-oscillator approach with rhythmic modulation
		osc = Mix([
			VarSaw.ar(freq, width: LFNoise1.ar(2).range(0.1, 0.9), mul: 0.6),
			Pulse.ar(freq * 0.5, width: LFTri.ar(0.3).range(0.2, 0.8), mul: 0.4),
			SinOsc.ar(freq * 2, mul: 0.2) // Harmonic for punch
		]);

		// Rhythmic envelope that responds to the pattern
		env = EnvGen.ar(
			Env([0, 1, 0.9, 0.7, 0], [attack, 0.05, sus * 0.3, sus * 0.7]),
			gate: rhythmGate > 0.1, // Only trigger when rhythm is active
			doneAction: 0
		);

		// Accent-based amplitude modulation
		accentMod = rhythmGate.lag(0.01); // Smooth the rhythmic changes

		// Heavy distortion modulated by rhythm
		dist = (osc * (distortion + (accentMod * 2))).tanh * 0.7;

		// Aggressive low-pass filtering with rhythmic modulation
		filter = RLPF.ar(dist,
			cutoff * (1 + (LFNoise1.ar(rate * 0.5) * 0.3) + (accentMod * 0.5)) * env.pow(0.5),
			resonance + (accentMod * 0.2));

		// Additional saturation and bite
		filter = (filter * (1.5 + (accentMod * 0.5))).softclip;

		// Final shaping with rhythmic amplitude
		osc = filter * env * amp * accentMod * 0.3;

		// Rhythmic panning for math rock feel
		pan = pan + (LFNoise1.kr(beatRate * 0.25) * 0.1 * (rhythmType > 0));
		osc = Pan2.ar(osc, pan);

		ReplaceOut.ar(bus, osc)
	}
).add;
