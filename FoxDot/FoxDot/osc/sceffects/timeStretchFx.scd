SynthDef.new(\timeStretchFx,
{|bus, tstretch, tstretchsize, tstretch_, tstretch_d, tstretchlfo, tstretchlfomul, tstretchlfoadd, tstretchsize_, tstretchsize_d, tstretchsizelfo, tstretchsizelfomul, tstretchsizelfoadd, sus|
var osc,stretched,xfade;
osc = In.ar(bus, 2);
tstretch = if(tstretch_<=0, tstretch, Line.kr(tstretch, tstretch_, sus*tstretch_d));
tstretch = if(tstretchlfo<=0, tstretch, tstretch * SinOsc.kr(tstretchlfo, 0, tstretchlfomul, tstretchlfoadd));
tstretchsize = if(tstretchsize_<=0, tstretchsize, Line.kr(tstretchsize, tstretchsize_, sus*tstretchsize_d));
tstretchsize = if(tstretchsizelfo<=0, tstretchsize, tstretchsize * SinOsc.kr(tstretchsizelfo, 0, tstretchsizelfomul, tstretchsizelfoadd));
stretched = PitchShift.ar(osc, tstretchsize, 1, 0, 0.004);
xfade = (1 - tstretch).abs.min(1);
osc = XFade2.ar(osc, stretched, xfade * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;