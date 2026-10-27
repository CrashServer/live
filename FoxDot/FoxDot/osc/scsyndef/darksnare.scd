SynthDef.new(\darksnare,
{|bus=0, freq=180, amp=1, sus=0.15, pan=0, fmod=0, tone=0.4, snap=0.8, body=0.6|
    var tonal, noise, transient, osc, env, pitchEnv;
    freq = In.kr(bus, 1);
    freq = if(freq > 0, freq, 180); // default to 180Hz if no freq

    env = EnvGen.ar(Env.perc(0.001, sus, curve: -6), doneAction: 2);
    pitchEnv = EnvGen.ar(Env.perc(0.001, 0.03, curve: -12));

    // Tonal body with pitch drop
    tonal = SinOsc.ar(freq + (pitchEnv * 400)) * body;
    tonal = tonal + (SinOsc.ar(freq * 0.8) * 0.3);

    // Filtered noise for snare wire
    noise = WhiteNoise.ar * EnvGen.ar(Env.perc(0.002, sus * 0.6, curve: -4));
    noise = BPF.ar(noise, 3500, 0.8) * 2;
    noise = HPF.ar(noise, 1500) * tone;

    // Transient snap
    transient = WhiteNoise.ar * EnvGen.ar(Env.perc(0.0001, 0.008, curve: -10));
    transient = HPF.ar(transient, 4000) * snap * 2;

    osc = (tonal * 0.5) + noise + transient;
    osc = (osc * 1.5).tanh;
    osc = HPF.ar(osc, 80);
    osc = LeakDC.ar(osc);
    osc = osc * env * amp * 0.6;
    osc = Pan2.ar(osc, pan);
    ReplaceOut.ar(bus, osc)},
    metadata: (
        credit: "CrashServer",
        description: "Professional dark snare drum with adjustable tone, snap and body",
        category: \drums,
        tags: [\snare, \dark, \dnb]
    )
).add;
