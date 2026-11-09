SynthDef.new(\fracture,
{|bus=0, freq=0, amp=1, sus=1, pan=0, fmod=0, atk=0.01, rel=0.2,
  density=12, branch=0.75, omori=0.12, stretch=1.6, shard=1.2, spread=0.8|
    // Fracture, sparks, breaking ice: a self-exciting (Hawkes) crackle.
    // Each crack raises the crack rate by branch/omori, decaying over omori
    // seconds, so a crack tends to set off more cracks. branch = average
    // offspring per crack: 0 = even Poisson rain (Dust), 0.9 = bursty
    // fracture, >= 1 runs away into a roar (capped at 0.95).
    // After soundDesign's crackle archetype.
    var trig, excite, rate, size, f0, ring, click, osc, env, modes, sr;
    freq = In.kr(bus, 1);
    freq = [freq, freq + fmod];
    sr = SampleRate.ir;
    branch = branch.clip(0, 0.95);
    omori = omori.max(0.005);

    // Hawkes intensity: base density + leaky sum of past cracks (time constant omori)
    excite = LocalIn.ar(1);
    rate = (density + excite).clip(0, 3000);
    trig = Dust.ar(rate);
    // (trig > 0): Dust's impulses have random height, mean 0.5, which halved
    // the branching ratio. Each crack must add exactly branch/omori.
    LocalOut.ar(Integrator.ar((trig > 0) * (branch / omori), exp(-1 / (omori * sr))));

    // Fragment size: power law (many small, few large). Small = higher and shorter.
    size = TRand.ar(0.0001, 1, trig).pow(shard.neg.reciprocal).clip(1, 12);
    f0 = (freq * 4 / size.sqrt).clip(80, 12000);

    // Plate-like modes ((2m+1)/3)^stretch, higher modes decay faster
    modes = (1..4).collect { |m| ((2 * m + 1) / 3).pow(stretch) };
    ring = modes.collect { |r, m|
        Ringz.ar(trig * size.sqrt * (0.5 ** m), (f0 * r).clip(40, 18000), (0.03 * size / (m + 1)).clip(0.004, 0.4))
    }.sum;

    // Snap of the break itself
    click = HPF.ar(WhiteNoise.ar, 2500) * Decay2.ar(trig, 0.0005, 0.004) * 0.6;

    osc = (ring * 0.08 + click);
    osc = LeakDC.ar(osc);
    env = EnvGen.ar(Env.linen(atk, sus, rel, curve: -2), doneAction: 2);
    osc = Mix(osc) * env * amp * 0.5;
    osc = Limiter.ar(osc, 0.9);
    osc = Pan2.ar(osc, (pan + TRand.ar(spread.neg, spread, trig) * 0.5).clip(-1, 1));
    ReplaceOut.ar(bus, osc)},
    metadata: (
        credit: "CrashServer (after soundDesign crackle archetype)",
        description: "Self-exciting crackle: fracture, sparks, breaking ice. branch = burstiness",
        category: \noise,
        tags: [\crackle, \fracture, \texture, \hawkes]
    )
).add;
