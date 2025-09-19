synthDef.new(\a_poly,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,
	  distortion=8, cutoff=800, resonance=0.7, attack=0.01,
	  poly1=3, poly2=5, polyMix=0.5, chaos=0.1|

		var osc, env, filter, dist, polyGate1, polyGate2, combinedGate;
		var freqMod, rhythmicFilter;

		freq = In.kr(bus, 1);

		// Two polyrhythmic pulse trains
		polyGate1 = LFPulse.kr(poly1, width: 0.3);
		polyGate2 = LFPulse.kr(poly2, width: 0.2);

		// Combine polyrhythms
		combinedGate = (polyGate1 * (1 - polyMix)) + (polyGate2 * polyMix);

		// Add chaos/complexity
		combinedGate = combinedGate * (1 + (LFNoise1.kr(chaos * 10) * chaos));

		// Frequency modulation based on polyrhythm
		freqMod = combinedGate * 20; // Slight pitch bend on accents
		freq = [freq + freqMod, freq + fmod, freq * 1.005] * Line.ar(Rand(0.98,1.02),1,0.01);
		freq = freq / 4;

		// Oscillators with polyrhythmic width modulation
		osc = Mix([
			VarSaw.ar(freq, width: LFNoise1.ar(2).range(0.1, 0.9) * combinedGate.lag(0.1), mul: 0.6),
			Pulse.ar(freq * 0.5, width: (LFTri.ar(0.3).range(0.2, 0.8) * combinedGate), mul: 0.4),
			SinOsc.ar(freq * 2, mul: 0.2 * combinedGate.lag(0.05))
		]);

		// Polyrhythmic envelope
		env = EnvGen.ar(
			Env([0, 1, 0.9, 0.7, 0], [attack, 0.05, sus * 0.3, sus * 0.7]),
			gate: combinedGate > 0.3,
			doneAction: 0
		);

		// Distortion modulated by polyrhythm
		dist = (osc * (distortion + (combinedGate * 3))).tanh * 0.7;

		// Rhythmic filter modulation
		rhythmicFilter = cutoff * (1 + (combinedGate * 0.8) + (LFNoise1.ar(rate * 0.5) * 0.3));
		filter = RLPF.ar(dist, rhythmicFilter * env.pow(0.5), resonance + (combinedGate * 0.3));

		// Additional saturation
		filter = (filter * (1.5 + (combinedGate * 0.8))).softclip;

		// Final output with polyrhythmic amplitude
		osc = filter * env * amp * (0.5 + (combinedGate * 0.5)) * 0.3;

		// Polyrhythmic stereo movement
		osc = Pan2.ar(osc, pan + (combinedGate * LFNoise1.kr(1) * 0.2));

		ReplaceOut.ar(bus, osc)
	}
).add;
