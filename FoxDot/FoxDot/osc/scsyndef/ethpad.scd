(
SynthDef.new(\ethpad,
	{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, attack=2.0, release=4.0|
		var osc, env, filter;
		freq = In.kr(bus, 1);

		freq = freq * ({LFNoise2.kr(4)} !8 * 0.1).midiratio;
		osc = Saw.ar(freq);
		osc = DelayC.ar(osc, 0.01, {Rand(0, 0.01)} ! osc.size);
		osc = Splay.ar(osc);
		osc = LPF.ar(osc, freq*4);
		osc = BPeakEQ.ar(osc, freq*8, 0.1, 8);
		osc = FreeVerb.ar(osc, mix: 0.6, room: 0.9);
		env = EnvGen.ar(Env([0, 0.8, 0.5, 0],[attack, 0.5 * sus, release * sus]));
		// env = EnvGen.ar(Env.asr(0.1*sus,1,0.001), doneAction: 2);
		osc = osc * env * 0.25 *amp;
		//osc = Pan2.ar(osc*0.5, pan);
		ReplaceOut.ar(bus, osc)}).add;
)
