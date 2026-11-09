// one_chip: One's (Unreason's) Chip, an 8-bit voice, as a FoxDot synth. Ported from unreason/src/devices/chip/dsp.ts.
//  - waves: 0-2 pulses of 12.5 / 25 / 50 % duty (band-limited, DC removed, as in One; pwm moves the duty at 1.5 Hz),
//    3 the 4-bit triangle, 4 noise (One's 15-bit LFSR clocked at 16× the note: random steps at that rate here),
//    5 metal (the LFSR's short loop: its exact 93-step sequence, after the same start)
//  - volume: linear attack, one-pole decay and release (time constants 0.2 d, 0.2 r), in 16 / 8 / 4 steps as chosen
//  - pitch: the sweep gliding home (exp(-t / sweept)), the vibrato after its delay (in over 0.2 s), the arpeggio
//    (One's 'held' arpeggio needs the other held notes: here it plays the note alone)
//  - soft: One's one-pole smoothing of the wave
// Renamed: vib→ovib (a FoxDot effect), vol→level, aa/ad/as/ar→aatk/adec/asus/arel, vel→velamp, velo = this note's velocity.
SynthDef.new(\one_chip, {
	|bus = 0, dry = 1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	wave = 1, pwm = 0, soft = 0.2, arp = 0, arphz = 50, sweep = 0, sweept = 0.1, ovib = 0, vibhz = 5.5, vibd = 0.25,
	aatk = 0.001, adec = 0.3, asus = 0.5, arel = 0.1, steps = 1, velamp = 0.3, velo = 0.8, level = -8|
	var sig;
	var t, gate, e, q, note, st, step, arpOff, f, w, duty, x, y;
	var fxon;
	freq = In.kr(bus, 1);
	note = freq.cpsmidi;
	t = Sweep.kr(1, 1);
	gate = Trig1.kr(1, sus);
	e = EnvGen.ar(Env([0, 1, asus, 0], [aatk, 1.0 * adec, 1.842 * arel], [0, -5, -9.2], releaseNode: 2), gate, doneAction: 2);
	q = Select.kr(steps, [0, 15, 7, 3]);
	e = Select.ar(q > 0, [e, (e * q).round / q.max(1)]);
	step = (t * arphz).floor;
	arpOff = Select.kr(arp.round, [0, 0,
		Select.kr(step % 2, [0, 12]), Select.kr(step % 3, [0, 7, 12]), Select.kr(step % 3, [0, 4, 7]), Select.kr(step % 3, [0, 3, 7]),
		Select.kr(step % 3, [0, 5, 7]), Select.kr(step % 4, [0, 4, 7, 11]), Select.kr(step % 4, [0, 3, 7, 10])]);
	st = note + (sweep * (t.neg / sweept).exp) + arpOff
		+ ((ovib / 100) * SinOsc.kr(vibhz, 0) * ((t - vibd) / 0.2).clip(0, 1));
	f = st.midicps;
	w = wave.round;
	duty = (Select.kr(w.min(2), [0.125, 0.25, 0.5]) + (pwm * SinOsc.kr(1.5))).clip(0.05, 0.95);
	x = Select.ar(w, [
		Pulse.ar(f, duty, 2), Pulse.ar(f, duty, 2), Pulse.ar(f, duty, 2),
		(LFTri.ar(f, 1) * 8).round / 8,
		LFNoise0.ar(f * 16).sign,
		Duty.ar(1 / (f * 16), 0, Dseq([Dseq([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1], 1), Dseq([-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1], inf)]))
	]);
	x = OnePole.ar(x, 1 - (1 - (soft * 0.9)));
	y = x * e * (1 - velamp + (velamp * velo)) * level.dbamp * 0.5 * amp;
	// One's routing, by name: dry goes to FoxDot's own bus, as any synth; the sends go to the buses oneFX.py's effects run
	// on: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14 (what a ducker listens to). With no dry sound
	// (dry = 0, a sound going only through an effect) FoxDot's bus gets an inaudible tone at half the sample rate while
	// the note lives, so FoxDot does not free it as silent.
	sig = Balance2.ar(y, y, pan, 2.sqrt);
	// an effect that is not running (oneFX.py sets control bus 15360 + its bus to 1 while it runs): a sound sent only
	// to effects (dry = 0) plays dry instead of not at all; with dry above 0 it only loses that effect.
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	ReplaceOut.ar(bus, Select.ar(dry > 0, [((LFPulse.ar(SampleRate.ir / 2) * 2) - 1) * 0.00012 ! 2, sig * dry]));
}).add;
