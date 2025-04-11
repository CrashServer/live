SynthDef.new(\coarse,
{|bus, coarse, sus, coarse_, coarse_d, coarselfo|
var osc;
osc = In.kr(bus, 1);
coarse = if(coarse_<=0, coarse, Line.kr(coarse, coarse_, sus*coarse_d));
coarse = if(coarselfo<=0, coarse, coarse * SinOsc.kr(coarselfo, 0, 1, 1));
osc = osc * LFPulse.ar(coarse / sus);
ReplaceOut.kr(bus, osc)}).add;