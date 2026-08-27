// Industrial drone - fixed, reliable
SynthDef.new(\industrialdrone,
	{|bus=0, amp=1, pan=0, freq=440, fmod=0, sus=4, atk=0.5, rel=1,
	  cutoff=800, res=0.4, drive=1.3, detune=0.01, feedback=0.4, noise=0.15, sub=0.5|
		var sig, env, osc1, osc2, subOsc, noiseLayer, filtered, final;

		freq = In.kr(bus, 1);
		freq = freq / 2;

		// Envelope
		env = EnvGen.ar(Env.linen(atk, sus, rel, 1, \sin), doneAction: 2);

		// Detuned saws
		osc1 = Mix.ar([
			DPW4Saw.ar(freq),
			DPW4Saw.ar(freq * (1 + detune)),
			DPW4Saw.ar(freq * (1 - detune))
		]) * 0.25;

		// Feedback FM
		osc2 = SinOscFB.ar(freq * 0.5, feedback) * 0.4;

		// Sub
		subOsc = SinOsc.ar(freq * 0.25) * sub;

		// Noise
		noiseLayer = LPF.ar(PinkNoise.ar, cutoff) * noise;

		sig = osc1 + osc2 + subOsc + noiseLayer;

		// Filter
		filtered = RLPF.ar(sig, cutoff.clip(100, 8000), res.clip(0.1, 0.8));

		// Saturation
		filtered = (filtered * drive).softclip;

		final = filtered * env * amp * 0.5;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
