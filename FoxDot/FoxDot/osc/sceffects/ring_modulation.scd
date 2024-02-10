SynthDef.new(\ring_modulation,
{|bus, ring, ringl, ringh, ring_, ring_d, ringl_, ringl_d, ringh_, ringh_d, sus|
var osc,mod;
osc = In.kr(bus, 1);
ring = if(ring_<=0, ring, Line.kr(ring, ring_, sus*ring_d));
ringl = if(ringl_<=0, ringl, Line.kr(ringl, ringl_, sus*ringl_d));
ringh = if(ringh_<=0, ringh, Line.kr(ringh, ringh_, sus*ringh_d));
mod = ring * SinOsc.ar(Clip.kr(XLine.kr(ringl, ringl + ringh), 20, 20000));
osc = ring1(osc, mod);
ReplaceOut.kr(bus, osc)}).add;