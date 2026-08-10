SynthDef.new(\wob, {
    |bus=0, amp=1, sus=1, pan=0, freq=0, fmod=0, blur=1, beat_dur=1,
     atk=0.015, rel=0.08,
     rate=2,       // LFO rate in Hz
     depth=0.85,   // filter LFO depth (0-1)
     cutoff=400,   // base filter cutoff
     res=2.2,      // filter resonance (MoogFF 0-4, 2-3 = classic dub)
     shape=0,      // LFO shape: 0=sine, 1=triangle, 2=saw-ramp
     sub=0.55,     // sub-octave sine level
     drive=1.8,    // pre-filter saturation
     detune=0.006, // L/R detuning for width
     drift=0.4,    // organic filter drift (LFNoise)
     glide=0.0     // portamento time in seconds
    |

    var sig, subOsc, sawOsc, lfo, filterFreq, driftMod, env;
    sus = sus * blur;
    freq = In.kr(bus, 1);

    // portamento
    freq = Lag.kr(freq, glide);

    // --- oscillators ---
    // sub-octave sine: always present, anchors the low end
    subOsc = SinOsc.ar(freq / 2) * sub;

    // main: detuned saw pair + pulse for grind
    sawOsc = Saw.ar([freq * (1 - detune), freq * (1 + detune)]);
    sawOsc = sawOsc + (Pulse.ar(freq, 0.38) * 0.45);

    // combine and saturate before filter
    sig = Mix(sawOsc) + subOsc;
    sig = (sig * drive).tanh;

    // --- morphable LFO ---
    // shape 0→1: sin→tri, shape 1→2: tri→saw
    lfo = SelectX.kr(shape.clip(0, 2), [
        SinOsc.kr(rate),
        LFTri.kr(rate),
        LFSaw.kr(rate)
    ]);
    lfo = (lfo + 1) * 0.5;  // unipolar 0..1

    // organic drift (low-rate noise on top of LFO)
    driftMod = LFNoise2.kr(0.25).range(1 - (drift * 0.18), 1 + (drift * 0.18));

    // filter cutoff = base * (1 + LFO*depth*8) * drift
    filterFreq = cutoff * (1 + (lfo * depth * 8)) * driftMod;
    filterFreq = filterFreq.clip(30, 18000);

    // --- 24 dB Moog ladder filter: the dub magic ---
    sig = MoogFF.ar(sig, filterFreq, res.clip(0, 3.92));

    // sub bypasses filter — keeps low end tight even with closed filter
    sig = sig + (subOsc * 0.3);

    // --- amplitude envelope ---
    env = EnvGen.ar(
        Env([0, 1, 0.88, 0.88, 0], [atk, 0.01, max(sus - atk - rel - 0.01, 0.001), rel]),
        doneAction: 0
    );

    sig = sig * env * amp * 0.32;
    sig = Pan2.ar(sig, pan);
    ReplaceOut.ar(bus, sig)
}, metadata: (
    credit: "CrashServer",
    description: "Ultimate dub wobble — MoogFF 24dB, morphable sin/tri/saw LFO, sub+saw engine, portamento",
    category: \bass,
    tags: [\dub, \wobble, \bass, \moog, \lfo]
)).add;
