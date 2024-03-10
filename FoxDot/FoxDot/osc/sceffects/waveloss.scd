SynthDef.new(\waveloss,
{|bus, drop, dropof, drop_, drop_d, dropof_, dropof_d, sus|
var osc;
osc = In.ar(bus, 2);
drop = if(drop_<=0, drop, Line.kr(drop, drop_, sus*drop_d));
dropof = if(dropof_<=0, dropof, Line.kr(dropof, dropof_, sus*dropof_d));
osc = WaveLoss.ar(osc, drop, outof: dropof, mode: 2);
ReplaceOut.ar(bus, osc)}).add;