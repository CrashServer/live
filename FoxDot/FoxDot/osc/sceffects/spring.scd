SynthDef.new(\spring,
{|bus, spring, sprdecay, sprdamp, sprtens, spring_, spring_d, springlfo, springlfomul, springlfoadd, sprdecay_, sprdecay_d, sprdecaylfo, sprdecaylfomul, sprdecaylfoadd, sprdamp_, sprdamp_d, sprdamplfo, sprdamplfomul, sprdamplfoadd, sprtens_, sprtens_d, sprtenslfo, sprtenslfomul, sprtenslfoadd, sus|
var osc,dry,wet,cutoff;
osc = In.ar(bus, 2);
spring = if(spring_<=0, spring, Line.kr(spring, spring_, sus*spring_d));
spring = if(springlfo<=0, spring, spring * SinOsc.kr(springlfo, 0, springlfomul, springlfoadd));
sprdecay = if(sprdecay_<=0, sprdecay, Line.kr(sprdecay, sprdecay_, sus*sprdecay_d));
sprdecay = if(sprdecaylfo<=0, sprdecay, sprdecay * SinOsc.kr(sprdecaylfo, 0, sprdecaylfomul, sprdecaylfoadd));
sprdamp = if(sprdamp_<=0, sprdamp, Line.kr(sprdamp, sprdamp_, sus*sprdamp_d));
sprdamp = if(sprdamplfo<=0, sprdamp, sprdamp * SinOsc.kr(sprdamplfo, 0, sprdamplfomul, sprdamplfoadd));
sprtens = if(sprtens_<=0, sprtens, Line.kr(sprtens, sprtens_, sus*sprtens_d));
sprtens = if(sprtenslfo<=0, sprtens, sprtens * SinOsc.kr(sprtenslfo, 0, sprtenslfomul, sprtenslfoadd));
dry = osc;
cutoff = 1000 + (sprtens * 6000);
wet = AllpassC.ar(osc, 0.01, 0.0031, sprdecay * 0.3);
wet = AllpassC.ar(wet, 0.01, 0.0053, sprdecay * 0.4);
wet = AllpassC.ar(wet, 0.01, 0.0072, sprdecay * 0.35);
wet = AllpassC.ar(wet, 0.01, 0.0097, sprdecay * 0.45);
wet = wet + CombC.ar(osc, 0.03, 0.0137, sprdecay * 0.6);
wet = wet + CombC.ar(osc, 0.03, 0.0193, sprdecay * 0.5);
wet = wet + CombC.ar(osc, 0.03, 0.0263, sprdecay * 0.7);
wet = LPF.ar(wet, cutoff);
wet = LPF.ar(wet, cutoff * 1.2);
wet = BHiShelf.ar(wet, 2000, 0.7, sprdamp * -8);
wet = LeakDC.ar(wet * 0.2);
osc = XFade2.ar(dry, wet, spring * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;