SynthDef.new(\snick,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, glide=1.0, glidedur=0.0, wide=0.0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = Line.kr(start: (freq * glide).clip(-50,22000), end: freq, dur: glidedur);
freq = [freq, freq+fmod];
amp=(amp * 4);
osc=(LFPar.ar(freq, mul: 1) * Blip.ar(((rate + 1) * 4)));
env=EnvGen.ar(Env.perc(attackTime: 0.01,releaseTime: sus,level: amp,curve: 0), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
