// one_fx_hall: One's (Unreason's) Hall as a persistent effect on a bus. Ported from unreason/src/devices/hall/dsp.ts.
// Reads stereo from inb (and clears it), writes to outb. One's network: a pre-delay, four all-pass diffusers (g 0.6),
// eight delay lines (29.7–73.1 ms × size) each damped by a one-pole low-pass, scaled to decay 60 dB in `decay` s,
// mixed by an 8×8 Hadamard (× 0.35355), the diffused input added (alternating sign); out: even lines left, odd right.
// The lines are fed back through LocalIn (one block), so each is read at its length minus a block: the same delay.
SynthDef.new(\one_fx_hall, {
	|inb = 8, outb = 0, outamt = 1, out2b = -1, out2amt = 0, pre = 15, size = 1, decay = 2.5, damp = 6000, width = 1, mix = 0.25|
	var sig;
	var sr = SampleRate.ir, bs = BlockSize.ir, ms = [29.7, 37.1, 41.1, 43.7, 53.0, 59.9, 67.7, 73.1],
		in, dl, dr, s, len, g, y, lp, x, h, w, l, r, m, sd, had;
	var on2;
	in = In.ar(inb, 2); dl = in[0]; dr = in[1];
	ReplaceOut.ar(inb, Silent.ar(2));
	s = DelayN.ar((dl + dr) * 0.5, 0.21, (pre * sr / 1000).floor.max(1) / sr);
	[4.7, 6.3, 8.9, 12.1].do { |d| var n = (d * sr / 1000).ceil - 1; s = AllpassN.ar(s, 0.02, n / sr, n / sr * 13.523) };
	len = ms.collect { |d| (d * size * sr / 1000).floor.clip(1, (d * 2.05 * sr / 1000).ceil - 1) };
	g = len.collect { |n| 10 ** (-3 * n / (decay * sr)) };
	y = LocalIn.ar(8);
	y = y.collect { |v, k| DelayN.ar(v, 0.16, (len[k] - bs).max(0) / sr) };
	lp = y.collect { |v| OnePole.ar(v, (-2pi * damp / sr).exp) };
	x = lp * g;
	had = { |v| var a = v.copy; [1, 2, 4].do { |hh| var b = a.copy; (0, hh * 2 .. 7).do { |k| (k .. k + hh - 1).do { |j| b[j] = a[j] + a[j + hh]; b[j + hh] = a[j] - a[j + hh] } }; a = b }; a };
	h = had.(x);
	w = h.collect { |v, k| (v * 0.35355) + (s * 0.5 * (if (k.odd) { -1 } { 1 })) };
	LocalOut.ar(w);
	l = lp[0] + lp[2] + lp[4] + lp[6]; r = lp[1] + lp[3] + lp[5] + lp[7];
	m = (l + r) * 0.5; sd = (l - r) * 0.5 * width;
	// Out at outamt, and a second output (One: an effect cabled to two places, e.g. the Echo into the Hall and the Out).
	sig = [(dl * (1 - mix)) + ((m + sd) * mix * 0.5), (dr * (1 - mix)) + ((m - sd) * mix * 0.5)];
	// sent only into another effect (outamt 0) that is not running: to the speakers instead
	on2 = In.kr(15360 + out2b.max(0)) * (out2b >= 0);
	outamt = outamt + ((outamt <= 0) * out2amt * (1 - on2));
	Out.ar(outb, sig * outamt);
	Out.ar(out2b.max(0), sig * out2amt * (out2b >= 0));
}).add;
