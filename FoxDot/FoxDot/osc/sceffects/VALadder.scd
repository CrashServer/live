SynthDef.new(\VALadder,
{|bus, valad, valadr, valadd, valadt, valadc, valad_, valad_d, valadlfo, valadr_, valadr_d, valadrlfo, valadd_, valadd_d, valaddlfo, valadt_, valadt_d, valadtlfo, valadc_, valadc_d, valadclfo, sus|
var osc;
osc = In.ar(bus, 2);
valad = if(valad_<=0, valad, Line.kr(valad, valad_, sus*valad_d));
valad = if(valadlfo<=0, valad, valad * SinOsc.kr(valadlfo, 0, 1, 1));
valadr = if(valadr_<=0, valadr, Line.kr(valadr, valadr_, sus*valadr_d));
valadr = if(valadrlfo<=0, valadr, valadr * SinOsc.kr(valadrlfo, 0, 1, 1));
valadd = if(valadd_<=0, valadd, Line.kr(valadd, valadd_, sus*valadd_d));
valadd = if(valaddlfo<=0, valadd, valadd * SinOsc.kr(valaddlfo, 0, 1, 1));
valadt = if(valadt_<=0, valadt, Line.kr(valadt, valadt_, sus*valadt_d));
valadt = if(valadtlfo<=0, valadt, valadt * SinOsc.kr(valadtlfo, 0, 1, 1));
valadc = if(valadc_<=0, valadc, Line.kr(valadc, valadc_, sus*valadc_d));
valadc = if(valadclfo<=0, valadc, valadc * SinOsc.kr(valadclfo, 0, 1, 1));
osc = VALadder.ar(osc*0.4, valad, valadr, valadd,valadt);
osc = Compander.ar(osc, osc, valadc, 1, 0.1, 0.01, 0.1 );
ReplaceOut.ar(bus, osc)}).add;