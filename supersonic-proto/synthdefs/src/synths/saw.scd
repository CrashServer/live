// saw — detuned sawtooth, adapted from FoxDot saw (CrashServer)
// Params: out, note, amp, sus, pan, attack, release, cutoff, rq, rate
// rate: phase offset / detune factor (0=thin, 1=wide stereo)

SynthDef(\fd_saw, {|out=0, note=60, amp=0.7, sus=1, pan=0, attack=0.01, release=0.1,
                     cutoff=8000, rq=0.8, rate=0.5|
    var freq, osc, dur, env, sig;
    freq = note.midicps;
    osc  = LFSaw.ar([freq, freq * (1 + rate * 0.002)], rate);
    osc  = RLPF.ar(osc, cutoff.clip(80, 20000), rq.clip(0.01, 1.0));
    dur  = (sus - attack - release).max(0.001);
    env  = EnvGen.ar(Env.linen(attack, dur, release, 1, \lin), doneAction: 2);
    sig  = Mix(osc) * 0.5 * env * amp;
    Out.ar(out, Pan2.ar(sig, pan));
}).writeDefFile(~outDir);
"fd_saw done".postln;
