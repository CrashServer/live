SynthDef.new(\tbass,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0.5, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0|
	var sig, sound, aenv, aenvGen, line, osc, env;
osc = Array.newClear(6);
env = Array.newClear(6);

	line = Line.kr(1.0, 0.0, sus);
	env[0] = EnvGen.kr(Env([0,1,0.051,0],[0.001,0.01,0.8], [4,-8]), line);
	env[1] = EnvGen.kr(Env([0,1,0.051,0],[0.005,0.5,1.5], [0,-8], releaseNode:2), line);
	env[2] = EnvGen.kr(Env([0,1,1,0],[0.01,0.01,0.2], [0,0,-4], releaseNode:2), line);
	env[3] = EnvGen.kr(Env([0,1,0],[0.002,2.8], [0,-4]), line);
	env[4] = EnvGen.kr(Env([0,1,1,0],[0.001,0.1,0.8], [4,0,-4], releaseNode:2), line);
	env[5] = EnvGen.kr(Env([0,1,0],[0.001,3.0], [0,-4]), line);

	freq = (freq / 4) * ((0..1)/1 - 0.5 * 0.0007 + 1);

	osc[0] = SinOsc.ar(freq * 11 + 0) * env[0];
	osc[1] = SinOsc.ar(freq * 6 * ( osc[0] * 2.5 + 1 )) * env[1];
	osc[2] = SinOsc.ar(freq * 2 * 1 + 0) * env[2];
	osc[3] = SinOsc.ar(freq * 1 * ( osc[2] * 2.5 + 1 ) + 0) * env[3];
	osc[4] = SinOsc.ar(freq * 1 * ( osc[1] * 2.5 + 1 ) * (osc[3] * 2.5 + 1)) * env[4];
	osc[5] = SinOsc.ar(freq * 2) * env[5];

	aenv = Env.adsr(0.001, 0.02, sus, rel, 1, -1);
	aenvGen = EnvGen.ar(aenv, line, doneAction:0);

	sig = osc * DC.ar([0.0, 0.0, 0.0,  0.0, 0.5, 0.5]);
	sig = sig * 0.5;
	sig = sig.flop.sum;
	sig = sig * aenvGen;
	sig = sig * AmpComp.kr(freq);
	sig = sig.sum;

	sound = Pan2.ar(sig, pan, amp);
		ReplaceOut.ar(bus, sound)}).add;