SynthDef.new(\a_vlead,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,
	  complexity=0.7, glitch=0.5, cutoff=3000|
		var osc, env, modFreq, chopped, filtered;
		freq = In.kr(bus, 1);

		// Complex frequency modulation
		modFreq = freq * [1, 1.003, 0.997] *
			(1 + (LFNoise1.ar([7.3, 11.7, 5.1]) * complexity * 0.1));

		// Multiple complex oscillators
		osc = Mix([
			VarSaw.ar(modFreq, width: LFNoise0.ar(16).range(0, 1), mul: 0.5),
			Pulse.ar(modFreq * 1.5,
				width: LFNoise1.ar([3.7, 8.1]).range(0.1, 0.9), mul: 0.4),
			// Granular-like component
			SinOsc.ar(modFreq * (2 + LFNoise0.ar(12)),
				LFNoise1.ar(8) * complexity, mul: 0.3)
		]);

		// Complex envelope with micro-variations
		env = EnvGen.ar(Env([0, 1, 0.8, 0.6, 0.3, 0],
			[0.001, 0.02, sus * 0.2, sus * 0.3, sus * 0.5]), doneAction: 0);

		// Glitchy chopping effect
		chopped = osc * LFPulse.ar(
			LFNoise0.ar(rate * 2).range(8, 64),
			width: LFNoise1.ar(4).range(0.1, 0.9)
		).range(glitch, 1);

		// Multi-stage filtering
		filtered = BPF.ar(chopped, cutoff * env.pow(0.3), 0.5, mul: 0.7);
		filtered = filtered + RLPF.ar(chopped, cutoff * 0.5, 0.3, mul: 0.3);

		osc = filtered * env * amp * 0.4;
		osc = Pan2.ar(osc, pan + (LFNoise1.ar(7) * 0.3));

		ReplaceOut.ar(bus, osc)
	}
).add;
