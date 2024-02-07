SynthDef.new(\VALadder,
{|bus, valad, valadr, valadd, valadt, valad_, valadr_, valadd_, valadt_, sus|
var osc;
osc = In.ar(bus, 2);
valad = valad+Line.kr(0, valad_, sus);
valadr = valadr+Line.kr(0, valadr_, sus);
valadd = valadd+Line.kr(0, valadd_, sus);
valadt = valadt+Line.kr(0, valadt_, sus);
osc = VALadder.ar(osc*0.4, valad, valadr, valadd,valadt);
ReplaceOut.ar(bus, osc)}).add;