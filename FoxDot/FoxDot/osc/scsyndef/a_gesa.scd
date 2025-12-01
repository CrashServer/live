SynthDef.new(\a_gesa,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,
	  distortion=8, cutoff=800, resonance=0.7, attack=0.01|
		var osc, env, filter, dist;
		freq = In.kr(bus, 1);

		// Slight frequency modulation and detuning for width
		freq = [freq, freq+fmod, freq*1.005] * Line.ar(Rand(0.98,1.02),1,0.01);
		freq = freq / 4; // Sub bass range

		// Multi-oscillator approach - sawtooth + square for aggression
		osc = Mix([
			VarSaw.ar(freq, width: LFNoise1.ar(2).range(0.1, 0.9), mul: 0.6),
			Pulse.ar(freq * 0.5, width: LFTri.ar(0.3).range(0.2, 0.8), mul: 0.4),
			SinOsc.ar(freq * 2, mul: 0.2) // Harmonic for punch
		]);

		// Aggressive envelope with quick attack and controlled sustain
		env = EnvGen.ar(Env([0, 1, 0.9, 0.7, 0],
			[attack, 0.05, sus * 0.3, sus * 0.7]), doneAction: 0);

		// Heavy distortion - key to Gesaffelstein sound
		dist = (osc * distortion).tanh * 0.7;

		// Aggressive low-pass filtering with resonance
		filter = RLPF.ar(dist,
			cutoff * (1 + (LFNoise1.ar(rate * 0.5) * 0.3)) * env.pow(0.5),
			resonance);

		// Additional saturation and bite
		filter = (filter * 1.5).softclip;

		// Final shaping
		osc = filter * env * amp * 0.3;

		// Slight stereo widening
		osc = Pan2.ar(osc, pan + (LFNoise1.ar(0.5) * 0.1));

		ReplaceOut.ar(bus, osc)
	}
).add;
