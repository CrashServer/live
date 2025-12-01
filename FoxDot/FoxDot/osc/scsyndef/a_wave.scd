SynthDef.new(\a_wave,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1, atk=0.01, decay=0.01, rel=0.01, peak=1, level=0.8, wide=0.5, cutoff=3500, rq=0.5, detune=0.5, chorus=0.3, unison=7|
var osc, env, center, sides, filterEnv, vibLFO, pwm, filtered, drift, detuneCurve;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq+fmod];

// Analog-style pitch drift - slow random walk
drift = LFNoise1.kr(0.05 ! 2).range(0.9995, 1.0005);
freq = freq * drift;

// Classic synthwave vibrato - subtle and musical
vibLFO = SinOsc.kr(5 + (vib * 2), Rand(0, 2*pi)).range(0.9985, 1.0015);
freq = freq * vibLFO;

// JP-8000 supersaw detune curve (approximation)
// Non-linear curve provides more musical sweet spots
detuneCurve = {|x|
	var curve = (10028.7312891634 * (x.pow(11))) -
	(50818.8652045924 * (x.pow(10))) +
	(111363.4808729368 * (x.pow(9))) -
	(138150.6761080548 * (x.pow(8))) +
	(106649.6679158292 * (x.pow(7))) -
	(53046.9642751875 * (x.pow(6))) +
	(17019.9518580080 * (x.pow(5))) -
	(3425.0836591318 * (x.pow(4))) +
	(404.2703938388 * (x.pow(3))) -
	(24.1878824391 * (x.pow(2))) +
	(0.6717417634 * x) +
	0.0030115596;
	curve
};

// Use bandlimited Saw (Saw.ar is bandlimited, LFSaw is not)
// Center saw - free-running (no phase reset) for analog character
center = Saw.ar(freq, mul: 0.4);

// Professional JP-8000 style supersaw: 6 detuned voices with non-linear curve
// Using the reverse-engineered detune algorithm for sweet spots
sides = Mix.fill(6, {
	arg i;
	var detuneFactors, thisDetune, thisFreq, oscDrift, ampVar;
	detuneFactors = [
		0.11002313,  // Voice 1 (lowest)
		0.06288439,  // Voice 2
		0.01952356,  // Voice 3
		0.01991221,  // Voice 4
		0.06216538,  // Voice 5
		0.10745242   // Voice 6 (highest)
	];
	thisDetune = freq * (detuneCurve.(detune.clip(0, 1)) * detuneFactors[i]);
	thisFreq = if(i < 3,
		freq - thisDetune,  // Lower voices
		freq + thisDetune   // Upper voices
	);
	// Individual pitch drift per oscillator (analog instability)
	oscDrift = LFNoise1.kr(0.08 + Rand(0, 0.04)).range(0.9998, 1.0002);
	thisFreq = thisFreq * oscDrift;

	// Slight amplitude variation for analog character
	ampVar = LFNoise1.kr(0.15 + Rand(0, 0.1)).range(0.90, 1.0);
	Saw.ar(thisFreq, mul: 0.5 * ampVar)
});

// Blend center and sides
osc = center + sides;

// Add clean PWM layer using bandlimited pulse - classic analog string/pad character
// Pulse width modulated by LFO - classic 70s/80s technique
pwm = Pulse.ar(freq, width: SinOsc.kr(chorus + LFNoise1.kr(0.1).range(-0.1, 0.1)).range(0.35, 0.65), mul: 0.12);
osc = osc + pwm;

// Filter envelope for synthwave movement - exponential curves for analog feel
filterEnv = EnvGen.ar(Env([0.6, 1, 0.85, 0.75], [atk, decay * 0.5, sus * 0.5], curve: [-4, 2, -2]));

// Multi-stage filtering approach (vintage synths often had multiple filter stages)
// Stage 1: Smooth Butterworth 4-pole (24dB/oct) - clean rolloff
filtered = BLowPass4.ar(osc, (cutoff * filterEnv).clip(100, 18000), rq);

// Stage 2: Add subtle resonant character (Moog-style if available, else RLPF)
// Lower mix prevents harshness while adding analog character
filtered = (filtered * 0.75) + (RLPF.ar(osc, cutoff * filterEnv, rq * 0.5) * 0.25);

// Clean high-pass to remove sub-mud without aliasing
filtered = BHiPass.ar(filtered, 25);

// Vintage-style soft saturation - emulates tube/transformer warmth
// Keep levels low to avoid harsh digital distortion (per Sound on Sound advice)
filtered = (filtered * 1.08).softclip * 0.96;

// Stereo chorus/ensemble effect - emulates Roland Dimension D / Juno chorus
// Multiple modulated allpass delays for lush stereo image
filtered = filtered + AllpassN.ar(filtered, 0.04,
	[LFNoise1.kr(0.12).range(0.008, 0.022), LFNoise1.kr(0.18).range(0.010, 0.028)],
	2.0, mul: 0.3 * wide
);

// Add subtle stereo width via short decorrelated delays
filtered = filtered + DelayN.ar(filtered, 0.02,
	[LFNoise1.kr(0.25).range(0.003, 0.008), LFNoise1.kr(0.28).range(0.004, 0.009)],
	mul: 0.15 * wide
);

// Main amplitude envelope - exponential curves for natural analog feel
env = EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve: [-4, 2, 0, -4]), doneAction: 0);
filtered = filtered * env;

osc = Mix(filtered) * 0.25;
osc = Pan2.ar(osc, pan);
	ReplaceOut.ar(bus, osc * amp)}).add;
