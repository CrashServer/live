SynthDef.new(\triode,
{|bus, triode, triode_, triode_d, triodelfo, triodelfomul, triodelfoadd, sus|
var osc,sc;
osc = In.ar(bus, 2);
triode = if(triode_<=0, triode, Line.kr(triode, triode_, sus*triode_d));
triode = if(triodelfo<=0, triode, triode * SinOsc.kr(triodelfo, 0, triodelfomul, triodelfoadd));
sc = triode * 10 + 1e-3;
osc = (osc * (osc > 0)) + (tanh(osc * sc) / sc * (osc < 0));
osc = LeakDC.ar(osc)*1.2;
ReplaceOut.ar(bus, osc)}).add;