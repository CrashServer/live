SynthDef.new(\subkick,
{|bus=0, freq=50, amp=1, sus=0.4, pan=0, fmod=0, click=0.5, punch=0.7, subt=0.3|
    var sub, bodyLayer, clickLayer, osc, env, pitchEnv;
    freq = In.kr(bus, 1);
    freq = if(freq > 0, freq, 50); // default to 50Hz if no freq

    env = EnvGen.ar(Env.perc(0.001, sus, curve: -4), doneAction: 2);
    pitchEnv = EnvGen.ar(Env.perc(0.001, subt, curve: -12));

    // Sub sine with pitch envelope
    sub = SinOsc.ar(freq + (pitchEnv * freq * 3));

    // Punchy mid body
    bodyLayer = SinOsc.ar(freq * 2 + (pitchEnv * freq * 8));
    bodyLayer = bodyLayer * EnvGen.ar(Env.perc(0.001, 0.08, curve: -6)) * punch;

    // Click transient
    clickLayer = HPF.ar(WhiteNoise.ar, 3000);
    clickLayer = clickLayer * EnvGen.ar(Env.perc(0.0001, 0.003)) * click * 3;

    osc = sub + bodyLayer + clickLayer;
    osc = Limiter.ar(osc, 0.95);
    osc = HPF.ar(osc, 25);
    osc = LeakDC.ar(osc);
    osc = osc * env * amp * 0.7;
    osc = Pan2.ar(osc, pan);
    ReplaceOut.ar(bus, osc)},
    metadata: (
        credit: "CrashServer",
        description: "Deep punchy kick drum for DnB with adjustable click, punch and sub tail",
        category: \drums,
        tags: [\kick, \sub, \dnb]
    )
).add;
