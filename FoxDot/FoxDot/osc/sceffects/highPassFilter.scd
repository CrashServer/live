SynthDef.new(\highPassFilter,
{|bus, hpf, hpr, hpf_, hpf_d, hpflfo, hpr_, hpr_d, hprlfo, sus|
var osc;
osc = In.ar(bus, 2);
hpf = if(hpf_<=0, hpf, Line.kr(hpf, hpf_, sus*hpf_d));
hpf = if(hpflfo<=0, hpf, hpf * SinOsc.kr(hpflfo, 0, 1, 1));
hpr = if(hpr_<=0, hpr, Line.kr(hpr, hpr_, sus*hpr_d));
hpr = if(hprlfo<=0, hpr, hpr * SinOsc.kr(hprlfo, 0, 1, 1));
osc = RHPF.ar(osc, hpf, hpr);
ReplaceOut.ar(bus, osc)}).add;