SynthDef.new(\cs80, {
	|bus = 0, freq = 440, amp = 1, gate = 1.0, pan = 0, fmod = 0, atk = 0.3, sus = 0.8, rel = 1.0, dec = 0.8, fatk = 0.75, fdec = 0.5, fsus = 0.8, frel = 1.0, cutoff = 2200, detune = 0.002, vibspeed = 4, vibdepth = 0.015, glide = 0.8, glidedur = 0.015|
	var env, fenv, vibr, ffreq, osc;
	freq = In.kr(bus, 1);
	
	freq = [freq, freq+fmod];
	//Envelopes for amplitude and frequency:
	env = Env.linen(atk, sus, rel, curve: \sin).kr(gate: gate, doneAction: 0);
	fenv = Env.adsr(fatk, fdec, fsus, frel, curve: 2).kr(gate: gate, doneAction: 0);
	//Giving the input freq vibrato:
	vibr = SinOsc.kr(vibspeed).range(1 / (1 + vibdepth), (1 + vibdepth));
	freq = freq * vibr;
	//See beatings.scd for help with dtune
	osc = Saw.ar([freq, freq * (1 + detune)], mul: env * amp * 0.25);
	osc = Mix.ar(osc);
	//Sending it through an LPF: (Keep ffreq below nyquist!!)
	ffreq = max(fenv * freq * 12, cutoff) + 100;
	osc = LPF.ar(osc, ffreq);
	osc = Mix(osc);
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)
},
metadata: (
	credit: "Mike Hairston",
	modified_by: "Bruno Ruviaro, Josh Mitchell, Jens Meisner",
	description: "Vangelis/Blade Runner lead sound, based on tutorial by meastempo ",
	category: \keyboards,
	tags: [\lead, \modulation, \analog, \cs80, \vangelis, \bladerunner]
)).add;
