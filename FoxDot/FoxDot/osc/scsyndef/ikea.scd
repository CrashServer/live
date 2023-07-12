(
SynthDef.new(\ikea,
  {|amp=1, sus=1, pan=0, freq=0, vib=0, fmod=0, rate=0, bus=0,instr=0, hhat=0.1, sn=0.1, harm=0|
    var osc, env, osc1, osc2, osc3, osc4, osc5, osc6, triggers;
      var trigMod = LFNoise0.ar(8).round;
    freq = In.kr(bus, 1);
    freq = [freq, freq+fmod] * Line.ar(Rand(0.5,1.5),1,0.02);
    freq=(freq / 4);
    amp=(amp * 0.4);
    triggers =   {
      TDuty.ar
      (
        Dxrand(((1/8!8) ++ (1/4!8) ++ [Dseq([1/16, 1/16], Drand([1, 2], inf))]) * 1.25, inf), //see above logic
        0,
        Dwhite(0.5, 1, inf) //trigger values are between 0.5, 1
      )
    }!2;
    // triggers = TDuty.ar([0.1, 1, 2, 0.5])!2;
    //GLITCH MODULATOR
    osc1 = BPF.ar(
      PinkNoise.ar(Decay.ar(triggers, hhat * LFNoise1.ar(4).abs)), //decay time is modulated
      15000,
      0.9,
      25 * LFNoise1.ar(8).range(0, 1) //extreme amplification of glitches.
    ).fold(-1, 1);
    // osc1 = DelayC.ar(osc1, 0.1, 0.2);
    //THE TWO SINS
    osc2 =
    LPF.ar
    (
      SinOsc.ar(44.midicps, 0, 0.5) + SinOsc.ar(90.midicps, 0, 0.6),
      // 32.midicps * 2
      freq
    ) + HPF.ar(LPF.ar(WhiteNoise.ar(0.008), 12000), 2400);
    // WHITE NOISE
    osc3 =
    BPF.ar
    (
      WhiteNoise.ar(Decay2.ar(triggers * LFNoise1.ar(8, 0.5, 0.5), 0.02, 0.1) * 0.05),
      TRand.ar(12000, 15000, triggers),
      0.9
    );
    // BASS SOUND
      osc4 =
    SinOsc.ar(0, (Sweep.ar(triggers[0] * trigMod, 2pi * [52.8, 740]) + (pi/3)).wrap(-pi, pi), [2, 0.05]).mean.tanh *
    EnvGen.ar(Env([0, 0.5, 0.4, 0], [0, 0.2, 0.01], -5), (triggers[0] * trigMod).abs)!2;
    osc2 =
    Pan2.ar
    (
      osc2 * EnvGen.ar(Env([0, 1, 0.6, 0], [0.0001, 0.4, 0.01]), triggers * LFNoise0.ar(8)),
      TRand.ar(-1, 1, triggers)
    );

    // SNARES
    osc5 = MiPlaits.ar(47, 14, LFNoise2.kr(0.5).range(0,0.5), 0.173, 0.827, triggers[0], TRand.kr(trig: triggers[0]).squared, fm_mod: sn, timb_mod: 0.43, decay: 0.4) * sn;

    // MELODY
    osc6 = MiRings.ar(osc5, 0, Latch.kr(SinOsc.ar(freq), triggers[1]), LFNoise2.kr(0.4).range(0,1), 0.5, 0.7, 0.25, model: 1, poly: 4);
    osc6 = CrossoverDistortion.ar(osc5 + osc6) * harm;
    // osc = osc1 + osc2 + osc3 + osc4 ;
    osc = Limiter.ar(MidEQ.ar(osc1 + osc2 + osc3 + osc4 + osc5 + osc6, 14000, 0.7, 0.8));
    // osc = osc5;
    env=EnvGen.ar(Env([0,1,0.8,0.8,0], [0.02, 0.01, sus/2, sus/2]), doneAction: 2);
    osc=(osc * env);
    osc = Mix(osc) * 0.5;
    osc = Pan2.ar(osc, pan);
    ReplaceOut.ar(bus, osc)}).add;
)
