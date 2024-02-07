SynthDef.new(\H_Equalizer,
{|bus, high, highfreq, high_, highfreq_, sus|
var osc;
osc = In.ar(bus, 2);
high = high+Line.kr(0, high_, sus);
highfreq = highfreq+Line.kr(0, highfreq_, sus);
osc = BHiShelf.ar(osc, freq: highfreq, db: abs(high).ampdb);
ReplaceOut.ar(bus, osc)}).add;