SynthDef.new(\arpymod,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0.5, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, cutoff=5000, rq=0.5, glide=1.0, glidedur=0, wide=0.0|
var osc, env, sub;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = Line.kr(start: (freq * glide).clip(-50,22000), end: freq, dur: glidedur);
freq = [freq, freq+fmod];
amp=(amp * 2);
osc=Impulse.ar(freq, phase: rate);
sub = LFPulse.ar(freq/4, iphase: 1-rate, mul:0.25);
		osc = MoogVCF.ar(osc + sub, cutoff, (1-rq.clip(0.1,1)), 2);
env=EnvGen.ar(Env.perc(attackTime: 0.001,releaseTime: (sus),level: amp,curve: -4), doneAction: 2);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;

