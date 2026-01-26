// Deep Techno HiHat - dthihat
// Based on TR-808/909 synthesis from Sound on Sound
// Features: 6 square wave oscillators (808 style), ring mod metallic, variable open/closed
SynthDef.new(\dthihat,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1,
  atk=0.001, decay=0.05, rel=0.05, peak=1, level=0.8,
  tone=8000, open=0, metallic=0.7, noise=0.6, ring=0.5, drive=1.5, bright=0.7|

var hihat, env, metalEnv, noiseEnv;
var squareOscs, ringMod, noisePart, highPart;

// 808/909 hihat frequency ratios - enharmonic for metallic character
// (Sound on Sound: "six square-wave oscillators tuned enharmonically")
var ratios = [1.0, 1.4471, 1.6170, 1.9265, 2.5028, 2.6637];
var freqs;

sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq + fmod];

// Base tone frequency (typically 8000-12000 Hz range)
tone = tone.clip(4000, 14000);
freqs = tone * ratios;

// === ENVELOPE SECTION ===

// Main envelope - sharp attack, variable decay based on open parameter
// (closed hat: ~50ms, open hat: ~300ms+)
env = EnvGen.ar(Env(
	[0, 1, 0.6, 0.15, 0],
	[atk, 0.003, decay + (open * 0.25), rel + (open * 0.2)],
	[-4, -2, -4, -6]
), doneAction: 2);

// Metallic component envelope - slightly different shape
metalEnv = EnvGen.ar(Env(
	[0, 1, 0.7, 0.1, 0],
	[0.0005, 0.005, decay + (open * 0.2), rel + (open * 0.15)],
	[-8, -3, -4, -5]
));

// Noise envelope - fastest decay for high freqs
noiseEnv = EnvGen.ar(Env(
	[0, 1, 0.4, 0],
	[0.0003, 0.008, decay + (open * 0.1)],
	[-4, -3, -5]
));

// === SQUARE WAVE OSCILLATORS (TR-808 STYLE) ===
// (Sound on Sound: "creates a complex cluster of partials")

squareOscs = Mix(
	freqs.collect({ |f, i|
		var detune = LFNoise1.kr(0.5).range(0.998, 1.002);
		Pulse.ar(
			f * detune,
			0.5,
			mul: metalEnv * (1 / (i + 1).sqrt) // Higher partials quieter
		)
	})
) * metallic * 0.3;

// === RING MODULATION - METALLIC CHARACTER ===

ringMod = Mix([
	// Cross-modulation of oscillator pairs
	SinOsc.ar(tone * 1.0) * SinOsc.ar(tone * 1.4471) * metalEnv * 0.4,
	SinOsc.ar(tone * 1.6170) * SinOsc.ar(tone * 1.9265) * metalEnv * 0.3,
	SinOsc.ar(tone * 2.5028) * SinOsc.ar(tone * 2.6637) * metalEnv * 0.25,
	// Additional inharmonic shimmer
	SinOsc.ar(tone * 0.7433) * SinOsc.ar(tone * 3.1415) * metalEnv * 0.2
]) * ring;

// === NOISE SECTION ===
// (Sound on Sound: "band-pass filtering isolates upper frequencies")

noisePart = Mix([
	// Main noise band
	BPF.ar(WhiteNoise.ar(), tone, 0.4, mul: noiseEnv),
	// Higher noise
	BPF.ar(WhiteNoise.ar(), tone * 1.5, 0.3, mul: noiseEnv * 0.7),
	// Very high shimmer
	HPF.ar(WhiteNoise.ar(), tone * 0.8, mul: noiseEnv * 0.5),
	// Filtered pink for body
	BPF.ar(PinkNoise.ar(), tone * 0.6, 0.5, mul: noiseEnv * 0.4)
]) * noise;

// === HIGH FREQUENCY ENHANCEMENT ===

highPart = Mix([
	// Bright click on attack
	HPF.ar(Impulse.ar(0), tone * 0.5) * EnvGen.ar(Env([0, 1, 0], [0.0001, 0.002])) * 0.3,
	// Ultra-high shimmer
	HPF.ar(WhiteNoise.ar(), 12000, mul: metalEnv * bright * 0.4)
]);

// === MIX AND PROCESSING ===

hihat = Mix([
	squareOscs * 0.4,
	ringMod * 0.35,
	noisePart * 0.5,
	highPart * 0.3
]) * env;

// Light drive for character
hihat = (hihat * drive).tanh;

// EQ shaping for deep techno hihat
hihat = BPeakEQ.ar(hihat, tone, 0.5, 3);           // Main frequency presence
hihat = BPeakEQ.ar(hihat, tone * 0.5, 0.7, -2);   // Reduce low-mids
hihat = BHiShelf.ar(hihat, 10000, 1, bright * 4); // Brightness control
hihat = HPF.ar(hihat, 4000);                       // Remove lows entirely

// Subtle compression for punch
hihat = Compander.ar(hihat, hihat, 0.5, 1, 0.3, 0.001, 0.05);

// Soft limiting
hihat = Limiter.ar(hihat, 0.95, 0.001);

hihat = hihat * amp * 0.5;
hihat = Mix(hihat) * 0.5;
hihat = Pan2.ar(hihat, pan);
ReplaceOut.ar(bus, hihat)
}).add;
