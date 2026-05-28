// donk — Ringz resonator donk, adapted from FoxDot donk (CrashServer)
// Params: out, note, amp, sus, pan
// sus: ring decay time (longer = more tail)
// Uses DetectSilence to auto-free when Ringz decays to silence

SynthDef(\fd_donk, {|out=0, note=60, amp=0.9, sus=0.5, pan=0|
    var freq, osc;
    freq = note.midicps / 2;
    osc  = Ringz.ar(Impulse.ar(0), [freq, freq + 1.5], sus, amp * 0.5);
    osc  = Mix(osc) * 0.5;
    DetectSilence.ar(osc, doneAction: 2);
    Out.ar(out, Pan2.ar(osc, pan));
}).writeDefFile(~outDir);
"fd_donk done".postln;
