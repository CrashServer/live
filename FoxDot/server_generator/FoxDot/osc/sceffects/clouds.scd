SynthDef.new(\clouds,
{|bus, clouds, cpos, csize, cdens, ctex, cmix, cgain, cfb, cmode|
var osc;
osc = In.ar(bus, 2);
osc = MiClouds.ar(osc, pit: clouds, pos: cpos, size:csize, dens: cdens, tex: ctex, drywet: cmix, in_gain: cgain, fb: cfb, mode:cmode);
ReplaceOut.ar(bus, osc);
ReplaceOut.ar(bus, osc)}).add;