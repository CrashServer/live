// Industrial bass - rich, deep, aggressive
SynthDef.new(\pumpbass,
	{|bus=0, amp=1, pan=0, freq=440, fmod=0, sus=1, atk=0.005, rel=0.1,
	  cutoff=1000, res=0.4, drive=1.5, feedback=0.3, sub=0.8, body=0.6, growl=0.4|
		var sig, env, osc1, osc2, osc3, subOsc, bodyOsc, filtered, final;
		var pitchEnv, subEnv, bodyEnv;

		freq = In.kr(bus, 1);
		freq = freq / 2;

		// Pitch envelope - subtle movement
		pitchEnv = EnvGen.ar(Env([1.08, 1.02, 1], [0.01, 0.08], [\exp, \lin]));

		// Envelopes
		env = EnvGen.ar(Env.perc(atk, sus + rel, 1, -4), doneAction: 2);
		subEnv = EnvGen.ar(Env([0, 1, 0.9, 0.5, 0], [0.01, 0.1, sus * 0.5, rel], [-2, -3, -4]));
		bodyEnv = EnvGen.ar(Env.perc(0.005, sus * 0.6, 1, -5));

		// === SUB - deep foundation ===
		subOsc = SinOsc.ar(freq * 0.5 * pitchEnv);
		subOsc = subOsc + (SinOsc.ar(freq * pitchEnv, 0, 0.3));
		subOsc = subOsc * subEnv * sub;

		// === BODY - detuned saws ===
		osc1 = DPW4Saw.ar(freq * pitchEnv);
		osc2 = DPW4Saw.ar(freq * pitchEnv * 1.005);
		osc3 = DPW4Saw.ar(freq * pitchEnv * 0.995);
		bodyOsc = ((osc1 + osc2 + osc3) * 0.2) * bodyEnv * body;

		// === GROWL - feedback FM ===
		sig = SinOscFB.ar(freq * pitchEnv * 0.5, feedback * 1.2) * growl * 0.5;
		sig = sig * env;

		// === PULSE for grit ===
		sig = sig + (Pulse.ar(freq * pitchEnv * 1.003, 0.35) * 0.25 * env);

		// Mix all
		sig = (subOsc * 0.5) + (bodyOsc * 0.35) + sig;

		// === FILTER - resonant LPF ===
		filtered = RLPF.ar(sig, (cutoff * env.linlin(0, 1, 0.5, 1)).clip(80, 8000), res.clip(0.15, 0.85));

		// === SATURATION - warm ===
		filtered = LPF.ar(filtered, 6000);
		filtered = (filtered * drive * 1.2).softclip;
		filtered = LPF.ar(filtered, 5000);

		// === COMPRESSION ===
		filtered = Compander.ar(filtered, filtered,
			thresh: 0.15,
			slopeBelow: 1,
			slopeAbove: 1/4,
			clampTime: 0.002,
			relaxTime: 0.06,
			mul: 2
		);

		// === EQ ===
		final = BLowShelf.ar(filtered, 60, 0.7, 3);
		final = BPeakEQ.ar(final, 120, 1, 2);
		final = BPeakEQ.ar(final, 400, 1, -2);

		final = Limiter.ar(final, 0.92, 0.002);
		final = final * amp * 0.6;
		final = Pan2.ar(final, pan);
		ReplaceOut.ar(bus, final);
	}
).add;
