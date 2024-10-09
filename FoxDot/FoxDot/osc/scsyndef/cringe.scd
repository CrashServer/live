SynthDef.new(\cringe,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0|
var snd, env;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];

		snd = SinOsc.ar(freq) * Env.perc(0.05,0.1).ar;
			snd = snd + LocalIn.ar(1);
			snd = DelayC.ar(snd, 1.0, [0.023, 0.0145,0.0234,0.05,0.34,0.68,0.1] + (LFNoise2.ar(1!7)*5e-3));
			snd = LeakDC.ar(snd);
		snd = HPF.ar(snd, 60);
		snd = snd + PitchShift.ar(snd * 0.5, 0.013, LFNoise2.ar(3 ! snd.size).linexp(-1,1,1,2));
				snd = LPF.ar(snd,3000);
				snd = snd*0.5;
				snd = snd.tanh;
				LocalOut.ar(snd.sum);
				snd = Splay.ar(snd);
				snd = snd * Env.linen(0.001, sus, 0.4, curve: \sin).ar(Done.freeSelf);
				snd = snd *0.5;
//osc = Mix(osc) * 0.5;
//osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, snd)},
metadata: (
	credit: "https://nathan.ho.name/",
	modified_by: "CrashServer",
	decription: "Hollow noise",
	category: \noise,
)).add;
