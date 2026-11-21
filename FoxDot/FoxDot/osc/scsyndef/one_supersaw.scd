// one_supersaw: One's Supersaw as a FoxDot synth (a note is one of One's eight voices). Ported from
// src/modules/hardcore-units/supersaw/dsp.ts.
//  - seven polyBLEP saws (as One's) at freq × (1 + spread × detune), spread 0, ∓0.11, ∓0.063, ∓0.019; the middle one
//    × (1 - 0.6 omix), the six × 0.55 omix; panned linearly, the middle one centred, the pairs 0.5 ± 0.5 width (0.5 + 0.5 |spread| / 0.11)
//  - their phases: One draws them from its xorshift (seed 8000), so its first note always starts from the same seven:
//    those are here, for every note (One's later notes draw new ones)
//  - thin: One's state-variable high-pass (k 1.41) at freq × (0.5 + thin), as BHiPass; One's TPT low-pass as BLowPass
//    (rq = k = 2 - 1.96 res) at cutoff × 2^(5 fenv fe), fe = exp(-t / 0.3), each side
//  - the ADSR: One's one-poles (OnePole, the same coefficients): to 1.02 by aatk until it reaches 1 (aatk ln 51), then
//    to asus by adec, after sus to 0 by arel
// Renamed: cut→cutoff, mix→omix, vol→level, aa/ad/as/ar→aatk/adec/asus/arel; velo = this note's velocity.
// The Phasors take an audio-rate trigger (DC.ar(0)): with a scalar one, Phasor reads its rate once a block.
SynthDef.new(\one_supersaw, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	detune = 0.35, omix = 0.7, width = 0.8, thin = 0, cutoff = 6000, res = 0.1, fenv = 0.2,
	aatk = 0.005, adec = 0.4, asus = 0.8, arel = 0.3, velo = 0.8, level = -12, gl = 0, beat_dur = 0.5, ocut = -1|
	var sig;
	var sr = SampleRate.ir, sd = SampleDur.ir, blep, t, gate, att, env, a = 0, b = 0, k, hz, l, r, co;
	var spread = [0, -0.11, 0.11, -0.063, 0.063, -0.019, 0.019], phases = [0.495785248, 0.977603168, 0.979461586, 0.909017194, 0.195794652, 0.89993186, 0.669545894];
	var fxon;
	sus = Select.kr(gl > 0, [sus, gl * beat_dur]);   // the note's own length when FoxDot's sus is its life (gl, beats)
	freq = In.kr(bus, 1);
	blep = { |t, dt| var a = t / dt, b = (t - 1) / dt; ((t < dt) * ((a + a) - (a * a) - 1)) + ((t > (1 - dt)) * ((b * b) + b + b + 1)) };
	t = Sweep.ar(1, 1);
	gate = t < sus;
	att = gate * (t < (aatk.max(0.001) * 51.log));
	co = { |s| (-1 / (s * sr)).exp };
	env = OnePole.ar((att * 1.02) + ((gate - att) * asus),
		(att * co.(aatk.max(0.001))) + ((gate - att) * co.(adec.max(0.005))) + ((1 - gate) * co.(arel.max(0.005))));
	spread.do { |sp, j|
		var dt = freq * (1 + (sp * detune)) * sd, tt = (Phasor.ar(DC.ar(0), dt, 0, 1) + phases[j] + dt).frac;
		var s = ((2 * tt) - 1 - blep.(tt, dt)) * if(j == 0, { 1 - (omix * 0.6) }, { omix * 0.55 });
		var p = if(j == 0, 0.5, { 0.5 + (sp.sign * 0.5 * width * (0.5 + (0.5 * sp.abs / 0.11))) });
		a = a + (s * (1 - p)); b = b + (s * p);
	};
	a = Select.ar(thin > 0, [a, BHiPass.ar(a, freq * (0.5 + thin), 1.41)]);
	b = Select.ar(thin > 0, [b, BHiPass.ar(b, freq * (0.5 + thin), 1.41)]);
	k = 2 - (1.96 * res.clip(0, 1));
	hz = (cutoff * (2 ** (fenv * 5 * ((t + sd).neg / 0.3).exp))).clip(40, sr * 0.45);
	l = BLowPass.ar(a, hz, k) * env * velo * level.dbamp * 0.35 * amp;
	r = BLowPass.ar(b, hz, k) * env * velo * level.dbamp * 0.35 * amp;
	Line.kr(0, 0, sus + (9.3 * arel.max(0.005)) + 0.02, doneAction: 2);
	// One's routing, by name: dry goes to FoxDot's own bus, as any synth; the sends go to the buses oneFX.py's effects run
	// on: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14 (what a ducker listens to). With no dry sound
	// (dry = 0, a sound going only through an effect) FoxDot's bus gets an inaudible tone at half the sample rate while
	// the note lives, so FoxDot does not free it as silent.
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
