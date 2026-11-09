// one_riff: One's Riff (a guitar) as a FoxDot synth. Ported from one/src/modules/rock-units/riff/dsp.ts.
//  - strings: Pluck (Karplus-Strong), excited by WhiteNoise through OnePole (the pick) for one period; One's Riff runs
//    the same algorithm step for step. chord: 0 the note, 1 + the fifth, 2 + the fifth and the octave, 3 + the octave.
//    double: a second take (each string detune cents sharp) on the right.
//  - palm mute darkens the loop and the pick, and shortens the sustain (decay × (1 - 0.85 mute)).
//  - amp: BHiPass 90 Hz, then tanh(d x + 0.15) - tanh(0.15) with d = 1 + 80 gain², × 1 / (1 + 1.5 gain); bass (shelf
//    120 Hz), mid (peak 750 Hz), treble (shelf 3 kHz); the cabinet: BHiPass 75, BLowPass 4.8 kHz, +3 dB at 2.2 kHz.
//  - the note rings until sus, then fades out over rel (linear), as One's does at the note's end.
// Names as One's (vol→level, mid→omid: mid is a FoxDot effect; vel is how much velocity counts, velo this note's velocity 0..1).
SynthDef.new(\one_riff, {
	|bus = 0, dry = 1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	chord = 1, bright = 0.6, decay = 3, mute = 0, double = 0.6, detune = 8, rel = 0.06, gain = 0.6, bass = 0, omid = 0, treble = 0, cab = 1, vel = 0.6, velo = 0.8, level = -10|
	var sig, lc, ec, dec, va, ch, h2, a2, a3, up, str, a, b, d, chain, env, l, r;
	var fxon;
	freq = In.kr(bus, 1);
	lc = 0.5 - (0.45 * bright); lc = lc + ((0.95 - lc) * mute * 0.7);
	ec = 0.8 * (1 - bright); ec = ec + ((0.95 - ec) * mute * 0.5);
	dec = decay * (1 - (0.85 * mute));
	va = 1 - vel + (vel * velo);
	ch = chord.round;
	h2 = Select.kr(ch, [7, 7, 7, 12]);
	a2 = ch > 0; a3 = ch.absdif(2) < 0.5;
	up = 2 ** (detune / 1200);
	str = { |f, k| Pluck.ar(OnePole.ar(WhiteNoise.ar, ec) * va * k, Impulse.ar(0), 0.05, (1 / f).clip(0.0005, 0.05), dec, lc) };
	a = str.(freq, 1) + str.(freq * (2 ** (h2 / 12)), a2) + str.(freq * 2, a3);
	b = str.(freq * up, 1) + str.(freq * up * (2 ** (h2 / 12)), a2) + str.(freq * up * 2, a3);
	d = 1 + (80 * gain * gain);
	chain = { |x|
		var y = ((BHiPass.ar(x, 90, 1.2) * d + 0.15).tanh - 0.15.tanh) / (1 + (1.5 * gain));
		y = BHiShelf.ar(BPeakEQ.ar(BLowShelf.ar(y, 120, 1, bass), 750, 1.1, omid), 3000, 1, treble);
		Select.ar(cab >= 0.5, [y, BPeakEQ.ar(BLowPass.ar(BHiPass.ar(y, 75, 1), 4800, 1.1), 2200, 1, 3)])
	};
	env = EnvGen.ar(Env([1, 1, 0], [sus, rel]), doneAction: 2);
	l = chain.(a); r = chain.(((1 - double) * a) + (double * b));
	l = l * env * level.dbamp * amp; r = r * env * level.dbamp * amp;
	// One's routing, as one_sub's: dry to FoxDot's bus, the sends to the buses oneFX.py's effects run on.
	sig = Balance2.ar(l, r, pan, 2.sqrt);
	// an effect that is not running (oneFX.py sets control bus 15360 + its bus to 1 while it runs): a sound sent only
	// to effects (dry = 0) plays dry instead of not at all; with dry above 0 it only loses that effect.
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	ReplaceOut.ar(bus, Select.ar(dry > 0, [((LFPulse.ar(SampleRate.ir / 2) * 2) - 1) * 0.00012 ! 2, sig * dry]));
}).add;
