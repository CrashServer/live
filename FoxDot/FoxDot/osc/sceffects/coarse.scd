SynthDef.new(\coarse,
{|bus, coarse, sus, coarse_|
var osc;
osc = In.kr(bus, 1);
coarse = coarse+Line.kr(0, coarse_, sus);
osc = osc * LFPulse.ar(coarse / sus);
ReplaceOut.kr(bus, osc)}).add;