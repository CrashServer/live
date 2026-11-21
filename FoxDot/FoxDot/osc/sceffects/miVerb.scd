SynthDef.new(\miVerb,
{|bus, mverb, mverbmix, mverbdamp, mverbdiff, mverbfreeze, mverb_, mverb_d, mverblfo, mverblfomul, mverblfoadd, mverblfophase, mverbmix_, mverbmix_d, mverbmixlfo, mverbmixlfomul, mverbmixlfoadd, mverbmixlfophase, mverbdamp_, mverbdamp_d, mverbdamplfo, mverbdamplfomul, mverbdamplfoadd, mverbdamplfophase, mverbdiff_, mverbdiff_d, mverbdifflfo, mverbdifflfomul, mverbdifflfoadd, mverbdifflfophase, mverbfreeze_, mverbfreeze_d, mverbfreezelfo, mverbfreezelfomul, mverbfreezelfoadd, mverbfreezelfophase, sus|
var osc;
osc = In.ar(bus, 2);
mverb = if(mverb_<=0, mverb, Line.kr(mverb, mverb_, sus*mverb_d));
mverb = if(mverblfo<=0, mverb, mverb * SinOsc.kr(mverblfo, mverblfophase, mverblfomul, mverblfoadd));
mverbmix = if(mverbmix_<=0, mverbmix, Line.kr(mverbmix, mverbmix_, sus*mverbmix_d));
mverbmix = if(mverbmixlfo<=0, mverbmix, mverbmix * SinOsc.kr(mverbmixlfo, mverbmixlfophase, mverbmixlfomul, mverbmixlfoadd));
mverbdamp = if(mverbdamp_<=0, mverbdamp, Line.kr(mverbdamp, mverbdamp_, sus*mverbdamp_d));
mverbdamp = if(mverbdamplfo<=0, mverbdamp, mverbdamp * SinOsc.kr(mverbdamplfo, mverbdamplfophase, mverbdamplfomul, mverbdamplfoadd));
mverbdiff = if(mverbdiff_<=0, mverbdiff, Line.kr(mverbdiff, mverbdiff_, sus*mverbdiff_d));
mverbdiff = if(mverbdifflfo<=0, mverbdiff, mverbdiff * SinOsc.kr(mverbdifflfo, mverbdifflfophase, mverbdifflfomul, mverbdifflfoadd));
mverbfreeze = if(mverbfreeze_<=0, mverbfreeze, Line.kr(mverbfreeze, mverbfreeze_, sus*mverbfreeze_d));
mverbfreeze = if(mverbfreezelfo<=0, mverbfreeze, mverbfreeze * SinOsc.kr(mverbfreezelfo, mverbfreezelfophase, mverbfreezelfomul, mverbfreezelfoadd));
osc = MiVerb.ar(osc, time: mverb.clip(0.0,1.0), drywet: mverbmix, damp: mverbdamp, hp: 0.1, freeze: mverbfreeze, diff: mverbdiff, mul:1.5);
ReplaceOut.ar(bus, osc)}).add;