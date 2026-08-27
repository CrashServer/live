SynthDef.new(\juno, {
    |bus=0, amp=1, sus=1, pan=0, freq=0, fmod=0, blur=1, beat_dur=1,
     atk=0.02, rel=0.15, junoshape=0.0, cutoff=3200, rq=0.7, junochorus=0.004|

    var sigL, sigR, sub, env, sig;

    sus = sus * blur;
    freq = In.kr(bus, 1);
    freq = freq + fmod;

    // DCO: saw <-> square crossfade (shape 0=saw, 1=square)
    // Two layers detuned slightly apart for stereo chorus
    sigL = XFade2.ar(
        DPW4Saw.ar(freq * (1 - junochorus)),
        Pulse.ar(freq * (1 - junochorus), 0.5),
        junoshape.linlin(0, 1, -1, 1)
    );
    sigR = XFade2.ar(
        DPW4Saw.ar(freq * (1 + junochorus)),
        Pulse.ar(freq * (1 + junochorus), 0.5),
        junoshape.linlin(0, 1, -1, 1)
    );

    // Sub sine one octave below, centred
    sub = SinOsc.ar(freq * 0.5, 0, 0.22);
    sigL = sigL + sub;
    sigR = sigR + sub;

    // LP filter for vintage VCF character
    sigL = RLPF.ar(sigL, cutoff.clip(80, 18000), rq.clip(0.05, 1.0));
    sigR = RLPF.ar(sigR, cutoff.clip(80, 18000), rq.clip(0.05, 1.0));

    env = EnvGen.ar(Env.linen(atk, sus, rel, 1, \sin), doneAction: 0);
    sig = [sigL, sigR] * env * amp * 0.28;
    sig = Balance2.ar(sig[0], sig[1], pan);

    ReplaceOut.ar(bus, sig);
},
metadata: (
    credit: "svdk",
    description: "Roland Juno-106 style: detuned DCO saw/square + sub + stereo chorus + LP filter",
    category: \pad,
    tags: [\juno, \pad, \analog, \chorus, \vintage]
)
).add;
