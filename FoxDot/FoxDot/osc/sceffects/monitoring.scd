SynthDef.new(\monitoring,
{|bus, mon, mon_, mon_d, sus|
var osc;
osc = In.ar(bus, 2);
mon = if(mon_<=0, mon, Line.kr(mon, mon_, sus*mon_d));
Out.ar([mon, mon+1], osc);
osc = osc*0;
ReplaceOut.ar(bus, osc)}).add;