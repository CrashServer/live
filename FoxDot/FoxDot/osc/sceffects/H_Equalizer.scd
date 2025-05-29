SynthDef.new(\H_Equalizer,
{|bus, high, highfreq, high_, high_d, highlfo, highlfomul, highlfoadd, highfreq_, highfreq_d, highfreqlfo, highfreqlfomul, highfreqlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
high = if(high_<=0, high, Line.kr(high, high_, sus*high_d));
high = if(highlfo<=0, high, high * SinOsc.kr(highlfo, 0, highlfomul, highlfoadd));
highfreq = if(highfreq_<=0, highfreq, Line.kr(highfreq, highfreq_, sus*highfreq_d));
highfreq = if(highfreqlfo<=0, highfreq, highfreq * SinOsc.kr(highfreqlfo, 0, highfreqlfomul, highfreqlfoadd));
osc = BHiShelf.ar(osc, freq: highfreq, db: abs(high).ampdb);
ReplaceOut.ar(bus, osc)}).add;