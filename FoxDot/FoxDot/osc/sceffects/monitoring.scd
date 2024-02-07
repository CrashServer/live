SynthDef.new(\monitoring,
{|bus, mon, mon_, sus|
var osc;
osc = In.ar(bus, 2);
mon = mon+Line.kr(0, mon_, sus);
Out.ar([mon, mon+1], osc);
osc = osc*0;
ReplaceOut.ar(bus, osc)}).add;