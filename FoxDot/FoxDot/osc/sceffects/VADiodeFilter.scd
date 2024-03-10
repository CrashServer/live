SynthDef.new(\VADiodeFilter,
{|bus, vadiod, vadiodr, vadiodd, vadiod_, vadiod_d, vadiodr_, vadiodr_d, vadiodd_, vadiodd_d, sus|
var osc;
osc = In.ar(bus, 2);
vadiod = if(vadiod_<=0, vadiod, Line.kr(vadiod, vadiod_, sus*vadiod_d));
vadiodr = if(vadiodr_<=0, vadiodr, Line.kr(vadiodr, vadiodr_, sus*vadiodr_d));
vadiodd = if(vadiodd_<=0, vadiodd, Line.kr(vadiodd, vadiodd_, sus*vadiodd_d));
osc = VADiodeFilter.ar(osc, vadiod, vadiodr, vadiodd);
osc = osc*0.5;
ReplaceOut.ar(bus, osc)}).add;