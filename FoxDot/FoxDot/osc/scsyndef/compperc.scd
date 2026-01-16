// Industrial percussion - clean, tight, deep
SynthDef.new(\compperc,
	{|bus=0, amp=1, pan=0, freq=800, decay=0.08, tone=0.6, noise=0.4, comp=5,
	  drive=1.3, ring=0.25, metal=0.3, body=0.4, bend=1.3|
		var sig, env, toneOsc, noiseOsc, bodyOsc, metalOsc, final;
		var pitchEnv, noiseEnv;

		// Pitch bend - subtle
		pitchEnv = EnvGen.ar(Env([bend, 1, 0.98], [0.002, 0.02], [\exp, \lin]));

		// Envelopes - tight
		env = EnvGen.ar(Env.perc(0.0003, decay, 1, -8), doneAction: 2);
		noiseEnv = EnvGen.ar(Env.perc(0.0001, decay * 0.35, 1, -12));

		// === TONE - clean sine stack ===
		toneOsc = SinOsc.ar(freq * pitchEnv);
		toneOsc = toneOsc + (SinOsc.ar(freq * pitchEnv * 2) * 0.25);
		toneOsc = toneOsc + (SinOsc.ar(freq * pitchEnv * 3) * 0.1);
		toneOsc = toneOsc * tone;

		// === BODY - lower resonance ===
		bodyOsc = SinOsc.ar(freq * pitchEnv * 0.5) * body;
		bodyOsc = bodyOsc * EnvGen.ar(Env.perc(0.001, decay * 0.6, 1, -6));

		// === NOISE - tight filtered burst ===
		noiseOsc = BPF.ar(WhiteNoise.ar, freq * 2, 0.4);
		noiseOsc = noiseOsc + HPF.ar(WhiteNoise.ar * 0.2, 5000);
		noiseOsc = noiseOsc * noiseEnv * noise;

		// === METAL - subtle ring mod ===
		metalOsc = SinOsc.ar(freq * pitchEnv * 1.5) * SinOsc.ar(freq * pitchEnv * 2.2);
		metalOsc = LPF.ar(metalOsc, 6000);
		metalOsc = metalOsc * Decay.ar(Impulse.ar(0), decay * ring) * metal;

		// Mix
		sig = (toneOsc + bodyOsc + noiseOsc + metalOsc) * env;

		// === CLEAN SATURATION ===
		sig = (sig * drive * 1.1).softclip;
		sig = LPF.ar(sig, 7000);

		// === PUNCHY COMPRESSION ===
		sig = Compander.ar(sig, sig,
			thresh: 0.08,
			slopeBelow: 1.15,
			slopeAbove: 1/comp,
			clampTime: 0.0002,
			relaxTime: 0.015,
			mul: comp.sqrt * 1.2
		);

		// === EQ ===
		final = BPeakEQ.ar(sig, freq * 0.5, 0.8, 2 * body);  // body
		final = BPeakEQ.ar(final, freq, 0.6, 1.5);            // fundamental
		final = BHiShelf.ar(final, 5000, 1, -2);              // smooth highs

		final = Limiter.ar(final, 0.9, 0.0005);
		final = final * amp * 0.5;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
