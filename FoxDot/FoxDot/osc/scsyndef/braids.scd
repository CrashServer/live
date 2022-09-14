SynthDef.new(\braids,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.0001, decay=0.01, rel=0.01, peak=1, level=0.8, timbre=0.5, color=0.5, model=0, decim=0, bbits=0, ws=0, cutoff=2800, rq=0.8, detune=0, glide=1, glidedur=0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = Line.kr(start: (freq * glide).clip(-50,22000), end: freq, dur: glidedur);
freq = [freq, freq+fmod];
		freq = [freq.cpsmidi + detune, freq.cpsmidi - detune];
		osc = MiBraids.ar(freq, timbre, color, model.clip(0,47), 0, 2, decim, bbits, ws)!2;
env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
		osc = RLPF.ar(osc, cutoff, rq);
osc=(osc * env);
osc = Mix(osc) * 0.5 * amp;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;