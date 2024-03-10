SynthDef.new(\test,
{|bus, test, testa, testb, testc, testd, test_, test_d, testa_, testa_d, testb_, testb_d, testc_, testc_d, testd_, testd_d, sus|
var osc;
osc = In.ar(bus, 2);
test = if(test_<=0, test, Line.kr(test, test_, sus*test_d));
testa = if(testa_<=0, testa, Line.kr(testa, testa_, sus*testa_d));
testb = if(testb_<=0, testb, Line.kr(testb, testb_, sus*testb_d));
testc = if(testc_<=0, testc, Line.kr(testc, testc_, sus*testc_d));
testd = if(testd_<=0, testd, Line.kr(testd, testd_, sus*testd_d));
osc = osc*test;
ReplaceOut.ar(bus, osc)}).add;