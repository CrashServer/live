SynthDef.new(\ring_modulation,
{|bus, ring, ringl, ringh, ring_, ring_d, ringlfo, ringlfomul, ringlfoadd, ringlfophase, ringl_, ringl_d, ringllfo, ringllfomul, ringllfoadd, ringllfophase, ringh_, ringh_d, ringhlfo, ringhlfomul, ringhlfoadd, ringhlfophase, sus|
var osc,mod;
osc = In.kr(bus, 1);
ring = if(ring_<=0, ring, Line.kr(ring, ring_, sus*ring_d));
ring = if(ringlfo<=0, ring, ring * SinOsc.kr(ringlfo, ringlfophase, ringlfomul, ringlfoadd));
ringl = if(ringl_<=0, ringl, Line.kr(ringl, ringl_, sus*ringl_d));
ringl = if(ringllfo<=0, ringl, ringl * SinOsc.kr(ringllfo, ringllfophase, ringllfomul, ringllfoadd));
ringh = if(ringh_<=0, ringh, Line.kr(ringh, ringh_, sus*ringh_d));
ringh = if(ringhlfo<=0, ringh, ringh * SinOsc.kr(ringhlfo, ringhlfophase, ringhlfomul, ringhlfoadd));
mod = ring * SinOsc.ar(Clip.kr(XLine.kr(ringl, ringl + ringh), 20, 20000));
osc = ring1(osc, mod);
ReplaceOut.kr(bus, osc)}).add;