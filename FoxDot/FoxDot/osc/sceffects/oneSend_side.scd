SynthDef.new(\oneSend_side,
{|bus, side, side_, side_d, sidelfo, sidelfomul, sidelfoadd, sidelfophase, sus|
var osc;
osc = In.ar(bus, 2);
side = if(side_<=0, side, Line.kr(side, side_, sus*side_d));
side = if(sidelfo<=0, side, side * SinOsc.kr(sidelfo, sidelfophase, sidelfomul, sidelfoadd));
Out.ar(14, osc * side);
ReplaceOut.ar(bus, osc)}).add;