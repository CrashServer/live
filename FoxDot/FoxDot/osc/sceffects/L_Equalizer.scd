SynthDef.new(\L_Equalizer,
{|bus, low, lowfreq, low_, low_d, lowlfo, lowlfomul, lowlfoadd, lowlfophase, lowfreq_, lowfreq_d, lowfreqlfo, lowfreqlfomul, lowfreqlfoadd, lowfreqlfophase, sus|
var osc;
osc = In.ar(bus, 2);
low = if(low_<=0, low, Line.kr(low, low_, sus*low_d));
low = if(lowlfo<=0, low, low * SinOsc.kr(lowlfo, lowlfophase, lowlfomul, lowlfoadd));
lowfreq = if(lowfreq_<=0, lowfreq, Line.kr(lowfreq, lowfreq_, sus*lowfreq_d));
lowfreq = if(lowfreqlfo<=0, lowfreq, lowfreq * SinOsc.kr(lowfreqlfo, lowfreqlfophase, lowfreqlfomul, lowfreqlfoadd));
osc = BLowShelf.ar(osc, freq: lowfreq, db: abs(low).ampdb);
ReplaceOut.ar(bus, osc)}).add;