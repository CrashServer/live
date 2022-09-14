SynthDef.new(\acidbass, {
	|bus = 0, gate = 1, freq = 440, amp = 1, pan = 0, fmod=0, atk = 0.001, dec = 0.4, sus = 1, rel = 0.3, curve = -4, rate = 4, width = 0.51, rq = 0.4, glide=1, glidedur=0|
	var ampEnv, filterEnv, osc;
	freq = In.kr(bus, 1);
	freq = Line.kr(start: (freq * glide).clip(-50,22000), end: freq, dur: glidedur);
	freq = [freq, freq+fmod];
	freq = freq/2;
	ampEnv = Env.adsr(
		attackTime: atk,
		decayTime: dec,
		sustainLevel: sus / 20,
		releaseTime: rel,
		peakLevel: amp * 0.1,
		curve: [0, curve, curve, curve]
	).kr(gate: gate, doneAction: 2);
	filterEnv = Env.adsr(
		attackTime: atk,
		decayTime: dec * 2,
		sustainLevel: sus * 1/20,
		releaseTime: rel,
		peakLevel: 2.pow(rate.clip(0,6)), // octaves multiplier
		curve: [-1 * curve, curve],
		bias: 1 // env sweeps from 1 to 2.pow(filterRange) and back
	).kr(gate: gate, doneAction: 2);
	osc = LFPulse.ar(freq: freq, width: width.clip(0.09,0.99)).range(-1, 1);
	osc = RLPF.ar(osc, freq * filterEnv, rq);
	osc = osc * ampEnv * amp * 2;
	osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)
},
metadata: (
	credit: "otophilia",
	modified_by: "Bruno Ruviaro, Josh Mitchell, Jens Meisner, CrashServer",
	description: "",
	category: \bass,
	tags: [\pitched, \acid, \phat, \subtractive]
	)
).add;
