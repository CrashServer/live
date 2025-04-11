SynthDef.new(\VALadder,
{|bus, valad, valadr, valadd, valadt, valadc, valad_, valad_d, valadlfo, valadlfomul, valadlfoadd, valadr_, valadr_d, valadrlfo, valadrlfomul, valadrlfoadd, valadd_, valadd_d, valaddlfo, valaddlfomul, valaddlfoadd, valadt_, valadt_d, valadtlfo, valadtlfomul, valadtlfoadd, valadc_, valadc_d, valadclfo, valadclfomul, valadclfoadd, sus|
var osc;
osc = In.ar(bus, 2);
valad = if(valad_<=0, valad, Line.kr(valad, valad_, sus*valad_d));
valad = if(valadlfo<=0, valad, valad * SinOsc.kr(valadlfo, 0, valadlfomul, valadlfoadd));
valadr = if(valadr_<=0, valadr, Line.kr(valadr, valadr_, sus*valadr_d));
valadr = if(valadrlfo<=0, valadr, valadr * SinOsc.kr(valadrlfo, 0, valadrlfomul, valadrlfoadd));
valadd = if(valadd_<=0, valadd, Line.kr(valadd, valadd_, sus*valadd_d));
valadd = if(valaddlfo<=0, valadd, valadd * SinOsc.kr(valaddlfo, 0, valaddlfomul, valaddlfoadd));
valadt = if(valadt_<=0, valadt, Line.kr(valadt, valadt_, sus*valadt_d));
valadt = if(valadtlfo<=0, valadt, valadt * SinOsc.kr(valadtlfo, 0, valadtlfomul, valadtlfoadd));
valadc = if(valadc_<=0, valadc, Line.kr(valadc, valadc_, sus*valadc_d));
valadc = if(valadclfo<=0, valadc, valadc * SinOsc.kr(valadclfo, 0, valadclfomul, valadclfoadd));
osc = VALadder.ar(osc*0.4, valad, valadr, valadd,valadt);
osc = Compander.ar(osc, osc, valadc, 1, 0.1, 0.01, 0.1 );
ReplaceOut.ar(bus, osc)}).add;