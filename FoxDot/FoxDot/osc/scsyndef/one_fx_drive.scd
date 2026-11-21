// one_fx_drive: One's (Unreason's) Drive as a persistent insert on a bus. Ported from unreason/src/devices/drive/dsp.ts.
// Reads stereo from inb (and clears it), writes to outb. Shapes: 0 tape (tanh), 1 tube (asymmetric), 2 hard clip,
// 3 fold (sin), 4 fuzz (biased tanh); gain up to 34/34/30/26/36 dB × drive, out level × gain^-0.4 as One's; then One's
// DC blocker (12 Hz) and tone low-pass (its TPT filter, k 1.41). As One, the shaper is smoothed by its integral
// (first-order antiderivative anti-aliasing).
SynthDef.new(\one_fx_drive, {
	|inb = 2, outb = 0, outamt = 1, out2b = -1, out2amt = 0, out3b = -1, out3amt = 0, type = 0, drive = 0.4, tone = 9000, level = 0, mix = 1|
	var sig;
	var sr = SampleRate.ir, in, db, g, x, y, t, shp, lc, ad, dx;
	var on2, on3;
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
	// Out at outamt, and a second output (One: an effect cabled to two places, e.g. the Echo into the Hall and the Out).
	sig = in + ((y - in) * mix);
	// sent only into another effect (outamt 0) that is not running: to the speakers instead
	on2 = In.kr(15360 + out2b.max(0)) * (out2b >= 0);
	on3 = In.kr(15360 + out3b.max(0)) * (out3b >= 0);
	outamt = outamt + ((outamt <= 0) * ((out2amt * (1 - on2)) + (out3amt * (1 - on3) * (out3b >= 0))));
	Out.ar(outb, sig * outamt);
	Out.ar(out2b.max(0), sig * out2amt * (out2b >= 0));
	// and a third (the Echo into the Hall and the Duck)
	Out.ar(out3b.max(0), sig * out3amt * (out3b >= 0));
}).add;
