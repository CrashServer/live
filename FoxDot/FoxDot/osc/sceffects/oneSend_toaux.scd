SynthDef.new(\oneSend_toaux,
{|bus, toaux, toaux_, toaux_d, toauxlfo, toauxlfomul, toauxlfoadd, toauxlfophase, sus|
var osc;
osc = In.ar(bus, 2);
toaux = if(toaux_<=0, toaux, Line.kr(toaux, toaux_, sus*toaux_d));
toaux = if(toauxlfo<=0, toaux, toaux * SinOsc.kr(toauxlfo, toauxlfophase, toauxlfomul, toauxlfoadd));
Out.ar(12, osc * toaux);
ReplaceOut.ar(bus, osc)}).add;