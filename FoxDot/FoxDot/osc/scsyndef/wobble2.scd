SynthDef(\wobble2,
{|bus=0, rate=1, decay=0.01, gate=1, freq, level=0.8, sus=0.1, atk=0.02, iphase=0.5, peak=1, amp=1, rel=0.1, fmod=0, wflo=0.1, wfhi=6, wfmax=8500, wet=0.4|
	var rev, osc, env, son;
	 env=EnvGen.ar(Env([0,1,0.8,0.8,0], [0.02, 0.01, sus/2, sus/2]), doneAction: 2);
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	son = MoogVCF.ar(
		in: (
			Pulse.ar([freq * 0.98, freq], mul:0.5) +
			PinkNoise.ar(LFNoise0.ar(2).range(0, 1.0)) +
			Saw.ar([freq, freq * 1.025], mul:2)
		).clip2(0.5),
		fco: LFCub.kr(
			freq:LFPulse.kr(0.25, iphase, width: 0.25).range(wflo, wfhi) ).exprange(40, wfmax),
		res: 0.4,
		mul:2
	);
	rev = Greyhole.ar(son * wet,
		delayTime:0.5, feedback:0.5, diff:0.4,
		damp:0.5, modDepth:0.8, modFreq:0.3);
	osc = son + rev;
	ReplaceOut.ar(bus, osc * env)},
    metadata: (
	credit: "CrashServer",
	description: "",
	category: \ambi,
	tags: []
	)
).add;
