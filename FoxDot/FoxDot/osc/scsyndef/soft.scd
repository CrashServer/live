SynthDef.new(\soft,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, glide=1.0, glidedur=0.0, wide=0.0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = Line.kr(start: (freq * glide).clip(-50,22000), end: freq, dur: glidedur);
freq = [freq, freq+fmod];
freq=(freq / 2);
amp=(amp / (100 * (1 + rate)));
osc=Klank.ar(`[[7, 5, 3, 1], [8, 4, 2, 1], [2, 4, 8, 16]], LFNoise0.ar((rate / sus)), freq);
env=EnvGen.ar(Env(times: sus,levels: [0, amp, 0],curve: 'lin'), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
