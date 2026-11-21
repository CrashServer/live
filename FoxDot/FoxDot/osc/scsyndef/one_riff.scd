// one_riff: One's Riff (a guitar) as a FoxDot synth. Ported from one/src/modules/rock-units/riff/dsp.ts.
//  - strings: Pluck (Karplus-Strong), excited by WhiteNoise through OnePole (the pick) for one period; One's Riff runs
//    the same algorithm step for step. chord: 0 the note, 1 + the fifth, 2 + the fifth and the octave, 3 + the octave.
//    double: a second take (each string detune cents sharp) on the right.
//  - palm mute darkens the loop and the pick a little, and shortens the sustain (decay × (1 - 0.85 mute)).
//  - amp, built against fizz: tightened first (BHiPass 80 + 420 tight Hz, BLowPass 5 kHz, +3 tight dB at 800 Hz); two
//    gain stages, tanh(g1 x + 0.15) - tanh(0.15) with g1 = 1 + 14 gain, then (BHiPass 40, BLowPass 4.2 kHz) tanh(0.8 g2 x)
//    with g2 = 1 + 4 gain², × 1.4 / (1 + 1.5 gain); bass (shelf 120 Hz), mid (peak 750 Hz), treble (shelf 3 kHz); the
//    cabinet, a 4x12: BHiPass 80, +3 dB at 110 Hz, -3 dB at 450 Hz, +3 dB at 2.4 kHz, a 4th-order Butterworth low-pass at
//    4.5 kHz and BLowPass 6 kHz.
//  - the note rings until sus, then fades out over rel (linear), as One's does at the note's end.
// Names as One's (vol→level, mid→omid: mid is a FoxDot effect; vel is how much velocity counts, velo this note's velocity 0..1).
SynthDef.new(\one_riff, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	chord = 1, bright = 0.6, decay = 3, mute = 0, double = 0.6, detune = 8, rel = 0.06, gain = 0.6, bass = 0, omid = 0, treble = 0, cab = 1, vel = 0.6, velo = 0.8, level = -10, tight = 0.3, gl = 0, beat_dur = 0.5, ocut = -1|
	var sig, lc, ec, dec, va, ch, h2, a2, a3, up, str, a, b, g1, g2, chain, env, l, r;
	var fxon;
	sus = Select.kr(gl > 0, [sus, gl * beat_dur]);   // the note's own length when FoxDot's sus is its life (gl, beats)
	freq = In.kr(bus, 1);
	lc = 0.5 - (0.45 * bright); lc = lc + ((0.85 - lc) * mute * 0.5);
	ec = 0.8 * (1 - bright); ec = ec + ((0.9 - ec) * mute * 0.4);
	dec = decay * (1 - (0.85 * mute));
	va = 1 - vel + (vel * velo);
	ch = chord.round;
	h2 = Select.kr(ch, [7, 7, 7, 12]);
	a2 = ch > 0; a3 = ch.absdif(2) < 0.5;
	up = 2 ** (detune / 1200);
	str = { |f, k| Pluck.ar(OnePole.ar(WhiteNoise.ar, ec) * va * k, Impulse.ar(0), 0.05, (1 / f).clip(0.0005, 0.05), dec, lc) };
	a = str.(freq, 1) + str.(freq * (2 ** (h2 / 12)), a2) + str.(freq * 2, a3);
	b = str.(freq * up, 1) + str.(freq * up * (2 ** (h2 / 12)), a2) + str.(freq * up * 2, a3);
	g1 = 1 + (14 * gain); g2 = 1 + (4 * gain * gain);
	chain = { |x|
		var y = BPeakEQ.ar(BLowPass.ar(BHiPass.ar(x, 80 + (420 * tight), 1.41), 5000, 1.41), 800, 1, 3 * tight), c;
		y = (y * g1 + 0.15).tanh - 0.15.tanh;
		y = (BLowPass.ar(BHiPass.ar(y, 40, 1.41), 4200, 1.41) * g2 * 0.8).tanh * 1.4 / (1 + (1.5 * gain));
		y = BHiShelf.ar(BPeakEQ.ar(BLowShelf.ar(y, 120, 1, bass), 750, 1.1, omid), 3000, 1, treble);
		c = BPeakEQ.ar(BPeakEQ.ar(BPeakEQ.ar(BHiPass.ar(y, 80, 1), 110, 1.2, 3), 450, 1, -3), 2400, 1, 3);
		c = BLowPass.ar(BLowPass.ar(BLowPass.ar(c, 4500, 1.848), 4500, 0.765), 6000, 1.41);
		Select.ar(cab >= 0.5, [y, c])
	};
	env = EnvGen.ar(Env([1, 1, 0], [sus, rel]), doneAction: 2);
	l = chain.(a); r = chain.(((1 - double) * a) + (double * b));
	l = l * env * level.dbamp * amp; r = r * env * level.dbamp * amp;
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
