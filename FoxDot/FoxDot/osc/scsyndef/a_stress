SynthDef.new(\a_stress,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,
	  filterFreq=1200, resonance=0.8, distortion=6, attack=0.01, release=0.1|
		var osc, env, filterEnv, filtered, dist;
		freq = In.kr(bus, 1);

		// Slight detuning for width - Justice often uses chorus-like effects
		freq = [freq, freq+fmod, freq*1.007, freq*0.996] * Line.ar(Rand(0.99,1.01),1,0.01);

		// Multiple detuned sawtooth oscillators - the foundation of Justice leads
		osc = Mix([
			Saw.ar(freq, mul: 0.7),
			Saw.ar(freq * 1.005, mul: 0.6),
			Saw.ar(freq * 0.995, mul: 0.6),
			Pulse.ar(freq * 0.5, width: 0.3, mul: 0.3) // Sub harmonic
		]);

		// Sharp, punchy envelope
		env = EnvGen.ar(Env([0, 1, 0.7, 0.4, 0],
			[attack, 0.05, sus * 0.6, release]), doneAction: 0);

		// Filter envelope - key to the Justice sound (filter opens with note)
		filterEnv = EnvGen.ar(Env([0.3, 1, 0.8, 0.5],
			[attack * 2, 0.1, sus * 0.9]), doneAction: 0);

		// Heavy saturation/distortion - Justice signature
		dist = (osc * distortion).tanh * 0.8;

		// The classic aggressive low-pass filter with high resonance
		filtered = RLPF.ar(dist,
			filterFreq * filterEnv * (1 + (LFNoise1.ar(rate) * 0.2)),
			resonance);

		// Additional character - slight bit reduction for digital edge
		filtered = Decimator.ar(filtered, 44100/2, bits: 10);

		// More saturation after filtering
		filtered = (filtered * 1.5).softclip;

		// Final output
		osc = filtered * env * amp * 0.4;

		// Stereo positioning with slight movement
		osc = Pan2.ar(osc, pan + (LFNoise1.ar(0.3) * 0.15));

		ReplaceOut.ar(bus, osc)
	}
).add;
