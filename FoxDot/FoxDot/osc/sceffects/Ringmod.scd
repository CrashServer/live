SynthDef.new(\Ringmod,
{|bus, ringzfreq, ringz, ringzfreq_, ringzfreq_d, ringzfreqlfo, ringz_, ringz_d, ringzlfo, sus|
var osc;
osc = In.ar(bus, 2);
ringzfreq = if(ringzfreq_<=0, ringzfreq, Line.kr(ringzfreq, ringzfreq_, sus*ringzfreq_d));
ringzfreq = if(ringzfreqlfo<=0, ringzfreq, ringzfreq * SinOsc.kr(ringzfreqlfo, 0, 1, 1));
ringz = if(ringz_<=0, ringz, Line.kr(ringz, ringz_, sus*ringz_d));
ringz = if(ringzlfo<=0, ringz, ringz * SinOsc.kr(ringzlfo, 0, 1, 1));
osc = Ringz.ar(osc, freq: ringzfreq, decaytime: ringz, mul: 0.05);
ReplaceOut.ar(bus, osc)}).add;