SynthDef.new(\reese, {
    |bus=0, amp=1, sus=1, pan=0, freq=0, fmod=0, blur=1, beat_dur=1,
     atk=0.01, rel=0.1, detune=0.022, cutoff=1200, rq=0.65|

    var osc1, osc2, sub, osc, env, sig;

    sus = sus * blur;
    freq = In.kr(bus, 1);
    freq = freq + fmod;

    // Two detuned saws — acoustic beating between them is the Reese character
    osc1 = LFSaw.ar(freq * (1 - detune));
    osc2 = LFSaw.ar(freq * (1 + detune));

    // Sub sine for depth
    sub = SinOsc.ar(freq * 0.5, 0, 0.5);

    // Stereo spread: each channel gets a different blend of the two saws
    osc = [osc1 + (osc2 * 0.6) + sub, osc2 + (osc1 * 0.6) + sub];

    // LP filter
    osc = RLPF.ar(osc, cutoff.clip(80, 8000), rq.clip(0.05, 1.0));

    // Warm saturation
    osc = osc.tanh;

    env = EnvGen.ar(Env.linen(atk, sus, rel, 1, \lin), doneAction: 0);
    sig = osc * env * amp * 0.3;
    sig = Balance2.ar(sig[0], sig[1], pan);

    ReplaceOut.ar(bus, sig);
},
metadata: (
    credit: "svdk",
    description: "DnB Reese bass: two detuned saws with acoustic beating + sub sine + saturation",
    category: \bass,
    tags: [\reese, \bass, \dnb, \detuned, \analog]
)
).add;
