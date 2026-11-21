SynthDef.new(\clouds,
{|bus, clouds, cpos, csize, cdens, ctex, cpitch, cgain, cfb, cmode, clouds_, clouds_d, cloudslfo, cloudslfomul, cloudslfoadd, cloudslfophase, cpos_, cpos_d, cposlfo, cposlfomul, cposlfoadd, cposlfophase, csize_, csize_d, csizelfo, csizelfomul, csizelfoadd, csizelfophase, cdens_, cdens_d, cdenslfo, cdenslfomul, cdenslfoadd, cdenslfophase, ctex_, ctex_d, ctexlfo, ctexlfomul, ctexlfoadd, ctexlfophase, cpitch_, cpitch_d, cpitchlfo, cpitchlfomul, cpitchlfoadd, cpitchlfophase, cgain_, cgain_d, cgainlfo, cgainlfomul, cgainlfoadd, cgainlfophase, cfb_, cfb_d, cfblfo, cfblfomul, cfblfoadd, cfblfophase, cmode_, cmode_d, cmodelfo, cmodelfomul, cmodelfoadd, cmodelfophase, sus|
var osc;
osc = In.ar(bus, 2);
clouds = if(clouds_<=0, clouds, Line.kr(clouds, clouds_, sus*clouds_d));
clouds = if(cloudslfo<=0, clouds, clouds * SinOsc.kr(cloudslfo, cloudslfophase, cloudslfomul, cloudslfoadd));
cpos = if(cpos_<=0, cpos, Line.kr(cpos, cpos_, sus*cpos_d));
cpos = if(cposlfo<=0, cpos, cpos * SinOsc.kr(cposlfo, cposlfophase, cposlfomul, cposlfoadd));
csize = if(csize_<=0, csize, Line.kr(csize, csize_, sus*csize_d));
csize = if(csizelfo<=0, csize, csize * SinOsc.kr(csizelfo, csizelfophase, csizelfomul, csizelfoadd));
cdens = if(cdens_<=0, cdens, Line.kr(cdens, cdens_, sus*cdens_d));
cdens = if(cdenslfo<=0, cdens, cdens * SinOsc.kr(cdenslfo, cdenslfophase, cdenslfomul, cdenslfoadd));
ctex = if(ctex_<=0, ctex, Line.kr(ctex, ctex_, sus*ctex_d));
ctex = if(ctexlfo<=0, ctex, ctex * SinOsc.kr(ctexlfo, ctexlfophase, ctexlfomul, ctexlfoadd));
cpitch = if(cpitch_<=0, cpitch, Line.kr(cpitch, cpitch_, sus*cpitch_d));
cpitch = if(cpitchlfo<=0, cpitch, cpitch * SinOsc.kr(cpitchlfo, cpitchlfophase, cpitchlfomul, cpitchlfoadd));
cgain = if(cgain_<=0, cgain, Line.kr(cgain, cgain_, sus*cgain_d));
cgain = if(cgainlfo<=0, cgain, cgain * SinOsc.kr(cgainlfo, cgainlfophase, cgainlfomul, cgainlfoadd));
cfb = if(cfb_<=0, cfb, Line.kr(cfb, cfb_, sus*cfb_d));
cfb = if(cfblfo<=0, cfb, cfb * SinOsc.kr(cfblfo, cfblfophase, cfblfomul, cfblfoadd));
cmode = if(cmode_<=0, cmode, Line.kr(cmode, cmode_, sus*cmode_d));
cmode = if(cmodelfo<=0, cmode, cmode * SinOsc.kr(cmodelfo, cmodelfophase, cmodelfomul, cmodelfoadd));
osc = MiClouds.ar(osc, pit: cpitch, pos: cpos, size:csize, dens: cdens, tex: ctex, drywet: clouds, in_gain: cgain, fb: cfb, mode:cmode);
ReplaceOut.ar(bus, osc)}).add;