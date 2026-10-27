// rsin — resonant sine with feedback, adapted from FoxDot rsin (CrashServer)
// Params: out, note, amp, sus, pan, attack, release, cutoff, rq, feedback
// feedback: SinOscFB self-feedback (0=sine, 0.5=harmonics, 1.5=dirty)
// cutoff/rq: resonant filter (low rq = high resonance)

SynthDef(\fd_rsin, {|out=0, note=60, amp=0.7, sus=1, pan=0, attack=0.01, release=0.2,
                      cutoff=2000, rq=0.1, feedback=0|
    var freq, osc, dur, env, sig;
    freq = note.midicps;
    osc  = SinOscFB.ar([freq, freq * 1.002], feedback.clip(0, 1.5));
    osc  = RLPF.ar(osc, cutoff.clip(40, 20000), rq.clip(0.01, 1.0));
    dur  = (sus - attack - release).max(0.001);
    env  = EnvGen.ar(Env.linen(attack, dur, release, 1, \sin), doneAction: 2);
    sig  = Mix(osc) * 0.5 * env * amp;
    sig  = HPF.ar(sig, 40);
    Out.ar(out, Pan2.ar(sig, pan));
}).writeDefFile(~outDir);
"fd_rsin done".postln;
