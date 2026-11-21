// one_hardkick: One's Hardcore Kick as a FoxDot synth. Ported from src/modules/hardcore-units/hardkick/dsp.ts.
//  - a sine and its 2nd and 3rd harmonics (body) from phase zero, one phase for the three (a Phasor, as One's); the pitch
//    is the note + tune, thrown up punch semitones and falling back as exp(-t / ptime), sagging drop semitones over the tail
//  - the click: One's noise (its xorshift, seed 909) through its y = x - 0.6 y[-1], fading by 0.92 a sample: the
//    111 samples it lasts, exactly as One's first kick plays them (a Dseq)
//  - level exp(-t / 0.9 tail) × velo into the distortion: tanh(x dg) / tanh(dg), dg = 1 + 30 odrive², a hard clip at
//    1 - 0.75 clip, the fold mixed in; eased in over 0.5 ms, cut over 12 ms at the tail's end
//  - tone: two one-poles; lowcut: One's one-pole high-pass (FOS, the same coefficients)
// A kick is a one-shot: it plays its tail, whatever sus is. One's kick is one voice, a new kick cutting the last (faded
// in 2 ms): here each kick plays out its own tail.
// Renamed: drive→odrive, vol→level; velo = this note's velocity (0..1, before the distortion as in One).
// The Phasors take an audio-rate trigger (DC.ar(0)): with a scalar one, Phasor reads its rate once a block.
SynthDef.new(\one_hardkick, {
	|bus = 0, dry = 1, ins = -1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, pan = 0, blur = 1,
	tune = 0, punch = 36, ptime = 0.022, click = 0.5, body = 0.4, tail = 0.32, odrop = 3, odrive = 0.7, clip = 0.4, ofold = 0,
	tone = 7000, lowcut = 30, velo = 0.8, level = -8, choke = 0, ocut = -1|
	var sig;
	var sr = SampleRate.ir, t, f0, fr, w, x, dg, c, fk, g, y, ln;
	var fxon, cid, first, cur, cg;
	freq = In.kr(bus, 1);
	tail = tail.max(0.03);
	t = Sweep.ar(1, 1);
	f0 = freq * (2 ** (tune / 12));
	fr = f0 * (2 ** (((punch * (t.neg / ptime.max(0.002)).exp) - (odrop * (t / tail).min(1))) / 12));
	w = 2pi * (Phasor.ar(DC.ar(0), fr / sr, 0, 1) + (fr / sr));
	x = w.sin + (body * ((0.5 * (2 * w).sin) + (0.3 * (3 * w).sin)));
	x = x + (click * Duty.ar(SampleDur.ir, 0, Dseq([-1.066193,-0.1703685,0.08366848,0.1978797,0.1578117,-0.6395378,-0.2015532,0.3788615,0.05555229,0.3175799,-0.4501844,-0.06572492,0.3116458,0.02476475,0.2920369,0.1253316,-0.2682621,-0.02790527,-0.1624028,0.1812064,0.05930582,0.1085749,0.1274488,-0.1752331,0.06982646,-0.1873023,0.2160988,-0.1310957,0.1628656,-0.01345529,0.09249218,-0.04692531,0.01008693,-0.06863277,0.04991145,-0.08389904,0.08486615,-0.007955272,0.05013534,-0.06334877,-0.005461903,-0.02766528,0.04736377,-0.05288318,0.02514792,0.01177187,-0.0176972,-0.001209695,-0.01531725,0.006663486,0.003861244,-0.01284624,-0.0002799251,0.001433092,-0.001131523,-0.00588231,-0.00628172,-0.002944465,-0.0070103,0.01107536,0.0006460544,0.001888797,-0.005019935,0.001792664,0.0007130175,0.001820168,-0.001144554,-0.001880186,0.002226776,-0.0009634273,0.00346665,-0.004561206,0.004790768,-0.003478679,0.0000794444,0.0006053971,-0.0009594231,0.0007769112,-0.001251328,0.001503259,0.000435569,-0.001479343,0.001304891,-0.001767433,0.0007535053,-0.00005412197,0.0009376112,-0.0009558997,0.0004943744,0.0002494481,0.000160514,-0.0002696422,-0.0003120698,-0.0001938195,0.0002603941,0.0002267655,-0.00005444989,-0.00006937606,0.0002810901,0.0001310307,-0.0001417132,0.0002700566,-0.00003059415,-0.00001379759,-0.00003306408,-0.00001287687,-0.0000593094,-0.00003362148,-0.0001122752,0.00005526409,-0.000117371, 0], 1)));
	x = x * (t.neg / (0.9 * tail)).exp * velo;
	dg = 1 + (30 * odrive * odrive);
	x = (x * dg).tanh / dg.tanh;
	c = 1 - (0.75 * clip);
	x = (x / c).clip(-1, 1);
	fk = 1 + (3 * ofold);
	x = ((1 - ofold) * x) + (ofold * (x * fk * 0.5pi).sin);
	g = (t / 0.0005).min(1) * (1 - ((t - tail) / 0.012).max(0)).max(0);
	y = x * g;
	y = OnePole.ar(OnePole.ar(y, (-2pi * tone.clip(60, sr * 0.45) / sr).exp), (-2pi * tone.clip(60, sr * 0.45) / sr).exp);
	ln = (-2pi * lowcut.clip(10, 400) / sr).exp;
	y = FOS.ar(y, ln, ln.neg, ln);
	y = y * level.dbamp * amp;
	// One's Hard Kick is one voice: a new kick cuts the last with a 2 ms fade. Each kick writes an id of its own to control
	// bus 15400 + choke (one per unit: the exporter numbers them) in its first block; one that reads another id there
	// fades out over 2 ms and ends.
	cid = Rand(1, 1000000);
	first = Sweep.kr(1, 1) < (ControlDur.ir * 1.5);
	cur = In.kr(15400 + choke);
	ReplaceOut.kr(15400 + choke, Select.kr(first, [cur, cid]));
	cg = EnvGen.kr(Env.asr(0, 1, 0.002), (first + ((cur - cid).abs < 0.5)).min(1), doneAction: 2);
	y = y * cg;
	Line.kr(0, 0, tail + 0.012 + 0.15, doneAction: 2);
	// One's routing, by name: dry goes to FoxDot's own bus, as any synth; the sends go to the buses oneFX.py's effects run
	// on: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14 (what a ducker listens to). With no dry sound
	// (dry = 0, a sound going only through an effect) FoxDot's bus gets an inaudible tone at half the sample rate while
	// the note lives, so FoxDot does not free it as silent.
	sig = Balance2.ar(y, y, pan, 2.sqrt);
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
