(
SynthDef.new(\pasha,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, cutoff=2800, rq=0.8|
		var osc, env, lfo;
		freq = In.kr(bus, 1);
		
		freq = [freq, freq+fmod];
		lfo = LFPar.kr([1,1.04], mul:0.5);
		osc = Pulse.ar(freq, lfo*rate);
		env = EnvGen.ar(Env([0,1,0.5,0.2,0], [0, 0.01, sus / 1.5, sus / 1.5], curve:'cub'), doneAction:3);
		osc = RLPF.ar(osc, cutoff, rq);
		osc = osc * env * amp;
		osc = Mix(osc) * 0.5;
		osc = Pan2.ar(osc, pan);
		ReplaceOut.ar(bus, osc)}).add;

)