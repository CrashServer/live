SynthDef.new(\envHPF,
{|bus, ehpf, ehpr, ehpa, ehps, ehpc, sus, ehpf_, ehpf_d, ehpflfo, ehpflfomul, ehpflfoadd, ehpr_, ehpr_d, ehprlfo, ehprlfomul, ehprlfoadd, ehpa_, ehpa_d, ehpalfo, ehpalfomul, ehpalfoadd, ehps_, ehps_d, ehpslfo, ehpslfomul, ehpslfoadd, ehpc_, ehpc_d, ehpclfo, ehpclfomul, ehpclfoadd|
var osc,env;
osc = In.ar(bus, 2);
ehpf = if(ehpf_<=0, ehpf, Line.kr(ehpf, ehpf_, sus*ehpf_d));
ehpf = if(ehpflfo<=0, ehpf, ehpf * SinOsc.kr(ehpflfo, 0, ehpflfomul, ehpflfoadd));
ehpr = if(ehpr_<=0, ehpr, Line.kr(ehpr, ehpr_, sus*ehpr_d));
ehpr = if(ehprlfo<=0, ehpr, ehpr * SinOsc.kr(ehprlfo, 0, ehprlfomul, ehprlfoadd));
ehpa = if(ehpa_<=0, ehpa, Line.kr(ehpa, ehpa_, sus*ehpa_d));
ehpa = if(ehpalfo<=0, ehpa, ehpa * SinOsc.kr(ehpalfo, 0, ehpalfomul, ehpalfoadd));
ehps = if(ehps_<=0, ehps, Line.kr(ehps, ehps_, sus*ehps_d));
ehps = if(ehpslfo<=0, ehps, ehps * SinOsc.kr(ehpslfo, 0, ehpslfomul, ehpslfoadd));
ehpc = if(ehpc_<=0, ehpc, Line.kr(ehpc, ehpc_, sus*ehpc_d));
ehpc = if(ehpclfo<=0, ehpc, ehpc * SinOsc.kr(ehpclfo, 0, ehpclfomul, ehpclfoadd));
env = EnvGen.ar(Env.new([0, 1, 1, 0.1], [ehpa*sus, sus-(ehpa*sus)-(ehps*sus), ehps], ehpc));
osc = RHPF.ar(osc, ehpf, ehpr, mul: env);
ReplaceOut.ar(bus, osc)}).add;