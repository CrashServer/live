SynthDef.new(\Ringmod,
{|bus, ringzfreq, ringz, ringzfreq_, ringz_, sus|
var osc;
osc = In.ar(bus, 2);
ringzfreq = ringzfreq+Line.kr(0, ringzfreq_, sus);
ringz = ringz+Line.kr(0, ringz_, sus);
osc = Ringz.ar(osc, freq: ringzfreq, decaytime: ringz, mul: 0.05);
ReplaceOut.ar(bus, osc)}).add;