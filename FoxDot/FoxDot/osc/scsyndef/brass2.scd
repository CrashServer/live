SynthDef.new(\brass2, {
	|bus=0, freq=440, amp=1, pan=0, fmod=0, atk=0.08, dec=0.1, sus=1, rel=0.2, peak=1, level=0.8, bright=0.5, tight=0.5, growl=0, rasp=0.3, vibrate=5, vibdepth=0.01, mute=0, fenv=0.5|
	var osc, env, fenvelope, vib, formantFreq;
	freq = In.kr(bus, 1);
	freq = freq + fmod;
	vib = SinOsc.kr(vibrate).range(1 - vibdepth, 1 + vibdepth);
	freq = freq * vib;
	osc = Saw.ar(freq) * 0.4;
	osc = osc + (Saw.ar(freq * 1.002) * 0.4);
	osc = osc + (Pulse.ar(freq, 0.3 + (tight * 0.2)) * 0.3);
	osc = osc + (HPF.ar(Saw.ar(freq * 2), 2000) * rasp * 0.2);
	osc = osc * SinOsc.kr(22).range(1 - (growl * 0.15), 1);
	fenvelope = EnvGen.ar(Env.perc(0.05, dec + 0.2));
	formantFreq = freq * (2 + (bright * 4) + (fenvelope * fenv * 6)) * (1 - (mute * 0.5));
	osc = RLPF.ar(osc, formantFreq.clip(100, 12000), 0.15 + (tight * 0.2));
	osc = osc + (BPF.ar(osc, freq * 3, 0.2) * 0.3 * bright);
	env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, dec, max(0.01, sus - atk - dec), rel], curve: \sin), doneAction: 0);
	osc = osc * env * amp * 0.4;
	osc = Pan2.ar(osc, pan);
	osc = LeakDC.ar(osc);
	ReplaceOut.ar(bus, osc)},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \keyboard,
	tags: []
	)
).add;
