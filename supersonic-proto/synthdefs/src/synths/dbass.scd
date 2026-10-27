// dbass — deep bass, adapted from FoxDot dbass (CrashServer)
// Params: out, note, amp, sus, pan, attack, release, cutoff, rq, phase
// Edit this file, then run: scripts/build.sh

SynthDef(\fd_dbass, {|out=0, note=60, amp=0.8, sus=1, pan=0, attack=0.02, release=0.12,
                       cutoff=2000, rq=0.5, phase=0.9|
    var freq, freqs, osc, dur, env, sig;
    freq   = note.midicps;
    freqs  = [freq, freq] * Line.ar(Rand(0.5, 1.5), 1, 0.025);
    freqs  = freqs / 4;
    osc    = VarSaw.ar(freqs,
                 width: LFTri.ar(0.5 / sus.max(0.05), iphase: phase, add: 0.8, mul: 0.2),
                 mul: amp * 0.4);
    dur    = ((sus - attack - release) * 0.5).max(0.001);
    env    = EnvGen.ar(Env([0, 1, 0.8, 0.8, 0], [attack, 0.01, dur, dur, release]), doneAction: 2);
    sig    = Mix(osc) * 0.5 * env;
    sig    = RLPF.ar(sig, cutoff.clip(60, 18000), rq.clip(0.01, 1.0));
    Out.ar(out, Pan2.ar(sig, pan));
}).writeDefFile(~outDir);
"fd_dbass done".postln;
