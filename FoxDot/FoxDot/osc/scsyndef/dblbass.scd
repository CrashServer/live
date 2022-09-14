SynthDef.new(\dblbass, {
	|bus = 0, amp = 1, freq = 440, fmod=0, atk = 0.001, sus=0, rel = 1.0, crv = \lin, vel = 1.0, freqdev = 4, op1mul = 0.5, op2mul = 0.5, op3mul = 0.5, spread = 1, subAmp = 0.3, pan=0, cutoff=3000, rq=0.5, glide=1, glidedur=0|
	var env, op1, op2, op3, op4, osc, sub;
	freq = In.kr(bus, 1);
	freq = Line.kr(start: (freq * glide).clip(-50,22000), end: freq, dur: glidedur);
	freq = [freq, freq+fmod];
	freq = (freq / 4);
	env = Env.linen(attackTime: atk, sustainTime: sus, releaseTime: rel, curve: crv).kr(doneAction: 0);
	op1 = SinOsc.ar(freq: freq * 4, mul: vel / 2 + op1mul);
	op2 = SinOsc.ar(freq: freq * 3, phase: op1, mul: vel / 2 + op2mul);
	op3 = SinOsc.ar(freq: freq * 2, phase: op2, mul: vel / 2 + op3mul);
	op4 = SinOsc.ar(freq: freq + NRand(-1 * freqdev, freqdev, 3), phase: op3, mul: amp * 0.5);
	osc = {DelayN.ar(in: op4, maxdelaytime: 0.06, delaytime: Rand(0.03, 0.06))} !8;
	osc = LeakDC.ar(osc);
	osc = Splay.ar(inArray: osc, spread: spread, level: 0.6, center: pan);
	sub = SinOsc.ar(freq: freq/2, mul: env * subAmp);
	//sub = Pan2.ar(sub, pan);
	osc = (osc + sub) * env;
	osc = RLPF.ar(osc, cutoff, rq);
	osc = Limiter.ar(osc);
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)
},
metadata: (
	credit: "Matias Monteagudo",
	modified_by: "Suhel Keswani, Josh Mitchell, Jens Meisner",
	description: "",
	category: \bass,
	tags: [\pitched, \bass]
)).add;
