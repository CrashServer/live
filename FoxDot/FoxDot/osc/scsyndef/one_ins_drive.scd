// one_ins_drive: One's Drive as an insert on one sound (One: a unit cabled into a Drive, the Drive into the mix), on a
// bus of its own (oneFX.py's fx_insert gives it one): the player's dry path goes to `inb` (its `ins` arg), this drives
// it and sends it on as an instrument does: dry to `outb` (0, the speakers; or the next insert's bus), and One's sends
// (todrive 2, toduck 6, tohall 8, toecho 10, toaux 12, side 14). Same shaping as one_fx_drive (unreason/src/devices/drive/dsp.ts).
SynthDef.new(\one_ins_drive, {
	|inb = 900, outb = 0, dry = 1, todrive = 0, toduck = 0, tohall = 0, toecho = 0, toaux = 0, side = 0, type = 0, drive = 0.4, tone = 9000, level = 0, mix = 1|
	var sr = SampleRate.ir, in, db, g, x, y, t, shp, lc, ad, dx, sig, fxon;
	in = In.ar(inb, 2);
	ReplaceOut.ar(inb, Silent.ar(2));
	t = type.round.clip(0, 4);
	db = Select.kr(t, [34, 34, 30, 26, 36]);
	g = Lag.kr((drive.clip(0, 1) * db).dbamp, 6.9 / (2pi * 30));
	x = in * g;
	// One's first-order antiderivative anti-aliasing: each shape's integral F, the output (F(x) - F(x[-1])) / (x - x[-1]),
	// or the shape at the midpoint when the step is too small to divide by (float32 here: below 1e-3)
	shp = { |v| Select.ar(t, [v.tanh, ((v >= 0) * (1 - v.neg.exp)) + ((v < 0) * ((1 - (0.6 * v).exp).neg / 0.6)), v.clip2(1), v.sin, (v + 0.4).tanh]) };
	lc = { |v| v.abs + (1 + (-2 * v.abs).exp).log - 2.log };
	ad = Select.ar(t, [lc.(x), ((x >= 0) * (x + x.neg.exp - 1)) + ((x < 0) * ((x.neg / 0.6) + (((0.6 * x).exp - 1) / 0.36))),
		Select.ar(x.abs <= 1, [x.abs - 0.5, 0.5 * x * x]), x.cos.neg, lc.(x + 0.4)]);
	dx = x - Delay1.ar(x);
	y = Select.ar(dx.abs > 1e-3, [shp.(x - (dx * 0.5)), (ad - Delay1.ar(ad)) / dx.abs.max(1e-3) * dx.sign]);
	y = LeakDC.ar(y, 1 - (2pi * 12 / sr));
	y = BLowPass.ar(y, tone.clip(20, sr * 0.45), 1.41) * level.dbamp * (g ** -0.4);
	sig = in + ((y - in) * mix);
	// sent only to effects that are not running: to the speakers instead (as One's instruments)
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	Out.ar(outb, sig * dry);
}).add;
