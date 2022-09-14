SynthDef.new(\creep,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, glide=1.0, glidedur=0.0, wide=0.0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = Line.kr(start: (freq * glide).clip(-50,22000), end: freq, dur: glidedur);
freq = [freq, freq+fmod];
amp=(amp / 2);
osc=PMOsc.ar(freq, (freq * rate), 10);
env=EnvGen.ar(Env(times: [sus, 0.001],levels: [0.0001, amp, 0],curve: 'exp'), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
