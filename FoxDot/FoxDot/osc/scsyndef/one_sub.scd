// one_sub: One's (and Unreason's) Sub as a FoxDot synth. Ported from unreason/src/devices/sub/dsp.ts.
//  - oscillators: saw / square / triangle / sine (osc 1 an octave shift, osc 2 semitones + cents), noise
//  - drive: tanh(x * (1 + 8 odrive)) / tanh(1 + 8 odrive), before the filter, as in One
//  - filter: One's TPT state-variable filter. For a set cutoff its low- and high-pass are exactly the
//    bilinear biquads BLowPass / BHiPass with rq = k (k = 2 - 1.96 res); band-pass = (x - lp - hp) / k.
//  - envelopes: One's are one-pole curves; these segments follow them (attack to 1 along a curve aimed at
//    1.25: -ln 5; decay 5 time constants of 0.3 d: -5; release 3.45 r: -11.5), released at sus.
//  - cutoff = cutoff * 2^(6 fenv env + kbd (note - 60)/12 + 4 lcut lfo + 5 cutcv), as in One (cutcv: its cutoff CV input, this note's).
//  - a Wobble (One's LFO) cabled into that input: cvw its shape (sine, tri, saw up, saw down, square, random, smooth),
//    cvrate in Hz, cvdepth (its depth × the cable's amount), cvph where it is in its cycle when the note starts.
// SC's Saw and Pulse are ±0.5 (×2 here), Balance2 is −3 dB at the centre (×√2): levels as One's.
// Names that are FoxDot effects or Python words are renamed: cut→cutoff, mix→omix, drive→odrive, vol→level,
// aa/ad/as/ar→aatk/adec/asus/arel, fa/fd/fs/fr→fatk/fdec/fsus/frel, vel→velo (this note's velocity 0..1).
SynthDef.new(\one_sub, {
	|bus = 0, dry = 1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	w1 = 0, oct1 = 0, w2 = 1, semi2 = 0, fine2 = 7, omix = 0.5, noise = 0,
	ftype = 0, cutoff = 1200, res = 0.3, fenv = 0.4, kbd = 0.5, odrive = 0.1,
	fatk = 0.005, fdec = 0.25, fsus = 0.2, frel = 0.2,
	aatk = 0.003, adec = 0.3, asus = 0.7, arel = 0.15,
	lw = 0, lrate = 4, lpitch = 0, lcut = 0, cutcv = 0, cvw = 0, cvrate = 1, cvdepth = 0, cvph = 0, vel = 0.6, velo = 0.8, level = -8|
	var sig;
	var note, lfo, cvp, cvl, pm, f, o1, o2, x, k, drv, fe, ae, oct, hz, lp, hp, bp, y, gate, env;
	var fxon;
	freq = In.kr(bus, 1);
	note = freq.cpsmidi;
	gate = Trig1.kr(1, sus);
	env = { |a, d, s, r| Env([0, 1, s, 0], [0.6 * a * 5.log, 1.5 * d, 3.45 * r], [5.log.neg, -5, -11.5], releaseNode: 2) };
	fe = EnvGen.kr(env.(fatk, fdec, fsus, frel), gate);
	ae = EnvGen.ar(env.(aatk, adec, asus, arel), gate, doneAction: 2);
	lfo = Select.kr(lw, [SinOsc.kr(lrate, Rand(0, 2pi)), LFTri.kr(lrate, Rand(0, 4)), LFPulse.kr(lrate, Rand(0, 1)) * 2 - 1, LFNoise0.kr(lrate)]);
	cvp = (Sweep.kr(0, cvrate) + cvph).frac;
	cvl = Select.kr(cvw, [sin(2pi * cvp), 1 - (4 * (cvp - 0.5).abs), (2 * cvp) - 1, 1 - (2 * cvp), (cvp < 0.5) * 2 - 1, LFNoise0.kr(cvrate), LFNoise1.kr(cvrate)]);
	pm = 2 ** (lfo * lpitch / 12);
	f = freq * pm;
	o1 = Select.ar(w1, [Saw.ar(f * (2 ** oct1), 2), Pulse.ar(f * (2 ** oct1), 0.5, 2), LFTri.ar(f * (2 ** oct1)), SinOsc.ar(f * (2 ** oct1))]);
	o2 = Select.ar(w2, [Saw.ar(f * (2 ** ((semi2 + (fine2 / 100)) / 12)), 2), Pulse.ar(f * (2 ** ((semi2 + (fine2 / 100)) / 12)), 0.5, 2), LFTri.ar(f * (2 ** ((semi2 + (fine2 / 100)) / 12))), SinOsc.ar(f * (2 ** ((semi2 + (fine2 / 100)) / 12)))]);
	x = (o1 * (1 - omix)) + (o2 * omix) + (WhiteNoise.ar * noise);
	drv = 1 + (odrive * 8);
	x = (x * drv).tanh / drv.tanh;
	k = 2 - (1.96 * res.clip(0, 1));
	oct = (6 * fenv * fe) + (kbd * (note - 60) / 12) + (4 * lcut * lfo) + (5 * (cutcv + (cvdepth * cvl)));
	hz = (cutoff * (2 ** oct)).clip(10, SampleRate.ir * 0.45);
	lp = BLowPass.ar(x, hz, k);
	hp = BHiPass.ar(x, hz, k);
	bp = (x - lp - hp) / k;
	y = Select.ar(ftype, [lp, bp, hp]) * ae * (1 - vel + (vel * velo)) * level.dbamp * 0.5 * amp;
	// One spreads its voices a little (the first: 12 % left, when osc 2 is in): a note here is that first voice.
	// One's routing, by name: dry goes to FoxDot's own bus, as any synth; the sends go to the buses oneFX.py's effects run
	// on: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14 (what a ducker listens to). With no dry sound
	// (dry = 0, a sound going only through an effect) FoxDot's bus gets an inaudible tone at half the sample rate while
	// the note lives, so FoxDot does not free it as silent.
	sig = Balance2.ar(y * (1 + (0.12 * (omix > 0))), y * (1 - (0.12 * (omix > 0))), pan, 2.sqrt);
	// an effect that is not running (oneFX.py sets control bus 15360 + its bus to 1 while it runs): a sound sent only
	// to effects (dry = 0) plays dry instead of not at all; with dry above 0 it only loses that effect.
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	ReplaceOut.ar(bus, Select.ar(dry > 0, [((LFPulse.ar(SampleRate.ir / 2) * 2) - 1) * 0.00012 ! 2, sig * dry]));
}).add;
