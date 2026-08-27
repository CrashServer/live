SynthDef(\tekno,
{|bus, freq=440, amp=1, sus=1, pan=0, vib=0, fmod=0, rate=1, slide=0, slidefrom=1, glide=0, bend=0, coarse=0,
  tcut=800, trez=0.5, tenv=4000, tdec=0.3, tlfo=0, tmod=0,
  tsub=0.6, tgrit=0.5, tfold=0, tpw=0.5, tsync=0, txmod=0|

var osc, sub, subSq, main, syncOsc, pw, env, filt, filtenv, filtlfo;
var folded, xmod, driftL, driftR, sigL, sigR, freqSlide;

// === FREQUENCY ===
freq = freq * Line.kr(slidefrom, 1, sus * 0.5) * Line.kr(1, 1 + slide, sus) * Lag.kr(1 + bend, 0.05);
freqSlide = Lag.kr(freq, glide);
freqSlide = Vibrato.kr(freqSlide, vib, depth: fmod);

// === SUB OSCILLATORS — SH-101 inspired ===
// Sine fundamental + square sub one octave below (like SH-101 sub)
sub = SinOsc.ar(freqSlide);
// Slight harmonic distortion on sub — not a dead sine
sub = (sub * 1.15).tanh;
// Square sub one octave down — the weight
subSq = Pulse.ar(freqSlide * 0.5, 0.5, 0.5);
subSq = LPF.ar(subSq, 250);
sub = (sub + subSq) * tsub;
sub = LPF.ar(sub, 400);

// === MAIN OSCILLATORS — Moog/Prophet inspired ===
// Osc 1: Saw with analog drift (not linear detune)
osc = DPW4Saw.ar(freqSlide * (1 + (LFNoise2.kr(0.3) * 0.002)));
// Osc 2: Saw slightly detuned with its own drift
main = DPW4Saw.ar(freqSlide * (1.005 + (LFNoise2.kr(0.25) * 0.002)));

// === HARD SYNC — Subsequent 37 style ===
// Sync oscillator: slave freq is higher, synced to master
// tsync 0 = off, 1 = one octave up sync, higher = more harmonics
syncOsc = SyncSaw.ar(freqSlide, freqSlide * (1 + tsync));
// Blend sync in
main = XFade2.ar(main, syncOsc, tsync.clip(0, 2) - 1);

// === CROSS MODULATION — Analog Four style ===
// Osc1 frequency-modulates Osc2
xmod = osc * txmod * freqSlide;
main = DPW4Saw.ar(freqSlide * 1.005 + xmod) * (1 - tsync.clip(0, 1)) + (main * tsync.clip(0, 1));

// === PULSE with PWM ===
pw = SinOsc.kr(rate * 0.7).range(tpw.clip(0.05, 0.95) * 0.6, tpw.clip(0.05, 0.95));
main = main + Pulse.ar(freqSlide, pw, 0.35);

// Mix oscillators
main = (osc * 0.4) + (main * 0.6);

// Stereo: analog drift between channels (not static micro-delay)
driftL = LFNoise2.kr(0.2) * 0.003;
driftR = LFNoise2.kr(0.17) * 0.003;
main = [
    main * (1 + driftL) + DelayC.ar(main, 0.01, LFNoise2.kr(0.3).range(0.0003, 0.0015)),
    main * (1 + driftR)
];

// === PRE-FILTER MULTIDRIVE — Moog Multidrive inspired ===
// Stage 1: soft saturation
main = (main * (1 + (tgrit * 3))).tanh;
// Stage 2: asymmetric clip — adds even harmonics like real tubes
main = main + (main.squared * tgrit * 0.3);
main = main.clip(-1.2, 0.9);

// === FILTER — dual stage ladder ===
filtenv = EnvGen.kr(Env.perc(0.001, tdec, 1, -5));
filtlfo = if(tlfo > 0, SinOsc.kr(tlfo).range(-1, 1) * tmod * 3000, 0);
filt = tcut + (filtenv * tenv) + filtlfo;
// Keyboard tracking
filt = filt + (freqSlide * 0.6);
filt = filt.clip(30, 18000);

// First filter: main resonant sweep (Moog ladder)
main = MoogFF.ar(main, filt, trez.clip(0, 0.97) * 4);
// Second filter: gentle LP to tame harshness (like a real circuit's output stage)
main = RLPF.ar(main, (filt * 1.5).clip(30, 18000), 0.7);

// === WAVEFOLDER — Make Noise / Intellijel style ===
// Sine-based transfer function (not linear fold2 — creates musical harmonics)
folded = (main * (1 + (tfold * 6))).sin;
folded = folded + ((main * (2 + (tfold * 4))).sin * 0.3);
main = XFade2.ar(main, folded, tfold.clip(0, 1) * 2 - 1);

// === MIX sub + main ===
osc = sub + main;

// === OUTPUT STAGE — analog console saturation ===
osc = (osc * 1.2).tanh;
osc = LeakDC.ar(osc);
osc = HPF.ar(osc, 25);

// EQ — body + presence
osc = BLowShelf.ar(osc, 80, 0.7, 3);
osc = BPeakEQ.ar(osc, 180, 2, -2);
osc = BPeakEQ.ar(osc, 900, 1.5, tgrit * -2);
osc = BPeakEQ.ar(osc, 2800, 0.6, tgrit * 2.5);

// === ENVELOPE ===
env = EnvGen.ar(Env.linen(0.003, sus - 0.008, 0.005, 1, -3), doneAction: 2);
osc = osc * env * amp * 0.4;

// Pan + output
osc = Balance2.ar(osc[0], osc[1], pan);
ReplaceOut.ar(bus, osc)}).add;
