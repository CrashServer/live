SynthDef.new(\dsaw,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0.5, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, detune=8, cutoff=800, rq=0.5|
	var osc, osc1, osc2, env;
	var nvoices1 = 5, nvoices2 = 7;
	sus = sus * blur;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];
	//amp=(amp / 4);
	osc1 = {
		var m = 2**(12/1200).rand2;
		var lfo = SinOsc.ar(Rand(0, 3)).range(0,1);
		DelayC.ar(LFSaw.ar(m * freq/2), 0.02, ExpRand(0.001, freq.reciprocal) * lfo);
	}.dup(nvoices1);

	osc2 = {
		var m = 2**(detune/1200).rand2;
		var lfo = SinOsc.ar(Rand(0, 3)).range(0,1);
		DelayC.ar(LFSaw.ar(m * freq), 0.02, ExpRand(0.001, freq.reciprocal) * lfo);
	}.dup(nvoices2);


	osc=(BLowPass4.ar(osc1, cutoff, rq) + osc2 / 4);
	env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 2);
	osc=Splay.ar(osc * env * amp * 0.5);
	ReplaceOut.ar(bus, osc)},
	metadata: (
	credit: "CrashServer",
	description: "",
	category: \saw,
	tags: []
	)
).add;

