SynthDef.new(\MoogFF,
{|bus, mpf, mpr, mpf_, mpf_d, mpflfo, mpflfomul, mpflfoadd, mpr_, mpr_d, mprlfo, mprlfomul, mprlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
mpf = if(mpf_<=0, mpf, Line.kr(mpf, mpf_, sus*mpf_d));
mpf = if(mpflfo<=0, mpf, mpf * SinOsc.kr(mpflfo, 0, mpflfomul, mpflfoadd));
mpr = if(mpr_<=0, mpr, Line.kr(mpr, mpr_, sus*mpr_d));
mpr = if(mprlfo<=0, mpr, mpr * SinOsc.kr(mprlfo, 0, mprlfomul, mprlfoadd));
osc = MoogFF.ar(osc, mpf, mpr,0,1);
ReplaceOut.ar(bus, osc)}).add;