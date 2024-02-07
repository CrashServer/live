SynthDef.new(\mimu,
{|bus, mu, mu_, sus|
var osc;
osc = In.ar(bus, 2);
mu = mu+Line.kr(0, mu_, sus);
osc = MiMu.ar(osc, mu);
ReplaceOut.ar(bus, osc)}).add;