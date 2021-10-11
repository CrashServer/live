SynthDef.new(\mimu,
{|bus, mu|
var osc;
osc = In.ar(bus, 2);
osc = MiMu.ar(osc, mu);
ReplaceOut.ar(bus, osc)}).add;