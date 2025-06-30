SynthDef.new(\Bell_Filter,
{|bus, bell, bellf, bellq, bell_, bell_d, belllfo, belllfomul, belllfoadd, bellf_, bellf_d, bellflfo, bellflfomul, bellflfoadd, bellq_, bellq_d, bellqlfo, bellqlfomul, bellqlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
bell = if(bell_<=0, bell, Line.kr(bell, bell_, sus*bell_d));
bell = if(belllfo<=0, bell, bell * SinOsc.kr(belllfo, 0, belllfomul, belllfoadd));
bellf = if(bellf_<=0, bellf, Line.kr(bellf, bellf_, sus*bellf_d));
bellf = if(bellflfo<=0, bellf, bellf * SinOsc.kr(bellflfo, 0, bellflfomul, bellflfoadd));
bellq = if(bellq_<=0, bellq, Line.kr(bellq, bellq_, sus*bellq_d));
bellq = if(bellqlfo<=0, bellq, bellq * SinOsc.kr(bellqlfo, 0, bellqlfomul, bellqlfoadd));
osc = NonlinearFilter.ar(osc, freq: bellf, shape:0, gain:bell, q:bellq, saturation: 1);
ReplaceOut.ar(bus, osc)}).add;