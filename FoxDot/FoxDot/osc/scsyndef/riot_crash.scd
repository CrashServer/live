// riot_crash: One's Riot Kit, its crash, as a FoxDot synth. Ported from one/src/modules/rock-units/riot/dsp.ts.
// One sums the eight voices, then drives the sum (tanh(1 + 6 odrive)): here each hit is driven alone, which is
// One exactly for a hit on its own (overlapping hits are driven a little less together than in One).
// Args as One's, per voice: tune (st), dec (× the voice's decay), lvl (dB), pan; the kit's odrive and level (dB);
// velo: the hit's velocity (One: 1 accented, 1 - acc / 2 otherwise).
SynthDef.new(\riot_crash, {
	|bus = 0, dry = 1, todrive = 0, toduck = 0, toecho = 0, tohall = 0, toaux = 0, side = 0, freq = 0, amp = 1, sus = 1, blur = 1, tune = 0, dec = 1, lvl = -12, pan = 0, odrive = 0.3, level = -4, velo = 1|
	var sig;
	var t = Sweep.ar(1, 1), tr = 2 ** (tune / 12), nz = WhiteNoise.ar, y, a, l, r, drv, svf, done, drop;
	var fxon;
	// One's TPT state-variable filter at a set cutoff: lp and hp as the bilinear biquads, bp from them.
	svf = { |x, hz, k| var lp = BLowPass.ar(x, hz, k), hp = BHiPass.ar(x, hz, k); [lp, (x - lp - hp) / k, hp] };
	// wider square waves (from 300 Hz) and more noise, band-passed at 7 kHz, high-passed at 4.5 kHz: a burst and a long wash
	y = (Mix(LFPulse.ar(300 * tr * [1, 1.342, 1.775, 2.13, 2.68, 3.17], 0, 0.5, 2, -1)) * 0.1) + (nz * 0.7);
	y = svf.(svf.(y, 7000 * tr, 0.8)[1], 4500 * tr, 1.0)[2] * (((t.neg / 0.02).exp * 0.6) + ((t.neg / (0.9 * dec)).exp * 0.8)) * 2;
	done = 4 * dec;
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
