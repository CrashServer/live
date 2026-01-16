// Simple sub bass - just works
SynthDef.new(\subbass,
	{|bus=0, amp=1, pan=0, freq=440, fmod=0, sus=1, atk=0.01, rel=0.1,
	  drive=1.5, sub=1, mid=0.3, feedback=0.2|
		var sig, env, subOsc, midOsc, final;

		freq = In.kr(bus, 1);
		freq = freq / 4;

		env = EnvGen.ar(
			Env([0, 1, 0.8, 0], [atk, sus, rel], [-2, -4]),
			doneAction: 2
		);

		subOsc = SinOsc.ar(freq) * sub;
		midOsc = SinOscFB.ar(freq * 2, feedback) * mid;
		midOsc = midOsc + (LFTri.ar(freq * 2) * mid * 0.5);

		sig = subOsc + midOsc;
		sig = (sig * drive).tanh;
		sig = LPF.ar(sig, 300);

		sig = Compander.ar(sig, sig,
			thresh: 0.15, slopeBelow: 1, slopeAbove: 0.3,
			clampTime: 0.005, relaxTime: 0.05, mul: 2
		);

		final = Limiter.ar(sig, 0.9, 0.01);
		final = final * env * amp * 0.7;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
