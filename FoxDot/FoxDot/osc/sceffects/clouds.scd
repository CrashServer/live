SynthDef.new(\clouds,
{|bus, clouds, cpos, csize, cdens, ctex, cpitch, cgain, cfb, cmode, clouds_, clouds_d, cloudslfo, cpos_, cpos_d, cposlfo, csize_, csize_d, csizelfo, cdens_, cdens_d, cdenslfo, ctex_, ctex_d, ctexlfo, cpitch_, cpitch_d, cpitchlfo, cgain_, cgain_d, cgainlfo, cfb_, cfb_d, cfblfo, cmode_, cmode_d, cmodelfo, sus|
var osc;
osc = In.ar(bus, 2);
clouds = if(clouds_<=0, clouds, Line.kr(clouds, clouds_, sus*clouds_d));
clouds = if(cloudslfo<=0, clouds, clouds * SinOsc.kr(cloudslfo, 0, 1, 1));
cpos = if(cpos_<=0, cpos, Line.kr(cpos, cpos_, sus*cpos_d));
cpos = if(cposlfo<=0, cpos, cpos * SinOsc.kr(cposlfo, 0, 1, 1));
csize = if(csize_<=0, csize, Line.kr(csize, csize_, sus*csize_d));
csize = if(csizelfo<=0, csize, csize * SinOsc.kr(csizelfo, 0, 1, 1));
cdens = if(cdens_<=0, cdens, Line.kr(cdens, cdens_, sus*cdens_d));
cdens = if(cdenslfo<=0, cdens, cdens * SinOsc.kr(cdenslfo, 0, 1, 1));
ctex = if(ctex_<=0, ctex, Line.kr(ctex, ctex_, sus*ctex_d));
ctex = if(ctexlfo<=0, ctex, ctex * SinOsc.kr(ctexlfo, 0, 1, 1));
cpitch = if(cpitch_<=0, cpitch, Line.kr(cpitch, cpitch_, sus*cpitch_d));
cpitch = if(cpitchlfo<=0, cpitch, cpitch * SinOsc.kr(cpitchlfo, 0, 1, 1));
cgain = if(cgain_<=0, cgain, Line.kr(cgain, cgain_, sus*cgain_d));
cgain = if(cgainlfo<=0, cgain, cgain * SinOsc.kr(cgainlfo, 0, 1, 1));
cfb = if(cfb_<=0, cfb, Line.kr(cfb, cfb_, sus*cfb_d));
cfb = if(cfblfo<=0, cfb, cfb * SinOsc.kr(cfblfo, 0, 1, 1));
cmode = if(cmode_<=0, cmode, Line.kr(cmode, cmode_, sus*cmode_d));
cmode = if(cmodelfo<=0, cmode, cmode * SinOsc.kr(cmodelfo, 0, 1, 1));
osc = MiClouds.ar(osc, pit: cpitch, pos: cpos, size:csize, dens: cdens, tex: ctex, drywet: clouds, in_gain: cgain, fb: cfb, mode:cmode);
ReplaceOut.ar(bus, osc)}).add;