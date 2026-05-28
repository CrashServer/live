// Compile FoxDot synths adapted for SuperSonic
// All var declarations must be at the TOP of each function in SC

var outDir = "/home/svdk/live/supersonic-proto/lib/synthdefs/";
("Writing to: " ++ outDir).postln;

SynthDef(\fd_bleep, {|note=60, amp=0.7, sus=1, pan=0, attack=0.01, release=0.08|
    var freq, dur, env, osc;
    freq = note.midicps;
    dur = (sus - attack - release).max(0.001);
    env = EnvGen.ar(Env([0,1,1,0], [attack, dur, release], \sine), doneAction:2);
    osc = SinOsc.ar(freq) * amp * env;
    Out.ar(0, Pan2.ar(osc, pan));
}).writeDefFile(outDir);
"fd_bleep done".postln;

SynthDef(\fd_dbass, {|note=48, amp=0.8, sus=1, pan=0, attack=0.02, release=0.12, cutoff=2000, rq=0.5, phase=0.9|
    var freq, freqs, osc, dur, env, sig;
    freq = note.midicps;
    freqs = [freq, freq] * Line.ar(Rand(0.5,1.5), 1, 0.025);
    freqs = freqs / 4;
    osc = VarSaw.ar(freqs,
        width: LFTri.ar(0.5 / sus.max(0.05), iphase: phase, add: 0.8, mul: 0.2),
        mul: amp * 0.4);
    dur = ((sus - attack - release) * 0.5).max(0.001);
    env = EnvGen.ar(Env([0,1,0.8,0.8,0], [attack, 0.01, dur, dur, release]), doneAction:2);
    sig = Mix(osc) * 0.5 * env;
    sig = RLPF.ar(sig, cutoff.clip(60, 18000), rq.clip(0.05, 1.0));
    Out.ar(0, Pan2.ar(sig, pan));
}).writeDefFile(outDir);
"fd_dbass done".postln;

SynthDef(\fd_reese, {|note=48, amp=0.8, sus=1, pan=0, attack=0.01, release=0.1, detune=0.022, cutoff=1200, rq=0.65|
    var freq, osc1, osc2, sub, osc, dur, env, sig;
    freq = note.midicps;
    osc1 = LFSaw.ar(freq * (1 - detune));
    osc2 = LFSaw.ar(freq * (1 + detune));
    sub  = SinOsc.ar(freq * 0.5, 0, 0.5);
    osc  = [osc1 + (osc2 * 0.6) + sub, osc2 + (osc1 * 0.6) + sub];
    osc  = RLPF.ar(osc, cutoff.clip(80, 8000), rq.clip(0.05, 1.0));
    osc  = osc.tanh;
    dur  = (sus - attack - release).max(0.001);
    env  = EnvGen.ar(Env.linen(attack, dur, release, 1, \lin), doneAction:2);
    sig  = Balance2.ar(osc[0], osc[1], pan) * env * amp * 0.3;
    Out.ar(0, sig);
}).writeDefFile(outDir);
"fd_reese done".postln;

SynthDef(\fd_juno, {|note=60, amp=0.7, sus=1, pan=0, attack=0.02, release=0.15, shape=0.0, cutoff=3200, rq=0.7, chorus=0.004|
    var freq, saw, sq, dco, ch1, ch2, osc, sub, dur, env;
    freq = note.midicps;
    saw  = LFSaw.ar(freq);
    sq   = LFPulse.ar(freq, 0, 0.5);
    dco  = XFade2.ar(saw, sq, shape.clip(-1,1));
    ch1  = LFSaw.ar(freq * (1 + chorus));
    ch2  = LFSaw.ar(freq * (1 - chorus));
    osc  = Mix([dco, ch1, ch2]) * 0.33;
    sub  = SinOsc.ar(freq * 0.5, mul: 0.3);
    osc  = osc + sub;
    osc  = RLPF.ar(osc, cutoff.clip(100, 18000), rq.clip(0.05, 1.0));
    dur  = (sus - attack - release).max(0.001);
    env  = EnvGen.ar(Env.linen(attack, dur, release, 1, \sine), doneAction:2);
    osc  = osc * env * amp * 0.5;
    Out.ar(0, Pan2.ar(osc, pan));
}).writeDefFile(outDir);
"fd_juno done".postln;

SynthDef(\fd_pluck, {|note=60, amp=0.8, sus=2, pan=0, attack=0.001, release=0.5|
    var freq, exc, osc, env;
    freq = note.midicps;
    exc  = WhiteNoise.ar(amp) * EnvGen.ar(Env.perc(0.001, 0.03), doneAction:0);
    osc  = CombL.ar(exc, 1.0/freq, 1.0/freq, sus * 2);
    env  = EnvGen.ar(Env.linen(attack, sus, release, 1, \sine), doneAction:2);
    osc  = LPF.ar(osc, 5000) * env * amp;
    Out.ar(0, Pan2.ar(osc, pan));
}).writeDefFile(outDir);
"fd_pluck done".postln;

SynthDef(\fd_sine, {|note=60, amp=0.7, sus=1, pan=0, attack=0.05, release=0.3, vib=0|
    var freq, vibSig, osc, dur, env;
    freq   = note.midicps;
    vibSig = SinOsc.ar(6, 0, vib * freq * 0.04);
    osc    = SinOsc.ar(freq + vibSig) * amp;
    dur    = (sus - attack - release).max(0.001);
    env    = EnvGen.ar(Env.linen(attack, dur, release, 1, \sine), doneAction:2);
    osc    = osc * env;
    Out.ar(0, Pan2.ar(osc, pan));
}).writeDefFile(outDir);
"fd_sine done".postln;

"All synthdefs written.".postln;
0.exit;
