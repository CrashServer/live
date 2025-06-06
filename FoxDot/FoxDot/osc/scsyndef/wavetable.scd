SynthDef.new(\wavetable,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=1.0, buf=0, pos=0, room=0.1, ratelfo=0, ratelfoadd=0.5, ratelfomul=0.5, phase=0, sample=0, detune=0.2|
var osc, env;
sus = sus * blur;
rate = In.kr(bus, 1);
rate = if(ratelfo<=0, rate, rate * SinOsc.kr(ratelfo, 0, ratelfomul, ratelfoadd));
osc = Osc.ar(buf, rate*LFNoise1.ar(detune!4).bipolar(detune).midiratio, phase.range(0,2pi));
osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, sus-0.1, 0.05]));
osc = HPF.ar(osc, 20);
osc = LPF.ar(osc, 8000);
osc = LeakDC.ar(osc);
osc=(osc * amp);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
