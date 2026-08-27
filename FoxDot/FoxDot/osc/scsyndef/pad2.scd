SynthDef.new(\pad2,
{|amp=1, sus=1, pan=0, freq=0, fmod=0, rate=4, bus=0, blur=1, beat_dur=1, atk=0.3, decay=0.3, rel=0.4, peak=0.8, level=0.5, gate=1|
	var osc, env, ampEnv, gen, modf, modrq;

	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = freq/2;
	freq = [freq, freq+fmod];
	ampEnv= EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 2);
	freq = { freq * LFNoise2.kr(1,0.01,1) }!12;
	gen = DPW4Saw.ar(freq: freq, mul: ampEnv);
	modf = LFCub.kr(1/12, mul: ampEnv).range(1, 1+rate);
	modrq = LFNoise2.kr(1/8, mul: ampEnv).range(0.1,1.0);
	osc = RLPF.ar(gen, freq * modf, modrq, ampEnv);
	osc = Mix(osc*amp*0.2);
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \pad,
	tags: []
	)
).add;
