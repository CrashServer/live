SynthDef.new(\a_fantom,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, cutoff=800, drive=8, crush=4|
		var osc, env, filter, crushed;
		freq = In.kr(bus, 1);
		
		// Wide detuning for that huge Justice sound
		freq = [freq, freq+fmod, freq*1.01, freq*0.99, freq*1.005] *
		Line.ar(Rand(0.98,1.02),1,0.02);
		
		// Stack of saws with different octaves
		osc = Mix([
			Saw.ar(freq, mul: 0.8),
			Saw.ar(freq * 2, mul: 0.4),
			Saw.ar(freq * 0.5, mul: 0.5),
			VarSaw.ar(freq * 1.5, width: LFNoise1.ar(2).range(0.1,0.9), mul: 0.3)
		]);
		
		// Aggressive envelope
		env = EnvGen.ar(Env([0, 1, 0.9, 0.6, 0],
			[0.005, 0.02, sus * 0.5, sus * 0.5]), doneAction: 0);
		
		// Extreme distortion
		osc = (osc * drive).fold(-0.7, 0.7);
		
		// Bit crushing for digital harshness
		crushed = Decimator.ar(osc, 44100/crush, bits: 8);
		
		// Filter sweep
		filter = RLPF.ar(crushed,
			cutoff * env.pow(0.4) * (1 + (SinOsc.ar(rate * 0.5) * 0.3)),
			0.9);
		
		// High-pass to clean up low end
		filter = RHPF.ar(filter, 80, 0.5);
		
		osc = filter * env * amp * 0.35;
		osc = Pan2.ar(osc, pan);
		
		ReplaceOut.ar(bus, osc)
	}
).add;
