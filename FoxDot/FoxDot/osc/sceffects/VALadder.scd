SynthDef.new(\VALadder,
{|bus, valad, valadr, valadd, valadt, valad_, valad_d, valadr_, valadr_d, valadd_, valadd_d, valadt_, valadt_d, sus|
var osc;
osc = In.ar(bus, 2);
valad = if(valad_<=0, valad, Line.kr(valad, valad_, sus*valad_d));
valadr = if(valadr_<=0, valadr, Line.kr(valadr, valadr_, sus*valadr_d));
valadd = if(valadd_<=0, valadd, Line.kr(valadd, valadd_, sus*valadd_d));
valadt = if(valadt_<=0, valadt, Line.kr(valadt, valadt_, sus*valadt_d));
osc = VALadder.ar(osc*0.4, valad, valadr, valadd,valadt);
ReplaceOut.ar(bus, osc)}).add;