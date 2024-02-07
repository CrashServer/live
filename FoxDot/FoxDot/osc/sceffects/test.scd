SynthDef.new(\test,
{|bus, test, testa, testb, testc, testd, test_, testa_, testb_, testc_, testd_, sus|
var osc;
osc = In.ar(bus, 2);
test = test+Line.kr(0, test_, sus);
testa = testa+Line.kr(0, testa_, sus);
testb = testb+Line.kr(0, testb_, sus);
testc = testc+Line.kr(0, testc_, sus);
testd = testd+Line.kr(0, testd_, sus);
osc = osc*test;
ReplaceOut.ar(bus, osc)}).add;