SynthDef.new(\drcomp,
{|bus, drcomp, drcomp_, drcomp_d, drcomplfo, drcomplfomul, drcomplfoadd, sus|
var osc,compOsc;
osc = In.ar(bus, 2);
drcomp = if(drcomp_<=0, drcomp, Line.kr(drcomp, drcomp_, sus*drcomp_d));
drcomp = if(drcomplfo<=0, drcomp, drcomp * SinOsc.kr(drcomplfo, 0, drcomplfomul, drcomplfoadd));
compOsc = Compander.ar(osc, osc, thresh: 0.1, slopeBelow:1, slopeAbove: 0.1, clampTime: 0.002, relaxTime: 0.05, mul:3);
compOsc = BLowShelf.ar(compOsc, 200, 1, 2, 1);
compOsc = BHiShelf.ar(compOsc, 6000, 1, 3);
osc = SelectX.ar(drcomp, [osc, compOsc*0.7]);
ReplaceOut.ar(bus, osc)}).add;