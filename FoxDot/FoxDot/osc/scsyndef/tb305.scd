SynthDef.new(\tb305, {
	|bus=0, amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, atk=0.001, decay=0.02, rel=0.3, peak=1, level=0.8, gate=1, cutoff=600, rq=0.4, wave=0.5,beef=2|

    var sig, ampEnv, filtEnv, effectiveCutoff;
	freq = In.kr(bus, 1);
	freq = freq/2;
	sig = Open303.ar(1, 1, freq.cpsmidi,velocity:0.79, waveform: wave, cutoff: cutoff, resonance: (1-rq)*100, envMod: fmod*100, distortion:beef, postgain: -6, pregain:4, accent:80 );

    ampEnv = EnvGen.kr(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);

    sig = sig * ampEnv * amp;
    ReplaceOut.ar(bus, Pan2.ar(sig, pan));
}).add;