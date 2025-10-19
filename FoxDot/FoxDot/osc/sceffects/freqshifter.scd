SynthDef.new(\freqshifter,
{|bus, fshift, fshiftmod, fshift_, fshift_d, fshiftlfo, fshiftlfomul, fshiftlfoadd, fshiftmod_, fshiftmod_d, fshiftmodlfo, fshiftmodlfomul, fshiftmodlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
fshift = if(fshift_<=0, fshift, Line.kr(fshift, fshift_, sus*fshift_d));
fshift = if(fshiftlfo<=0, fshift, fshift * SinOsc.kr(fshiftlfo, 0, fshiftlfomul, fshiftlfoadd));
fshiftmod = if(fshiftmod_<=0, fshiftmod, Line.kr(fshiftmod, fshiftmod_, sus*fshiftmod_d));
fshiftmod = if(fshiftmodlfo<=0, fshiftmod, fshiftmod * SinOsc.kr(fshiftmodlfo, 0, fshiftmodlfomul, fshiftmodlfoadd));
osc = FreqShift.ar(osc, fshift, fshiftmod);
ReplaceOut.ar(bus, osc)}).add;