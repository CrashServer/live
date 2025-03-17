SynthDef.new(\idist,
{|bus, idist, idist_, idist_d, sus|
var osc;
osc = In.ar(bus, 2);
idist = if(idist_<=0, idist, Line.kr(idist, idist_, sus*idist_d));
osc = LinXFade2.ar(InsideOut.ar(osc,0.4), osc, 1-idist);
osc = LeakDC.ar(osc);
ReplaceOut.ar(bus, osc)}).add;