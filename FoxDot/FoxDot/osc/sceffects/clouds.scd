SynthDef.new(\clouds,
{|bus, clouds, cpos, csize, cdens, ctex, cpitch, cgain, cfb, cmode, clouds_, clouds_d, cpos_, cpos_d, csize_, csize_d, cdens_, cdens_d, ctex_, ctex_d, cpitch_, cpitch_d, cgain_, cgain_d, cfb_, cfb_d, cmode_, cmode_d, sus|
var osc;
osc = In.ar(bus, 2);
clouds = if(clouds_<=0, clouds, Line.kr(clouds, clouds_, sus*clouds_d));
cpos = if(cpos_<=0, cpos, Line.kr(cpos, cpos_, sus*cpos_d));
csize = if(csize_<=0, csize, Line.kr(csize, csize_, sus*csize_d));
cdens = if(cdens_<=0, cdens, Line.kr(cdens, cdens_, sus*cdens_d));
ctex = if(ctex_<=0, ctex, Line.kr(ctex, ctex_, sus*ctex_d));
cpitch = if(cpitch_<=0, cpitch, Line.kr(cpitch, cpitch_, sus*cpitch_d));
cgain = if(cgain_<=0, cgain, Line.kr(cgain, cgain_, sus*cgain_d));
cfb = if(cfb_<=0, cfb, Line.kr(cfb, cfb_, sus*cfb_d));
cmode = if(cmode_<=0, cmode, Line.kr(cmode, cmode_, sus*cmode_d));
osc = MiClouds.ar(osc, pit: cpitch, pos: cpos, size:csize, dens: cdens, tex: ctex, drywet: clouds, in_gain: cgain, fb: cfb, mode:cmode);
ReplaceOut.ar(bus, osc)}).add;