SynthDef.new(\L_Equalizer,
{|bus, low, lowfreq, low_, lowfreq_, sus|
var osc;
osc = In.ar(bus, 2);
low = low+Line.kr(0, low_, sus);
lowfreq = lowfreq+Line.kr(0, lowfreq_, sus);
osc = BLowShelf.ar(osc, freq: lowfreq, db: abs(low).ampdb);
ReplaceOut.ar(bus, osc)}).add;