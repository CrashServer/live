SynthDef.new(\abass,
	{|bus=0, amp=1, gate=1, pan=0, freq=440, atk=0.001, decay=0.01, sus=1,rel=0.01, level=0.8, peak=1, fmod=0, blur=1, cutoff=2800, rq=0.8,rate=1|
	var sig, sig1, sig2, sig3, osc, env;

	sus = sus * blur;
	freq = In.kr(bus, 1);

	freq = [freq, freq+fmod];

	freq = SinOsc.ar(freq*rate.lag(0.3)) * (0.5).lag(0.3) * LFNoise1.kr(4).range(0.9,1.1) + 1 * freq;
	sig = SinOsc.ar(freq.lag(0.1) * [1,8,2,4,1.002]);
	sig1 = LFPulse.ar(freq * [1,4,1.001,2 * LFNoise1.kr(1/10).range(0.999,1.001),1/2], mul:1.00);
	sig = sig + sig1;
	sig = sig.fold2(SinOsc.kr(1/13).range(0.9,1));
	sig = sig.wrap2(SinOsc.kr(1/14).range(0.9,1));
	sig = LPF.ar(sig, 5500);
	//sig = sig * 1;
	sig = HPF.ar(sig, 80);
	sig = sig * EnvGen.ar(Env.adsr(0.01,0.1,0.8,0.1),gate,doneAction:2);
	sig = sig * EnvGen.ar(Env.adsr(0.005,0.1,0.8,0.1),gate,doneAction:2);
	//add a ADSR envelope
	env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 2);
		sig = RLPF.ar(sig, cutoff, rq);
	sig = sig.tanh;
	osc = Mix(sig) * 0.25;
	osc = Pan2.ar(osc * env , pan);
	ReplaceOut.ar(bus, osc * amp)
	},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \bass,
	tags: []
	)

).add;
