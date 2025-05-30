SynthDef.new(\loop,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=1.0, buf=0, pos=0, room=0.1, ratelfo=0, ratelfoadd=0.5, ratelfomul=0.5, sample=0, beat_stretch=1, looping=1.0, clip=0|
var osc, env;
sus = sus * blur;
rate = In.kr(bus, 1);
rate = if(ratelfo<=0, rate, rate * SinOsc.kr(ratelfo, 0, ratelfomul, ratelfoadd));
rate = (rate * (1-(beat_stretch>0))) + ((BufDur.kr(buf) / sus) * (beat_stretch>0));
rate = if(ratelfo<=0, rate, rate * SinOsc.kr(ratelfo, 0, ratelfomul, ratelfoadd));
clip = if(clip<=0, 1, (clip/sus)*0.5);
osc = PlayBuf.ar(2, buf, BufRateScale.kr(buf) * rate, startPos: BufSampleRate.kr(buf) * pos, loop: looping);
osc = osc * EnvGen.ar(Env([0,1,1,0],[0.05, (sus*clip)-0.05, 0.05]));
osc=(osc * amp);
osc = Splay.ar(osc, level:1,spread:wide, center:pan, levelComp: true);
	ReplaceOut.ar(bus, osc)}).add;
