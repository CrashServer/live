SynthDef.new(\test,
{|bus, test, testa, testb, testc, testd, test_, test_d, testlfo, testlfomul, testlfoadd, testa_, testa_d, testalfo, testalfomul, testalfoadd, testb_, testb_d, testblfo, testblfomul, testblfoadd, testc_, testc_d, testclfo, testclfomul, testclfoadd, testd_, testd_d, testdlfo, testdlfomul, testdlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
test = if(test_<=0, test, Line.kr(test, test_, sus*test_d));
test = if(testlfo<=0, test, test * SinOsc.kr(testlfo, 0, testlfomul, testlfoadd));
testa = if(testa_<=0, testa, Line.kr(testa, testa_, sus*testa_d));
testa = if(testalfo<=0, testa, testa * SinOsc.kr(testalfo, 0, testalfomul, testalfoadd));
testb = if(testb_<=0, testb, Line.kr(testb, testb_, sus*testb_d));
testb = if(testblfo<=0, testb, testb * SinOsc.kr(testblfo, 0, testblfomul, testblfoadd));
testc = if(testc_<=0, testc, Line.kr(testc, testc_, sus*testc_d));
testc = if(testclfo<=0, testc, testc * SinOsc.kr(testclfo, 0, testclfomul, testclfoadd));
testd = if(testd_<=0, testd, Line.kr(testd, testd_, sus*testd_d));
testd = if(testdlfo<=0, testd, testd * SinOsc.kr(testdlfo, 0, testdlfomul, testdlfoadd));
osc = osc*test;
ReplaceOut.ar(bus, osc)}).add;