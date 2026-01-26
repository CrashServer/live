// Deep Techno Clap - dtclap
// Based on TR-808/909 synthesis from Attack Magazine
// Features: multi-hit "doubling", filtered noise, reverb tail, tight envelope
SynthDef.new(\dtclap,
{|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0, blur=1, beat_dur=1,
  atk=0.001, decay=0.12, rel=0.15, peak=1, level=0.8,
  tone=1200, spread=3, thick=0.6, snap=0.7, room=0.3, drive=2, tight=0|

var clap, env, multiEnv, spreadEnv, roomSig;
var mainNoise, spreadNoise, snapSig, bodyNoise;
var numHits, hitTimes, hitAmps;

sus = sus * blur;
freq = In.kr(bus, 1);
freq = [freq, freq + fmod];

// Clap tone center (typically 800-1500 Hz)
tone = tone.clip(600, 2000);

// Tighten decay for tight parameter
decay = decay * (1 - (tight * 0.4));
rel = rel * (1 - (tight * 0.3));

// === MULTI-HIT ENVELOPE (808/909 CHARACTERISTIC) ===
// (Attack Magazine: "double up the clap signal to make it seem like a group")

// Number of "hands" in the clap (2-4 hits)
numHits = spread.clip(1, 4).round;

// Create staggered hits with decreasing amplitude
// Hit timings: slightly irregular like real handclaps
multiEnv = Mix([
	EnvGen.ar(Env([0, 1, 0], [0.0001, 0.015], [-4])),
	EnvGen.ar(Env([0, 0, 0.9, 0], [0.012, 0.0001, 0.018], [-4])) * (numHits >= 2),
	EnvGen.ar(Env([0, 0, 0.75, 0], [0.027, 0.0001, 0.02], [-4])) * (numHits >= 3),
	EnvGen.ar(Env([0, 0, 0.6, 0], [0.038, 0.0001, 0.022], [-4])) * (numHits >= 4)
]);

// Main envelope - the overall shape
env = EnvGen.ar(Env(
	[0, 1, 0.7, 0.3, 0],
	[atk, 0.01, decay, rel],
	[-4, -2, -4, -5]
), doneAction: 2);

// Spread envelope - for the reverb/room tail
spreadEnv = EnvGen.ar(Env(
	[0, 0.3, 1, 0.5, 0],
	[0.01, 0.02, decay * 0.5, rel * 2],
	[2, -2, -3, -4]
));

// === MAIN NOISE SECTION ===
// (Attack Magazine: "heavy lifting can be done with white noise and a filter")

mainNoise = Mix([
	// Core clap band - mid frequencies
	BPF.ar(WhiteNoise.ar(), tone, 0.5, mul: multiEnv),
	// Upper mid presence
	BPF.ar(WhiteNoise.ar(), tone * 1.5, 0.4, mul: multiEnv * 0.7),
	// Lower body
	BPF.ar(PinkNoise.ar(), tone * 0.6, 0.6, mul: multiEnv * thick * 0.5)
]);

// High-pass filter the clap (Attack Magazine: "highpass at 12dB/octave")
mainNoise = HPF.ar(mainNoise, 200);

// Resonance for bite (Attack Magazine: "resonance approximately 62")
mainNoise = RLPF.ar(mainNoise, tone * 2.5, 0.4) * 0.7 + (mainNoise * 0.5);

// === SNAP/CRACK COMPONENT ===

snapSig = Mix([
	// High frequency crack
	HPF.ar(WhiteNoise.ar(), 6000, mul: EnvGen.ar(Env([0, 1, 0], [0.0003, 0.008], [-4]))) * snap,
	// Very high transient
	BPF.ar(WhiteNoise.ar(), 8000, 0.3, mul: EnvGen.ar(Env([0, 1, 0], [0.0001, 0.005], [-8]))) * snap * 0.6,
	// Click attack
	Impulse.ar(0) * 0.3 * snap
]);

// === BODY/THICKNESS ===

bodyNoise = Mix([
	// Low-mid body
	BPF.ar(PinkNoise.ar(), 500, 0.8, mul: env * thick),
	// Slight tonal hint
	Ringz.ar(Impulse.ar(0), tone * 0.8, 0.03, mul: env * thick * 0.3)
]);

// === ROOM/REVERB SIMULATION ===
// (Attack Magazine: subtle reverb for depth)

roomSig = Mix([
	// Early reflections via comb filters
	CombL.ar(mainNoise * 0.3, 0.1, 0.023, 0.08),
	CombL.ar(mainNoise * 0.25, 0.1, 0.031, 0.07),
	CombL.ar(mainNoise * 0.2, 0.1, 0.041, 0.06),
	// Diffuse tail
	LPF.ar(
		AllpassL.ar(
			AllpassL.ar(mainNoise * 0.4, 0.05, 0.017, 0.1),
			0.05, 0.023, 0.12
		),
		4000
	)
]) * room * spreadEnv;

// === MIX AND PROCESSING ===

clap = Mix([
	mainNoise * 0.5,
	snapSig * 0.3,
	bodyNoise * 0.25,
	roomSig * 0.4
]) * env;

// Drive for techno character
clap = (clap * drive).tanh;

// EQ shaping for deep techno clap
clap = BPeakEQ.ar(clap, tone, 0.6, 2);        // Main frequency emphasis
clap = BPeakEQ.ar(clap, 400, 0.7, thick * 3); // Body
clap = BPeakEQ.ar(clap, 3000, 0.5, snap * 4); // Crack/presence
clap = BPeakEQ.ar(clap, 7000, 0.4, 2);        // Air/brightness
clap = HPF.ar(clap, 150);                      // Clean up lows

// Compression for punch
// (Attack Magazine: "medium attack/release with punch enhancement")
clap = Compander.ar(clap, clap, 0.4, 1, 0.4, 0.005, 0.05);

// Soft limiting
clap = Limiter.ar(clap, 0.95, 0.001);

clap = clap * amp * 0.6;
clap = Mix(clap) * 0.5;
clap = Pan2.ar(clap, pan);
ReplaceOut.ar(bus, clap)
}).add;
