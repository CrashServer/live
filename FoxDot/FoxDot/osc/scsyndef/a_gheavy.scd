SynthDef.new(\a_gheavy,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, drive=12, cutoff=600, bitcrush=8|
		var osc, env, crushed, filtered;
		freq = In.kr(bus, 1);

		freq = [freq, freq+fmod] * Line.ar(Rand(0.95,1.05),1,0.02);
		freq = freq / 4;

		// Harsh sawtooth with sub
		osc = Mix([
			VarSaw.ar(freq, width: 0.1, mul: 0.8),
			VarSaw.ar(freq * 0.5, width: 0.8, mul: 0.6),
			Pulse.ar(freq * 1.5, width: 0.1, mul: 0.3)
		]);

		// Sharp envelope
		env = EnvGen.ar(Env([0, 1, 0.8, 0.6, 0],
			[0.005, 0.02, sus * 0.4, sus * 0.6]), doneAction: 0);

		// Extreme distortion
		osc = (osc * drive).fold(-0.8, 0.8);

		// Bit crushing for digital harshness
		crushed = Decimator.ar(osc, 44100/bitcrush, bits: 6);

		// Aggressive filtering
		filtered = RHPF.ar(crushed, 60, 0.5); // High-pass to clean up mud
		filtered = RLPF.ar(filtered, cutoff * env.pow(0.3), 0.8);

		osc = filtered * env * amp * 0.25;
		osc = Pan2.ar(osc, pan);

		ReplaceOut.ar(bus, osc)
	}
).add;
