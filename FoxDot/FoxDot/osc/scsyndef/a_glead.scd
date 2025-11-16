SynthDef.new(\a_glead,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, distortion=6, cutoff=1200, bitcrush=4, chaos=0.3|
		var osc, env, crushed, filtered, noise;
		freq = In.kr(bus, 1);

		freq = [freq, freq+fmod] * Line.ar(Rand(0.97,1.03),1,0.02);

		// Harsh oscillators with chaos
		osc = Mix([
			VarSaw.ar(freq * [1, 1.01], width: LFNoise1.ar(8).range(0.0, 0.3), mul: 0.7),
			Pulse.ar(freq * 0.5, width: LFNoise0.ar(12).range(0.1, 0.9), mul: 0.4),
			// Chaotic FM component
			SinOsc.ar(freq * 1.5, SinOsc.ar(freq * 3.7) * chaos, mul: 0.3)
		]);

		// Aggressive envelope
		env = EnvGen.ar(Env([0, 1, 0.9, 0.4, 0],
			[0.005, 0.03, sus * 0.2, sus * 0.8]), doneAction: 0);

		// Heavy distortion and bit crushing
		osc = (osc * distortion).fold(-0.7, 0.7);
		crushed = Decimator.ar(osc, 44100/bitcrush, bits: 8);

		// Harsh filtering with movement
		filtered = RHPF.ar(crushed, 80, 0.7); // Clean up low end
		filtered = RLPF.ar(filtered,
			cutoff * (1 + (LFNoise1.ar(rate) * 0.5)) * env.pow(0.4), 0.9);

		osc = filtered * env * amp * 0.3;
		osc = Pan2.ar(osc, pan + (LFNoise1.ar(3) * 0.2));

		ReplaceOut.ar(bus, osc)
	}
).add;
