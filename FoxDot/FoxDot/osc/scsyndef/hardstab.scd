// Industrial stab - fixed
SynthDef.new(\hardstab,
	{|bus=0, amp=1, pan=0, freq=440, fmod=0, sus=0.2, atk=0.001, rel=0.15,
	  cutoff=3000, res=0.5, comp=6, drive=3, detune=0.01, fold=0.3, feedback=0.2|
		var sig, env, oscs, filtered, compressed, final;

		freq = In.kr(bus, 1);

		// Punchy envelope
		env = EnvGen.ar(
			Env.perc(atk, sus + rel, 1, -6),
			doneAction: 2
		);

		// Detuned saws
		oscs = Mix.ar([
			DPW4Saw.ar(freq),
			DPW4Saw.ar(freq * (1 + detune)),
			DPW4Saw.ar(freq * (1 - detune)),
			DPW4Saw.ar(freq * 2) * 0.3,
			DPW4Saw.ar(freq * 2 * (1 + detune)) * 0.3
		]) * 0.25;

		// Add pulse
		oscs = oscs + (LFPulse.ar(freq, width: 0.3).bipolar * 0.2);

		// Feedback layer
		oscs = oscs + (SinOscFB.ar(freq, feedback * 2) * feedback * 0.3);

		sig = oscs;

		// Saturation
		sig = (sig * drive).tanh;
		sig = sig + ((sig * fold * 4).fold(-1, 1) * fold * 0.3);

		// Filter with envelope
		filtered = RLPF.ar(sig,
			(cutoff * EnvGen.ar(Env.perc(0.001, sus * 0.5))).clip(50, 15000),
			res.clip(0.1, 0.9)
		);

		// Compression
		compressed = Compander.ar(filtered, filtered,
			thresh: 0.05, slopeBelow: 1, slopeAbove: 1/comp,
			clampTime: 0.0005, relaxTime: 0.02, mul: comp
		);

		compressed = Limiter.ar(compressed, 0.9, 0.001);

		final = compressed * env * amp * 0.5;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
