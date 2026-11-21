// one_fx_bus: One's (Unreason's) EQ on the whole mix, as the songs' "Bus" unit (a low cut under the kick's
// fundamental before the Out). Reads the speakers (bus 0-1) and replaces them, so it runs last, after the notes and
// One's effects. Ported from unreason/src/devices/eq/dsp.ts: RBJ cookbook biquads; the cuts 4th-order Butterworth
// (two sections, Q 0.5412 and 1.3066), switched by lc / hc (0-1, a crossfade); low shelf, peak, high shelf; out gain.
// Then One's own way out (one/src/engine/worklet.ts): the Out's level (ovol, dB) and its limiter, which acts only on
// overs: the gain falls at once to keep the louder channel at 0.98 and comes back by 0.0002 of the way a sample (at
// 48 kHz; ~100 ms) - a peak follower of 1 - 0.98 / peak. limit=0 leaves it out.
SynthDef.new(\one_fx_bus, {
	|ovol = 0, limit = 1, lc = 0, lcf = 30, lsf = 120, lsg = 0, mf = 1000, mg = 0, mq = 0.7, hsf = 8000, hsg = 0, hc = 0, hcf = 18000, out = 0|
	var sr = SampleRate.ir, x, l, h, sos, pass, shelf, peak, pk, u;
	// a biquad from the cookbook's (b0 b1 b2 a0 a1 a2): SC's SOS adds b1 y1 + b2 y2, so the a's go in negated
	sos = { |sig, c| SOS.ar(sig, c[0] / c[3], c[1] / c[3], c[2] / c[3], c[4].neg / c[3], c[5].neg / c[3]) };
	pass = { |hi, f, q| var w = 2pi * f.clip(10, sr * 0.45) / sr, cs = cos(w), al = sin(w) / (2 * q), k = if(hi, 1 + cs, 1 - cs);
		[k / 2, if(hi, k.neg, k), k / 2, 1 + al, -2 * cs, 1 - al] };
	shelf = { |hi, f, g| var a = 10 ** (g / 40), w = 2pi * f.clip(10, sr * 0.45) / sr, cs = cos(w), s = if(hi, -1, 1),
		al = sin(w) / sqrt(2), r = 2 * sqrt(a) * al, p = a + 1, m = a - 1;
		[a * (p - (s * m * cs) + r), 2 * s * a * (m - (s * p * cs)), a * (p - (s * m * cs) - r), p + (s * m * cs) + r, -2 * s * (m + (s * p * cs)), p + (s * m * cs) - r] };
	peak = { |f, g, q| var a = 10 ** (g / 40), w = 2pi * f.clip(10, sr * 0.45) / sr, cs = cos(w), al = sin(w) / (2 * q);
		[1 + (al * a), -2 * cs, 1 - (al * a), 1 + (al / a), -2 * cs, 1 - (al / a)] };
	x = In.ar(0, 2);
	l = sos.(sos.(x, pass.(true, lcf, 0.5412)), pass.(true, lcf, 1.3066));
	x = x + ((l - x) * lc.clip(0, 1));
	x = sos.(sos.(sos.(x, shelf.(false, lsf, lsg)), peak.(mf, mg, mq)), shelf.(true, hsf, hsg));
	h = sos.(sos.(x, pass.(false, hcf, 0.5412)), pass.(false, hcf, 1.3066));
	x = x + ((h - x) * hc.clip(0, 1));
	x = x * out.dbamp * ovol.dbamp;
	pk = x[0].abs.max(x[1].abs);
	u = PeakFollower.ar((1 - (0.98 / pk.max(1e-9))).max(0), 0.9998 ** (48000 / sr));
	x = x * (1 - (u * (limit > 0)));
	ReplaceOut.ar(0, x);
}).add;
