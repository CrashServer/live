// foundry_kick: One's Foundry Kit, its kick voice, as a FoxDot synth. Ported from one/src/modules/one-units/foundry/dsp.ts.
// Per voice, as One: tune (st), kdec (s), knock, click, kdrive, mb (grit), lvl (dB, One's lvl0); the rumble: rumble (dB, -40 off), rdec (s), rdrive, rcut (Hz), rduck; beat_dur (s per beat, sent by FoxDot: the duck recovers over 0.22 beat), every (beats between kicks, × beat_dur: the rumble is ducked again at each; 0: once); pan (One's fixed pan for this voice by default).
// The kit's: glue, level (dB, One's vol).
// One sums the voices, adds the room and the rumble, then glues the sum (tanh(g x) / g, g = 0.3 + 1.7 glue):
// here each hit is glued alone, which is One exactly for a hit on its own.
SynthDef.new(\foundry_kick, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, blur = 1, tune = 0, lvl = 0, kdec = 0.3, knock = 0.45, click = 0.5, kdrive = 3.2, mb = 0.5, rumble = -9, rdec = 2.2, rdrive = 5, rcut = 190, rduck = 0.95, beat_dur = 0.4615, every = 0, pan = 0,
	glue = 0.25, level = -4, velo = 1, choke = -1, ocut = -1|
	var sig;
	var t = Sweep.ar(1, 1), tr = 2 ** (tune / 12), nz = WhiteNoise.ar, y, g, l, r, a, wet, gl, done, svf, op, room, extra = 0;
	var fr, hi, lens, keep, o, s, w, rum, duck, t1, t2, ea, ec, d, m;
	var chk, fxon;
	// One's TPT state-variable filter at a set cutoff (lp, bp, hp: the bilinear biquads it equals, rq = k), and its
	// one-pole low-pass (y += a (x - y), a from Hz).
	svf = { |in, hz, k| var lp = BLowPass.ar(in, hz, k), hp = BHiPass.ar(in, hz, k); [lp, (in - lp - hp) / k, hp] };
	op = { |in, hz| OnePole.ar(in, (-2pi * hz / SampleRate.ir).exp) };
	// (no room for this voice in One)
	// a sine falling from 260 Hz to the root (43.65 Hz × tune, tau 28 ms), a knock an octave up, a click; driven, the band above 200 Hz driven harder (grit); the rumble
	fr = (43.65 * tr) + ((260 - 43.65) * tr * (t.neg / 0.028).exp);
	y = (SinOsc.ar(fr) * (t.neg / kdec).exp * (1 - (t.neg / 0.0008).exp)) + (SinOsc.ar(2 * fr) * knock * (t.neg / 0.08).exp)
		+ (svf.(nz, 3740, 1.34)[1] * 1.34 * 1.7 * click * (t.neg / 0.0025).exp);
	y = (y * kdrive).tanh / kdrive.tanh;
	// the grit: the band above 200 Hz (a fourth-order high-pass) driven harder, the body left as it is
	hi = BHiPass.ar(BHiPass.ar(y, 200, 1.848), 200, 0.765);
	y = y - hi + ((hi * (1 + (6 * mb))).tanh / (1 + (2 * mb)));
	y = BHiPass.ar(y, 25, 1.41);
	// The rumble: the kick into four lines mixed by a Householder matrix, damped at 400 Hz (T60 rdec), driven, low-passed
	// (fourth order at rcut), high-passed at 50 Hz, ducked by the kick (to 1 - rduck, back over 0.22 beat), at rumble (dB) ×
	// the kick's level, in the middle.
	lens = ([1031, 1327, 1523, 1871] * SampleRate.ir / 48000).round;
	keep = 10 ** (-3 * lens / (rdec * SampleRate.ir));
	o = LocalIn.ar(4);
	s = o.sum;
	w = op.((o - (0.5 * s)) * keep, 400) + (y * velo * 0.5);
	LocalOut.ar(DelayN.ar(w, 0.05, (lens - BlockSize.ir + 0.1) / SampleRate.ir));
	rum = BHiPass.ar(BLowPass.ar(BLowPass.ar((s * rdrive * 0.3).tanh, rcut, 1.848), rcut, 0.765), 50, 1.41);
	duck = 1 - (rduck * (Select.ar(every > 0, [t, t % (every * beat_dur).max(0.001)]).neg / (0.22 * beat_dur)).exp);
	extra = rum * duck * (rumble > -39.5) * rumble.dbamp * lvl.dbamp * 0.9;
	done = max(9.21 * kdec, Select.kr(rumble > -39.5, [0, rdec * 1.5 + 0.5]));
	y = y * velo;
	g = lvl.dbamp * 1;
	a = (pan.clip(-1, 1) + 1) * pi / 4;
	l = (y * a.cos * g) + extra; r = (y * a.sin * g) + extra;
	Line.kr(0, 1, done, doneAction: 2);
	// the glue (on One's whole kit): tanh(g x) / g, after the level
	gl = 0.3 + (1.7 * glue);
	sig = ([l, r] * level.dbamp * 2.sqrt * gl).tanh / gl * amp;
	// one voice (choke >= 0, from the exporter): the next note of the same unit takes the voice over, this one fades
	// in 2 ms (its id on control bus 15400 + choke; choke < 0: plays as it is)
	chk = [Rand(1, 1000000), Sweep.kr(1, 1) < (ControlDur.ir * 1.5), Select.kr(choke >= 0, [15399, 15400 + choke.max(0)])];
	chk = chk ++ [In.kr(chk[2])];
	ReplaceOut.kr(chk[2], Select.kr(chk[1], [chk[3], chk[0]]));
	sig = sig * EnvGen.kr(Env.asr(0, 1, 0.002), (chk[1] + ((chk[3] - chk[0]).abs < 0.5) + (choke < 0)).min(1), doneAction: 2);
	// ocut (from the exporter): a section turning this unit down silences it at once, as One does (control bus
	// 15700 + cut changes: oneFX's one_cut); ocut < 0: nothing
	sig = sig * EnvGen.kr(Env.asr(0, 1, 0.005), ((In.kr(15700 + ocut.max(0)) - Latch.kr(In.kr(15700 + ocut.max(0)), Impulse.kr(0))).abs < 0.5) + (ocut < 0), doneAction: 2);
	// One's routing, by name: dry goes to FoxDot's own bus, as any synth; the sends go to the buses oneFX.py's effects run
	// on: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14 (what a ducker listens to). With no dry sound
	// (dry = 0, a sound going only through an effect) FoxDot's bus gets an inaudible tone at half the sample rate while
	// the note lives, so FoxDot does not free it as silent.
	// an effect that is not running (oneFX.py sets control bus 15360 + its bus to 1 while it runs): a sound sent only
	// to effects (dry = 0) plays dry instead of not at all; with dry above 0 it only loses that effect.
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	// an insert (ins: its bus, from fx_insert): the dry sound goes there, FoxDot's bus keeps the inaudible tone
	Out.ar(ins.max(0), sig * dry * (ins >= 0));
	ReplaceOut.ar(bus, Select.ar((dry > 0) * (ins < 0), [((LFPulse.ar(SampleRate.ir / 2) * 2) - 1) * 0.00012 ! 2, sig * dry]));
}).add;
