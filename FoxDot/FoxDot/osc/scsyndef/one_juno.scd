// one_juno: One's Juno (synthwave's poly synth) as a FoxDot synth. Ported from one/src/modules/retro-units/juno/dsp.ts.
//  - One's polyBLEP oscillators, written out (they alias as One's do), from One's phases: the saw (0), with spread two
//    more (0.33, 0.67) at ∓ 25 spread cents, × 0.7; the pulse, its width pw + 0.45 pwm lfo (0.05..0.95); a square an
//    octave down (sub); noise; all × 1 / sqrt(1 + saw² (3 with spread) + pulse² + sub² + noise²)
//  - the LFO: a triangle from -1 at the note, fading in over ldelay; vibrato 2^(0.05 ovib lfo), PWM, cutoff (2 lcut oct)
//  - a one-pole high-pass at ohpf; tanh(1.2 x); the 24 dB low-pass: One's two state-variable stages (k 1.4, then
//    2 - 1.96 × 0.97 res) as the biquads they equal at a set cutoff (BLowPass, rq = k), cutoff moved per sample:
//    cutoff × 2^(7 fenv fe (0.6 + 0.4 vv) + kbd (note - 60)/12 + 2 lcut lfo)
//  - One's one-pole envelopes as one_sub's, but the decay as the release (3.45 d, curve -11.5: the same time constant,
//    run out at -100 dB, as One's is with sustain 0); × vv = 1 - velamp + velamp velo
//  - drive: tanh(m dg) × 0.5 / tanh(min(3, dg/2)), dg = 0.8 + 14 odrive² (no drive: tanh(0.8 m))
//  - pump: ducked at each beat (beat_dur, FoxDot's), back over 0.55 beat: × 1 - pump u², u = max(0, 1 - beat frac / 0.55);
//    bph is where in its beat the note starts (0: on the beat)
//  - the chorus (ochorus 1: I, 2: II, 3: I+II): two taps of a delay swept by a triangle in opposite directions, each
//    one-poled at 9 kHz, (dry + tap) × 0.75 left and right. One's taps read a fractional delay d as floor(d) + 2 - frac(d):
//    the same here (DelayL at that delay).
// Per note: One's drive, pump and chorus work on the sum of its voices, its LFO and chorus sweep run on from the unit's
// start (here each note has its own, from their start); the mono voice's legato glide is not here.
// Names as One's except hpf→ohpf, cut→cutoff, vib→ovib, chorus→ochorus, drive→odrive (FoxDot effects), vol→level,
// aa/ad/as/ar→aatk/adec/asus/arel, fa/fd/fs/fr→fatk/fdec/fsus/frel, vel→velamp; velo this note's velocity.
SynthDef.new(\one_juno, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	saw = 1, pulse = 0, pw = 0.5, pwm = 0, sub = 0, noise = 0, spread = 0, ohpf = 20, cutoff = 2000, res = 0.15, fenv = 0.3, kbd = 0.5,
	fatk = 0.005, fdec = 0.4, fsus = 0.3, frel = 0.4, aatk = 0.005, adec = 0.4, asus = 0.8, arel = 0.4,
	lrate = 4.5, ldelay = 0.4, ovib = 0, lcut = 0, ochorus = 2, odrive = 0, pump = 0, velamp = 0.5, velo = 0.8, level = -10, beat_dur = 0.5, bph = 0, choke = -1, gl = 0, ocut = -1|
	var sig, sr, t, note, gate, env, fe, ae, vv, lph, lf, f, dt, blep, ph, x, on3, w, pp, sq, tw, ps, s, mix, cut, k2, y, dg, m, fr, u;
	var mode, chRate, chDepth, chMid, cph, tri, tap, l, r;
	var chk, fxon;
	sus = Select.kr(gl > 0, [sus, gl * beat_dur]);   // the note's own length when FoxDot's sus is its life (gl, beats)
	freq = In.kr(bus, 1);
	sr = SampleRate.ir;
	note = freq.cpsmidi;
	t = Sweep.ar(0, 1);
	gate = Trig1.kr(1, sus);
	env = { |a, d, s, r| Env([0, 1, s, 0], [0.6 * a * 5.log, 3.45 * d, 3.45 * r], [5.log.neg, -11.5, -11.5], releaseNode: 2) };
	fe = EnvGen.ar(env.(fatk, fdec, fsus, frel), gate);
	ae = EnvGen.ar(env.(aatk, adec, asus, arel), gate);
	vv = 1 - velamp + (velamp * velo);
	// the LFO, a triangle from -1, faded in over ldelay
	lph = (Phasor.ar(DC.ar(0), lrate / sr) + (lrate / sr)).frac;
	lf = (1 - (4 * (lph - 0.5).abs)) * (t / ldelay.max(0.001)).min(1);
	f = freq * (2 ** (ovib * 0.05 * lf)); dt = f / sr;
	blep = { |p, d| var a = p / d, b = (p - 1) / d; ((p < d) * (a + a - (a * a) - 1)) + ((p > (1 - d)) * ((b * b) + b + b + 1)) };
	// One's oscillators: the step added before the phase is read
	ph = { |d, p0| (Phasor.ar(DC.ar(0), d) + d + p0).frac };
	on3 = spread > 0;
	x = [0, -1, 1].collect { |det, k|
		var d = dt * (2 ** (det * spread * 25 / 1200)), p = ph.(d, [0, 0.33, 0.67][k]);
		saw * ((2 * p) - 1 - blep.(p, d)) * (if(k > 0) { 0.7 * on3 } { 1 })
	}.sum;
	w = (pw + (pwm * 0.45 * lf)).clip(0.05, 0.95);
	pp = ph.(dt, 0);
	tw = pp - w + (pp < w);
	sq = ((pp < w) * 2) - 1 + blep.(pp, dt) - blep.(tw, dt);
	ps = ph.(dt * 0.5, 0);
	s = ((ps < 0.5) * 2) - 1 + blep.(ps, dt * 0.5) - blep.((ps + 0.5).frac, dt * 0.5);
	mix = 1 / (1 + (saw * saw * Select.kr(on3, [1, 3])) + (pulse * pulse) + (sub * sub) + (noise * noise)).sqrt;
	x = (x + (pulse * sq) + (sub * s) + (noise * WhiteNoise.ar)) * mix;
	// the high-pass, then the 24 dB low-pass
	x = x - OnePole.ar(x, exp(-2pi * ohpf / sr));
	cut = (cutoff * (2 ** ((fenv * fe * 7 * (0.6 + (0.4 * vv))) + (kbd * (note - 60) / 12) + (lcut * 2 * lf)))).clip(20, sr * 0.45);
	k2 = 2 - (1.96 * (res * 0.97).clip(0, 1));
	y = BLowPass.ar(BLowPass.ar((x * 1.2).tanh, cut, K2A.ar(1.4)), cut, K2A.ar(k2));
	m = y * ae * vv;
	dg = 0.8 + (14 * odrive * odrive);
	m = Select.ar(odrive > 0, [(m * 0.8).tanh, (m * dg).tanh * 0.5 / (dg * 0.5).min(3).tanh]);
	// the pump: ducked at each beat, back over half a beat
	fr = ((t / beat_dur) + bph).frac; u = (1 - (fr / 0.55)).max(0);
	m = m * (1 - (pump * u * u)) * level.dbamp;
	// the chorus
	mode = ochorus.round;
	chRate = Select.kr(mode, [0, 0.513, 0.863, 9.75]);
	chDepth = Select.kr(mode, [0, 0.0019, 0.0019, 0.0003]) * sr;
	chMid = Select.kr(mode >= 3, [0.0035, 0.0034]) * sr;
	cph = (Phasor.ar(DC.ar(0), chRate / sr) + (chRate / sr)).frac;
	tri = 1 - (4 * (cph - 0.5).abs);
	tap = { |d| var i = d.floor, fd = d - i; OnePole.ar(DelayL.ar(m, 0.01, (i + ((fd > 0) * (2 - fd))) / sr), exp(-2pi * 9000 / sr)) };
	l = Select.ar(mode > 0, [m, (m + tap.(chMid + (chDepth * tri))) * 0.75]) * amp;
	r = Select.ar(mode > 0, [m, (m + tap.(chMid - (chDepth * tri))) * 0.75]) * amp;
	FreeSelf.kr(TDelay.kr(Done.kr(ae), 0.02));
	// One's routing, as one_sub's: dry to FoxDot's bus, the sends to the buses oneFX.py's effects run on.
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
