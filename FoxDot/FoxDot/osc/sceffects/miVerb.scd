SynthDef.new(\miVerb,
{|bus, mverb, mverbmix, mverbdamp, mverbdiff, mverbfreeze|
var osc;
osc = In.ar(bus, 2);
osc = MiVerb.ar(osc, time: mverb.clip(0.0,1.0), drywet: mverbmix, damp: mverbdamp, hp: 0.1, freeze: mverbfreeze, diff: mverbdiff, mul:1.5);
ReplaceOut.ar(bus, osc)}).add;