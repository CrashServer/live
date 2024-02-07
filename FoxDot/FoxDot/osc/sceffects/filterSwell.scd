SynthDef.new(\filterSwell,
{|bus, swell, sus, hpr, swell_, hpr_|
var osc,env;
osc = In.ar(bus, 2);
swell = swell+Line.kr(0, swell_, sus);
hpr = hpr+Line.kr(0, hpr_, sus);
env = EnvGen.kr(Env([0,1,0], times:[(sus*0.25), (sus*0.25)], curve:\sin));
osc = RHPF.ar(osc, env * swell * 2000, hpr);
ReplaceOut.ar(bus, osc)}).add;