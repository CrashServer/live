SynthDef.new(\vibrato,
{|bus, vib, vibdepth, vib_, vib_d, viblfo, viblfomul, viblfoadd, vibdepth_, vibdepth_d, vibdepthlfo, vibdepthlfomul, vibdepthlfoadd, sus|
var osc;
osc = In.kr(bus, 1);
vib = if(vib_<=0, vib, Line.kr(vib, vib_, sus*vib_d));
vib = if(viblfo<=0, vib, vib * SinOsc.kr(viblfo, 0, viblfomul, viblfoadd));
vibdepth = if(vibdepth_<=0, vibdepth, Line.kr(vibdepth, vibdepth_, sus*vibdepth_d));
vibdepth = if(vibdepthlfo<=0, vibdepth, vibdepth * SinOsc.kr(vibdepthlfo, 0, vibdepthlfomul, vibdepthlfoadd));
osc = Vibrato.ar(osc, vib, depth: vibdepth);
ReplaceOut.kr(bus, osc)}).add;