SynthDef.new(\miVerb,
{|bus, mverb, mverbmix, mverbdamp, mverbdiff, mverbfreeze|
var osc;
osc = In.ar(bus, 2);
osc = MiVerb.ar(osc, time: mverb.clip(1), drywet: mverbmix, damp: mverbdamp, freeze: mverbfreeze, diff: mverbdiff);
ReplaceOut.ar(bus, osc)}).add;