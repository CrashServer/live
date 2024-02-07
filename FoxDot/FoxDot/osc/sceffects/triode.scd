SynthDef.new(\triode,
{|bus, triode, triode_, sus|
var osc,sc;
osc = In.ar(bus, 2);
triode = triode+Line.kr(0, triode_, sus);
sc = triode * 10 + 1e-3;
osc = (osc * (osc > 0)) + (tanh(osc * sc) / sc * (osc < 0));
osc = LeakDC.ar(osc)*1.2;
ReplaceOut.ar(bus, osc)}).add;