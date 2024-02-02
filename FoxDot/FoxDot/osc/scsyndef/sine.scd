(
SynthDef.new(\sine,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.001, decay=0.01, rel=0.01, peak=1, cutoff=2800, rq=0.8, level=0.8|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);

freq = [freq, freq+fmod];
osc = SinOscFB.ar(freq, rate);
env=EnvGen.ar(Env(times: [atk, sus],levels: [0, amp, 0],curve: 'lin'), doneAction: 2);
		osc=(osc * env);
		osc = RLPF.ar(osc, cutoff, rq);
osc = Mix(osc) * 0.2;
osc = Pan2.ar(osc, pan);
ReplaceOut.ar(bus, osc)}).add;
)