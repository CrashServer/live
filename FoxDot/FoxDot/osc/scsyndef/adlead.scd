// adlead — AdLib/OPL2 lead: bright sine carrier + heavy feedback for the buzzy
// sawtooth-ish HERAD lead, with chip vibrato. Cuts through, no filter.
SynthDef.new(\adlead,
{|amp=1, sus=1, pan=0, freq=0, vib=0.4, fmod=0, bus=0, blur=1, atk=0.006, rel=0.2,
  ratio=1, index=4, feedback=1.2, mdec=0.5, msus=0.6, wave=0|
	var oplshape, mod, car, modEnv, env, sig, vibr;
	freq = In.kr(bus, 1);
	sus = sus * blur;
	vibr = SinOsc.kr(6.2, Rand(0, 2pi)).range(1 - (vib * 0.02), 1 + (vib * 0.02));
	freq = (freq + fmod) * vibr;
	oplshape = {|s, ws| Select.ar(ws.clip(0, 3), [ s, s.max(0), s.abs, (s.abs * 2 - 1).max(0) ]); };
	modEnv = EnvGen.kr(Env([1, msus], [mdec], -3));
	mod = SinOscFB.ar(freq * ratio, feedback.clip(0, 4)) * index * modEnv;
	car = oplshape.(SinOsc.ar(freq, mod), wave);
	env = EnvGen.ar(Env([0, 1, 0.8, 0], [atk, (sus * 0.3).max(0.02), (sus * 0.7 + rel).max(0.05)], [-2, 0, -3]), doneAction: 2);
	sig = Pan2.ar(car * env * amp * 0.28, pan);
	ReplaceOut.ar(bus, sig)},
	metadata: (credit: "CrashServer / Claude", description: "OPL2/AdLib FM lead", category: \keyboard, tags: [\fm, \adlib, \lead])
).add;
