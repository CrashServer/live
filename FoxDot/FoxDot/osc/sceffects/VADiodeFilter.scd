SynthDef.new(\VADiodeFilter,
{|bus, vadiod, vadiodr, vadiodd, vadiod_, vadiodr_, vadiodd_, sus|
var osc;
osc = In.ar(bus, 2);
vadiod = vadiod+Line.kr(0, vadiod_, sus);
vadiodr = vadiodr+Line.kr(0, vadiodr_, sus);
vadiodd = vadiodd+Line.kr(0, vadiodd_, sus);
osc = VADiodeFilter.ar(osc, vadiod, vadiodr, vadiodd);
osc = osc*0.5;
ReplaceOut.ar(bus, osc)}).add;