SynthDef.new(\orbitPan,
{|bus, orbit, orbitwidth, orbit_, orbit_d, orbitlfo, orbitlfomul, orbitlfoadd, orbitwidth_, orbitwidth_d, orbitwidthlfo, orbitwidthlfomul, orbitwidthlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
orbit = if(orbit_<=0, orbit, Line.kr(orbit, orbit_, sus*orbit_d));
orbit = if(orbitlfo<=0, orbit, orbit * SinOsc.kr(orbitlfo, 0, orbitlfomul, orbitlfoadd));
orbitwidth = if(orbitwidth_<=0, orbitwidth, Line.kr(orbitwidth, orbitwidth_, sus*orbitwidth_d));
orbitwidth = if(orbitwidthlfo<=0, orbitwidth, orbitwidth * SinOsc.kr(orbitwidthlfo, 0, orbitwidthlfomul, orbitwidthlfoadd));
osc = Pan2.ar(Mix.ar(osc), SinOsc.kr(orbit / beat_dur) * orbitwidth);
ReplaceOut.ar(bus, osc)}).add;