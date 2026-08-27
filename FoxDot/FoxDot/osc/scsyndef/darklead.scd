// Dark lead - fixed, reliable
SynthDef.new(\darklead,
	{|bus=0, amp=1, pan=0, freq=440, fmod=0, sus=1, atk=0.01, rel=0.2,
	  cutoff=2000, res=0.35, drive=1.5, detune=0.006, width=0.5, sub=0.4|
		var sig, env, osc1, osc2, osc3, subOsc, filtered, final;

		freq = In.kr(bus, 1);

		// Envelope
		env = EnvGen.ar(Env.perc(atk, sus + rel, 1, -4), doneAction: 2);

		// Detuned saws
		osc1 = DPW4Saw.ar(freq);
		osc2 = DPW4Saw.ar(freq * (1 + detune));
		osc3 = DPW4Saw.ar(freq * (1 - detune));

		// Pulse for width
		sig = ((osc1 + osc2 + osc3) * 0.25) + (LFPulse.ar(freq, width: width).bipolar * 0.2);

		// Sub
		subOsc = SinOsc.ar(freq * 0.5) * sub;
		sig = sig + subOsc;

		// Filter
		filtered = RLPF.ar(sig, cutoff.clip(100, 12000), res.clip(0.1, 0.9));

		// Saturation
		filtered = (filtered * drive).softclip;
		filtered = LPF.ar(filtered, 8000);

		final = filtered * env * amp * 0.5;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
