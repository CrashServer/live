// one_fx_drive: One's (Unreason's) Drive as a persistent insert on a bus. Ported from unreason/src/devices/drive/dsp.ts.
// Reads stereo from inb (and clears it), writes to outb. Shapes: 0 tape (tanh), 1 tube (asymmetric), 2 hard clip,
// 3 fold (sin), 4 fuzz (biased tanh); gain up to 34/34/30/26/36 dB × drive, out level × gain^-0.4 as One's; then One's
// DC blocker (12 Hz) and tone low-pass (its TPT filter, k 1.41). One also smooths the shaper by its integral (ADAA):
// not here, so the top end aliases a little more.
SynthDef.new(\one_fx_drive, {
	|inb = 2, outb = 0, outamt = 1, out2b = -1, out2amt = 0, type = 0, drive = 0.4, tone = 9000, level = 0, mix = 1|
	var sig;
	var sr = SampleRate.ir, in, db, g, x, y, t;
	var on2;
	in = In.ar(inb, 2);
	ReplaceOut.ar(inb, Silent.ar(2));
	t = type.round.clip(0, 4);
	db = Select.kr(t, [34, 34, 30, 26, 36]);
	g = Lag.kr((drive.clip(0, 1) * db).dbamp, 6.9 / (2pi * 30));
	x = in * g;
	y = Select.ar(t, [x.tanh, ((x >= 0) * (1 - x.neg.exp)) + ((x < 0) * ((1 - (0.6 * x).exp).neg / 0.6)), x.clip2(1), x.sin, (x + 0.4).tanh]);
	y = LeakDC.ar(y, 1 - (2pi * 12 / sr));
	y = BLowPass.ar(y, tone.clip(20, sr * 0.45), 1.41) * level.dbamp * (g ** -0.4);
	// Out at outamt, and a second output (One: an effect cabled to two places, e.g. the Echo into the Hall and the Out).
	sig = in + ((y - in) * mix);
	// sent only into another effect (outamt 0) that is not running: to the speakers instead
	on2 = In.kr(15360 + out2b.max(0)) * (out2b >= 0);
	outamt = outamt + ((outamt <= 0) * out2amt * (1 - on2));
	Out.ar(outb, sig * outamt);
	Out.ar(out2b.max(0), sig * out2amt * (out2b >= 0));
}).add;
