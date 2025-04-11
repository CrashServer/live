SynthDef.new(\VADiodeFilter,
{|bus, vadiod, vadiodr, vadiodd, vadiodc, vadiod_, vadiod_d, vadiodlfo, vadiodr_, vadiodr_d, vadiodrlfo, vadiodd_, vadiodd_d, vadioddlfo, vadiodc_, vadiodc_d, vadiodclfo, sus|
var osc;
osc = In.ar(bus, 2);
vadiod = if(vadiod_<=0, vadiod, Line.kr(vadiod, vadiod_, sus*vadiod_d));
vadiod = if(vadiodlfo<=0, vadiod, vadiod * SinOsc.kr(vadiodlfo, 0, 1, 1));
vadiodr = if(vadiodr_<=0, vadiodr, Line.kr(vadiodr, vadiodr_, sus*vadiodr_d));
vadiodr = if(vadiodrlfo<=0, vadiodr, vadiodr * SinOsc.kr(vadiodrlfo, 0, 1, 1));
vadiodd = if(vadiodd_<=0, vadiodd, Line.kr(vadiodd, vadiodd_, sus*vadiodd_d));
vadiodd = if(vadioddlfo<=0, vadiodd, vadiodd * SinOsc.kr(vadioddlfo, 0, 1, 1));
vadiodc = if(vadiodc_<=0, vadiodc, Line.kr(vadiodc, vadiodc_, sus*vadiodc_d));
vadiodc = if(vadiodclfo<=0, vadiodc, vadiodc * SinOsc.kr(vadiodclfo, 0, 1, 1));
osc = VADiodeFilter.ar(osc*0.5, vadiod, vadiodr, vadiodd);
osc = Compander.ar(osc, osc, vadiodc, 1, 0.1, 0.01, 0.1 );
ReplaceOut.ar(bus, osc)}).add;