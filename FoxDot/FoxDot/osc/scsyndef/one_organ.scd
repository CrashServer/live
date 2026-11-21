// one_organ: One's Organ (a tonewheel organ) as a FoxDot synth. Ported from one/src/modules/trap-units/organ/dsp.ts.
//  - nine sines at the drawbars' footages (ratios 0.5 1.5 1 2 3 4 5 6 8), each at 10^((d - 8) 3/20) (0: off), from the
//    phases One's first voice has (its seeded rng(1935)), × 0.35 / max(1, sqrt(2 Σ bars))
//  - the percussion: the third harmonic's wheel (2⅔') × perc × 0.9, dying with time constant 0.15 + 0.8 pdecay
//  - keyed on linearly over attack, off linearly over release + 5 ms
//  - the click: noise × a 0.985-per-sample decay through One's state-variable band-pass at 2.6 kHz (k 1.2: the bilinear
//    band-pass it equals, BBandPass), × click × 0.06
//  - overdrive: tanh(m dg) / tanh(min(3, 0.6 dg)), dg = 1 + 10 odrive²
//  - the Leslie: crossover at 800 Hz (One's SVF low-pass, k 1.41: BLowPass, rq = k); the horn (above) and the drum
//    (below) each a moving delay, level and side, their rotors from where One's start (horn 0, drum 0.25) at One's
//    starting speeds (0.8, 0.7 Hz), moving to chorale (0.8, 0.66) or tremolo (6.7, 5.9) with time constants 0.15 s and
//    0.875 s. One's taps read a fractional delay d as floor(d) + 2 - frac(d): the same here (DelayL at that delay).
// Per note: One's overdrive and Leslie work on the sum of its voices (here each note has its own, and its rotors start
// with the note); the click's noise is random here.
// Names as One's except drive→odrive, vol→level (FoxDot effects).
SynthDef.new(\one_organ, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	d1 = 8, d2 = 8, d3 = 8, d4 = 0, d5 = 0, d6 = 0, d7 = 0, d8 = 0, d9 = 0,
	perc = 0, pdecay = 0.3, click = 0.4, attack = 0.004, release = 0.03, odrive = 0.15, leslie = 0.7, speed = 0, level = -10, gl = 0, beat_dur = 0.5, ocut = -1|
	var sig, sr, t, bars, norm, ph0, ratio, wheels, x, env, ck, dg, m, fast, hornT, drumT, hornHz, drumHz, hornPh, drumPh;
	var lo, hi, hs, hc, ds, ms, tap, hl, hr, amH, amD, dl, l, r;
	var fxon;
	sus = Select.kr(gl > 0, [sus, gl * beat_dur]);   // the note's own length when FoxDot's sus is its life (gl, beats)
	freq = In.kr(bus, 1);
	sr = SampleRate.ir;
	t = Sweep.ar(0, 1);
	ratio = [0.5, 1.5, 1, 2, 3, 4, 5, 6, 8];
	ph0 = [0.1203170, 0.0004174635, 0.02945925, 0.1975305, 0.1544959, 0.3705125, 0.1045449, 0.9903493, 0.6376688];
	bars = [d1, d2, d3, d4, d5, d6, d7, d8, d9].collect { |d| (d > 0) * (10 ** ((d - 8) * 3 / 20)) };
	norm = 0.35 / (bars.sum * 2).sqrt.max(1);
	// One adds the step before it reads the phase: each wheel's first sample is at ph0 + its step
	wheels = ratio.collect { |k, i| SinOsc.ar(freq * k, 2pi * (ph0[i] + (freq * k / sr)).frac) };
	x = (wheels * bars).sum + (perc * exp(t.neg / (0.15 + (pdecay * 0.8))) * wheels[4] * 0.9);
	env = EnvGen.ar(Env([0, 1, 0], [attack.max(1 / sr), release + 0.005], \lin, releaseNode: 1), Trig1.kr(1, sus));
	ck = (0.985 ** (t * sr - 1)) * (t * sr < 459);
	m = (x * env * norm) + (click * BBandPass.ar(ck * WhiteNoise.ar, 2600, (0.6 + 1.36.sqrt).log * 2 / 2.log * sin(2pi * 2600 / sr) / (2pi * 2600 / sr)) / 1.2 * 0.06);
	dg = 1 + (10 * odrive * odrive);
	m = (m * dg).tanh / (dg * 0.6).min(3).tanh;
	// the Leslie
	fast = speed > 0.5;
	hornT = Select.kr(fast, [0.8, 6.7]); drumT = Select.kr(fast, [0.66, 5.9]);
	hornHz = hornT + ((0.8 - hornT) * exp(t.neg / 0.15));
	drumHz = drumT + ((0.7 - drumT) * exp(t.neg / 0.875));
	hornPh = (Phasor.ar(DC.ar(0), hornHz / sr) + (hornHz / sr)).frac;
	drumPh = (Phasor.ar(DC.ar(0), drumHz / sr) + (drumHz / sr) + 0.25).frac;
	lo = BLowPass.ar(m, 800, 1.41); hi = m - lo;
	hs = sin(2pi * hornPh); hc = sin(2pi * (hornPh + 0.25)); ds = sin(2pi * drumPh);
	ms = 0.0006 * sr * leslie;
	tap = { |in, d| var i = d.floor, f = d - i; DelayL.ar(in, 0.01, (i + ((f > 0) * (2 - f))) / sr) };
	hl = tap.(hi, 2 + (ms * (1 + hs))); hr = tap.(hi, 2 + (ms * (1 - hs)));
	amH = 1 - (0.35 * leslie * (0.5 + (0.5 * hc))); amD = 1 - (0.18 * leslie * (0.5 + (0.5 * ds)));
	dl = tap.(lo, 2 + (ms * 0.4 * (1 + ds))) * amD;
	l = (hl * amH * (1 + (0.3 * leslie * hc))) + (dl * (1 + (0.15 * leslie * ds)));
	r = (hr * amH * (1 - (0.3 * leslie * hc))) + (dl * (1 - (0.15 * leslie * ds)));
	l = (l * level.dbamp).clip2(2) * amp; r = (r * level.dbamp).clip2(2) * amp;
	FreeSelf.kr(TDelay.kr(Done.kr(env), 0.01));
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
