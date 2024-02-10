SynthDef.new(\Ringmod,
{|bus, ringzfreq, ringz, ringzfreq_, ringzfreq_d, ringz_, ringz_d, sus|
var osc;
osc = In.ar(bus, 2);
ringzfreq = if(ringzfreq_<=0, ringzfreq, Line.kr(ringzfreq, ringzfreq_, sus*ringzfreq_d));
ringz = if(ringz_<=0, ringz, Line.kr(ringz, ringz_, sus*ringz_d));
osc = Ringz.ar(osc, freq: ringzfreq, decaytime: ringz, mul: 0.05);
ReplaceOut.ar(bus, osc)}).add;