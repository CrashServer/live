SynthDef(\grandpiano,
{|bus=0, freq=440, fmod=0, amp=1, sus=1, pan=0, vib=0, blur=1, vel=0.7, bright=0.5, body=0.6, pedal=0, wide=0.3|
var osc, hammer, strings, partials, sympathetic, env, damperEnv;
var freqSlide, velBright, rq;
sus = sus * blur;
freq = In.kr(bus, 1);
freq = Vibrato.kr(freq, vib, depth: fmod);
freqSlide = freq;

// === VELOCITY → BRIGHTNESS ===
// Soft = warm (low cutoff), hard = bright (high cutoff)
velBright = vel.linexp(0, 1, 800, 12000) * (0.5 + (bright * 0.8));

// === HAMMER STRIKE ===
// Percussive click — filtered noise burst
hammer = HPF.ar(WhiteNoise.ar, 1000) * EnvGen.ar(Env.perc(0.001, 0.008 + (vel * 0.01)));
hammer = LPF.ar(hammer, velBright * 2);
hammer = hammer * vel * 0.15;

// === STRING FUNDAMENTAL ===
// Detuned pair for natural beating (real piano strings are 2-3 per note)
strings = SinOsc.ar(freqSlide, 0, 0.4);
strings = strings + SinOsc.ar(freqSlide * 1.0008, 0, 0.35);
strings = strings + SinOsc.ar(freqSlide * 0.9996, 0, 0.25);

// === INHARMONIC PARTIALS ===
// Piano strings aren't perfectly harmonic — slight stretch
partials = SinOsc.ar(freqSlide * 2.001, 0, 0.18 * vel);
partials = partials + SinOsc.ar(freqSlide * 3.005, 0, 0.09 * vel);
partials = partials + SinOsc.ar(freqSlide * 4.012, 0, 0.05 * vel);
partials = partials + SinOsc.ar(freqSlide * 5.02, 0, 0.03 * vel);
partials = partials + SinOsc.ar(freqSlide * 6.03, 0, 0.015 * vel * bright);

// Brightness filter — velocity + bright control
osc = strings + partials + hammer;
osc = RLPF.ar(osc, velBright, 0.5);

// === BODY RESONANCE ===
// Soundboard simulation — low shelf + gentle resonances
osc = BLowShelf.ar(osc, 200, 0.8, body * 4);
osc = BPeakEQ.ar(osc, 250, 1.5, body * 2);
osc = BPeakEQ.ar(osc, 2500, 1, vel * 2);

// === SYMPATHETIC STRING RESONANCE ===
// Other strings ring when a note plays — the piano's "halo"
sympathetic = Ringz.ar(osc * 0.005, freqSlide * 2, 0.3) * body;
sympathetic = sympathetic + Ringz.ar(osc * 0.003, freqSlide * 1.5, 0.25) * body;
sympathetic = sympathetic + Ringz.ar(osc * 0.002, freqSlide * 3, 0.2) * body * bright;
sympathetic = LPF.ar(sympathetic, 6000);
osc = osc + sympathetic;

// === MULTI-STAGE ENVELOPE ===
// Fast attack → bright initial decay → slower body decay → pedal tail
env = EnvGen.ar(
    Env(
        [0, 1, 0.6, 0.3, 0],
        [0.003, 0.08, sus * 0.6, sus * 0.4 + (pedal * 4)],
        [2, -4, -3, -5]
    ),
    doneAction: 2
);

// === DAMPER SIMULATION ===
// When note releases, brief "thunk" as damper hits string
damperEnv = EnvGen.ar(Env.perc(0.001, 0.02), gate: 1 - EnvGen.kr(Env([1, 1, 0], [sus, 0.01])));
osc = osc + (BPF.ar(WhiteNoise.ar(0.02), freqSlide * 0.5, 0.3) * damperEnv * (1 - pedal));

osc = osc * env * amp * 0.6;

// Cleanup
osc = HPF.ar(osc, 30);
osc = LPF.ar(osc, 14000);
osc = LeakDC.ar(osc);

// Stereo — slight spread based on register (low=center, high=wider)
osc = Pan2.ar(osc, pan + (LFNoise2.kr(0.2) * wide * 0.2));
ReplaceOut.ar(bus, osc)},
metadata: (
    credit: "CrashServer",
    description: "Physical model grand piano — hammer, strings, body, sympathetic resonance",
    category: \keyboard,
    tags: [\piano, \acoustic, \keys]
)).add;
