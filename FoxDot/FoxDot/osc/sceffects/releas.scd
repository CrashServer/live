SynthDef.new(\releas,
{|bus, r, sus, rc|
var osc,env;
osc = In.ar(bus, 2);

env = EnvGen.ar(Env.new(levels: [1,0,0], times:[r*sus, sus - r*sus], curve:[rc,0]));
osc = osc*env;
ReplaceOut.ar(bus, osc)}).add;