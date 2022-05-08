SynthDef.new(\envHPF,
{|bus, ehpf, ehpr, ehpa, ehps, ehpc, sus|
var osc,env;
osc = In.ar(bus, 2);
env = EnvGen.ar(Env.new([0, 1, 1, 0.1], [ehpa*sus, sus-(ehpa*sus)-(ehps*sus), ehps], ehpc));
osc = RHPF.ar(osc, ehpf, ehpr, mul: env);
ReplaceOut.ar(bus, osc)}).add;