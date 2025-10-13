SynthDef.new(\synthwave,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.5, cutoff=3500, rq=0.5, detune=0.08, chorus=0.3, unison=7|
var osc, env, center, sides, filterEnv, vibLFO, pwm, filtered;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];

vibLFO = SinOsc.kr(5 + (vib * 2), Rand(0, 2*pi)).range(0.998, 1.002);
freq = freq * vibLFO;


center = Saw.ar(freq, mul: 0.35);


sides = Mix.fill(6, {|i|
	var detuneAmount = detune * ((i+1) * 0.015);  // Tighter detune for cleaner sound
	var thisFreq = if(i < 3,
		freq * (1 - detuneAmount),
		freq * (1 + detuneAmount)
	);
	// Slight amplitude variation for analog character
	var ampVar = LFNoise1.kr(0.2).range(0.92, 1.0);
	Saw.ar(thisFreq, mul: 0.55 * ampVar)
});


osc = center + sides;


pwm = Pulse.ar(freq, width: SinOsc.kr(chorus).range(0.35, 0.65), mul: 0.15);
osc = osc + pwm;


filterEnv = EnvGen.ar(Env([0.6, 1, 0.85, 0.75], [atk, decay * 0.5, sus * 0.5], curve: [2, -2, -1]));


filtered = BLowPass4.ar(osc, (cutoff * filterEnv).clip(80, 18000), rq);


filtered = (filtered * 0.7) + (RLPF.ar(osc, cutoff * filterEnv, rq * 0.6) * 0.3);


filtered = BHiPass.ar(filtered, 30);


filtered = (filtered * 1.15).softclip * 0.95;


filtered = filtered + AllpassN.ar(filtered, 0.04,
	LFNoise1.kr(0.15 ! 2).range(0.008, 0.025),
	1.5, mul: 0.25 * wide
);

env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
filtered = filtered * env;

osc = Mix(filtered) * 0.4;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc * amp)}).add;
