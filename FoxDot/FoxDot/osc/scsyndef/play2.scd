SynthDef.new(\play2,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=1.0, buf=0, pos=0, room=0.1, ratelfo=0, ratelfoadd=0.5, ratelfomul=0.5|
var osc, env;
sus = sus * blur;
rate = In.kr(bus, 1);
rate = if(ratelfo<=0, rate, rate * SinOsc.kr(ratelfo, 0, ratelfomul, ratelfoadd));
osc=PlayBuf.ar(2, buf, (BufRateScale.ir(buf) * rate), startPos: (BufSampleRate.kr(buf) * pos));
osc=(osc * amp);
osc = Splay.ar(osc, level:1,spread:wide, center:pan, levelComp: true);
	ReplaceOut.ar(bus, osc)}).add;
