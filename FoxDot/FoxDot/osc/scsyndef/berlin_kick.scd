// berlin_kick: One's (Unreason's) Berlin Kit, its kick voice, as a FoxDot synth. Ported from unreason/src/devices/berlin/dsp.ts.
// Per voice, as One: tune (st), dec (× the voice's decay), lvl (dB), x (its character: punch); pan (One's fixed pan for
// this voice by default). The kit's: oroom (One's room, a FoxDot effect name), odrive, level (dB), rumble and rdec (s), beat_dur (s per beat, sent by FoxDot: the duck recovers over 0.22 beat), every (beats between kicks, × beat_dur: the rumble is ducked again at each; 0: once).
// One sums the voices, adds the room and the rumble, then soft-clips the sum (tanh(4 odrive x) / (4 odrive)):
// here each hit is clipped alone, which is One exactly for a hit on its own.
SynthDef.new(\berlin_kick, {
	|bus = 0, dry = 1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, blur = 1, tune = 0, dec = 1, lvl = 0, x = 0.6, pan = 0,
	oroom = 0.4, odrive = 0.2, level = -4, velo = 1, rumble = 0.25, rdec = 2.6, beat_dur = 0.4615, every = 0|
	var sig;
	var t = Sweep.ar(1, 1), tr = 2 ** (tune / 12), nz = WhiteNoise.ar, y, g, l, r, a, wet, sat, done, svf, op, room, extraL = 0, extraR = 0, f = SinOsc.ar(43.65 * tr + ((260 - 43.65) * tr * (t.neg / 0.028).exp)), f2, env, body, cl, d, lo, hi, rum, s, o, w, lens, keep, duck;
	var fxon;
	// One's TPT state-variable filter at a set cutoff (lp, bp, hp), and its one-pole low-pass (y += a (x - y), a from Hz).
	svf = { |in, hz, k| var lp = BLowPass.ar(in, hz, k), hp = BHiPass.ar(in, hz, k); [lp, (in - lp - hp) / k, hp] };
	op = { |in, hz| OnePole.ar(in, (-2pi * hz / SampleRate.ir).exp) };
	// (no room for this voice in One)
	// One's room: four damped combs (feedback 0.8, damping a = 0.35) summed, then two all-passes (g 0.6) per side.
	room = { |in|
		var cl = [1557, 1617, 1491, 1422] * SampleRate.ir / 44100, al = [225, 556, 241, 579] * SampleRate.ir / 44100, fb, o, s, rl, rr;
		fb = LocalIn.ar(4);
		o = fb;
		LocalOut.ar(DelayN.ar(in + (OnePole.ar(o, 0.65) * 0.8), 0.05, (cl.round - BlockSize.ir) / SampleRate.ir));
		s = o.sum * 0.25;
		rl = AllpassN.ar(AllpassN.ar(s, 0.02, al[0].round / SampleRate.ir, al[0].round / SampleRate.ir * 13.523), 0.02, al[1].round / SampleRate.ir, al[1].round / SampleRate.ir * 13.523);
		rr = AllpassN.ar(AllpassN.ar(s, 0.02, al[2].round / SampleRate.ir, al[2].round / SampleRate.ir * 13.523), 0.02, al[3].round / SampleRate.ir, al[3].round / SampleRate.ir * 13.523);
		[rl, rr]
	};
	// a sine falling from 260 Hz to the root (43.65 Hz × tune), a knock an octave up, a click; driven, the top driven harder
	f2 = SinOsc.ar(2 * (43.65 * tr + ((260 - 43.65) * tr * (t.neg / 0.028).exp)));
	env = (t.neg / (0.34 * dec)).exp * (1 - (t.neg / 0.0008).exp);
	body = (f * env) + (f2 * 0.45 * (t.neg / 0.08).exp);
	cl = svf.(nz, 3740, 1.34)[1] * 1.34 * 1.7 * (0.3 + (0.4 * x)) * (t.neg / 0.0025).exp;
	d = 1 + (2.6 * x);
	y = ((body + cl) * d).tanh / d.tanh;
	lo = op.(y, 200); hi = y - lo;
	y = lo + ((hi * (1 + (3 * x))).tanh / (1 + x));
	y = y - op.(y, 25);
	// The rumble: four lines mixed by a Householder matrix, damped at 400 Hz, driven, low-passed twice at 150 Hz,
	// high-passed at 50 Hz, ducked by the kick (to 0.05, back over 0.22 beat), at rumble × the kick's level.
	lens = [1031, 1327, 1523, 1871] * SampleRate.ir / 48000;
	keep = 10 ** (-3 * lens.round / (rdec * SampleRate.ir));
	o = LocalIn.ar(4);
	s = o.sum;
	w = op.((o - (0.5 * s)) * keep, 400) + (body * velo * 0.5);
	LocalOut.ar(DelayN.ar(w, 0.05, (lens.round - BlockSize.ir) / SampleRate.ir));
	rum = svf.(svf.(svf.((s * 2.2).tanh, 150, 1.41)[0], 150, 1.41)[0], 50, 1.41)[2];
	duck = 1 - (0.95 * (Select.ar(every > 0, [t, t % (every * beat_dur).max(0.001)]).neg / (0.22 * beat_dur)).exp);
	extraL = rum * duck * rumble * lvl.dbamp * 0.9; extraR = extraL;
	done = max(9.21 * 0.34 * dec, Select.kr(rumble > 0, [0, rdec * 1.5 + 0.5]));
	y = y * velo;
	g = lvl.dbamp * 1;
	a = (pan.clip(-1, 1) + 1) * pi / 4;
	l = y * a.cos * g + extraL; r = y * a.sin * g + extraR;

	sat = { |v| Select.ar(odrive * 4 > 0.01, [v, (v * odrive * 4).tanh / (odrive * 4).max(0.01)]) };
	Line.kr(0, 1, done, doneAction: 2);
	// One's routing, by name: dry goes to FoxDot's own bus, as any synth; the sends go to the buses oneFX.py's effects run
	// on: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14 (what a ducker listens to). With no dry sound
	// (dry = 0, a sound going only through an effect) FoxDot's bus gets an inaudible tone at half the sample rate while
	// the note lives, so FoxDot does not free it as silent.
	sig = [sat.(l), sat.(r)] * level.dbamp * 2.sqrt * amp;
	// an effect that is not running (oneFX.py sets control bus 15360 + its bus to 1 while it runs): a sound sent only
	// to effects (dry = 0) plays dry instead of not at all; with dry above 0 it only loses that effect.
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	ReplaceOut.ar(bus, Select.ar(dry > 0, [((LFPulse.ar(SampleRate.ir / 2) * 2) - 1) * 0.00012 ! 2, sig * dry]));
}).add;
