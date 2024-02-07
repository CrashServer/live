SynthDef.new(\ring_modulation,
{|bus, ring, ringl, ringh, ring_, ringl_, ringh_, sus|
var osc,mod;
osc = In.kr(bus, 1);
ring = ring+Line.kr(0, ring_, sus);
ringl = ringl+Line.kr(0, ringl_, sus);
ringh = ringh+Line.kr(0, ringh_, sus);
mod = ring * SinOsc.ar(Clip.kr(XLine.kr(ringl, ringl + ringh), 20, 20000));
osc = ring1(osc, mod);
ReplaceOut.kr(bus, osc)}).add;