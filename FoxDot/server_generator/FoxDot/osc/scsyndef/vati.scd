(
SynthDef.new(\vati,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=12, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.0, off=7|
var osc, env, sig1, sig2, sig3, sig4, tracking, ringmod;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
amp=(amp / 4);
sig1 = Pulse.ar(freq, 0.17);
sig2 = Pulse.ar((freq.cpsmidi - 12).midicps, 0.17);
		sig3 = Pulse.ar((freq.cpsmidi + (off)).midicps, 0.17);
		sig4 = LFTri.ar((freq.cpsmidi - (off)).midicps);
tracking = ((freq * 1) + freq) * rate;
osc = sig1 + sig2 + sig3 + (sig4 * 2);
osc = RLPF.ar(osc, tracking, 1, 0.33);
osc=(osc * amp);
env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
ReplaceOut.ar(bus, osc)}).add;
)