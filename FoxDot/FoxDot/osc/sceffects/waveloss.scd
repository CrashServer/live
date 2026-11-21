SynthDef.new(\waveloss,
{|bus, drop, dropof, drop_, drop_d, droplfo, droplfomul, droplfoadd, droplfophase, dropof_, dropof_d, dropoflfo, dropoflfomul, dropoflfoadd, dropoflfophase, sus|
var osc;
osc = In.ar(bus, 2);
drop = if(drop_<=0, drop, Line.kr(drop, drop_, sus*drop_d));
drop = if(droplfo<=0, drop, drop * SinOsc.kr(droplfo, droplfophase, droplfomul, droplfoadd));
dropof = if(dropof_<=0, dropof, Line.kr(dropof, dropof_, sus*dropof_d));
dropof = if(dropoflfo<=0, dropof, dropof * SinOsc.kr(dropoflfo, dropoflfophase, dropoflfomul, dropoflfoadd));
osc = WaveLoss.ar(osc, drop, outof: dropof, mode: 2);
ReplaceOut.ar(bus, osc)}).add;