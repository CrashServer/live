SynthDef.new(\crunch,
{|bus, crunch, crunch_, crunch_d, crunchlfo, crunchlfomul, crunchlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
crunch = if(crunch_<=0, crunch, Line.kr(crunch, crunch_, sus*crunch_d));
crunch = if(crunchlfo<=0, crunch, crunch * SinOsc.kr(crunchlfo, 0, crunchlfomul, crunchlfoadd));
osc = osc + (crunch * 0.6 * (HPF.ar(osc,800)*(1+(8*crunch))).distort);
osc = LPF.ar(osc, 20000 - (crunch*12000));
ReplaceOut.ar(bus, osc)}).add;