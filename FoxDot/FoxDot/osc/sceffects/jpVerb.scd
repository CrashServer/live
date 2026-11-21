SynthDef.new(\jpVerb,
{|bus, jpverb, jpmix, jpdamp, jpsize, jpverb_, jpverb_d, jpverblfo, jpverblfomul, jpverblfoadd, jpverblfophase, jpmix_, jpmix_d, jpmixlfo, jpmixlfomul, jpmixlfoadd, jpmixlfophase, jpdamp_, jpdamp_d, jpdamplfo, jpdamplfomul, jpdamplfoadd, jpdamplfophase, jpsize_, jpsize_d, jpsizelfo, jpsizelfomul, jpsizelfoadd, jpsizelfophase, sus|
var osc,dry;
osc = In.ar(bus, 2);
jpverb = if(jpverb_<=0, jpverb, Line.kr(jpverb, jpverb_, sus*jpverb_d));
jpverb = if(jpverblfo<=0, jpverb, jpverb * SinOsc.kr(jpverblfo, jpverblfophase, jpverblfomul, jpverblfoadd));
jpmix = if(jpmix_<=0, jpmix, Line.kr(jpmix, jpmix_, sus*jpmix_d));
jpmix = if(jpmixlfo<=0, jpmix, jpmix * SinOsc.kr(jpmixlfo, jpmixlfophase, jpmixlfomul, jpmixlfoadd));
jpdamp = if(jpdamp_<=0, jpdamp, Line.kr(jpdamp, jpdamp_, sus*jpdamp_d));
jpdamp = if(jpdamplfo<=0, jpdamp, jpdamp * SinOsc.kr(jpdamplfo, jpdamplfophase, jpdamplfomul, jpdamplfoadd));
jpsize = if(jpsize_<=0, jpsize, Line.kr(jpsize, jpsize_, sus*jpsize_d));
jpsize = if(jpsizelfo<=0, jpsize, jpsize * SinOsc.kr(jpsizelfo, jpsizelfophase, jpsizelfomul, jpsizelfoadd));
dry = osc;
osc = JPverb.ar(osc, t60: jpverb, damp: jpdamp, size: jpsize);
osc = SelectX.ar(jpmix, [dry, osc]);
ReplaceOut.ar(bus, osc)}).add;