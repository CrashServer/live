SynthDef.new(\sitar2,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.1, rel=0.01, peak=1, level=0.8, wide=0.0|
var osc, env;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
sus=(sus * 4);
osc=LFNoise0.ar([400, 8500], amp);
		osc=(osc * XLine.ar(1, 1e-06, ((sus+decay)*0.1 )));
freq=((265 / (freq * [0.666, 0.669])) * 0.005);
osc=CombL.ar(osc, delaytime: freq, maxdelaytime: 2);
//env=EnvGen.ar(Env(times: [sus],levels: [(amp * 1), (amp * 1)],curve: 'step'), doneAction: 0);
env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
osc=(osc * env);
osc = Mix(osc) * 0.5;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;