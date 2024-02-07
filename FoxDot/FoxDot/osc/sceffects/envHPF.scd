SynthDef.new(\envHPF,
{|bus, ehpf, ehpr, ehpa, ehps, ehpc, sus, ehpf_, ehpr_, ehpa_, ehps_, ehpc_|
var osc,env;
osc = In.ar(bus, 2);
ehpf = ehpf+Line.kr(0, ehpf_, sus);
ehpr = ehpr+Line.kr(0, ehpr_, sus);
ehpa = ehpa+Line.kr(0, ehpa_, sus);
ehps = ehps+Line.kr(0, ehps_, sus);
ehpc = ehpc+Line.kr(0, ehpc_, sus);
env = EnvGen.ar(Env.new([0, 1, 1, 0.1], [ehpa*sus, sus-(ehpa*sus)-(ehps*sus), ehps], ehpc));
osc = RHPF.ar(osc, ehpf, ehpr, mul: env);
ReplaceOut.ar(bus, osc)}).add;