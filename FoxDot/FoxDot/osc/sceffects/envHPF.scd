SynthDef.new(\envHPF,
{|bus, ehpf, ehpr, ehpa, ehps, ehpc, sus, ehpf_, ehpf_d, ehpr_, ehpr_d, ehpa_, ehpa_d, ehps_, ehps_d, ehpc_, ehpc_d|
var osc,env;
osc = In.ar(bus, 2);
ehpf = if(ehpf_<=0, ehpf, Line.kr(ehpf, ehpf_, sus*ehpf_d));
ehpr = if(ehpr_<=0, ehpr, Line.kr(ehpr, ehpr_, sus*ehpr_d));
ehpa = if(ehpa_<=0, ehpa, Line.kr(ehpa, ehpa_, sus*ehpa_d));
ehps = if(ehps_<=0, ehps, Line.kr(ehps, ehps_, sus*ehps_d));
ehpc = if(ehpc_<=0, ehpc, Line.kr(ehpc, ehpc_, sus*ehpc_d));
env = EnvGen.ar(Env.new([0, 1, 1, 0.1], [ehpa*sus, sus-(ehpa*sus)-(ehps*sus), ehps], ehpc));
osc = RHPF.ar(osc, ehpf, ehpr, mul: env);
ReplaceOut.ar(bus, osc)}).add;