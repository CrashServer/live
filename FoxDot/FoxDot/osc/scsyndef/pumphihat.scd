// Industrial hihat - clean, crisp, tight
SynthDef.new(\pumphihat,
	{|bus=0, amp=1, pan=0, freq=9000, decay=0.06, open=0, comp=4,
	  tone=0.5, noise=0.6, metal=0.4, bright=0.5|
		var sig, env, noiseOsc, metalOsc, toneOsc, final;
		var metalFreqs, decayTime;

		decayTime = decay + (open * 0.35);
		env = EnvGen.ar(Env.perc(0.0003, decayTime, 1, -7 - (open * 3)), doneAction: 2);

		// === NOISE - filtered, clean ===
		noiseOsc = WhiteNoise.ar;
		noiseOsc = HPF.ar(noiseOsc, 5000);
		noiseOsc = BPF.ar(noiseOsc, freq, 0.5);
		noiseOsc = noiseOsc * noise;

		// === METALLIC - inharmonic partials ===
		metalFreqs = [205, 263, 340, 432, 557, 710] * (freq / 8000);
		metalOsc = Mix.ar(
			metalFreqs.collect({|f, i|
				SinOsc.ar(f) * (1 / (i + 1.5))
			})
		) * 0.35;
		metalOsc = metalOsc * metal;

		// === TONE - high sine cluster ===
		toneOsc = Mix.ar([
			SinOsc.ar(freq * 0.8),
			SinOsc.ar(freq * 1.2) * 0.6,
			SinOsc.ar(freq * 1.5) * 0.3
		]) * 0.2 * tone;

		// Mix
		sig = (noiseOsc + metalOsc + toneOsc) * env;

		// === CLEAN SATURATION ===
		sig = (sig * 1.3).softclip;

		// === COMPRESSION ===
		sig = Compander.ar(sig, sig,
			thresh: 0.1,
			slopeBelow: 1.1,
			slopeAbove: 1/comp,
			clampTime: 0.0001,
			relaxTime: 0.008 + (open * 0.01),
			mul: comp.sqrt
		);

		// === EQ - crisp ===
		final = BLowShelf.ar(sig, 400, 1, -6);            // cut lows
		final = BPeakEQ.ar(final, 6000, 0.7, 2 * bright); // presence
		final = BHiShelf.ar(final, 10000, 1, 2 * bright); // air

		final = Limiter.ar(final, 0.85, 0.0003);
		final = final * amp * 0.4;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
