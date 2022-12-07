SynthDef.new(\MiRings,
{|bus, mring, rstruct, rbright, rpos, rmodel, rpoly, regg|
var osc;
osc = In.ar(bus, 2);
osc = MiRings.ar(osc,osc,osc, rstruct, rbright, mring, rpos, rmodel, rpoly, regg);
ReplaceOut.ar(bus, osc)}).add;