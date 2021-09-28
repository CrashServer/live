SynthDef.new(\miVerb,
{|bus, mverb, mverbmix, mverbdamp, mverbdiff|
var osc;
osc = In.ar(bus, 2);
osc = MiVerb.ar(osc, mverb, mverbmix, mverbdamp, 0.05, 0, mverbdiff);
ReplaceOut.ar(bus, osc)}).add;