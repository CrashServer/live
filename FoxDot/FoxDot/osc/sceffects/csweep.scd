SynthDef.new(\csweep,
{|bus, csweep, cswfreq, cswdepth, cswrate, cswdecay, csweep_, csweep_d, csweeplfo, csweeplfomul, csweeplfoadd, cswfreq_, cswfreq_d, cswfreqlfo, cswfreqlfomul, cswfreqlfoadd, cswdepth_, cswdepth_d, cswdepthlfo, cswdepthlfomul, cswdepthlfoadd, cswrate_, cswrate_d, cswratelfo, cswratelfomul, cswratelfoadd, cswdecay_, cswdecay_d, cswdecaylfo, cswdecaylfomul, cswdecaylfoadd, sus|
var osc,dry,wet,deltime,lfo;
osc = In.ar(bus, 2);
csweep = if(csweep_<=0, csweep, Line.kr(csweep, csweep_, sus*csweep_d));
csweep = if(csweeplfo<=0, csweep, csweep * SinOsc.kr(csweeplfo, 0, csweeplfomul, csweeplfoadd));
cswfreq = if(cswfreq_<=0, cswfreq, Line.kr(cswfreq, cswfreq_, sus*cswfreq_d));
cswfreq = if(cswfreqlfo<=0, cswfreq, cswfreq * SinOsc.kr(cswfreqlfo, 0, cswfreqlfomul, cswfreqlfoadd));
cswdepth = if(cswdepth_<=0, cswdepth, Line.kr(cswdepth, cswdepth_, sus*cswdepth_d));
cswdepth = if(cswdepthlfo<=0, cswdepth, cswdepth * SinOsc.kr(cswdepthlfo, 0, cswdepthlfomul, cswdepthlfoadd));
cswrate = if(cswrate_<=0, cswrate, Line.kr(cswrate, cswrate_, sus*cswrate_d));
cswrate = if(cswratelfo<=0, cswrate, cswrate * SinOsc.kr(cswratelfo, 0, cswratelfomul, cswratelfoadd));
cswdecay = if(cswdecay_<=0, cswdecay, Line.kr(cswdecay, cswdecay_, sus*cswdecay_d));
cswdecay = if(cswdecaylfo<=0, cswdecay, cswdecay * SinOsc.kr(cswdecaylfo, 0, cswdecaylfomul, cswdecaylfoadd));
dry = osc;
deltime = cswfreq.reciprocal;
lfo = SinOsc.kr(cswrate).range(1 - cswdepth, 1 + cswdepth);
wet = CombC.ar(osc, 0.05, (deltime * lfo).clip(0.00005, 0.05), cswdecay);
wet = LeakDC.ar(wet);
osc = XFade2.ar(dry, wet, csweep * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;