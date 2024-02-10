SynthDef.new(\pitchShift,
{|bus, pshift, pshift_, pshift_d, sus|
var osc;
osc = In.kr(bus, 1);
pshift = if(pshift_<=0, pshift, Line.kr(pshift, pshift_, sus*pshift_d));
osc = osc * (1.059463**pshift);
ReplaceOut.kr(bus, osc)}).add;