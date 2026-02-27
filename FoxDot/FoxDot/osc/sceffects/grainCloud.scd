SynthDef.new(\grainCloud,
{|bus, gcloud, gcloud_density, gcloud_size, gcloud_spray, gcloud_spread, gcloud_, gcloud_d, gcloudlfo, gcloudlfomul, gcloudlfoadd, gcloud_density_, gcloud_density_d, gcloud_densitylfo, gcloud_densitylfomul, gcloud_densitylfoadd, gcloud_size_, gcloud_size_d, gcloud_sizelfo, gcloud_sizelfomul, gcloud_sizelfoadd, gcloud_spray_, gcloud_spray_d, gcloud_spraylfo, gcloud_spraylfomul, gcloud_spraylfoadd, gcloud_spread_, gcloud_spread_d, gcloud_spreadlfo, gcloud_spreadlfomul, gcloud_spreadlfoadd, sus|
var osc,grainTrig,grainBuf,grainSig;
osc = In.ar(bus, 2);
gcloud = if(gcloud_<=0, gcloud, Line.kr(gcloud, gcloud_, sus*gcloud_d));
gcloud = if(gcloudlfo<=0, gcloud, gcloud * SinOsc.kr(gcloudlfo, 0, gcloudlfomul, gcloudlfoadd));
gcloud_density = if(gcloud_density_<=0, gcloud_density, Line.kr(gcloud_density, gcloud_density_, sus*gcloud_density_d));
gcloud_density = if(gcloud_densitylfo<=0, gcloud_density, gcloud_density * SinOsc.kr(gcloud_densitylfo, 0, gcloud_densitylfomul, gcloud_densitylfoadd));
gcloud_size = if(gcloud_size_<=0, gcloud_size, Line.kr(gcloud_size, gcloud_size_, sus*gcloud_size_d));
gcloud_size = if(gcloud_sizelfo<=0, gcloud_size, gcloud_size * SinOsc.kr(gcloud_sizelfo, 0, gcloud_sizelfomul, gcloud_sizelfoadd));
gcloud_spray = if(gcloud_spray_<=0, gcloud_spray, Line.kr(gcloud_spray, gcloud_spray_, sus*gcloud_spray_d));
gcloud_spray = if(gcloud_spraylfo<=0, gcloud_spray, gcloud_spray * SinOsc.kr(gcloud_spraylfo, 0, gcloud_spraylfomul, gcloud_spraylfoadd));
gcloud_spread = if(gcloud_spread_<=0, gcloud_spread, Line.kr(gcloud_spread, gcloud_spread_, sus*gcloud_spread_d));
gcloud_spread = if(gcloud_spreadlfo<=0, gcloud_spread, gcloud_spread * SinOsc.kr(gcloud_spreadlfo, 0, gcloud_spreadlfomul, gcloud_spreadlfoadd));
grainBuf = LocalBuf(SampleRate.ir * 0.5, 2).clear;
RecordBuf.ar(osc, grainBuf, loop: 1);
grainTrig = Impulse.ar(gcloud_density);
grainSig = GrainBuf.ar(2, grainTrig, gcloud_size, grainBuf, 1 + (gcloud_spray * LFNoise1.kr(gcloud_density * 0.5)), LFNoise1.kr(gcloud_density).range(0, 1), 2, 0);
grainSig = Splay.ar(grainSig, gcloud_spread);
osc = XFade2.ar(osc, grainSig, gcloud * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;