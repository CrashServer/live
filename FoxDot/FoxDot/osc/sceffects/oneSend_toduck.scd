SynthDef.new(\oneSend_toduck,
{|bus, toduck, toduck_, toduck_d, toducklfo, toducklfomul, toducklfoadd, toducklfophase, sus|
var osc;
osc = In.ar(bus, 2);
toduck = if(toduck_<=0, toduck, Line.kr(toduck, toduck_, sus*toduck_d));
toduck = if(toducklfo<=0, toduck, toduck * SinOsc.kr(toducklfo, toducklfophase, toducklfomul, toducklfoadd));
Out.ar(6, osc * toduck);
ReplaceOut.ar(bus, osc)}).add;