// adlib — authentic OPL2/AdLib 2-operator FM (YM3812 / HERAD "Dune" character).
// Real chip feedback (SinOscFB, 1-sample) + the four OPL operator waveforms
// (wave/mwave: 0 sine · 1 half-sine · 2 abs-sine · 3 quarter-sine) + enveloped
// modulation index. NO filter — bright & buzzy like the real chip. Optional 9-bit
// DAC grit. Params: wave, mwave, ratio, index, feedback (0-4), mdec, msus, grit.
SynthDef.new(\adlib,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, bus=0, blur=1, atk=0.004, rel=0.25,
  wave=0, mwave=0, ratio=1, index=4, feedback=0.5, mdec=0.35, msus=0.5, grit=0|
	var oplshape, mod, car, modEnv, env, sig, vibr;
	freq = In.kr(bus, 1);
	sus = sus * blur;
	vibr = SinOsc.kr(6.4, 0).range(1 - (vib * 0.03), 1 + (vib * 0.03));
	freq = (freq + fmod) * vibr;
	oplshape = {|s, ws| Select.ar(ws.clip(0, 3), [ s, s.max(0), s.abs, (s.abs * 2 - 1).max(0) ]); };
	modEnv = EnvGen.kr(Env([1, msus], [mdec], -3));
	mod = oplshape.(SinOscFB.ar(freq * ratio, feedback.clip(0, 4)), mwave) * index * modEnv;
	car = oplshape.(SinOsc.ar(freq, mod), wave);
	car = Select.ar(grit > 0, [ car, (car * 256).round / 256 ]);
	env = EnvGen.ar(Env([0, 1, 0.85, 0], [atk, (sus * 0.5).max(0.02), (sus * 0.5 + rel).max(0.05)], [-2, 0, -3]), doneAction: 2);
	sig = car * env * amp * 0.3;
	sig = Pan2.ar(sig, pan);
	ReplaceOut.ar(bus, sig)},
	metadata: (credit: "CrashServer / Claude", description: "OPL2/AdLib 2-op FM", category: \keyboard, tags: [\fm, \adlib, \dune])
).add;
