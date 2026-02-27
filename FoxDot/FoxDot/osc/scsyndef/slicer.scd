SynthDef.new(\slicer,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=1.0, buf=0, pos=0, room=0.1, ratelfo=0, ratelfoadd=0.5, ratelfomul=0.5, sample=0, slice_start=0, slice_end=1|
var osc, env;
sus = sus * blur;
rate = In.kr(bus, 1);
rate = if(ratelfo<=0, rate, rate * SinOsc.kr(ratelfo, 0, ratelfomul, ratelfoadd));
osc = PlayBuf.ar(2, buf, BufRateScale.kr(buf) * (BufDur.kr(buf) * (slice_end - slice_start).max(0.001) / sus) * rate, startPos: BufFrames.kr(buf) * slice_start, loop: 0);
osc = osc * EnvGen.ar(Env([0,1,1,0],[0.01, sus-0.02, 0.01]));
osc=(osc * amp);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)},
).add;
