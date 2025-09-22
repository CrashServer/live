SynthDef.new(\jpVerb,
{|bus, jpverb, jpmix, jpdamp, jpsize, jpverb_, jpverb_d, jpverblfo, jpverblfomul, jpverblfoadd, jpmix_, jpmix_d, jpmixlfo, jpmixlfomul, jpmixlfoadd, jpdamp_, jpdamp_d, jpdamplfo, jpdamplfomul, jpdamplfoadd, jpsize_, jpsize_d, jpsizelfo, jpsizelfomul, jpsizelfoadd, sus|
var osc,dry;
osc = In.ar(bus, 2);
jpverb = if(jpverb_<=0, jpverb, Line.kr(jpverb, jpverb_, sus*jpverb_d));
jpverb = if(jpverblfo<=0, jpverb, jpverb * SinOsc.kr(jpverblfo, 0, jpverblfomul, jpverblfoadd));
jpmix = if(jpmix_<=0, jpmix, Line.kr(jpmix, jpmix_, sus*jpmix_d));
jpmix = if(jpmixlfo<=0, jpmix, jpmix * SinOsc.kr(jpmixlfo, 0, jpmixlfomul, jpmixlfoadd));
jpdamp = if(jpdamp_<=0, jpdamp, Line.kr(jpdamp, jpdamp_, sus*jpdamp_d));
jpdamp = if(jpdamplfo<=0, jpdamp, jpdamp * SinOsc.kr(jpdamplfo, 0, jpdamplfomul, jpdamplfoadd));
jpsize = if(jpsize_<=0, jpsize, Line.kr(jpsize, jpsize_, sus*jpsize_d));
jpsize = if(jpsizelfo<=0, jpsize, jpsize * SinOsc.kr(jpsizelfo, 0, jpsizelfomul, jpsizelfoadd));
dry = osc;
osc = JPverb.ar(osc, t60: jpverb, damp: jpdamp, size: jpsize);
osc = SelectX.ar(jpmix, [dry, osc]);
ReplaceOut.ar(bus, osc)}).add;