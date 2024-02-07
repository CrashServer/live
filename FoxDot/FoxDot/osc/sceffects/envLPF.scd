SynthDef.new(\envLPF,
{|bus, elpf, elpr, elpa, elps, elpc, sus, elpf_, elpr_, elpa_, elps_, elpc_|
var osc,env;
osc = In.ar(bus, 2);
elpf = elpf+Line.kr(0, elpf_, sus);
elpr = elpr+Line.kr(0, elpr_, sus);
elpa = elpa+Line.kr(0, elpa_, sus);
elps = elps+Line.kr(0, elps_, sus);
elpc = elpc+Line.kr(0, elpc_, sus);
env = EnvGen.ar(Env.new([0.01, 1, 1, 0.01], [elpa*sus, sus-(elpa*sus)-(elps*sus), elps], elpc), doneAction:0);
osc = RLPF.ar(osc, LinLin.ar(env, 0,1,0,elpf)+10, elpr, mul: 1);
ReplaceOut.ar(bus, osc)}).add;