// adbass — AdLib/OPL2 FM bass: abs-sine carrier (adds the octave/body), moderate
// feedback, low ratio, punchy percussive envelope. The chunky HERAD bass.
SynthDef.new(\adbass,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, bus=0, blur=1, atk=0.003, rel=0.12,
  ratio=1, index=3, feedback=0.5, mdec=0.25, msus=0.3, wave=2, mwave=0, grit=0|
	var oplshape, mod, car, modEnv, env, sig;
	freq = In.kr(bus, 1);
	sus = sus * blur;
	freq = (freq + fmod);
	oplshape = {|s, ws| Select.ar(ws.clip(0, 3), [ s, s.max(0), s.abs, (s.abs * 2 - 1).max(0) ]); };
	modEnv = EnvGen.kr(Env([1, msus], [mdec], -4));
	mod = oplshape.(SinOscFB.ar(freq * ratio, feedback.clip(0, 4)), mwave) * index * modEnv;
	car = oplshape.(SinOsc.ar(freq, mod), wave);
	car = car + (SinOsc.ar(freq * 0.5) * 0.3);   // sub reinforcement for weight
	car = Select.ar(grit > 0, [ car, (car * 256).round / 256 ]);
	env = EnvGen.ar(Env.perc(atk, (sus + rel).max(0.05), 1, -4), doneAction: 2);
	sig = Pan2.ar(car * env * amp * 0.3, pan);
	ReplaceOut.ar(bus, sig)},
	metadata: (credit: "CrashServer / Claude", description: "OPL2/AdLib FM bass", category: \bass, tags: [\fm, \adlib, \bass])
).add;
