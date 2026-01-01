SynthDef.new(\rsin,
	{|amp=1, gate=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, para1=70, rsing=0|
	var env, sig,sig2;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];

	env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
	sig = FreeVerb2.ar(*XFade2.ar(
		SinOscFB.ar([60,4],VarSaw.kr(rate)+SinOsc.ar(4, mul:rsing)),
	   	SinOscFB.ar([freq*2,freq],para1),VarSaw.kr(0.1)));
	sig = sig.tanh * env * 0.4;
	sig = BLowShelf.ar(sig,40,1.0,-12);
	sig = HPF.ar(sig, 40);
	sig = Splay.ar(LeakDC.ar(Limiter.ar(sig, 1)));
	sig = Mix(sig) * 1.8;
	sig = Pan2.ar(sig, pan);
	ReplaceOut.ar(bus, (sig * amp))},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \experiment,
	tags: []
	)
).add;
