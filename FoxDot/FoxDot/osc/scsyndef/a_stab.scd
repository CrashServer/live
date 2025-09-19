SynthDef.new(\a_stab,
	{|amp=1, sus=0.3, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,
	  filterFreq=1000, resonance=0.7, distortion=5|
		var osc, env, filterEnv, filtered, chord;
		freq = In.kr(bus, 1);

		// Chord intervals (root, third, fifth, octave)
		chord = [freq, freq * 1.25, freq * 1.5, freq * 2];

		// Detuned sawtooth chord
		osc = Mix(chord.collect({|f|
			Mix([
				Saw.ar([f, f*1.003], mul: 0.15),
				Pulse.ar(f * 0.5, width: 0.2, mul: 0.1)
			])
		}));

		// Sharp stab envelope
		env = EnvGen.ar(Env([0, 1, 0.3, 0], [0.005, 0.1, sus]), doneAction: 0);

		// Filter envelope
		filterEnv = EnvGen.ar(Env([0.5, 1, 0.2], [0.01, sus * 0.9]), doneAction: 0);

		// Heavy distortion
		osc = (osc * distortion).tanh;

		// Aggressive filtering
		filtered = RLPF.ar(osc, filterFreq * filterEnv, resonance);

		osc = filtered * env * amp * 0.3;
		osc = Pan2.ar(osc, pan);

		ReplaceOut.ar(bus, osc)
	}
).add;
