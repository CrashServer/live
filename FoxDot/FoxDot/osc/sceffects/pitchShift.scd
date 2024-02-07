SynthDef.new(\pitchShift,
{|bus, pshift, pshift_, sus|
var osc;
osc = In.kr(bus, 1);
pshift = pshift+Line.kr(0, pshift_, sus);
osc = osc * (1.059463**pshift);
ReplaceOut.kr(bus, osc)}).add;