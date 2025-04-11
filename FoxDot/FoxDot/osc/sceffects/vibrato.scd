SynthDef.new(\vibrato,
{|bus, vib, vibdepth, vib_, vib_d, viblfo, vibdepth_, vibdepth_d, vibdepthlfo, sus|
var osc;
osc = In.kr(bus, 1);
vib = if(vib_<=0, vib, Line.kr(vib, vib_, sus*vib_d));
vib = if(viblfo<=0, vib, vib * SinOsc.kr(viblfo, 0, 1, 1));
vibdepth = if(vibdepth_<=0, vibdepth, Line.kr(vibdepth, vibdepth_, sus*vibdepth_d));
vibdepth = if(vibdepthlfo<=0, vibdepth, vibdepth * SinOsc.kr(vibdepthlfo, 0, 1, 1));
osc = Vibrato.ar(osc, vib, depth: vibdepth);
ReplaceOut.kr(bus, osc)}).add;