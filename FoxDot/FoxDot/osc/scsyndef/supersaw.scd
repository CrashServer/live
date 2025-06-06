SynthDef.new(\supersaw,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, cutoff=1800, rq=0.8|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);

freq = {freq * LFNoise2.kr(0.5).range(0.98, 1.02)}!3;
freq = [freq, freq+fmod];
amp=(amp / 4);
osc=LFSaw.ar(freq,rate);
osc=(osc * amp);
//env=EnvGen.ar(Env(times: [0.01, (sus - 0.01), 0.01],levels: [0, 1, 1, 0],curve: 'lin'), doneAction: 0);
env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
osc = RLPF.ar(osc, cutoff, rq);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
