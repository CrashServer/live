SynthDef.new(\mimu,
{|bus, mu, mu_, mu_d, sus|
var osc;
osc = In.ar(bus, 2);
mu = if(mu_<=0, mu, Line.kr(mu, mu_, sus*mu_d));
osc = MiMu.ar(osc, mu);
ReplaceOut.ar(bus, osc)}).add;