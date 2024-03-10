SynthDef.new(\vibrato,
{|bus, vib, vibdepth, vib_, vib_d, vibdepth_, vibdepth_d, sus|
var osc;
osc = In.kr(bus, 1);
vib = if(vib_<=0, vib, Line.kr(vib, vib_, sus*vib_d));
vibdepth = if(vibdepth_<=0, vibdepth, Line.kr(vibdepth, vibdepth_, sus*vibdepth_d));
osc = Vibrato.ar(osc, vib, depth: vibdepth);
ReplaceOut.kr(bus, osc)}).add;