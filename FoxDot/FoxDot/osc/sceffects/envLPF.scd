SynthDef.new(\envLPF,
{|bus, elpf, elpr, elpa, elps, elpc, sus, elpf_, elpf_d, elpr_, elpr_d, elpa_, elpa_d, elps_, elps_d, elpc_, elpc_d|
var osc,env;
osc = In.ar(bus, 2);
elpf = if(elpf_<=0, elpf, Line.kr(elpf, elpf_, sus*elpf_d));
elpr = if(elpr_<=0, elpr, Line.kr(elpr, elpr_, sus*elpr_d));
elpa = if(elpa_<=0, elpa, Line.kr(elpa, elpa_, sus*elpa_d));
elps = if(elps_<=0, elps, Line.kr(elps, elps_, sus*elps_d));
elpc = if(elpc_<=0, elpc, Line.kr(elpc, elpc_, sus*elpc_d));
env = EnvGen.ar(Env.new([0.01, 1, 1, 0.01], [elpa*sus, sus-(elpa*sus)-(elps*sus), elps], elpc), doneAction:0);
osc = RLPF.ar(osc, LinLin.ar(env, 0,1,0,elpf)+10, elpr, mul: 1);
ReplaceOut.ar(bus, osc)}).add;