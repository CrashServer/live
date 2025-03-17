SynthDef.new(\VADiodeFilter,
{|bus, vadiod, vadiodr, vadiodd, vadiodc, vadiod_, vadiod_d, vadiodr_, vadiodr_d, vadiodd_, vadiodd_d, vadiodc_, vadiodc_d, sus|
var osc;
osc = In.ar(bus, 2);
vadiod = if(vadiod_<=0, vadiod, Line.kr(vadiod, vadiod_, sus*vadiod_d));
vadiodr = if(vadiodr_<=0, vadiodr, Line.kr(vadiodr, vadiodr_, sus*vadiodr_d));
vadiodd = if(vadiodd_<=0, vadiodd, Line.kr(vadiodd, vadiodd_, sus*vadiodd_d));
vadiodc = if(vadiodc_<=0, vadiodc, Line.kr(vadiodc, vadiodc_, sus*vadiodc_d));
osc = VADiodeFilter.ar(osc*0.5, vadiod, vadiodr, vadiodd);
osc = Compander.ar(osc, osc, vadiodc, 1, 0.1, 0.01, 0.1 );
ReplaceOut.ar(bus, osc)}).add;