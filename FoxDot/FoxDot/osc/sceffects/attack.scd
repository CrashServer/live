SynthDef.new(\attack,
{|bus, a, sus, ac|
var osc,env;
osc = In.ar(bus, 2);

env = EnvGen.ar(Env.new(levels: [0,1,1], times:[a*sus, sus - a*sus], curve:[ac,0]));
osc = osc*env;
ReplaceOut.ar(bus, osc)}).add;