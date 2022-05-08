SynthDef.new(\loop,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1.0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0, buf=0, pos=0, room=0.1, sample=0, beat_stretch=1|
var osc, env;
sus = sus * blur;
//rate = In.kr(bus, 1);
//rate = (rate * (1-(beat_stretch>0))) + ((BufDur.kr(buf) / ((beat_stretch<=0) + abs(beat_stretch))) * (beat_stretch>0));
		osc = PlayBuf.ar(2,buf, BufRateScale.kr(buf)*rate, startPos: BufFrames.kr(buf)*rate*pos / sus);
		osc = osc * Env.linen(0, BufDur.kr(buf)*rate/sus, 0.01).ar;
		osc = (osc*30.dbamp).tanh * -10.dbamp;
		osc=(osc * amp);
osc = Splay.ar(osc, level:1,spread:wide, center:pan, levelComp: true);
	ReplaceOut.ar(bus, osc)}).add;
