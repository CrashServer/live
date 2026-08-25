// adbell — AdLib/OPL2 FM bell/mallet: inharmonic non-integer ratio + fast-decaying
// modulator brightness = metallic struck tone that dulls to a sine tail.
SynthDef.new(\adbell,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, bus=0, blur=1, atk=0.001, rel=0.4,
  ratio=3.5, index=6, feedback=0.2, mdec=0.25, wave=0|
	var mod, car, modEnv, env, sig;
	freq = In.kr(bus, 1);
	sus = sus * blur;
	freq = (freq + fmod);
	modEnv = EnvGen.kr(Env([1, 0], [mdec], -3));
	mod = SinOscFB.ar(freq * ratio, feedback.clip(0, 4)) * index * modEnv;
	car = SinOsc.ar(freq, mod);
	car = Select.ar(wave.clip(0,3), [ car, car.max(0), car.abs, (car.abs*2-1).max(0) ]);
	env = EnvGen.ar(Env.perc(atk, (sus + rel).max(0.1), 1, -4), doneAction: 2);
	sig = Pan2.ar(car * env * amp * 0.3, pan);
	ReplaceOut.ar(bus, sig)},
	metadata: (credit: "CrashServer / Claude", description: "OPL2/AdLib FM bell", category: \keyboard, tags: [\fm, \adlib, \bell])
).add;
