// one_ins_crush: One's (Unreason's) Crush as an insert on one sound, on a bus of its own (see one_ins_drive for the
// routing). Ported from unreason/src/devices/crush/dsp.ts: a sample held each period (sr / rate), each period stretched
// or shortened at random by the jitter (± 0.8 jit), quantised mid-tread to `bits` (quiet sounds drop out below the first
// step, no hiss), mixed with the dry sound by `mix`. One's rate CV input is not here.
SynthDef.new(\one_ins_crush, {
	|inb = 900, outb = 0, dry = 1, todrive = 0, toduck = 0, tohall = 0, toecho = 0, toaux = 0, side = 0, bits = 8, rate = 11025, jit = 0, mix = 1|
	var sr = SampleRate.ir, in, q, per, trig, held, sig, fxon;
	in = In.ar(inb, 2);
	ReplaceOut.ar(inb, Silent.ar(2));
	q = 2 ** (bits.clip(1, 16) - 1);
	per = 1 / rate.clip(20, sr);
	trig = TDuty.ar((per * (1 + (jit * (Dwhite(0, 1) - 0.5) * 1.6))).max(1 / sr));
	held = Latch.ar(in, trig);
	held = (held.clip2(1) * q).round / q;
	sig = in + ((held - in) * mix);
	fxon = In.kr(15360 + [2, 6, 8, 10, 12]);
	dry = Select.kr(dry > 0, [((todrive * (1 - fxon[0])) + (toduck * (1 - fxon[1])) + (tohall * (1 - fxon[2])) + (toecho * (1 - fxon[3])) + (toaux * (1 - fxon[4]))).min(1), dry]);
	Out.ar(2, sig * todrive); Out.ar(6, sig * toduck); Out.ar(8, sig * tohall); Out.ar(10, sig * toecho); Out.ar(12, sig * toaux); Out.ar(14, sig * side);
	Out.ar(outb, sig * dry);
}).add;
