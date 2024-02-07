SynthDef.new(\squiz,
{|bus, squiz, squiz_, sus|
var osc;
osc = In.ar(bus, 2);
squiz = squiz+Line.kr(0, squiz_, sus);
osc = Squiz.ar(osc, squiz);
ReplaceOut.ar(bus, osc)}).add;