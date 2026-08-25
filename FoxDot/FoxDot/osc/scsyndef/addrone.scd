// addrone — AdLib/OPL2 FM pad/drone: 2 detuned FM voices + a sine sub under slow
// vibrato, long attack/release. The atmospheric HERAD sub-bed (Dune "sand & wind").
SynthDef.new(\addrone,
{|amp=1, sus=1, pan=0, freq=0, vib=0.3, fmod=0, bus=0, blur=1, atk=1.5, rel=1.5,
  ratio=1, index=2.5, feedback=0.4, detune=0.006, sub=0.35, wave=0|
	var oplshape, mkvoice, car, env, sig, vibr;
	freq = In.kr(bus, 1);
	sus = sus * blur;
	vibr = SinOsc.kr(0.2, Rand(0, 2pi)).range(1 - (vib * 0.02), 1 + (vib * 0.02));
	freq = (freq + fmod) * vibr;
	oplshape = {|s, ws| Select.ar(ws.clip(0, 3), [ s, s.max(0), s.abs, (s.abs * 2 - 1).max(0) ]); };
	mkvoice = {|f|
		var mod = SinOscFB.ar(f * ratio, feedback.clip(0, 4)) * index;
		oplshape.(SinOsc.ar(f, mod), wave);
	};
	car = (mkvoice.(freq * (1 - detune)) + mkvoice.(freq * (1 + detune))) * 0.5;
	car = car + (SinOsc.ar(freq * 0.5) * sub);
	env = EnvGen.ar(Env.linen(atk, (sus - atk).max(0.1), rel, 1, \sin), doneAction: 2);
	sig = Pan2.ar(car * env * amp * 0.28, pan);
	ReplaceOut.ar(bus, sig)},
	metadata: (credit: "CrashServer / Claude", description: "OPL2/AdLib FM drone/pad", category: \pad, tags: [\fm, \adlib, \pad])
).add;
