SynthDef.new(\spinPan,
{|bus, spin, sus, spin_, spin_d, spinlfo, spinlfomul, spinlfoadd|
var osc;
osc = In.ar(bus, 2);
spin = if(spin_<=0, spin, Line.kr(spin, spin_, sus*spin_d));
spin = if(spinlfo<=0, spin, spin * SinOsc.kr(spinlfo, 0, spinlfomul, spinlfoadd));
osc = osc * [FSinOsc.ar(spin / 2, iphase: 1, mul: 0.5, add: 0.5), FSinOsc.ar(spin / 2, iphase: 3, mul: 0.5, add: 0.5)];
ReplaceOut.ar(bus, osc)}).add;