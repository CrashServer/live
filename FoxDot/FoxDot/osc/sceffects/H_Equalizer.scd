SynthDef.new(\H_Equalizer,
{|bus, high, highfreq, high_, high_d, highfreq_, highfreq_d, sus|
var osc;
osc = In.ar(bus, 2);
high = if(high_<=0, high, Line.kr(high, high_, sus*high_d));
highfreq = if(highfreq_<=0, highfreq, Line.kr(highfreq, highfreq_, sus*highfreq_d));
osc = BHiShelf.ar(osc, freq: highfreq, db: abs(high).ampdb);
ReplaceOut.ar(bus, osc)}).add;