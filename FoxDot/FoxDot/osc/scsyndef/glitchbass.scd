SynthDef.new(\glitchbass,
	{|amp=1, sus=1, gate=1, pan=0, freq=0, rate=1, vib=0, fmod=0, cutoff=2000, rq=0.8, mul=1, bus=0, atk=0.0001, decay=0.01, rel=0.01, level=0.8, peak=1|
	var osc, pulse, filter,env,clip;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	freq = freq/2;

	clip = LinLin.kr(rate, 0, 1, 2e-12, 2e-1);
	osc = AllpassC.ar(SinOsc.ar(freq).tanh, 1, TExpRand.ar(2e-4,clip, Impulse.ar(rate)), 2);
	osc = AllpassN.ar(osc, 0.01, XLine.kr(0.0001, 0.01, 20), 0.2);
	osc = osc/2;

	env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 2);
	osc = BLowPass4.ar(osc,(cutoff*(env.squared))+200+freq,rq);
	osc = HPF.ar(osc, 40);
	osc = Mix(osc*env*amp) * 0.5;
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \experiment,
	tags: []
	)
).add;