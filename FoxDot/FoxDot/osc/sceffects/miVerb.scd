SynthDef.new(\miVerb,
{|bus, mverb, mverbmix, mverbdamp, mverbdiff, mverbfreeze, mverb_, mverb_d, mverbmix_, mverbmix_d, mverbdamp_, mverbdamp_d, mverbdiff_, mverbdiff_d, mverbfreeze_, mverbfreeze_d, sus|
var osc;
osc = In.ar(bus, 2);
mverb = if(mverb_<=0, mverb, Line.kr(mverb, mverb_, sus*mverb_d));
mverbmix = if(mverbmix_<=0, mverbmix, Line.kr(mverbmix, mverbmix_, sus*mverbmix_d));
mverbdamp = if(mverbdamp_<=0, mverbdamp, Line.kr(mverbdamp, mverbdamp_, sus*mverbdamp_d));
mverbdiff = if(mverbdiff_<=0, mverbdiff, Line.kr(mverbdiff, mverbdiff_, sus*mverbdiff_d));
mverbfreeze = if(mverbfreeze_<=0, mverbfreeze, Line.kr(mverbfreeze, mverbfreeze_, sus*mverbfreeze_d));
osc = MiVerb.ar(osc, time: mverb.clip(0.0,1.0), drywet: mverbmix, damp: mverbdamp, hp: 0.1, freeze: mverbfreeze, diff: mverbdiff, mul:1.5);
ReplaceOut.ar(bus, osc)}).add;