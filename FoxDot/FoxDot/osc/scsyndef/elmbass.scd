SynthDef.new(\elmbass,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=1, bus=0, blur=1, beat_dur=1, atk=0.001, decay=0.01, rel=0.1, peak=1, level=0.8, emallet=0.5, etimbre=0.3, ebright=0.5, edamp=0.5, ewide=0.5, emodel=1, eamp=0.8, epos=0.5, bow=0, blow=0, bowtimbre=0.8, blowtimbre=0.8, gate=1|
var osc, env, susDiv;
sus = sus * blur;
		susDiv = sus*0.25;
		freq = In.kr(bus, 1);
freq = [freq, freq+fmod];
freq = freq/4;
osc = MiElements.ar(
			freq.cpsmidi, freq.cpsmidi,
			gate: gate, //Trig1.kr(1.0, sus);,
			pit: freq.cpsmidi,
			geom: 0, //LFNoise1.kr(0.1,0.5,0.5),
			contour: 0,
			bow_level: bow, bow_timb: bowtimbre,
			blow_level: blow, blow_timb:blowtimbre,
			mallet: emallet,
			strike_level:1, strike_timb: etimbre.clip(0,0.5),
			strength: eamp,
			flow: 0,
			bright: ebright,
			damp: edamp,
			pos: epos,
			space: ewide.clip(0,0.99),
			model: emodel,
		);
		// env = EnvGen.ar(Env.perc(atk, sus), doneAction:2);
		// env = EnvGen.ar(Env.adsr(atk, decay, level, rel, peak), doneAction: 2, timeScale: sus);
		env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
		// osc = RLPF.ar(osc, cutoff, rq);
		osc=(osc * env * amp).tanh;
osc = Mix(osc);
		osc = LeakDC.ar(osc);
//		osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc)}).add;


/*SynthDef.new(\elmbass,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.001, decay=0.05, rel=0.001, peak=1, level=0.8, emallet=0.5, etimbre=0.3, ebright=0.5, edamp=0.5, ewide=0.5, emodel=0, eamp=0.8, epos=0.5, bow=0, blow=0, bowtimbre=0.8, blowtimbre=0.8|
var osc, env, susDiv;
sus = sus * blur;
		susDiv = sus*0.25;
		freq = In.kr(bus, 1);
		freq = [freq, freq+fmod];
		freq = freq/4;

osc = MiElements.ar(
			freq.cpsmidi, freq.cpsmidi,
			gate: LFPulse.ar(rate),
			pit: freq.cpsmidi,
			geom: 0, //LFNoise1.kr(0.1,0.5,0.5),
			contour: 0.5,
			bow_level: 0, bow_timb: bowtimbre,
			blow_level: 0, blow_timb:blowtimbre,
			mallet: emallet,
			strike_level:1, strike_timb: etimbre.clip(0,0.5),
			strength: eamp,
			flow: 0,
			bright: ebright,
			damp: edamp,
			pos: epos,
			space: ewide.clip(0,0.99),
			model: emodel,
			mul: 2
		);
		env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 2);
		osc=(osc * env * amp).tanh;
		osc = Mix(osc);
//		osc = LeakDC.ar(osc);
		ReplaceOut.ar(bus, osc)}).add;*/
