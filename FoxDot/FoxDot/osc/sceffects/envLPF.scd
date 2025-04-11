SynthDef.new(\envLPF,
{|bus, elpf, elpr, elpa, elps, elpc, sus, elpf_, elpf_d, elpflfo, elpr_, elpr_d, elprlfo, elpa_, elpa_d, elpalfo, elps_, elps_d, elpslfo, elpc_, elpc_d, elpclfo|
var osc,env;
osc = In.ar(bus, 2);
elpf = if(elpf_<=0, elpf, Line.kr(elpf, elpf_, sus*elpf_d));
elpf = if(elpflfo<=0, elpf, elpf * SinOsc.kr(elpflfo, 0, 1, 1));
elpr = if(elpr_<=0, elpr, Line.kr(elpr, elpr_, sus*elpr_d));
elpr = if(elprlfo<=0, elpr, elpr * SinOsc.kr(elprlfo, 0, 1, 1));
elpa = if(elpa_<=0, elpa, Line.kr(elpa, elpa_, sus*elpa_d));
elpa = if(elpalfo<=0, elpa, elpa * SinOsc.kr(elpalfo, 0, 1, 1));
elps = if(elps_<=0, elps, Line.kr(elps, elps_, sus*elps_d));
elps = if(elpslfo<=0, elps, elps * SinOsc.kr(elpslfo, 0, 1, 1));
elpc = if(elpc_<=0, elpc, Line.kr(elpc, elpc_, sus*elpc_d));
elpc = if(elpclfo<=0, elpc, elpc * SinOsc.kr(elpclfo, 0, 1, 1));
env = EnvGen.ar(Env.new([0.01, 1, 1, 0.01], [elpa*sus, sus-(elpa*sus)-(elps*sus), elps], elpc), doneAction:0);
osc = RLPF.ar(osc, LinLin.ar(env, 0,1,0,elpf)+10, elpr, mul: 1);
ReplaceOut.ar(bus, osc)}).add;