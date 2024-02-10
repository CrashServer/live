SynthDef.new(\resonz,
{|bus, rfreq, resonz, rfreq_, rfreq_d, resonz_, resonz_d, sus|
var osc;
osc = In.ar(bus, 2);
rfreq = if(rfreq_<=0, rfreq, Line.kr(rfreq, rfreq_, sus*rfreq_d));
resonz = if(resonz_<=0, resonz, Line.kr(resonz, resonz_, sus*resonz_d));
osc = Resonz.ar(osc, freq: rfreq, bwr: resonz);
ReplaceOut.ar(bus, osc)}).add;