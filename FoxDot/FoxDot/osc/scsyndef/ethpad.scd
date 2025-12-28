SynthDef.new(\ethpad,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1, bus=0, attack=2.0, release=4.0|
	var osc, env, filter;
	freq = In.kr(bus, 1);

	freq = freq * ({LFNoise2.kr(4)} !8 * 0.1).midiratio;
	osc = LFSaw.ar(freq, rate);
	osc = DelayC.ar(osc, 0.01, {Rand(0, 0.01)} ! osc.size);
	osc = Splay.ar(osc);
	osc = LPF.ar(osc, freq*4);
	osc = BPeakEQ.ar(osc, freq*8, 0.1, 8);
	osc = FreeVerb.ar(osc, mix: 0.6, room: 0.9);
	env = EnvGen.ar(Env([0, 0.8, 0.5, 0],[attack, 0.5 * sus, release * sus]), doneAction: 2);
	osc = osc * env * 0.25 *amp;
	ReplaceOut.ar(bus, osc)},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \pad,
	tags: []
	)
).add;
