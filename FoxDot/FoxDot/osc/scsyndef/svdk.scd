SynthDef.new(\svdk, {
    |bus=0, amp=1, sus=1, pan=0, freq=0, fmod=0,
     atk=0.01, rel=0.1, blur=1, beat_dur=1,
     grit=0.5, noise=0.3, cutoff=800, res=0.5,
     track=1, fenv=0.3, slide=0.05, body=0.5,
     drift=0.3, harm=0.2|

    var osc, nz, sub, subSine, subDeep, env, fltEnv, sig, freqSlide, fltFreq;
    var filtered, rq, bassPath, midPath, harmonics;
    var panMod, driftL, driftR, sigL, sigR;

    sus = sus * blur;
    freq = In.kr(bus, 1);
    freq = freq + fmod;

    // === PORTAMENTO ===
    freqSlide = Lag.kr(freq, slide);

    // === OSCILLATOR STACK ===

    // Triple detuned saws - Juno character
    osc = LFSaw.ar(freqSlide, 0, 0.5);
    osc = osc + LFSaw.ar(freqSlide * 1.006, 0.33, 0.4);
    osc = osc + LFSaw.ar(freqSlide * 0.998, 0.66, 0.3);

    // === HARMONICS LAYER ===
    // Adds upper partials for richness
    harmonics = SinOsc.ar(freqSlide * 2, 0, 0.2 * harm);           // 2nd harmonic (octave)
    harmonics = harmonics + SinOsc.ar(freqSlide * 3, 0, 0.12 * harm); // 3rd (fifth above oct)
    harmonics = harmonics + SinOsc.ar(freqSlide * 5, 0, 0.08 * harm); // 5th (major third 2 oct up)
    harmonics = harmonics + Pulse.ar(freqSlide * 2, 0.3, 0.1 * harm); // Gritty 2nd

    // === SUB OSCILLATORS - THE BODY ===
    // Deep sub (one octave below)
    subDeep = SinOsc.ar(freqSlide * 0.25, 0, 0.4 * body);  // Two octaves down

    // Sine sub for clean low weight
    subSine = SinOsc.ar(freqSlide * 0.5, 0, 0.7 * body);

    // Pulse sub for grit in the lows
    sub = Pulse.ar(freqSlide * 0.5, 0.5, 0.4 * body);

    // Triangle at fundamental for warmth
    sub = sub + LFTri.ar(freqSlide, 0, 0.3 * body);

    // === NOISE ===
    nz = WhiteNoise.ar * noise * 0.5;
    nz = nz + (PinkNoise.ar * noise * 0.3);

    // Mix main oscillators + harmonics (goes through filter)
    midPath = osc + harmonics + nz;

    // === FILTER ENVELOPE ===
    fltEnv = EnvGen.kr(
        Env.perc(0.001, sus * 0.4, 1, -6),
        levelScale: fenv
    );

    // Keyboard tracking
    fltFreq = cutoff + (freq * track * 0.25) + (fltEnv * cutoff * 2);
    fltFreq = fltFreq.clip(60, 6000);

    // Resonance
    rq = (1 - res).linexp(0, 1, 0.05, 1);

    // Main resonant filter on mids only
    filtered = RLPF.ar(midPath, fltFreq, rq);

    // Add resonant peak emphasis
    filtered = filtered + (BPF.ar(midPath, fltFreq, 0.1) * res * 0.4);

    // === BASS PATH - bypasses harsh filter, stays fat ===
    bassPath = subDeep + subSine + sub;
    bassPath = LPF.ar(bassPath, 300);  // Keep it subby
    bassPath = (bassPath * (1 + (grit * 0.6))).tanh;  // Warm saturation on bass

    // === COMBINE PATHS ===
    sig = filtered + bassPath;

    // === BOSS MT-2 METAL ZONE DISTORTION ===
    // Pre-gain
    sig = sig * (1 + (grit * 3));

    // Stage 1: Soft saturation
    sig = (sig * 1.5).tanh;

    // Stage 2: Hard clip
    sig = (sig * (1 + (grit * 2))).clip(-0.75, 0.75);

    // Stage 3: Wave folding for harmonics
    sig = sig + ((sig * grit * 2).fold(-0.5, 0.5) * grit * 0.4);

    // Stage 4: Final saturation
    sig = (sig * (1 + grit)).tanh;

    // === EQ SHAPING ===
    // Bass boost for body
    sig = BLowShelf.ar(sig, 80, 1, body * 5);
    sig = BLowShelf.ar(sig, 150, 1, body * 3);

    // Slight mid cut
    sig = BPeakEQ.ar(sig, 500, 1.5, grit * -3);

    // Upper mid presence
    sig = BPeakEQ.ar(sig, 2000, 0.8, grit * 3);

    // High presence (controllable scream)
    sig = BHiShelf.ar(sig, 3500, 1, grit * res * 3);

    // === CLEAN UP ===
    sig = HPF.ar(sig, 25);
    sig = LPF.ar(sig, 16000);
    sig = LeakDC.ar(sig);

    // === AMPLITUDE ENVELOPE ===
    env = EnvGen.ar(
        Env.linen(atk, sus, rel, 1, -2),
        doneAction: 2
    );

    sig = sig * env * amp * 0.35;

    // === STEREO DRIFT ===
    // Slow movement for long sustained notes
    // Multiple LFOs at different rates for organic movement
    driftL = LFNoise2.kr(0.3 + (drift * 0.2)) * drift * 0.4;
    driftR = LFNoise2.kr(0.25 + (drift * 0.15)) * drift * 0.4;

    // Slight pitch drift between channels for width
    sigL = sig * (1 + (LFNoise2.kr(0.1) * drift * 0.003));
    sigR = sig * (1 + (LFNoise2.kr(0.12) * drift * 0.003));

    // Apply base pan + drift
    sigL = sigL * (1 - (pan + driftL).clip(-1, 1)).sqrt;
    sigR = sigR * (1 + (pan + driftR).clip(-1, 1)).sqrt;

    // Additional stereo widening via subtle delay
    sigR = DelayC.ar(sigR, 0.02, drift * 0.008);

    ReplaceOut.ar(bus, [sigL, sigR]);
}).add;
