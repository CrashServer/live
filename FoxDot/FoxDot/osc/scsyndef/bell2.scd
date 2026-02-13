SynthDef.new(\bell2, {
	|bus=0, freq=440, amp=1, pan=0, fmod=0,
	atk=0.001, dec=2, sus=1, rel=1, peak=1, level=0.5,
	bright=0.5, damp=0.5, hard=0.5, round=0.3,
	inharm=0.01, fmamt=1, fmratio=2.4,
	strike=0.3, shimmer=0.3|

	var osc, env, strikeOsc, mod, decayMult;
	var p1, p2, p3, p4, p5;

	freq = In.kr(bus, 1);
	freq = freq + fmod;

	// Shimmer via slight detune
	freq = freq * SinOsc.kr(3).range(1 - (shimmer * 0.003), 1 + (shimmer * 0.003));

	decayMult = (1 - (damp * 0.7)) * (dec + sus);

	// FM modulation
	mod = SinOsc.ar(freq * fmratio) * fmamt * freq * EnvGen.ar(Env.perc(0.001, 0.3));

	// 5 partials (reduced from 8 for performance)
	p1 = SinOsc.ar(freq * 0.5 + mod) * 0.4 * EnvGen.ar(Env.perc(0.001, 2 * decayMult, curve: -4));
	p2 = SinOsc.ar(freq + mod) * EnvGen.ar(Env.perc(0.001, 1.5 * decayMult, curve: -4));
	p3 = SinOsc.ar(freq * (1.19 + (inharm * 0.1)) + mod) * 0.6 * bright * EnvGen.ar(Env.perc(0.001, 1.2 * decayMult, curve: -4));
	p4 = SinOsc.ar(freq * 2 + mod) * 0.25 * EnvGen.ar(Env.perc(0.001, 0.8 * decayMult, curve: -4));
	p5 = SinOsc.ar(freq * (2.51 + (inharm * 0.2)) + mod) * 0.15 * bright * EnvGen.ar(Env.perc(0.001, 0.5 * decayMult, curve: -4));

	osc = p1 + p2 + p3 + p4 + p5;

	// Round - low-pass
	osc = LPF.ar(osc, freq * (4 + (bright * 8) - (round * 3)));

	// Strike transient
	strikeOsc = WhiteNoise.ar * EnvGen.ar(Env.perc(0.0001, 0.005 + (hard * 0.01)));
	strikeOsc = BPF.ar(strikeOsc, 3000, 0.5);
	osc = osc + (strikeOsc * strike * 2);

	// Envelope
	env = EnvGen.ar(
		Env([0, peak, level, level, 0], [atk, dec * 0.3, max(0.01, sus - atk - dec), rel], curve: -4),
		doneAction: 0
	);

	osc = osc * env * amp * 0.3;
	osc = Pan2.ar(osc, pan);
	osc = LeakDC.ar(osc);

	ReplaceOut.ar(bus, osc);
},
metadata: (
	credit: "Custom FoxDot synth",
	description: "Tuneable bell with partials, damping, FM, strike",
	category: \percussion,
	tags: [\bell, \mallet, \vibraphone, \glockenspiel]
)).add;
