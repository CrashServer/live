SynthDef.new(\vibrato,
{|bus, vib, vibdepth, vib_, vibdepth_, sus|
var osc;
osc = In.kr(bus, 1);
vib = vib+Line.kr(0, vib_, sus);
vibdepth = vibdepth+Line.kr(0, vibdepth_, sus);
osc = Vibrato.ar(osc, vib, depth: vibdepth);
ReplaceOut.kr(bus, osc)}).add;