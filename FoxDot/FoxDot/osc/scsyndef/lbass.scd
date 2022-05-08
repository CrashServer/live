SynthDef.new(\lbass,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.09, rel=0.05, peak=1, level=0.8, detune=0.3,  oscmix=0.5, submix=0.5, cutoff=4500, rq=0.5, tone=0.16, wide=0.0|
var osc, osc1, osc2, sub, oscf, env, envf;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
freq=(freq/2);
		osc1 = LFTri.ar([freq + detune, freq-detune], LFNoise0.ar(2,4));
		osc2 = LFSaw.ar([freq + detune, freq-detune], LFNoise0.ar(6,2));
		sub = LPF.ar(LFPulse.ar(freq/2),400);
		env = EnvGen.ar(Env([0, peak, level, level, 0], [atk,decay,sus-(atk+decay+rel),rel], curve:\sin), doneAction: 0);
		envf = EnvGen.ar(Env.adsr(0.01,0.05,tone,0.5));
		osc = SelectX.ar(oscmix, [osc1, osc2]);
		osc = HPF.ar(osc, 150);
		osc = SelectX.ar(submix, [osc*0.8, sub]);
		osc = MoogFF.ar(osc, (cutoff*envf).clip(20,20000), rq.clip(0,3.99), mul:2);
		osc = LeakDC.ar(osc);
osc=(osc * env);
osc = Pan2.ar(osc*amp, pan);
	ReplaceOut.ar(bus, osc)}).add;