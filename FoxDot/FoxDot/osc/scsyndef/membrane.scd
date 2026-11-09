SynthDef.new(\membrane,
{|bus=0, freq=0, amp=1, sus=1, pan=0, fmod=0,
  decay=0.6, strike=0.3, tension=0.4, hardness=0.5, shell=0.3|
    // Drum membrane on the modes of an ideal drumhead (Bessel zeros):
    // a tunable tom / floor tom / timpani / hand drum, not a swept sine.
    // strike: 0 = centre (round modes 1, 2.296, 3.6 only) .. 1 = edge (all modes)
    // tension: pitch drop at the attack; scales every mode so the drum stays in tune
    // hardness: stick brightness  shell: two fixed body resonances  decay: ring time
    // After soundDesign's kit archetype.
    var ratios, round, amps, decays, stick, exc, bend, son, shellRes, end;
    freq = In.kr(bus, 1);
    freq = (freq + fmod).clip(30, 2000);

    ratios = [1, 1.594, 2.136, 2.296, 2.653, 2.918, 3.156, 3.501, 3.6, 4.06, 4.231, 4.602];
    round  = [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0];           // (0,n) modes: centre hits
    amps   = ratios.collect { |r, i| (round[i].max(strike.clip(0, 1))) / (i + 1).sqrt };
    decays = ratios.collect { |r| decay.max(0.05) * r.reciprocal.pow(0.7) };

    // Stick: a click plus a short noise burst, low-passed by hardness
    stick = Decay2.ar(Impulse.ar(0), 0.0003, 0.002) +
            (LPF.ar(WhiteNoise.ar, hardness.linexp(0, 1, 800, 12000)) * Decay2.ar(Impulse.ar(0), 0.0005, 0.006) * 0.5);

    // Tension: every mode starts sharp and falls to pitch together
    bend = 1 + (tension.clip(0, 2) * EnvGen.kr(Env.perc(0, 0.08 + (decay * 0.1), 1, -6)));
    exc = DynKlank.ar(`[ratios, amps, decays], stick, freq * bend);

    shellRes = (Ringz.ar(stick, 190, 0.08) + Ringz.ar(stick, 470, 0.05)) * shell * 0.3;

    son = (exc + shellRes + (stick * hardness * 0.2));
    son = LeakDC.ar(son) * amp * 0.02;   // calibrated: peaks ~ -6..-11 dBFS (resonators accumulate the stick burst)
    son = Limiter.ar(son, 0.95);
    end = Line.kr(0, 0, decay.max(0.05) * 2.2 + 0.1, doneAction: 2);
    ReplaceOut.ar(bus, Pan2.ar(son, pan))},
    metadata: (
        credit: "CrashServer (after soundDesign kit archetype)",
        description: "Modal drum membrane (Bessel modes): strike position, tension drop, stick hardness, shell",
        category: \drums,
        tags: [\drum, \tom, \membrane, \physical, \modal]
    )
).add;
