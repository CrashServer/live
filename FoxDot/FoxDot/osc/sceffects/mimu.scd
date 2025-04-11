SynthDef.new(\mimu,
{|bus, mu, mu_, mu_d, mulfo, sus|
var osc;
osc = In.ar(bus, 2);
mu = if(mu_<=0, mu, Line.kr(mu, mu_, sus*mu_d));
mu = if(mulfo<=0, mu, mu * SinOsc.kr(mulfo, 0, 1, 1));
osc = MiMu.ar(osc, mu);
ReplaceOut.ar(bus, osc)}).add;