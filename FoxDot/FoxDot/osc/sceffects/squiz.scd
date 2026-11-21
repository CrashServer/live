SynthDef.new(\squiz,
{|bus, squiz, squiz_, squiz_d, squizlfo, squizlfomul, squizlfoadd, squizlfophase, sus|
var osc;
osc = In.ar(bus, 2);
squiz = if(squiz_<=0, squiz, Line.kr(squiz, squiz_, sus*squiz_d));
squiz = if(squizlfo<=0, squiz, squiz * SinOsc.kr(squizlfo, squizlfophase, squizlfomul, squizlfoadd));
osc = Squiz.ar(osc, squiz);
ReplaceOut.ar(bus, osc)}).add;