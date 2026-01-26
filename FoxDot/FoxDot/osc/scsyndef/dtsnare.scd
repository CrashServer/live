// Deep Techno Snare - dtsnare
// Based on synthesis techniques from Sound on Sound's Synth Secrets
// Features: dual tonal modes (180Hz/330Hz), filtered noise, snare wire emulation, saturation
SynthDef.new(\dtsnare,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1,
  atk=0.001, decay=0.15, rel=0.1, peak=1, level=0.8,
  tone=0.6, snap=0.7, body=0.5, snares=0.8, drive=2.5, pitch=200, tight=0|

var snare, env, toneEnv, snapEnv, snareEnv;
var tonal, noisePart, snareSig, snapSig;

sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq + fmod];

// Use pitch parameter or fall back to freq, typical snare around 180-250Hz
pitch = Select.kr(pitch > 100, [freq.clip(150, 350), pitch]);

// Adjust decay based on tight parameter (0 = loose/deep, 1 = tight/snappy)
decay = decay * (1 - (tight * 0.5));
rel = rel * (1 - (tight * 0.4));

// === ENVELOPE SECTION ===

// Main envelope - sharp attack, controlled decay
// (Sound on Sound: "Attack: 0, Sustain: 0, Decay/Release: 2")
env = EnvGen.ar(Env(
	[0, 1, 0.6, 0.2, 0],
	[atk, 0.008, decay, rel],
	[-4, -3, -4]
), doneAction: 2);

// Tone envelope for pitched components - slightly longer
toneEnv = EnvGen.ar(Env(
	[0, 1, 0.5, 0],
	[0.001, 0.02, decay * 0.8],
	[-4, -2, -4]
));

// Snap envelope - very short for the crack
snapEnv = EnvGen.ar(Env([0, 1, 0], [0.0005, 0.012], [-4]));

// Snare wire envelope - slightly delayed attack, longer tail
snareEnv = EnvGen.ar(Env(
	[0, 0.3, 1, 0.4, 0],
	[0.002, 0.005, decay * 0.6, rel * 1.2],
	[2, -2, -3, -4]
));

// === TONAL SECTION ===
// (Sound on Sound: "180Hz and 330Hz represent the 0,1 mode partials")

tonal = Mix([
	// Fundamental mode ~180Hz with pitch drop
	SinOsc.ar(
		pitch * EnvGen.ar(Env([1.8, 1.1, 1], [0.003, 0.015], [-4])),
		mul: toneEnv * tone
	),
	// Second mode ~330Hz (ratio ~1.83)
	SinOsc.ar(
		pitch * 1.83 * EnvGen.ar(Env([1.5, 1], [0.008], [-3])),
		mul: toneEnv * tone * 0.6
	),
	// Body resonance - adds weight
	Ringz.ar(Impulse.ar(0), pitch * 0.8, 0.04, mul: toneEnv * body * 0.4),
	// Slight triangle for low-end
	LFTri.ar(pitch * 0.5, mul: toneEnv * body * 0.3)
]);

// === NOISE SECTION ===
// (Sound on Sound: "noise generator whose output can be treated by a filter")

noisePart = Mix([
	// Main noise band - mid frequencies for body
	BPF.ar(WhiteNoise.ar(), 1200, 0.7, mul: env * 0.8),
	// High noise - brightness and air
	HPF.ar(WhiteNoise.ar(), 5000, mul: env * 0.5),
	// Pink noise for natural density
	BPF.ar(PinkNoise.ar(), 800, 1.0, mul: env * 0.4),
	// Low-mid noise for body
	BPF.ar(WhiteNoise.ar(), 400, 0.8, mul: env * body * 0.5)
]);

// === SNARE WIRE EMULATION ===
// (Sound on Sound: "closer to some form of band-limited noise generator")

snareSig = Mix([
	// Main snare rattle - bandpassed noise with modulation
	BPF.ar(
		WhiteNoise.ar() * LFNoise2.ar(800).range(0.7, 1),
		2000,
		0.4,
		mul: snareEnv * snares
	),
	// Higher snare frequencies
	BPF.ar(WhiteNoise.ar(), 4500, 0.3, mul: snareEnv * snares * 0.6),
	// Characteristic snare "buzz" via ring mod
	BPF.ar(WhiteNoise.ar(), 3000, 0.5) *
		SinOsc.ar(180).abs * snareEnv * snares * 0.3
]);

// === SNAP/CRACK ===

snapSig = Mix([
	// High frequency crack
	BPF.ar(WhiteNoise.ar(), 7000, 0.2, mul: snapEnv * snap),
	// Click transient
	HPF.ar(Impulse.ar(0), 2000, mul: snapEnv * snap * 0.5),
	// Bright noise burst
	HPF.ar(WhiteNoise.ar(), 8000, mul: snapEnv * snap * 0.4)
]);

// === MIX AND PROCESSING ===

snare = Mix([
	tonal * 0.35,
	noisePart * 0.4,
	snareSig * 0.5,
	snapSig * 0.3
]) * env;

// Drive/saturation for techno character
snare = (snare * drive).fold(-0.7, 0.7);

// EQ shaping for deep techno snare
snare = BPeakEQ.ar(snare, pitch, 0.6, 2);        // Body emphasis
snare = BPeakEQ.ar(snare, 200, 0.8, body * 3);  // Low-end punch
snare = BPeakEQ.ar(snare, 3500, 0.5, snap * 4); // Crack/snap presence
snare = BPeakEQ.ar(snare, 7000, 0.4, 2);        // Air
snare = HPF.ar(snare, 80);                       // Clean up sub rumble

// Soft limiting
snare = Limiter.ar(snare, 0.95, 0.001);

snare = snare * amp * 0.6;
snare = Mix(snare) * 0.5;
snare = Pan2.ar(snare, pan);
ReplaceOut.ar(bus, snare)
}).add;
