SynthDef.new(\resonz,
{|bus, rfreq, resonz, rfreq_, rfreq_d, rfreqlfo, rfreqlfomul, rfreqlfoadd, resonz_, resonz_d, resonzlfo, resonzlfomul, resonzlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
rfreq = if(rfreq_<=0, rfreq, Line.kr(rfreq, rfreq_, sus*rfreq_d));
rfreq = if(rfreqlfo<=0, rfreq, rfreq * SinOsc.kr(rfreqlfo, 0, rfreqlfomul, rfreqlfoadd));
resonz = if(resonz_<=0, resonz, Line.kr(resonz, resonz_, sus*resonz_d));
resonz = if(resonzlfo<=0, resonz, resonz * SinOsc.kr(resonzlfo, 0, resonzlfomul, resonzlfoadd));
osc = Resonz.ar(osc, freq: rfreq, bwr: resonz);
ReplaceOut.ar(bus, osc)}).add;