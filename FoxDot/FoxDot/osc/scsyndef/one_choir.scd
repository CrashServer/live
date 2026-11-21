// one_choir: One's Choir as a FoxDot synth. Ported from one/src/modules/trap-units/choir/dsp.ts.
//  - three singers on the note (men: five, the last two an octave down), each One's polyBLEP saw (written out here, so
//    it aliases as One's does), from the phases, vibrato and drift phases One's first voice has (its seeded rng(1600)):
//    pitch 2^(DETUNE ens + 0.7 ens sin(drift) + vibD min(1, t/0.6) sin(vib)), ens = 22 cents × ens, vibD = 0.35 st × ovib,
//    vibrato at 4.6 + 0.37 s Hz, drift at 0.11 + 0.06 s Hz; panned -0.8, 0, 0.8, -0.4, 0.4 (linear)
//  - One's amp envelope (one-pole attack aatk, release arel, as one_sub's) × (0.6 + 0.4 velo)
//  - breath: noise × breath/4 riding each side's level (× |side| × 0.6)
//  - the vowel (a e i o u by ovowel, formants moved by size): four of One's state-variable band-passes per side (the
//    right a hair up: g × 1.01), as the bilinear band-passes they equal (BBandPass, bandwidth from k), × each formant's
//    level × 2.2; plus the throat one-poled (0.08) × bright/4; × One's level compensation across vowels
// Per note: One's vowel filters and breath work on the sum of the notes (linear but for the breath, which rides the
// sum's level); the breath's noise is random here.
// Names as One's except vowel→ovowel, vib→ovib (FoxDot effects), vol→level, aa/ar→aatk/arel; velo this note's velocity.
SynthDef.new(\one_choir, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	ovowel = 0, size = 0, ens = 0.5, ovib = 0.4, breath = 0.3, bright = 0.3, men = 0, aatk = 0.5, arel = 1.5, velo = 0.8, level = -8, gl = 0, beat_dur = 0.5, ocut = -1|
	var sig, sr, t, vf, vg, bw, lev, ref, vx, v0, vfr, sz, fq, fg, ks, bwk, comp, vol, ensO, vibD, isMen, a, ph0, vib0, drift0, det, pans;
	var blep, saw, sl, sr2, nz, ol, or, l, r, env;
	var fxon;
	sus = Select.kr(gl > 0, [sus, gl * beat_dur]);   // the note's own length when FoxDot's sus is its life (gl, beats)
	freq = In.kr(bus, 1);
	sr = SampleRate.ir;
	t = Sweep.ar(0, 1);
	vf = [[800, 1150, 2800, 3500], [400, 1600, 2700, 3300], [350, 1700, 2700, 3700], [450, 800, 2830, 3500], [325, 700, 2530, 3500]];
	vg = [[0, -4, -20, -36], [0, -24, -30, -35], [0, -20, -30, -36], [0, -9, -16, -28], [0, -12, -30, -40]];
	bw = [80, 90, 120, 130];
	lev = { |f, g, w| (f.collect { |x, k| g[k] * g[k] * w[k] / (x * x) }).sum.sqrt };
	ref = lev.(vf[0], vg[0].dbamp, bw);
	// the vowel, between its two neighbours
	vx = ovowel.clip(0, 1) * 4; v0 = vx.floor.min(3); vfr = vx - v0; sz = 2 ** (size.neg * 0.5);
	fq = 4.collect { |k| ((Select.kr(v0, vf.collect(_[k])) * (1 - vfr)) + (Select.kr(v0 + 1, vf.collect(_[k])) * vfr)) * sz };
	fg = 4.collect { |k| ((Select.kr(v0, vg.collect(_[k])) * (1 - vfr)) + (Select.kr(v0 + 1, vg.collect(_[k])) * vfr)).dbamp };
	bwk = bw * (1 + (size * 0.3));
	ks = 4.collect { |k| (bwk[k] / fq[k]).clip(0.02, 1.5) };
	comp = (ref / lev.(fq, fg, bwk)).min(2);
	isMen = men > 0.5;
	vol = level.dbamp * Select.kr(isMen, [1, 0.8]) * comp * 0.7;
	ensO = ens * 22 / 1200; vibD = ovib * 0.35 / 12;
	env = EnvGen.ar(Env([0, 1, 1, 0], [0.6 * aatk * 5.log, 0.45, 3.45 * arel], [5.log.neg, -5, -11.5], releaseNode: 2), Trig1.kr(1, sus));
	a = env * (0.6 + (0.4 * velo));
	ph0 = [0.1007196, 0.1956186, 0.8040130, 0.2362519, 0.8155627];
	vib0 = [0.01578407, 0.4842877, 0.4265191, 0.6644075, 0.2908831];
	drift0 = [0.6739363, 0.5233067, 0.4360916, 0.1449588, 0.08319977];
	det = [-1, 0.15, 1, -0.5, 0.6]; pans = [-0.8, 0, 0.8, -0.4, 0.4];
	blep = { |p, dt| var u = p / dt, w = (p - 1) / dt; ((p < dt) * (u + u - (u * u) - 1)) + ((p > (1 - dt)) * ((w * w) + w + w + 1)) };
	// One's saw: the step added before the phase is read
	saw = { |f, p0| var dt = f / sr, p = (Phasor.ar(DC.ar(0), dt) + dt + p0).frac; (2 * p) - 1 - blep.(p, dt) };
	sl = 0; sr2 = 0;
	5.do { |s|
		var off, f, x;
		off = (det[s] * ensO) + (sin(2pi * ((drift0[s] + ((0.11 + (0.06 * s)) * t)).frac)) * ensO * 0.7)
			+ (vibD * (t / 0.6).min(1) * sin(2pi * ((vib0[s] + ((4.6 + (s * 0.37)) * t)).frac)));
		f = freq * (if(s >= 3) { 0.5 } { 1 }) * (2 ** off);
		x = saw.(f, ph0[s]) * a * (if(s >= 3) { isMen } { 1 });
		sl = sl + (x * (1 - pans[s]) * 0.5); sr2 = sr2 + (x * (1 + pans[s]) * 0.5);
	};
	// breath: noise riding the singers' level, a little
	nz = breath * 0.25 * WhiteNoise.ar;
	sl = sl + (nz * sl.abs * 0.6); sr2 = sr2 + (nz * sr2.abs * 0.6);
	// One's band-pass × k is the bilinear band-pass with Q = 1/k: BBandPass with bw = 2 asinh(k/2) / ln 2 × sin w / w
	ol = 0; or = 0;
	4.do { |k|
		var w = 2pi * fq[k] / sr, wr = 2 * atan(1.01 * tan(w / 2)), b = ((ks[k] / 2) + ((ks[k] / 2).squared + 1).sqrt).log * 2 / 2.log;
		ol = ol + (BBandPass.ar(sl, fq[k], b * sin(w) / w) * fg[k]);
		or = or + (BBandPass.ar(sr2, wr * sr / 2pi, b * sin(wr) / wr) * fg[k]);
	};
	// a little of the throat unfiltered, low-passed: brightness and body
	l = ((ol * 2.2) + (OnePole.ar(sl, 0.92) * bright * 0.25)) * vol * amp;
	r = ((or * 2.2) + (OnePole.ar(sr2, 0.92) * bright * 0.25)) * vol * amp;
	FreeSelf.kr(TDelay.kr(Done.kr(env), 0.05));
	// One's routing, as one_sub's: dry to FoxDot's bus, the sends to the buses oneFX.py's effects run on.
	sig = Balance2.ar(l, r, pan, 2.sqrt);
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
