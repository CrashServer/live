SynthDef.new(\resonz,
{|bus, rfreq, resonz, rfreq_, resonz_, sus|
var osc;
osc = In.ar(bus, 2);
rfreq = rfreq+Line.kr(0, rfreq_, sus);
resonz = resonz+Line.kr(0, resonz_, sus);
osc = Resonz.ar(osc, freq: rfreq, bwr: resonz);
ReplaceOut.ar(bus, osc)}).add;