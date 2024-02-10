SynthDef.new(\octer,
{|bus, octer, octersub, octersubsub, octer_, octer_d, octersub_, octersub_d, octersubsub_, octersubsub_d, sus|
var osc,oct1,oct2,oct3,sub;
osc = In.ar(bus, 2);
octer = if(octer_<=0, octer, Line.kr(octer, octer_, sus*octer_d));
octersub = if(octersub_<=0, octersub, Line.kr(octersub, octersub_, sus*octersub_d));
octersubsub = if(octersubsub_<=0, octersubsub, Line.kr(octersubsub, octersubsub_, sus*octersubsub_d));
oct1 = 2.0 * LeakDC.ar(abs(osc));
sub = LPF.ar(osc, 440);
oct2 = ToggleFF.ar(sub);
oct3 = ToggleFF.ar(oct2);
osc = SelectX.ar(octer, [osc, octer*oct1, DC.ar(0)]);
osc = osc + (octersub * oct2 * sub) + (octersubsub * oct3 * sub);
ReplaceOut.ar(bus, osc)}).add;