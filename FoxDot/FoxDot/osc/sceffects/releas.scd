SynthDef.new(\releas,
{|bus, r, sus, rc, r_, r_d, rlfo, rc_, rc_d, rclfo|
var osc,env;
osc = In.ar(bus, 2);
r = if(r_<=0, r, Line.kr(r, r_, sus*r_d));
r = if(rlfo<=0, r, r * SinOsc.kr(rlfo, 0, 1, 1));
rc = if(rc_<=0, rc, Line.kr(rc, rc_, sus*rc_d));
rc = if(rclfo<=0, rc, rc * SinOsc.kr(rclfo, 0, 1, 1));
env = EnvGen.ar(Env.new(levels: [1,0,0], times:[r*sus, sus - r*sus], curve:[rc,0]));
osc = osc*env;
ReplaceOut.ar(bus, osc)}).add;