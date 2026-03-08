SynthDef.new(\octclean,
{|bus, octclean, ocsub, ocup, octclean_, octclean_d, octcleanlfo, octcleanlfomul, octcleanlfoadd, ocsub_, ocsub_d, ocsublfo, ocsublfomul, ocsublfoadd, ocup_, ocup_d, ocuplfo, ocuplfomul, ocuplfoadd, sus|
var osc,dry,sub,up;
osc = In.ar(bus, 2);
octclean = if(octclean_<=0, octclean, Line.kr(octclean, octclean_, sus*octclean_d));
octclean = if(octcleanlfo<=0, octclean, octclean * SinOsc.kr(octcleanlfo, 0, octcleanlfomul, octcleanlfoadd));
ocsub = if(ocsub_<=0, ocsub, Line.kr(ocsub, ocsub_, sus*ocsub_d));
ocsub = if(ocsublfo<=0, ocsub, ocsub * SinOsc.kr(ocsublfo, 0, ocsublfomul, ocsublfoadd));
ocup = if(ocup_<=0, ocup, Line.kr(ocup, ocup_, sus*ocup_d));
ocup = if(ocuplfo<=0, ocup, ocup * SinOsc.kr(ocuplfo, 0, ocuplfomul, ocuplfoadd));
dry = osc;
sub = PitchShift.ar(osc, 0.1, 0.5, 0, 0.004);
up = PitchShift.ar(osc, 0.05, 2.0, 0, 0.004);
osc = osc + (sub * ocsub) + (up * ocup);
osc = XFade2.ar(dry, LeakDC.ar(osc), octclean * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;