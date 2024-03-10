SynthDef.new(\filterSwell,
{|bus, swell, sus, hpr, swell_, swell_d, hpr_, hpr_d|
var osc,env;
osc = In.ar(bus, 2);
swell = if(swell_<=0, swell, Line.kr(swell, swell_, sus*swell_d));
hpr = if(hpr_<=0, hpr, Line.kr(hpr, hpr_, sus*hpr_d));
env = EnvGen.kr(Env([0,1,0], times:[(sus*0.25), (sus*0.25)], curve:\sin));
osc = RHPF.ar(osc, env * swell * 2000, hpr);
ReplaceOut.ar(bus, osc)}).add;