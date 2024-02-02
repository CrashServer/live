SynthDef.new(\VADiodeFilter,
{|bus, vadiod, vadiodr, vadiodd|
var osc;
osc = In.ar(bus, 2);
osc = VADiodeFilter.ar(osc, vadiod, vadiodr, vadiodd);
osc = osc*0.5;
ReplaceOut.ar(bus, osc)}).add;