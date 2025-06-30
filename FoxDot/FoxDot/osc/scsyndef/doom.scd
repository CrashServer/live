SynthDef.new(\doomSynth,
    {|bus=0, freq=440, amp=0.5, pan=0, atk=0.001, decay=0.01, sus=1,rel=0.01, pw=0.5, cutoff=3000, rq=0.5, rate=1, wnoise=0.1|
    var sig, osc1, osc2, noise, env, lfo;
		freq = In.kr(bus, 1);

	freq = freq / 4;
		freq = freq*LFNoise1.kr(1!8).bipolar(1/8).midiratio;
		osc1 = LFSaw.ar(freq, 0.75);
    osc2 = Pulse.ar(freq * 1.01, pw.clip(0.01, 0.99)); // Pulse width control
    sig= osc1 + osc2;
		sig = sig + WhiteNoise.ar(wnoise.clip(0,1));

    	sig = (sig*20).clip(-1, 1); // Hard clip

    // Modulation: LFO for filter cutoff
    lfo = SinOsc.kr(4).range(0, 1000);
    cutoff = (cutoff + lfo).clip(20, 20000); // Modulate cutoff, keep in range

    // Filter: Low Pass Filter
    sig = RLPF.ar(sig, cutoff, rq.clip(0.01, 1)); // Resonant LPF

    // Distortion 2: Tanh Saturation (post-filter)
    // distAmt controls the gain before Tanh
		sig = (sig * (200)).tanh;

    // Envelope: ADSR
	env = EnvGen.ar(Env([0, 1, 1, 1, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);
    sig = sig * env *0.25;

    // Panning & Output
    sig = Pan2.ar(sig, pan);
    ReplaceOut.ar(bus, sig);
}).add;