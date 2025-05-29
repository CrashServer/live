SynthDef.new(\monitoring,
{|bus, mon, mon_, mon_d, monlfo, monlfomul, monlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
mon = if(mon_<=0, mon, Line.kr(mon, mon_, sus*mon_d));
mon = if(monlfo<=0, mon, mon * SinOsc.kr(monlfo, 0, monlfomul, monlfoadd));
Out.ar([mon, mon+1], osc);
osc = osc*0;
ReplaceOut.ar(bus, osc)}).add;