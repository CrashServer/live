SynthDef.new(\lead,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0.5, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.8, peak=1, level=0.8, wide=0.0, cutoff=5000, rq=0.4|
var osc, env, voices, freqs, phases;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
voices = 15;
env = EnvGen.ar(Env.adsr(atk, 0.5, sus, rel), Line.kr(1.0, 0.0, sus), doneAction:2);
freqs = {Rand(-1,1)*2**(freq/2200)}.dup(voices);
phases = Array.fill(voices, { 1.0.rand2 });
		osc =  LFSaw.ar(freq + freqs, phases);
		osc =  RLPF.ar(osc, cutoff, rq);
osc=(osc * env * amp);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;