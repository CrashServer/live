SynthDef.new(\orientmod,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0, room=0.7, mix=0.3, cutoff=5000, rq=0.5|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
		
freq = [freq, freq+fmod];
		osc=(LFPulse.ar(freq, LFNoise1.ar(rate,1), 0.25, 0.25) + LFPulse.ar(freq, LFNoise2.ar(rate,1), 0.1, 0.25));
env=EnvGen.ar(Env.perc(attackTime: 0.001,releaseTime: sus,level: amp,curve: 4), doneAction: 0);
		osc = BLowPass4.ar(osc, cutoff, rq.clip(0.1,1));
		osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
