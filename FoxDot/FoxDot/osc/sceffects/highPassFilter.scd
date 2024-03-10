SynthDef.new(\highPassFilter,
{|bus, hpf, hpr, hpf_, hpf_d, hpr_, hpr_d, sus|
var osc;
osc = In.ar(bus, 2);
hpf = if(hpf_<=0, hpf, Line.kr(hpf, hpf_, sus*hpf_d));
hpr = if(hpr_<=0, hpr, Line.kr(hpr, hpr_, sus*hpr_d));
osc = RHPF.ar(osc, hpf, hpr);
ReplaceOut.ar(bus, osc)}).add;