SynthDef.new(\waveloss,
{|bus, drop, dropof, drop_, dropof_, sus|
var osc;
osc = In.ar(bus, 2);
drop = drop+Line.kr(0, drop_, sus);
dropof = dropof+Line.kr(0, dropof_, sus);
osc = WaveLoss.ar(osc, drop, outof: dropof, mode: 2);
ReplaceOut.ar(bus, osc)}).add;