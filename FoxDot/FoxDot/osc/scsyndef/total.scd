SynthDef.new(\total,
	{|bus=0, amp=1, fmod=0, sus=1, blur=1, rate=0.5, freq=220, atk=0.25, rel=0.2, gate=1, pan=0, mod=0|

	var sig, env, osc;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
    sig = mean(FreqShift.ar(c=SinOscFB.ar(SinOscFB.ar(SinOscFB.ar(freq/b=(1..8),1),mod/b)+b*[mod, 99, freq],1),1/b)+c);
	sig = sig * LinSelectX.kr(rate,[1, SinOsc.ar(4, 0, 1)]);
	env=EnvGen.ar(Env(times: [atk, (sus * 1)],levels: [0, amp, 0],curve: 'lin'), doneAction: 0);
	osc=(sig * env * amp);
	osc = Mix(osc) * 0.4;
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \experiment,
	tags: []
	)
).add;