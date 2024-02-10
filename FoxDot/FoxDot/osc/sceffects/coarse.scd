SynthDef.new(\coarse,
{|bus, coarse, sus, coarse_, coarse_d|
var osc;
osc = In.kr(bus, 1);
coarse = if(coarse_<=0, coarse, Line.kr(coarse, coarse_, sus*coarse_d));
osc = osc * LFPulse.ar(coarse / sus);
ReplaceOut.kr(bus, osc)}).add;