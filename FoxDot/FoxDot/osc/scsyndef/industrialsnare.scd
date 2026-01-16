// Industrial snare - brutal, layered, crushed
SynthDef.new(\industrialsnare,
	{|bus=0, amp=1, pan=0, freq=180, decay=0.2, tone=0.5, noise=0.7, comp=10,
	  drive=4, ring=0.3, rattle=0.5, bend=3, snap=0.6|
		var sig, env, toneOsc, noiseOsc, rattleOsc, ringOsc, snapOsc, compressed, final;
		var pitchEnv, noiseEnv, rattleEnv, snapEnv;

		// Envelopes
		pitchEnv = EnvGen.ar(Env([bend, 1.2, 1], [0.001, 0.015], [\exp, \lin]));
		env = EnvGen.ar(Env.perc(0.0005, decay, 1, -6), doneAction: 2);
		noiseEnv = EnvGen.ar(Env.perc(0.0003, decay * 0.8, 1, -4));
		rattleEnv = EnvGen.ar(Env.perc(0.001, decay * 1.2, 1, -3));
		snapEnv = EnvGen.ar(Env.perc(0.0001, 0.008, 1, -12));

		// === TONE - body of snare ===

		toneOsc = SinOsc.ar(freq * pitchEnv);
		toneOsc = toneOsc + SinOsc.ar(freq * pitchEnv * 1.6, toneOsc * 2) * 0.4; // FM
		toneOsc = toneOsc + SinOscFB.ar(freq * pitchEnv * 0.5, 0.8) * 0.3;
		toneOsc = toneOsc * env * tone;

		// === NOISE - main snare character ===

		noiseOsc = WhiteNoise.ar;
		noiseOsc = BPF.ar(noiseOsc, 2000, 0.8) + HPF.ar(noiseOsc, 4000) * 0.5;
		noiseOsc = noiseOsc * noiseEnv * noise;

		// === RATTLE - snare wires ===

		rattleOsc = Mix.ar([
			Crackle.ar(1.95) * 0.3,
			LFNoise0.ar(8000) * 0.4,
			Dust2.ar(12000) * 0.3
		]);
		rattleOsc = RHPF.ar(rattleOsc, 3000, 0.4);
		rattleOsc = rattleOsc * rattleEnv * rattle;

		// === RING - metallic ===

		ringOsc = SinOsc.ar(freq * 3.2) * SinOsc.ar(freq * 4.7);
		ringOsc = ringOsc + (SinOsc.ar(freq * 2.1) * SinOsc.ar(freq * 5.3) * 0.5);
		ringOsc = ringOsc * Decay.ar(Impulse.ar(0), decay * ring) * ring;

		// === SNAP - transient ===

		snapOsc = Impulse.ar(0) * 10;
		snapOsc = snapOsc + HPF.ar(WhiteNoise.ar, 6000) * snapEnv;
		snapOsc = RHPF.ar(snapOsc, 4000, 0.2) * snap;

		// === MIX ===

		sig = toneOsc + noiseOsc + rattleOsc + ringOsc + snapOsc;

		// === DISTORTION CHAIN ===

		// Stage 1: Soft saturation
		sig = (sig * drive).tanh;

		// Stage 2: Hard clip for aggression
		sig = (sig * 2).clip(-1, 1);

		// Stage 3: Fold for harmonics
		sig = sig + ((sig * drive * 0.5).fold(-0.7, 0.7) * 0.3);

		// === BRUTAL COMPRESSION ===

		// First stage - transient shaping
		compressed = Compander.ar(sig, sig,
			thresh: 0.02,
			slopeBelow: 2,        // expand transient
			slopeAbove: 1/comp,
			clampTime: 0.00002,
			relaxTime: 0.01,
			mul: comp * 1.5
		);

		// Second stage - brick wall
		compressed = Compander.ar(compressed, compressed,
			thresh: 0.2,
			slopeBelow: 1,
			slopeAbove: 0.05,
			clampTime: 0.0001,
			relaxTime: 0.02,
			mul: 3
		);

		// Limiter
		compressed = Limiter.ar(compressed, 0.95, 0.0003);

		// === EQ ===

		final = BPeakEQ.ar(compressed, 200, 0.6, 3);    // body
		final = BPeakEQ.ar(final, 1000, 0.5, -2);       // mud cut
		final = BPeakEQ.ar(final, 4000, 0.7, 4 * snap); // snap
		final = BHiShelf.ar(final, 8000, 1, 3);         // air

		final = final * amp * 0.35;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
