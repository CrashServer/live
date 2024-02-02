SynthDef(\wobble, {
|out=0, rate=6, decay=0.01, gate=1, cutoff=8500, freq, level=0.8, sus=0.1, atk=0.02, wphase=0.5, peak=1, amp=1, rel=0.1, bus=0, fmod=0|
var rev, osc, env, son;
env=EnvGen.ar(Env([0,peak,level,level,0], [atk, decay, sus/2, sus/2]), doneAction: 2);
	freq = In.kr(bus, 1);
	
freq = [freq, freq+fmod];
son = MoogVCF.ar(
in: (
Pulse.ar([freq * 0.98, freq], mul:0.5) +
PinkNoise.ar(LFNoise0.ar(2).range(0, 1.0)) +
Saw.ar([freq, freq * 1.025], mul:2)
).clip2(0.5),
fco: LFCub.kr(
freq:LFPulse.kr(wphase, 0.5, width: 0.25).range(0.1, rate) ).exprange(40, cutoff),
res: 0.4,
mul:2
);
osc = (son*amp);
osc = Mix(osc) * 0.2;
osc = HPF.ar(osc, 40);
ReplaceOut.ar(bus, osc * env);
}).add;