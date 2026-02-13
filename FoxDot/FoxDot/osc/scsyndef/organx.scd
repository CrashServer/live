SynthDef.new(\organx, {
	|bus=0, freq=440, amp=1, pan=0, fmod=0,
	atk=0.005, dec=0.1, sus=1, rel=0.1, peak=1, level=0.8,
	d1=0.8, d2=0.8, d3=0.8, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0,
	click=0.3,
	leslie=0, leslierate=6,
	perc=0, perctime=0.2, perchard=0,
	drive=0.3|

	var osc, env, clickOsc, percOsc;
	var leslieLo, leslieHi, loFreq, hiFreq;

	freq = In.kr(bus, 1);
	freq = [freq, freq + fmod];

	// 9 drawbars
	osc = SinOsc.ar(freq * 0.5) * d1;      // 16'
	osc = osc + (SinOsc.ar(freq * 1.5) * d2);  // 5 1/3'
	osc = osc + (SinOsc.ar(freq) * d3);        // 8'
	osc = osc + (SinOsc.ar(freq * 2) * d4);    // 4'
	osc = osc + (SinOsc.ar(freq * 3) * d5);    // 2 2/3'
	osc = osc + (SinOsc.ar(freq * 4) * d6);    // 2'
	osc = osc + (SinOsc.ar(freq * 5) * d7);    // 1 3/5'
	osc = osc + (SinOsc.ar(freq * 6) * d8);    // 1 1/3'
	osc = osc + (SinOsc.ar(freq * 8) * d9);    // 1'
	osc = osc / 3;

	// Key click
	clickOsc = HPF.ar(WhiteNoise.ar, 1500);
	clickOsc = clickOsc * EnvGen.ar(Env.perc(0.001, 0.01)) * click * 2;
	osc = osc + clickOsc;

	// Percussion (2nd or 3rd harmonic based on perchard)
	percOsc = SinOsc.ar(freq * (2 + perchard));
	percOsc = percOsc * EnvGen.ar(Env.perc(0.001, perctime)) * perc;
	osc = osc + percOsc;

	// Overdrive
	osc = (osc * (1 + (drive * 4))).tanh;

	// Amplitude envelope
	env = EnvGen.ar(
		Env([0, peak, level, level, 0], [atk, dec, max(0.01, sus - atk - dec), rel], curve: \lin),
		doneAction: 0
	);

	osc = osc * env;

	// Leslie speaker (simplified - always active, amount controlled by leslie param)
	loFreq = leslierate * 0.8;
	hiFreq = leslierate;

	leslieLo = LPF.ar(osc, 800);
	leslieHi = HPF.ar(osc, 800);

	// Amplitude modulation
	leslieLo = leslieLo * SinOsc.kr(loFreq).range(1 - (leslie * 0.2), 1);
	leslieHi = leslieHi * SinOsc.kr(hiFreq).range(1 - (leslie * 0.3), 1);

	// Pan modulation
	leslieLo = Pan2.ar(Mix(leslieLo), SinOsc.kr(loFreq).range(-0.3, 0.3) * leslie);
	leslieHi = Pan2.ar(Mix(leslieHi), SinOsc.kr(hiFreq, pi/2).range(-0.7, 0.7) * leslie);

	osc = leslieLo + leslieHi;

	osc = osc * amp * 0.4;
	osc = LeakDC.ar(osc);

	ReplaceOut.ar(bus, osc);
},
metadata: (
	credit: "Custom FoxDot synth",
	description: "Hammond-style organ with 9 drawbars, key click, leslie speaker, percussion",
	category: \organ,
	tags: [\organ, \hammond, \keys, \drawbar, \leslie, \rock, \jazz]
)).add;
