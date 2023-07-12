SynthDef.new(\superbass,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, cutoff=5000, rq=0.0, rqd=0.0, detune=0.5, gate=1, fdecay=4, sub=1|
var osc, env, detuneCurve, centerGain, sideGain, center, detuneFactor, freqs, side, filterEnv, subOsc;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = freq/2;
		detuneCurve = { |x|
		(10028.7312891634*x.pow(11)) -
		(50818.8652045924*x.pow(10)) +
		(111363.4808729368*x.pow(9)) -
		(138150.6761080548*x.pow(8)) +
		(106649.6679158292*x.pow(7)) -
		(53046.9642751875*x.pow(6)) +
		(17019.9518580080*x.pow(5)) -
		(3425.0836591318*x.pow(4)) +
		(404.2703938388*x.pow(3)) -
		(24.1878824391*x.pow(2)) +
		(0.6717417634*x) +
		0.0030115596
	};
	centerGain = { |x| (-0.55366 * x) + 0.99785 };
	sideGain = { |x| (-0.73764 * x.pow(2)) + (1.2841 * x) + 0.044372 };

	center = LFSaw.ar(freq, Rand());
		detuneFactor = freq * detuneCurve.(detune.clip(0,1));
	freqs = [
		(freq - (detuneFactor * 0.11002313)),
		(freq - (detuneFactor * 0.06288439)),
		(freq - (detuneFactor * 0.01952356)),
		// (freq + (detuneFactor * 0)),
		(freq + (detuneFactor * 0.01991221)),
		(freq + (detuneFactor * 0.06216538)),
		(freq + (detuneFactor * 0.10745242))
		];
		side = Mix.fill(6, { |n|
			LFSaw.ar(freqs[n], Rand(0, 2))
		});

		subOsc = LFPulse.ar(freq/2, 0, mul: sub);
		osc = (center * centerGain.(1)) + (side * sideGain.(1) + subOsc);
		osc = HPF.ar(osc ! 2, freq);

		filterEnv = EnvGen .ar( Env .new([10e-10, 1, 10e-10], [0.01, sus*fdecay],  'exp' ), gate, doneAction: 2);
		osc = VALadder.ar(osc, cutoff*filterEnv, rq,rqd,0);
		env=EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 2);

osc=(osc * env * amp) ;
osc = Mix(osc*0.5);
osc = Pan2.ar(osc*0.25, pan);
	ReplaceOut.ar(bus, osc)},
metadata: (
		credit: "by CrashServer (audionerd supersaw based)",
	category: \bass,
	tags: [\ebm, \bass, \supersaw]
)).add;

/// Based on supersaw by audionerd https://gist.github.com/audionerd/fe50790b7601cba65ddd855caffb05ad ///
///

