SynthDef.new(\envLPF,
{|bus, elpf, elpr, elpa, elps, elpc, sus|
var osc,env;
osc = In.ar(bus, 2);
env = EnvGen.ar(Env.new([0.01, 1, 1, 0.01], [elpa*sus, sus-(elpa*sus)-(elps*sus), elps], elpc), doneAction:0);
osc = RLPF.ar(osc, LinLin.ar(env, 0,1,0,elpf)+10, elpr, mul: 1);
ReplaceOut.ar(bus, osc)}).add;