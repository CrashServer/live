// one_hoover: One's Hoover as a FoxDot synth. Ported from src/modules/hardcore-units/hoover/dsp.ts.
//  - three pulses detune cents apart (One's polyBLEP pulses, from One's phases 0, 0.33, 0.66), their widths
//    0.5 + 0.38 pwm sin(LFO) (0.31, 0.43, 0.57 Hz, from One's phases 0, 0.37, 0.71), clamped 0.06..0.94
//  - the saw an octave down (polyBLEP, phase 0.1) × 0.8 sub
//  - the swoop: every note starts dip semitones low, rising as exp(-t / diptime)
//  - One's TPT state-variable low-pass (BLowPass, rq = k = 2 - 1.96 res) at cutoff × 2^(4 fenv (0.7 fe + 0.3 env)),
//    fe = exp(-t / 0.25), then tanh(x (1 + 6 odrive)) / tanh(1 + 6 odrive)
//  - the amp: One's one-poles (attack aatk, release arel time constants) on the gate (OnePole, the same coefficients)
//  - the chorus: delays of 7 + 3 sin and 11 - 3 sin ms (0.7 Hz), left and right, dry × (1 - 0.4 ochorus)
// One's Hoover is one voice: a note while another is held glides to it (glide) without its filter envelope starting
// again. A FoxDot note is a note of its own: no glide, no legato. One's phases and LFOs run on from note to note; here
// each note starts from where One's first note does.
// Renamed: cut→cutoff, drive→odrive, chorus→ochorus, vol→level, aa/ar→aatk/arel; velo = this note's velocity.
// The Phasors take an audio-rate trigger (DC.ar(0)): with a scalar one, Phasor reads its rate once a block.
SynthDef.new(\one_hoover, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	detune = 22, pwm = 0.7, sub = 0.6, dip = 7, diptime = 0.09, cutoff = 1800, res = 0.2, fenv = 0.35,
	aatk = 0.006, arel = 0.18, odrive = 0.35, ochorus = 0.8, velo = 0.8, level = -12, choke = -1, gl = 0, beat_dur = 0.5, ocut = -1|
	var sig;
	var sr = SampleRate.ir, sd = SampleDur.ir, blep, t, gate, env, fe, fr, det, x, ds, ts, k, hz, dg, y, s, cl, cr, l, r;
	var chk, fxon;
	sus = Select.kr(gl > 0, [sus, gl * beat_dur]);   // the note's own length when FoxDot's sus is its life (gl, beats)
	freq = In.kr(bus, 1);
	blep = { |t, dt| var a = t / dt, b = (t - 1) / dt; ((t < dt) * ((a + a) - (a * a) - 1)) + ((t > (1 - dt)) * ((b * b) + b + b + 1)) };
	t = Sweep.ar(1, 1);
	gate = t < sus;
	env = OnePole.ar(gate, (gate * (-1 / (aatk.max(0.001) * sr)).exp) + ((1 - gate) * (-1 / (arel.max(0.005) * sr)).exp));
	fr = freq * (2 ** (dip.neg * (t.neg / diptime.max(0.005)).exp / 12));
	det = detune / 1200;
	x = [[0, 0, 0, 0.31], [1, 0.33, 0.37, 0.43], [2, 0.66, 0.71, 0.57]].collect { |v|
		var fv = fr * (2 ** ((v[0] - 1) * det)), dt = fv * sd, tt, t2, pw;
		pw = (0.5 + (0.38 * pwm * SinOsc.ar(v[3], 2pi * v[2]))).clip(0.06, 0.94);
		tt = (Phasor.ar(DC.ar(0), dt, 0, 1) + v[1] + dt).frac;
		t2 = (tt + 1 - pw).frac;
		((tt < pw) * 2 - 1) + blep.(tt, dt) - blep.(t2, dt)
	}.sum;
	ds = fr * 0.5 * sd;
	ts = (Phasor.ar(DC.ar(0), ds, 0, 1) + 0.1 + ds).frac;
	x = (x / 3) + (sub * ((2 * ts) - 1 - blep.(ts, ds)) * 0.8);
	fe = ((t + sd).neg / 0.25).exp;
	k = 2 - (1.96 * res.clip(0, 1));
	hz = (cutoff * (2 ** (fenv * 4 * ((fe * 0.7) + (0.3 * env))))).clip(40, sr * 0.45);
	dg = 1 + (6 * odrive);
	y = (BLowPass.ar(x, hz, k) * dg).tanh / dg.tanh * env * velo;
	s = SinOsc.ar(0.7, 0);
	cl = DelayL.ar(y, 0.02, (7 + (3 * s)) / 1000);
	cr = DelayL.ar(y, 0.02, (11 - (3 * s)) / 1000);
	l = ((y * (1 - (0.4 * ochorus))) + (cl * ochorus)) * level.dbamp * amp;
	r = ((y * (1 - (0.4 * ochorus))) + (cr * ochorus)) * level.dbamp * amp;
	Line.kr(0, 0, sus + (11.5 * arel.max(0.005)) + 0.03, doneAction: 2);
	// One's routing, by name: dry goes to FoxDot's own bus, as any synth; the sends go to the buses oneFX.py's effects run
	// on: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14 (what a ducker listens to). With no dry sound
	// (dry = 0, a sound going only through an effect) FoxDot's bus gets an inaudible tone at half the sample rate while
	// the note lives, so FoxDot does not free it as silent.
	sig = Balance2.ar(l, r, pan, 2.sqrt);
	// one voice (choke >= 0, from the exporter): the next note of the same unit takes the voice over, this one fades
	// in 2 ms (its id on control bus 15400 + choke; choke < 0: plays as it is)
	chk = [Rand(1, 1000000), Sweep.kr(1, 1) < (ControlDur.ir * 1.5), Select.kr(choke >= 0, [15399, 15400 + choke.max(0)])];
	chk = chk ++ [In.kr(chk[2])];
	ReplaceOut.kr(chk[2], Select.kr(chk[1], [chk[3], chk[0]]));
	sig = sig * EnvGen.kr(Env.asr(0, 1, 0.002), (chk[1] + ((chk[3] - chk[0]).abs < 0.5) + (choke < 0)).min(1), doneAction: 2);
	// ocut (from the exporter): a section turning this unit down silences it at once, as One does (control bus
	// 15700 + cut changes: oneFX's one_cut); ocut < 0: nothing
	sig = sig * EnvGen.kr(Env.asr(0, 1, 0.005), ((In.kr(15700 + ocut.max(0)) - Latch.kr(In.kr(15700 + ocut.max(0)), Impulse.kr(0))).abs < 0.5) + (ocut < 0), doneAction: 2);
	// an effect that is not running (oneFX.py sets control bus 15360 + its bus to 1 while it runs): a sound sent only
	// to effects (dry = 0) plays dry instead of not at all; with dry above 0 it only loses that effect.
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	// an insert (ins: its bus, from fx_insert): the dry sound goes there, FoxDot's bus keeps the inaudible tone
	Out.ar(ins.max(0), sig * dry * (ins >= 0));
	ReplaceOut.ar(bus, Select.ar((dry > 0) * (ins < 0), [((LFPulse.ar(SampleRate.ir / 2) * 2) - 1) * 0.00012 ! 2, sig * dry]));
}).add;
