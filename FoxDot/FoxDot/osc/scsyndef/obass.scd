SynthDef.new(\obass,
{|amp=1, sus=1, pan=0, freq=440, vib=0, fmod=0, rate=8, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
//freq=(freq / 4);
//amp=(amp * 0.45);
		osc = SinOsc.ar(freq, 0.0);
		env = EnvGen.ar(Env([0,1,1,0], [0.001,0.52,1.35], curve:'exp'));
		//env=EnvGen.ar(Env.perc(attackTime: atk,releaseTime: sus,level: amp,curve: 'lin'), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;