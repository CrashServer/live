SynthDef.new(\adsr,
{|bus, a, r, sus, ac, rc|
var osc,env;
osc = In.ar(bus, 2);
env = EnvGen.ar(Env.new(levels: [0,1,1,0], times:[a*sus, max((a*sus + r*sus), sus - (a*sus + r*sus)), r*sus], curve:[ac,0,rc]));
osc = osc*env;
ReplaceOut.ar(bus, osc)}).add;