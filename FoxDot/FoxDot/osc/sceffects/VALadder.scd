SynthDef.new(\VALadder,
{|bus, valad, valadr, valadd, valadt|
var osc;
osc = In.ar(bus, 2);
osc = VALadder.ar(osc, valad, valadr, valadd,valadt);
ReplaceOut.ar(bus, osc)}).add;