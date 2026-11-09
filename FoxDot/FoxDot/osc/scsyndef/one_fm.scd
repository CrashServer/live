// one_fm: One's (Unreason's) Bell, a 4-operator FM synth, as a FoxDot synth. Ported from unreason/src/devices/fm/dsp.ts.
//  - operators start at phase 0 (as One's free voices do); op k runs at freq * r<k>
//  - modulation: One adds l * 1.1 * env * brightness cycles to a modulator's target phase: here 2pi times that, in radians
//  - op 4 feedback: One's fb * 0.25 cycles × (the last two outputs) ≈ SinOscFB with pi * fb radians
//  - each op's level decays as exp(-t / d) (d ≥ 19.9: held); the amp envelope follows One's one-pole ADSR
//  - algorithms: 0 stack 4→3→2→1, 1 pairs 4→3 + 2→1, 2 three into one, 3 additive; carriers' levels are their mix
// Renamed: vol→level, as→asus (Python word), and aa/ad/ar→aatk/adec/arel, vel→velamp, velo = this note's velocity.
SynthDef.new(\one_fm, {
	|bus = 0, dry = 1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	algo = 1, fb = 0, r1 = 1, l1 = 1, d1 = 8, r2 = 3.5, l2 = 0.55, d2 = 2, r3 = 3, l3 = 0.35, d3 = 1.5, r4 = 7, l4 = 0.4, d4 = 0.8,
	aatk = 0.002, adec = 3, asus = 0, arel = 1.5, velb = 0.6, velamp = 0.5, velo = 0.8, level = -8|
	var sig;
	var gate, ae, dec, e1, e2, e3, e4, br, o1, o2, o3, o4, ix, y, a, car, norm;
	var fxon;
	freq = In.kr(bus, 1);
	gate = Trig1.kr(1, sus);
	ae = EnvGen.ar(Env([0, 1, asus, 0], [0.6 * aatk * 5.log, 1.5 * adec, 3.45 * arel], [5.log.neg, -5, -11.5], releaseNode: 2), gate, doneAction: 2);
	dec = { |d| Select.kr(d >= 19.9, [EnvGen.kr(Env([1, 0.0001], [d * 9.2103], \exp)), 1]) };
	e1 = dec.(d1); e2 = dec.(d2); e3 = dec.(d3); e4 = dec.(d4);
	br = 1 - velb + (velb * velo);
	ix = 2pi * 1.1 * br;
	a = algo.round;
	o4 = SinOscFB.ar(freq * r4, pi * fb);
	// as modulators (index in radians) or carriers, by algorithm
	o3 = SinOsc.ar(freq * r3, Select.ar(a, [o4 * l4 * e4 * ix, o4 * l4 * e4 * ix, DC.ar(0), DC.ar(0)]));
	o2 = SinOsc.ar(freq * r2, Select.ar(a, [o3 * l3 * e3 * ix, DC.ar(0), DC.ar(0), DC.ar(0)]));
	o1 = SinOsc.ar(freq * r1, Select.ar(a, [o2 * l2 * e2 * ix, o2 * l2 * e2 * ix, ((o2 * l2 * e2) + (o3 * l3 * e3) + (o4 * l4 * e4)) * ix, DC.ar(0)]));
	y = Select.ar(a, [
		o1 * l1 * e1,
		(o1 * l1 * e1) + (o3 * l3 * e3),
		o1 * l1 * e1,
		(o1 * l1 * e1) + (o2 * l2 * e2) + (o3 * l3 * e3) + (o4 * l4 * e4)
	]);
	norm = Select.kr(a, [1, 1.4, 1, 2.5]);
	y = y * ae * (1 - velamp + (velamp * velo)) * level.dbamp / norm * 0.5 * amp;
	// One spreads its voices a little (the first: 10 % left): a note here is that first voice.
	// One's routing, by name: dry goes to FoxDot's own bus, as any synth; the sends go to the buses oneFX.py's effects run
	// on: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14 (what a ducker listens to). With no dry sound
	// (dry = 0, a sound going only through an effect) FoxDot's bus gets an inaudible tone at half the sample rate while
	// the note lives, so FoxDot does not free it as silent.
	sig = Balance2.ar(y * 1.1, y * 0.9, pan, 2.sqrt);
	// an effect that is not running (oneFX.py sets control bus 15360 + its bus to 1 while it runs): a sound sent only
	// to effects (dry = 0) plays dry instead of not at all; with dry above 0 it only loses that effect.
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	ReplaceOut.ar(bus, Select.ar(dry > 0, [((LFPulse.ar(SampleRate.ir / 2) * 2) - 1) * 0.00012 ! 2, sig * dry]));
}).add;
