SynthDef.new(\VALadder,
{|bus, valad, valadr, valadd, valadt, valadc, valad_, valad_d, valadr_, valadr_d, valadd_, valadd_d, valadt_, valadt_d, valadc_, valadc_d, sus|
var osc;
osc = In.ar(bus, 2);
valad = if(valad_<=0, valad, Line.kr(valad, valad_, sus*valad_d));
valadr = if(valadr_<=0, valadr, Line.kr(valadr, valadr_, sus*valadr_d));
valadd = if(valadd_<=0, valadd, Line.kr(valadd, valadd_, sus*valadd_d));
valadt = if(valadt_<=0, valadt, Line.kr(valadt, valadt_, sus*valadt_d));
valadc = if(valadc_<=0, valadc, Line.kr(valadc, valadc_, sus*valadc_d));
osc = VALadder.ar(osc*0.4, valad, valadr, valadd,valadt);
osc = Compander.ar(osc, osc, valadc, 1, 0.1, 0.01, 0.1 );
ReplaceOut.ar(bus, osc)}).add;