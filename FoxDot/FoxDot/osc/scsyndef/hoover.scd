SynthDef(\hoover,
{|bus=0, amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, atk=0.01, decay=0.2, rel=0.01, peak=1, level=0.8, gate=1, porta=1, portadur=0.125|
    var osc, env, midfreqs, vibamount;

    // Portamento:
	freq = In.kr(bus, 1);
	freq = Line.kr(start: (freq * porta).clip(-50,22000), end: freq, dur: sus*portadur);
	freq = [freq, freq+fmod];

	// vibrato doesn't fade in until note is held:
    vibamount = EnvGen.kr(Env([0,0,1],[0.0,0.4], loopNode:1), HPZ1.kr(freq).abs);
    // Vibrato (slightly complicated to allow it to fade in):
    freq = LinXFade2.kr(freq, freq * LFPar.kr(3).exprange(0.98, 1.02), vibamount * 2 - 1);

    // We want to chorus the frequencies to have a period of 0.258 seconds
    // ie freq difference is 0.258.reciprocal == 3.87
    midfreqs = freq + (3.87 * (-2 .. 2));

    // Add some drift to the frequencies so they don't sound so digitally locked in phase:
    midfreqs = midfreqs.collect{|f| f + (LFNoise1.kr(2) * 3) };

    // Now we generate the main sound via Saw oscs:
    osc = Saw.ar(midfreqs).sum
        // also add the subharmonic, the pitch-locked bass:
        + SinOsc.ar(freq * [0.25, 0.5, 0.75], 0, [1, 0.3, 0.2] * 2).sum;

    // As the pitch scoops away, we low-pass filter it to allow the sound to stop without simply gating it
	// osc = RLPF.ar(osc, freq * 1).lag(0.01);

    // Add a bit more mid-frequency emphasis to the sound
    osc = osc + BPF.ar(osc, 1000, mul: 0.5) + BPF.ar(osc, 3000, mul: 0.3);

    // This envelope mainly exists to allow the synth to free when needed:
    osc = osc * EnvGen.ar(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);

	ReplaceOut.ar(bus, Pan2.ar(osc * 0.15 * amp, pan));
}).add;

/// based on https://mcld.co.uk/blog/2009/reverse-engineering-the-rave-hoover.html