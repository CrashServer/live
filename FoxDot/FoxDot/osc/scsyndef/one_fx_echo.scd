// one_fx_echo: One's (Unreason's) Echo as a persistent effect on a bus. Ported from unreason/src/devices/echo/dsp.ts.
// Reads stereo from inb (and clears it), writes to outb. Time: `ms`, or with sync a division of the beat (`div`, One's
// list: 1/32 … 2 bars) × beat_dur; a change glides (One: 0.0005 a sample). The repeats are low-passed (`tone`) and fed
// back: stereo through tanh, or ping-pong (the mono input into the left, each side into the other).
SynthDef.new(\one_fx_echo, {
	|inb = 10, outb = 0, outamt = 1, out2b = -1, out2amt = 0, sync = 1, div = 7, ms = 350, fb = 0.45, tone = 3500, mode = 1, mix = 0.3, beat_dur = 0.5|
	var sig;
	var sr = SampleRate.ir, in, x, y, want, time, d, dl, dr, f, c, wl, wr;
	var on2;
	in = In.ar(inb, 2); x = in[0]; y = in[1];
	ReplaceOut.ar(inb, Silent.ar(2));
	want = Select.kr(sync, [ms / 1000, Select.kr(div, [0.125, 1 / 6, 0.25, 1 / 3, 0.375, 0.5, 2 / 3, 0.75, 1, 2, 4, 8]) * beat_dur]).clip(1 / sr, 4.1);
	time = Lag.kr(want, 6.9 * 2000 / sr);
	f = fb.clip(0, 0.98);
	c = (-2pi * tone / sr).exp;
	d = DelayL.ar(LocalIn.ar(2), 4.2, (time - (BlockSize.ir / sr)).max(0));
	dl = OnePole.ar(d[0], c); dr = OnePole.ar(d[1], c);
	wl = Select.ar(mode, [x + (dl * f).tanh, ((x + y) * 0.5) + (dr * f)]);
	wr = Select.ar(mode, [y + (dr * f).tanh, dl * f]);
	LocalOut.ar([wl, wr]);
	// Out at outamt, and a second output (One: an effect cabled to two places, e.g. the Echo into the Hall and the Out).
	sig = [(x * (1 - mix)) + (dl * mix), (y * (1 - mix)) + (dr * mix)];
	// sent only into another effect (outamt 0) that is not running: to the speakers instead
	on2 = In.kr(15360 + out2b.max(0)) * (out2b >= 0);
	outamt = outamt + ((outamt <= 0) * out2amt * (1 - on2));
	Out.ar(outb, sig * outamt);
	Out.ar(out2b.max(0), sig * out2amt * (out2b >= 0));
}).add;
