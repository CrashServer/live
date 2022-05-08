(SynthDef(\fmperc,{|bus=0, amp=0.1, atk=0.015, decay=0.01, sus=1,rel=0.01, level=0.8, peak=1, gate=1, pan=0, freq=0, fmod=0, vel=0.7, rate=1, blur=1, beat_dur=1, f0r=2, f1r=2, f2r=4, fm0=1, fm1=0.6, fm2=0.3|
	var osc, env;
	var ff0,ff1,ff2, mod0, mod1, mod2;
	freq = In.kr(bus, 1);

	env = EnvGen.kr(Env.perc(Rand(0.8,1.2)*atk, sus, curve: -4), doneAction:2)*vel;

	env = env*PinkNoise.ar(1!2).range(0.1,1).lag(0.01);
	ff0 = freq * f0r + {Rand(-3,3)}.dup;
	ff1 = freq * f1r + {Rand(-3,3)}.dup;
	ff2 = freq * f2r + {Rand(-3,3)}.dup;

	mod0 = SinOsc.ar(ff0) * freq * fm0 * env.pow(0.8);
	mod1 = SinOsc.ar(ff1) * freq * fm1 * env.pow(1.4);
	mod2 = SinOsc.ar(ff2) * freq * fm2 * env.pow(2.5);

	osc = SinOsc.ar(
		freq
		+ LFTri.ar(env.pow(0.5) * LFNoise1.kr(0.3).range(1,5), Rand(0.0,2pi), mul: env.pow(0.2) *  freq * 0.005)
		+ [mod0, mod1, mod2].sum
		+ WhiteNoise.ar(freq/8!2).lag(0.001)
	);

	osc = tanh(osc).softclip;
	osc = HPF.ar(osc*env.pow(0.5), freq);
	osc = MidEQ.ar(osc, freq*5, rq:env.pow(0.5)*3.5 + 0.1, db: -32);

	osc = OnePole.ar(osc, 0.8);
	osc = Pan2.ar(osc,pan);
	ReplaceOut.ar(0,osc);

}).add

)