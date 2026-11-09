// one_fx_squash: One's (Unreason's) Squash compressor as a persistent effect on a bus, with its side input.
// Ported from unreason/src/devices/comp/dsp.ts. Reads stereo from inb and from sideb (and clears both), writes to outb.
// key: 1 listens to the input, 2 to the side (One's 'auto' is decided by the exporter: side when something is cabled).
// The gain computer with a soft knee as One's; the release-held peak (One: max(want, a_r y + (1 - a_r) want)) as a
// peak follower floored by what is wanted, then the attack smoothing (one-pole); gain(dB), makeup, mix as One's.
SynthDef.new(\one_fx_squash, {
	|inb = 12, sideb = 14, outb = 0, outamt = 1, out2b = -1, out2amt = 0, thr = -18, ratio = 4, att = 5, rel = 150, knee = 6, gain = 0, key = 2, mix = 1|
	var sig;
	var sr = SampleRate.ir, in, side, k, lvl, o, rr, soft, hard, c1, c2, want, aa, ar, y1, gr, g, w;
	var on2;
	in = In.ar(inb, 2); side = In.ar(sideb, 2);
	ReplaceOut.ar(inb, Silent.ar(2)); ReplaceOut.ar(sideb, Silent.ar(2));
	k = Select.ar(key >= 2, [in, side]);
	lvl = max(max(k[0].abs, k[1].abs), 1e-6).ampdb;
	o = lvl - thr; rr = 1 - (1 / ratio.max(1));
	hard = o * rr;
	soft = rr * ((o + (knee / 2)) ** 2) / (2 * knee.max(1e-6));
	c1 = (2 * o) < knee.neg;
	c2 = ((2 * o.abs) <= knee) * (knee > 0);
	want = (1 - c1) * ((c2 * soft) + ((1 - c2) * hard));
	ar = (-1 / (sr * rel / 1000)).exp; aa = (-1 / (sr * att / 1000)).exp;
	y1 = max(want, PeakFollower.ar(want, ar));
	gr = OnePole.ar(y1, aa);
	g = gr.neg.dbamp;
	w = (g * gain.dbamp * mix) + 1 - mix;
	// Out at outamt, and a second output (One: an effect cabled to two places, e.g. the Echo into the Hall and the Out).
	sig = in * w;
	// sent only into another effect (outamt 0) that is not running: to the speakers instead
	on2 = In.kr(15360 + out2b.max(0)) * (out2b >= 0);
	outamt = outamt + ((outamt <= 0) * out2amt * (1 - on2));
	Out.ar(outb, sig * outamt);
	Out.ar(out2b.max(0), sig * out2amt * (out2b >= 0));
}).add;
