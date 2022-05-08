SynthDef.new(\test,
{|bus, test, testa, testb, testc, testd|
var osc;
osc = In.ar(bus, 2);
osc = osc*test;
ReplaceOut.ar(bus, osc)}).add;