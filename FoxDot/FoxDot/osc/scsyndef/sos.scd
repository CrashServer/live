SynthDef.new(\sos,
{|amp=1, gate=1, rel=1,dur=8, bus=0, freq=200, pan=0, fmod=0, sus=1, rate=0.01|
	var env,sig,sig2,freqs;

		freqs = (Rand(60, 40)).midicps + SinOsc.ar(Rand(0, 8));
	env = EnvGen.ar(Env(curve: 'lin',levels: [0, amp, 0],times: (sus * 1.2)), doneAction: 0);
	sig = FreeVerb2.ar(*XFade2.ar(SinOscFB.ar([Rand(1, 240),Rand(1, 240)],VarSaw.kr(Rand(1, 400))), SinOscFB.ar([freqs * 1.2,freqs],VarSaw.kr(rate+1)+Rand(2, 2000)/2),VarSaw.kr(0.1)));
	sig2 = RLPF.ar(BrownNoise.ar(1), Rand(200, 1600), 0.015,1);

	sig = (sig + (sig2 * Rand(0, 0.01))) * env;
	sig = HPF.ar(sig.tanh * 0.4, 40);

	sig = Pan2.ar(sig, pan);
	ReplaceOut.ar(bus, (sig * amp))},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \experiment,
	tags: []
	)
).add;

