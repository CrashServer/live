// riot_snare: One's Riot Kit, its snare, as a FoxDot synth. Ported from one/src/modules/rock-units/riot/dsp.ts.
// One sums the eight voices, then drives the sum (tanh(1 + 6 odrive)): here each hit is driven alone, which is
// One exactly for a hit on its own (overlapping hits are driven a little less together than in One).
// Args as One's, per voice: tune (st), dec (× the voice's decay), lvl (dB), pan; the kit's odrive and level (dB);
// velo: the hit's velocity (One: 1 accented, 1 - acc / 2 otherwise).
SynthDef.new(\riot_snare, {
	|bus = 0, dry = 1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, blur = 1, tune = 0, dec = 1, lvl = -3, pan = 0, odrive = 0.3, level = -4, velo = 1|
	var sig;
	var t = Sweep.ar(1, 1), tr = 2 ** (tune / 12), nz = WhiteNoise.ar, y, a, l, r, drv, svf, done, drop;
	var fxon;
	// One's TPT state-variable filter at a set cutoff: lp and hp as the bilinear biquads, bp from them.
	svf = { |x, hz, k| var lp = BLowPass.ar(x, hz, k), hp = BHiPass.ar(x, hz, k); [lp, (x - lp - hp) / k, hp] };
	// two drum modes (180, 330 Hz, falling a little), the wires (noise high-passed at 1.8 kHz), the stick's crack
	drop = 1 + (0.4 * (t.neg / 0.008).exp);
	y = (((SinOsc.ar(180 * tr * drop) * 0.55) + (SinOsc.ar(330 * tr * drop) * 0.35)) * (t.neg / (0.07 * dec)).exp)
		+ (svf.(nz, 1800 * tr, 1.0)[2] * (t.neg / (0.18 * dec)).exp * 1.3) + (nz * (t.neg / 0.0015).exp * 0.6);
	done = 1.2 * dec;
	y = y * velo;
	a = (pan.clip(-1, 1) + 1) * pi / 4;
	drv = 1 + (odrive * 6);
	l = (y * a.cos * lvl.dbamp * drv).tanh / drv.tanh;
	r = (y * a.sin * lvl.dbamp * drv).tanh / drv.tanh;
	Line.kr(0, 1, done, doneAction: 2);
	// One's routing, by name: dry goes to FoxDot's own bus, as any synth; the sends go to the buses oneFX.py's effects run
	// on: todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14 (what a ducker listens to). With no dry sound
	// (dry = 0, a sound going only through an effect) FoxDot's bus gets an inaudible tone at half the sample rate while
	// the note lives, so FoxDot does not free it as silent.
	sig = [l, r] * level.dbamp * 2.sqrt * amp;
	// an effect that is not running (oneFX.py sets control bus 15360 + its bus to 1 while it runs): a sound sent only
	// to effects (dry = 0) plays dry instead of not at all; with dry above 0 it only loses that effect.
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	ReplaceOut.ar(bus, Select.ar(dry > 0, [((LFPulse.ar(SampleRate.ir / 2) * 2) - 1) * 0.00012 ! 2, sig * dry]));
}).add;
