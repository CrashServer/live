SynthDef.new(\MoogFF,
{|bus, mpf, mpr, mpf_, mpf_d, mpr_, mpr_d, sus|
var osc;
osc = In.ar(bus, 2);
mpf = if(mpf_<=0, mpf, Line.kr(mpf, mpf_, sus*mpf_d));
mpr = if(mpr_<=0, mpr, Line.kr(mpr, mpr_, sus*mpr_d));
osc = MoogFF.ar(osc, mpf, mpr,0,1);
ReplaceOut.ar(bus, osc)}).add;