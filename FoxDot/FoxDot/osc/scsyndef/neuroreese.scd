SynthDef.new(\neuroreese,
{|bus=0, freq=0, amp=1, sus=1, pan=0, fmod=0, atk=0.001, decay=0.1, rel=0.1,
  detune=0.008, morph=0.5, drive=2, cutoff=3000, rq=0.3, modrate=4, moddepth=800|
    var osc, env, filterEnv, mod, voices, processed, sub;
    freq = In.kr(bus, 1);
    freq = [freq, freq+fmod] / 2;

    env = EnvGen.ar(Env([0, 1, 0.7, 0.7, 0], [atk, decay, sus, rel], curve: -4), doneAction: 2);
    filterEnv = EnvGen.ar(Env.perc(0.001, sus * 0.5), levelScale: moddepth);
    mod = SinOsc.kr(modrate).range(-1, 1) * moddepth;

    // 5 detuned saw voices with slight phase randomization
    voices = Array.fill(5, {|i|
        var dt = detune * (i - 2) * freq;
        Saw.ar(freq + dt + (LFNoise2.kr(0.2).range(-0.5, 0.5)))
    });
    osc = Mix(voices) / 3;

    // Crossfade between clean and folded
    osc = SelectX.ar(morph, [osc, (osc * drive).fold(-0.8, 0.8)]);

    // Modulated bandpass for that "talking" quality
    osc = BPF.ar(osc, (cutoff + mod + filterEnv).clip(80, 12000), rq) * 3;

    // Sub layer
    sub = BLowPass4.ar(Mix(voices) / 3, 120, 0.5) * 0.4;
    osc = osc + sub;

    osc = (osc * drive * 0.5).tanh;
    osc = HPF.ar(osc, 28);
    osc = LeakDC.ar(osc);
    osc = Mix(osc * env * amp) * 0.4;
    osc = Pan2.ar(osc, pan);
    ReplaceOut.ar(bus, osc)},
    metadata: (
        credit: "CrashServer",
        description: "Modern neurofunk reese bass with detuned voices and modulated filter",
        category: \bass,
        tags: [\neuro, \reese, \dnb]
    )
).add;
