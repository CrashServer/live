SynthDef.new(\attack,
{|bus, a, sus, ac, a_, a_d, alfo, alfomul, alfoadd, ac_, ac_d, aclfo, aclfomul, aclfoadd|
var osc,env;
osc = In.ar(bus, 2);
a = if(a_<=0, a, Line.kr(a, a_, sus*a_d));
a = if(alfo<=0, a, a * SinOsc.kr(alfo, 0, alfomul, alfoadd));
ac = if(ac_<=0, ac, Line.kr(ac, ac_, sus*ac_d));
ac = if(aclfo<=0, ac, ac * SinOsc.kr(aclfo, 0, aclfomul, aclfoadd));
env = EnvGen.ar(Env.new(levels: [0,1,1], times:[a*sus, sus - a*sus], curve:[ac,0]));
osc = osc*env;
ReplaceOut.ar(bus, osc)}).add;