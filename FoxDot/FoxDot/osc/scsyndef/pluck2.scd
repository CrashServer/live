SynthDef.new(\pluck2,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.001, decay=0.006, rel=0.0015, peak=1, level=0.8, wide=0.0, gate=1, c1=0.1, c3=30, velo=1|
var osc, env, inp;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = freq/2;
freq = [freq, freq+fmod];
//env = EnvGen.ar(Env.new([0,1, 1, 0],[0.001,0.006, 0.0005],[5,-5, -8]), gate, doneAction:0);
env=Env([0, peak, level, 0], [atk, decay, max((atk + decay + rel), sus)], [5,-5,-8]);
		velo = velo.clip(0.1,1);
		inp = velo * LFDClipNoise.ar(1000*rate) * EnvGen.ar(env, gate, doneAction:2);
		osc = DWGPlucked.ar(freq, velo, gate,0.14, c1+0.01,c3+0.01,inp);
osc = Mix(osc*amp);
osc = Pan2.ar(osc*0.03, pan);
	ReplaceOut.ar(bus, osc)}).add;
