SynthDef.new(\miVerb,
{|bus, mverb, mverbmix, mverbdamp, mverbdiff, mverbfreeze, mverb_, mverbmix_, mverbdamp_, mverbdiff_, mverbfreeze_, sus|
var osc;
osc = In.ar(bus, 2);
mverb = mverb+Line.kr(0, mverb_, sus);
mverbmix = mverbmix+Line.kr(0, mverbmix_, sus);
mverbdamp = mverbdamp+Line.kr(0, mverbdamp_, sus);
mverbdiff = mverbdiff+Line.kr(0, mverbdiff_, sus);
mverbfreeze = mverbfreeze+Line.kr(0, mverbfreeze_, sus);
osc = MiVerb.ar(osc, time: mverb.clip(0.0,1.0), drywet: mverbmix, damp: mverbdamp, hp: 0.1, freeze: mverbfreeze, diff: mverbdiff, mul:1.5);
ReplaceOut.ar(bus, osc)}).add;