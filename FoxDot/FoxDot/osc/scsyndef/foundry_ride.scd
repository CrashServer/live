// foundry_ride: One's Foundry Kit, its ride voice, as a FoxDot synth. Ported from one/src/modules/one-units/foundry/dsp.ts.
// Per voice, as One: tune (st), dec (× the voice's decay), lvl (dB); pan (One's fixed pan for this voice by default).
// The kit's: oroom (One's room, a FoxDot effect name: this voice sends 0.08 of itself to it), size, glue, level (dB, One's vol).
// One sums the voices, adds the room and the rumble, then glues the sum (tanh(g x) / g, g = 0.3 + 1.7 glue):
// here each hit is glued alone, which is One exactly for a hit on its own.
SynthDef.new(\foundry_ride, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, blur = 1, tune = 0, dec = 1, lvl = -14, pan = 0.35,
	oroom = 0.4, size = 1, glue = 0.25, level = -4, velo = 1, choke = -1, ocut = -1|
	var sig;
	var t = Sweep.ar(1, 1), tr = 2 ** (tune / 12), nz = WhiteNoise.ar, y, g, l, r, a, wet, gl, done, svf, op, room, extra = 0;
	var fr, hi, lens, keep, o, s, w, rum, duck, t1, t2, ea, ec, d, m;
	var chk, fxon;
	// One's TPT state-variable filter at a set cutoff (lp, bp, hp: the bilinear biquads it equals, rq = k), and its
	// one-pole low-pass (y += a (x - y), a from Hz).
	svf = { |in, hz, k| var lp = BLowPass.ar(in, hz, k), hp = BHiPass.ar(in, hz, k); [lp, (in - lp - hp) / k, hp] };
	op = { |in, hz| OnePole.ar(in, (-2pi * hz / SampleRate.ir).exp) };
	// One's room: six damped combs (lengths × size, feedback 0.7 + 0.12 size, damping a = 0.3) summed, then two
	// all-passes (g 0.6) per side. Linear, so this voice's own copy adds up like One's one room.
	room = { |in|
		var cl = ([1557, 1617, 1491, 1422, 1277, 1356] * 1.5 * SampleRate.ir / 44100).round, al = ([225, 556, 241, 579] * SampleRate.ir / 44100).round, len, o, s, rl, rr;
		len = (cl / 1.5 * size).round.min(cl).max(BlockSize.ir + 1);
		o = LocalIn.ar(6);
		LocalOut.ar(DelayN.ar(in + (OnePole.ar(o, 0.7) * (0.7 + (0.12 * size.min(1)))), 0.06, (len - BlockSize.ir + 0.1) / SampleRate.ir));
		s = o.sum / 6;
		al = (al + 0.1) / SampleRate.ir;
		rl = AllpassN.ar(AllpassN.ar(s, 0.02, al[0], al[0] * 13.523), 0.02, al[1], al[1] * 13.523);
		rr = AllpassN.ar(AllpassN.ar(s, 0.02, al[2], al[2] * 13.523), 0.02, al[3], al[3] * 13.523);
		[rl, rr]
	};
	// the metal × 3.1 as sines and noise, band-passed at 5.5 kHz, 450 ms, high-passed at 1 kHz
	m = SinOsc.ar([205.3, 304.4, 369.6, 522.7, 540.0, 800.0] * 3.1 * tr, [0, 1, 2, 3, 4, 5]).sum;
	y = BHiPass.ar(svf.((m / 6 * 0.5) + (nz * 0.4), 5480 * tr, 1.28)[1] * 1.28 * (t.neg / (0.45 * dec)).exp * (1 - (t.neg / 0.0005).exp), 1000, 1.41);
	done = 9.21 * 0.45 * dec;
	y = y * velo;
	g = lvl.dbamp * 1.4;
	a = (pan.clip(-1, 1) + 1) * pi / 4;
	l = (y * a.cos * g) + extra; r = (y * a.sin * g) + extra;
	wet = room.(y * g * 0.08) * oroom;
	l = l + wet[0]; r = r + wet[1];
	Line.kr(0, 1, done + (2 * (oroom > 0)), doneAction: 2);
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
