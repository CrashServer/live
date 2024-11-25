SynthDef.new(\virus,
	{|len = 2, freq = 420, fmod = 0.1, vib = 0.25, rate = 1, gate = 1, bus=0, amp=1, sus=1, blur=1, cutoff=5400|
	var osc, mainEnv, speed, freqs, pulse, a, bass, tone1, tone2, tone3, noise, impulse;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	mainEnv = EnvGen.kr(Env.triangle(len,1), gate, doneAction:2);
	 speed = Array.geom(4, rate, [1.75, 1.25].choose);
	 freqs = Array.geom(8, freq/2, 1.5);
	 pulse = {|rat1,rat2|LFPulse.ar(rat1, [0,0.5,1].choose)*LFPulse.ar(rat2)};
	 a = Lag.ar(HenonN.ar(
		speed.choose*(mainEnv*10000.rand),
		fmod, vib,
	), 0.01);
	bass = SinOsc.ar(freqs!2*(a*1.0.rand), 0, Lag.ar(pulse.(rate, speed.choose), 0.001));
	tone1 = SinOsc.ar([(freqs+Rand(0,5))*a,(freqs+Rand(0,5))*a], 0, 0.01*pulse.(speed.choose, speed.choose));
	 tone2 = Pan2.ar(SinOsc.ar(freqs.choose*a, 0, 0.1*pulse.(speed.choose, rate)), a);
	 tone3 = SinOsc.ar([freqs.choose,freqs.choose*a], 0, 0.05*pulse.(speed.choose, rate))*mainEnv.round(0.25);
	noise = Pan2.ar(PinkNoise.ar(a*0.1*pulse.(rate,rate)), a);
	impulse = RLPF.ar(Impulse.ar(pulse.(rate, speed.choose), a), freqs.choose+(a*10), 0.01, 0.1).tanh;
	osc = (bass+tone1+tone2+tone3+noise+impulse).tanh;
	osc = LPF.ar(osc, cutoff);
		ReplaceOut.ar(bus, osc * amp);
	}
).add;
