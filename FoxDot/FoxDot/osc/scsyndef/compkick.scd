// Industrial kick - clean, deep, punchy
SynthDef.new(\compkick,
	{|bus=0, amp=1, pan=0, freq=50, punch=0.7, comp=8, release=0.35, click=0.4,
	  drive=1.5, sub=1, body=0.6, tone=0.3|
		var sig, subOsc, bodyOsc, clickSig, final;
		var pitchEnv, env, clickEnv, subEnv;

		freq = In.kr(bus, 1);
		// Pitch envelope - tight
		pitchEnv = EnvGen.ar(Env([5, 1.8, 1.1, 1], [0.003, 0.015, 0.06], [\exp, \exp, \lin]));

		// Envelopes - punchy
		env = EnvGen.ar(Env.perc(0.001, release, 1, -6), doneAction: 2);
		subEnv = EnvGen.ar(Env([0, 1, 0.8, 0.3, 0], [0.005, 0.05, 0.12, release], [-2, -3, -5]));
		clickEnv = EnvGen.ar(Env.perc(0.0005, 0.012, 1, -10));

		// === SUB - pure and deep ===
		subOsc = SinOsc.ar(freq * pitchEnv * 0.5);
		// Add subtle second harmonic for weight
		subOsc = subOsc + (SinOsc.ar(freq * pitchEnv, 0, 0.12));
		subOsc = subOsc * subEnv * sub;

		// === BODY - punchy mids ===
		bodyOsc = SinOsc.ar(freq * pitchEnv);
		// Phase mod for slight grit
		bodyOsc = SinOsc.ar(freq * pitchEnv, bodyOsc * tone * 1.5);
		bodyOsc = bodyOsc * env * body;

		// === CLICK - tight transient ===
		clickSig = HPF.ar(WhiteNoise.ar, 2000);
		clickSig = BPF.ar(clickSig, 3500, 0.5);
		clickSig = clickSig * clickEnv * click * 0.4;

		// Mix
		sig = (subOsc * 0.55) + (bodyOsc * 0.35) + clickSig;

		// === SUBTLE SATURATION ===
		sig = (sig * drive).softclip;
		sig = LPF.ar(sig, 8000);

		// === TIGHT COMPRESSION ===
		sig = Compander.ar(sig, sig,
			thresh: 0.1,
			slopeBelow: 1,
			slopeAbove: 1/comp,
			clampTime: 0.0008,
			relaxTime: 0.035,
			mul: comp.sqrt
		);

		// === EQ - clean and deep ===
		final = BLowShelf.ar(sig, 50, 0.7, 4);         // deep sub
		final = BPeakEQ.ar(final, 80, 1.2, 2);         // weight
		final = BPeakEQ.ar(final, 250, 1, -3);         // clear mud
		final = BPeakEQ.ar(final, 3000, 0.8, 2.5 * punch); // punch

		final = Limiter.ar(final, 0.95, 0.001);
		final = final * amp * 0.7;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
