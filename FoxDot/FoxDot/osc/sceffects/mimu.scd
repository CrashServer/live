SynthDef.new(\mimu,
{|bus, mu, mu_, mu_d, mulfo, mulfomul, mulfoadd, mulfophase, sus|
var osc;
osc = In.ar(bus, 2);
mu = if(mu_<=0, mu, Line.kr(mu, mu_, sus*mu_d));
mu = if(mulfo<=0, mu, mu * SinOsc.kr(mulfo, mulfophase, mulfomul, mulfoadd));
osc = MiMu.ar(osc, mu);
ReplaceOut.ar(bus, osc)}).add;