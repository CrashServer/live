(
SynthDef(\faim,
	{|bus=0, amp=0.1, atk=0.001, decay=0.01, sus=1,rel=0.01, level=0.8, peak=1, gate=1, pan=0, freq=0, fmod=0, vib=0, blur=1|
	var osc;

	sus = sus*blur;
	freq = In.kr(bus, 1);

	freq = [freq, freq+fmod];

		osc= VSTPlugin.ar()

	osc = osc * EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);


	ReplaceOut.ar(bus, osc);
}).add;
)