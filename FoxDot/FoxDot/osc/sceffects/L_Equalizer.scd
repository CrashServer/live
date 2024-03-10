SynthDef.new(\L_Equalizer,
{|bus, low, lowfreq, low_, low_d, lowfreq_, lowfreq_d, sus|
var osc;
osc = In.ar(bus, 2);
low = if(low_<=0, low, Line.kr(low, low_, sus*low_d));
lowfreq = if(lowfreq_<=0, lowfreq, Line.kr(lowfreq, lowfreq_, sus*lowfreq_d));
osc = BLowShelf.ar(osc, freq: lowfreq, db: abs(low).ampdb);
ReplaceOut.ar(bus, osc)}).add;