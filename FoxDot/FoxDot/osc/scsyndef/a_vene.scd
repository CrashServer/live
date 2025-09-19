SynthDef.new(\a_vene,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,
	  distortion=10, cutoff=500, bitcrush=6, sub=0.4|
		var osc, env, crushed, filtered;
		freq = In.kr(bus, 1);

		freq = [freq, freq+fmod] * Line.ar(Rand(0.97,1.03),1,0.02);
		freq = freq / 4;

		// Aggressive multi-layered bass
		osc = Mix([
			VarSaw.ar(freq, width: 0.1, mul: 0.7),
			VarSaw.ar(freq * 0.5, width: 0.8, mul: 0.5),
			Pulse.ar(freq * 1.5, width: 0.1, mul: 0.4),
			// Deep sub component
			SinOsc.ar(freq * 0.25, mul: sub)
		]);

		// Sharp, aggressive envelope
		env = EnvGen.ar(Env([0, 1, 0.8, 0.5, 0],
			[0.003, 0.01, sus * 0.4, sus * 0.6]), doneAction: 0);

		// Extreme processing
		osc = (osc * distortion).fold(-0.8, 0.8);
		crushed = Decimator.ar(osc, 44100/bitcrush, bits: 6);

		// Aggressive filtering
		filtered = RHPF.ar(crushed, 50, 0.5);
		filtered = RLPF.ar(filtered, cutoff * env.pow(0.2), 0.9);

		osc = filtered * env * amp * 0.3;
		osc = Pan2.ar(osc, pan);

		ReplaceOut.ar(bus, osc)
	}
).add;
