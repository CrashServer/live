SynthDef.new(\foghorn,
{|bus=0, freq=0, amp=1, sus=1, pan=0, fmod=0, atk=0.05, rel=0.3,
  growl=0.3, subweight=0.7, dirt=0.2|
    var sub, mid, grit, osc, env, lfo;
    freq = In.kr(bus, 1);
    freq = [freq, freq+fmod] / 4; // two octaves down

    env = EnvGen.ar(Env.linen(atk, sus, rel, curve: -2), doneAction: 2);
    lfo = LFTri.kr(0.2).range(0.98, 1.02);

    // Pure sub sine
    sub = SinOsc.ar(freq * lfo) * subweight;

    // Growling mid with FM feedback
    mid = SinOscFB.ar(freq * 2, growl * LFNoise2.kr(3).range(0.1, 0.9));
    mid = BLowPass4.ar(mid, 400, 0.4) * (1 - subweight);

    // Gritty texture layer
    grit = LFSaw.ar(freq * 2) * LFPulse.ar(freq * 3, width: 0.3);
    grit = BHiPass.ar(grit, 200);
    grit = (grit * 4).fold(-0.5, 0.5) * dirt;

    osc = sub + mid + grit;
    osc = LeakDC.ar(osc);
    osc = Limiter.ar(osc * env * amp, 0.95);
    osc = Mix(osc) * 0.5;
    osc = Pan2.ar(osc, pan);
    ReplaceOut.ar(bus, osc)},
    metadata: (
        credit: "CrashServer",
        description: "Dark droning sub bass with harmonic growl",
        category: \bass,
        tags: [\sub, \dark, \drone]
    )
).add;
