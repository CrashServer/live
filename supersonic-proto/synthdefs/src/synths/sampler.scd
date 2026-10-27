// fd_sampler — mono buffer playback for play() patterns
// Params: out, buf, amp, pan, rate
// doneAction:2 on PlayBuf — synth frees when buffer finishes

SynthDef(\fd_sampler, {|out=0, buf=0, amp=0.8, pan=0, rate=1|
    var sig;
    sig = PlayBuf.ar(1, buf, rate * BufRateScale.kr(buf), doneAction: 2);
    sig = sig * amp;
    Out.ar(out, Pan2.ar(sig, pan));
}).writeDefFile(~outDir);
"fd_sampler done".postln;
