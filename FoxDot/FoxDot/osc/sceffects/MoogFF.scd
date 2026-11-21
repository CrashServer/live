SynthDef.new(\MoogFF,
{|bus, mpf, mpr, mpf_, mpf_d, mpflfo, mpflfomul, mpflfoadd, mpflfophase, mpr_, mpr_d, mprlfo, mprlfomul, mprlfoadd, mprlfophase, sus|
var osc;
osc = In.ar(bus, 2);
mpf = if(mpf_<=0, mpf, Line.kr(mpf, mpf_, sus*mpf_d));
mpf = if(mpflfo<=0, mpf, mpf * SinOsc.kr(mpflfo, mpflfophase, mpflfomul, mpflfoadd));
mpr = if(mpr_<=0, mpr, Line.kr(mpr, mpr_, sus*mpr_d));
mpr = if(mprlfo<=0, mpr, mpr * SinOsc.kr(mprlfo, mprlfophase, mprlfomul, mprlfoadd));
osc = MoogFF.ar(osc, mpf, mpr,0,1);
ReplaceOut.ar(bus, osc)}).add;