// sine — sine with feedback, adapted from FoxDot sine (CrashServer)
// Params: out, note, amp, sus, pan, attack, release, cutoff, rq, rate
// rate: feedback amount (0=clean sine, 0.1=slight warmth, 1+=harsh)

SynthDef(\fd_sine, {|out=0, note=60, amp=0.7, sus=1, pan=0, attack=0.001, release=0.05,
                       cutoff=2800, rq=0.8, rate=0.1|
    var freq, osc, env, sig;
    freq = note.midicps;
    osc  = SinOscFB.ar([freq, freq * 1.001], rate.clip(0, 1.9));
    osc  = RLPF.ar(osc, cutoff.clip(40, 20000), rq.clip(0.01, 1.0));
    osc  = HPF.ar(osc, 40);
    env  = EnvGen.ar(Env.linen(attack, (sus - attack - release).max(0.001), release, amp, \sin), doneAction: 2);
    sig  = Mix(osc) * 0.2 * env;
    Out.ar(out, Pan2.ar(sig, pan));
}).writeDefFile(~outDir);
"fd_sine done".postln;
