SynthDef(\tb304, {
	|bus=0, amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, atk=0.005, decay=0.2, rel=0.3, peak=1, level=0.8, gate=1, cutoff=100, rq=0.7, top=1500, fAtk=0.001, fDec=0.15, fSus=0.0, fRel=0.2, wave=0|

    var sig, ampEnv, filtEnv, effectiveCutoff;
	freq = In.kr(bus, 1);
	freq = [freq, freq+fmod];

	sig = SelectX.ar(wave, [Saw.ar(freq), Pulse.ar(freq/2, 0.5)]);

    filtEnv = EnvGen.kr(
        Env.adsr(fAtk, fDec, fSus, fRel, curve: -2.0),
        gate
    );
    effectiveCutoff = cutoff + (filtEnv * top);
    effectiveCutoff = effectiveCutoff.clip(20, 15000);

    //sig = RLPF.ar(sig, effectiveCutoff, res);
	sig = MoogFF.ar(sig, effectiveCutoff, 4- (rq * 4), 0,1.5);
	//sig = VAKorg35.ar(sig*0.1, effectiveCutoff, 1-res, 5.5,0);
	//sig = sig*0.5;

    ampEnv = EnvGen.kr(Env([0, peak, level, level, 0], [atk, decay, max((atk + decay + rel), sus - (atk + decay + rel)), rel], curve:\sin), doneAction: 0);

    sig = sig * ampEnv * amp;
    ReplaceOut.ar(bus, Pan2.ar(sig, pan));
}).add;

