SynthDef.new(\drift,
{|bus, drift, driftspeed, driftdepth, driftsmooth, drift_, drift_d, driftlfo, driftlfomul, driftlfoadd, driftspeed_, driftspeed_d, driftspeedlfo, driftspeedlfomul, driftspeedlfoadd, driftdepth_, driftdepth_d, driftdepthlfo, driftdepthlfomul, driftdepthlfoadd, driftsmooth_, driftsmooth_d, driftsmoothlfo, driftsmoothlfomul, driftsmoothlfoadd, sus|
var osc,dry,drifted,delayMod,maxDelay;
osc = In.ar(bus, 2);
drift = if(drift_<=0, drift, Line.kr(drift, drift_, sus*drift_d));
drift = if(driftlfo<=0, drift, drift * SinOsc.kr(driftlfo, 0, driftlfomul, driftlfoadd));
driftspeed = if(driftspeed_<=0, driftspeed, Line.kr(driftspeed, driftspeed_, sus*driftspeed_d));
driftspeed = if(driftspeedlfo<=0, driftspeed, driftspeed * SinOsc.kr(driftspeedlfo, 0, driftspeedlfomul, driftspeedlfoadd));
driftdepth = if(driftdepth_<=0, driftdepth, Line.kr(driftdepth, driftdepth_, sus*driftdepth_d));
driftdepth = if(driftdepthlfo<=0, driftdepth, driftdepth * SinOsc.kr(driftdepthlfo, 0, driftdepthlfomul, driftdepthlfoadd));
driftsmooth = if(driftsmooth_<=0, driftsmooth, Line.kr(driftsmooth, driftsmooth_, sus*driftsmooth_d));
driftsmooth = if(driftsmoothlfo<=0, driftsmooth, driftsmooth * SinOsc.kr(driftsmoothlfo, 0, driftsmoothlfomul, driftsmoothlfoadd));
dry = osc;
maxDelay = 0.05;
delayMod = LFNoise2.kr(driftspeed).range(0, driftdepth * maxDelay);
delayMod = Lag.kr(delayMod, driftsmooth * 0.1);
drifted = DelayC.ar(osc, maxDelay, delayMod);
osc = XFade2.ar(dry, drifted, drift * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;