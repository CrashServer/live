SynthDef.new(\MoogFF,
{|bus, mpf, mpr, mpf_, mpr_, sus|
var osc;
osc = In.ar(bus, 2);
mpf = mpf+Line.kr(0, mpf_, sus);
mpr = mpr+Line.kr(0, mpr_, sus);
osc = MoogFF.ar(osc, mpf, mpr,0,1);
ReplaceOut.ar(bus, osc)}).add;