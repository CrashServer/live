SynthDef.new(\resonz,
{|bus, rfreq, resonz, rfreq_, rfreq_d, rfreqlfo, resonz_, resonz_d, resonzlfo, sus|
var osc;
osc = In.ar(bus, 2);
rfreq = if(rfreq_<=0, rfreq, Line.kr(rfreq, rfreq_, sus*rfreq_d));
rfreq = if(rfreqlfo<=0, rfreq, rfreq * SinOsc.kr(rfreqlfo, 0, 1, 1));
resonz = if(resonz_<=0, resonz, Line.kr(resonz, resonz_, sus*resonz_d));
resonz = if(resonzlfo<=0, resonz, resonz * SinOsc.kr(resonzlfo, 0, 1, 1));
osc = Resonz.ar(osc, freq: rfreq, bwr: resonz);
ReplaceOut.ar(bus, osc)}).add;