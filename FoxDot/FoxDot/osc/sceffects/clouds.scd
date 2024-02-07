SynthDef.new(\clouds,
{|bus, clouds, cpos, csize, cdens, ctex, cpitch, cgain, cfb, cmode, clouds_, cpos_, csize_, cdens_, ctex_, cpitch_, cgain_, cfb_, cmode_, sus|
var osc;
osc = In.ar(bus, 2);
clouds = clouds+Line.kr(0, clouds_, sus);
cpos = cpos+Line.kr(0, cpos_, sus);
csize = csize+Line.kr(0, csize_, sus);
cdens = cdens+Line.kr(0, cdens_, sus);
ctex = ctex+Line.kr(0, ctex_, sus);
cpitch = cpitch+Line.kr(0, cpitch_, sus);
cgain = cgain+Line.kr(0, cgain_, sus);
cfb = cfb+Line.kr(0, cfb_, sus);
cmode = cmode+Line.kr(0, cmode_, sus);
osc = MiClouds.ar(osc, pit: cpitch, pos: cpos, size:csize, dens: cdens, tex: ctex, drywet: clouds, in_gain: cgain, fb: cfb, mode:cmode);
ReplaceOut.ar(bus, osc)}).add;