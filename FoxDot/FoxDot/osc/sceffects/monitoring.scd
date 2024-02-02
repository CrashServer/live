SynthDef.new(\monitoring,
{|bus, mon|
var osc;
osc = In.ar(bus, 2);
Out.ar([mon, mon+1], osc);
osc = osc*0;
ReplaceOut.ar(bus, osc)}).add;