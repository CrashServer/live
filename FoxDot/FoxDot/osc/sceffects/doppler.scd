SynthDef.new(\doppler,
{|bus, doppler, dopspd, dopdist, doppler_, doppler_d, dopplerlfo, dopplerlfomul, dopplerlfoadd, dopspd_, dopspd_d, dopspdlfo, dopspdlfomul, dopspdlfoadd, dopdist_, dopdist_d, dopdistlfo, dopdistlfomul, dopdistlfoadd, sus|
var osc,dry,wet,pos,dist,delmod,ampmod,filtmod;
osc = In.ar(bus, 2);
doppler = if(doppler_<=0, doppler, Line.kr(doppler, doppler_, sus*doppler_d));
doppler = if(dopplerlfo<=0, doppler, doppler * SinOsc.kr(dopplerlfo, 0, dopplerlfomul, dopplerlfoadd));
dopspd = if(dopspd_<=0, dopspd, Line.kr(dopspd, dopspd_, sus*dopspd_d));
dopspd = if(dopspdlfo<=0, dopspd, dopspd * SinOsc.kr(dopspdlfo, 0, dopspdlfomul, dopspdlfoadd));
dopdist = if(dopdist_<=0, dopdist, Line.kr(dopdist, dopdist_, sus*dopdist_d));
dopdist = if(dopdistlfo<=0, dopdist, dopdist * SinOsc.kr(dopdistlfo, 0, dopdistlfomul, dopdistlfoadd));
dry = osc;
pos = SinOsc.kr(dopspd);
dist = 1 + (dopdist * (1 - pos) * 0.5);
delmod = dopdist * 0.008 * SinOsc.kr(dopspd);
wet = DelayC.ar(osc, 0.1, (0.01 + delmod).clip(0.0001, 0.1));
ampmod = 1 / dist;
wet = wet * ampmod;
filtmod = (12000 / dist).clip(200, 12000);
wet = LPF.ar(wet, filtmod);
wet = Balance2.ar(wet[0], wet[1], pos);
wet = LeakDC.ar(wet);
osc = XFade2.ar(dry, wet, doppler * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;