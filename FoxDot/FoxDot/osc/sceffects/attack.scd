SynthDef.new(\attack,
{|bus, a, sus, ac, a_, a_d, ac_, ac_d|
var osc,env;
osc = In.ar(bus, 2);
a = if(a_<=0, a, Line.kr(a, a_, sus*a_d));
ac = if(ac_<=0, ac, Line.kr(ac, ac_, sus*ac_d));
env = EnvGen.ar(Env.new(levels: [0,1,1], times:[a*sus, sus - a*sus], curve:[ac,0]));
osc = osc*env;
ReplaceOut.ar(bus, osc)}).add;