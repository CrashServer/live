SynthDef.new(\omi,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, fmamp=0.1, fmrate=200, fb=0, xfb=0.1, cutoff=5000, rq=0.5|
var osc, env, extFM;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
env=EnvGen.ar(Env.perc(attackTime: atk,releaseTime: sus,level: amp,curve: 'lin'), doneAction: 0);
extFM = SinOsc.ar(fmrate,0,fmamp);
    osc = MiOmi.ar(extFM, pit: freq.cpsmidi, fm1: 0.5, fm2: 0.5, fb: fb, xfb: xfb, cutoff: cutoff/6000, space: 1, env: 0.5, reson:rq);
		// osc = MiOmi.ar(pit: freq.cpsmidi, level1:1, level2:0.5, ratio1:0.49, fm1:0.38);
osc = Mix(osc*env) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;
