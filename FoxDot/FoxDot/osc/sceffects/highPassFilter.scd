SynthDef.new(\highPassFilter,
{|bus, hpf, hpr, hpf_, hpr_, sus|
var osc;
osc = In.ar(bus, 2);
hpf = hpf+Line.kr(0, hpf_, sus);
hpr = hpr+Line.kr(0, hpr_, sus);
osc = RHPF.ar(osc, hpf, hpr);
ReplaceOut.ar(bus, osc)}).add;