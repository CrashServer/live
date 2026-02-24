SynthDef.new(\glitchstab,
{|bus=0, freq=0, amp=1, sus=0.1, pan=0, fmod=0,
  glitchamt=0.5, bits=8, cutoff=4000, rq=0.7|
    var osc, env, glitch, trig, pitched, dry;
    freq = In.kr(bus, 1);
    freq = [freq, freq+fmod];

    env = EnvGen.ar(Env.perc(0.001, sus, curve: -8), doneAction: 2);
    trig = Impulse.ar(LFNoise0.kr(20).range(10, 80));

    // Sharp attack transient
    osc = Blip.ar(freq, LFNoise0.kr(10).range(3, 12)) * 0.5;
    osc = osc + (Pulse.ar(freq * 2, 0.1) * 0.3);

    dry = osc;

    // Glitch processing
    glitch = Latch.ar(osc, trig);
    glitch = glitch.round(2.pow(bits.neg));
    pitched = PitchShift.ar(osc, 0.02, TRand.kr(0.9, 1.1, trig));

    osc = SelectX.ar(glitchamt, [dry, (glitch * 0.5) + (pitched * 0.5)]);
    osc = RLPF.ar(osc, cutoff * env.pow(0.5) + 200, rq);
    osc = (osc * 2).tanh;

    osc = Mix(osc * env * amp) * 0.4;
    osc = Pan2.ar(osc, pan);
    ReplaceOut.ar(bus, osc)},
    metadata: (
        credit: "CrashServer",
        description: "Glitchy stab synth for dark DnB hits",
        category: \stab,
        tags: [\glitch, \dnb, \stab]
    )
).add;
