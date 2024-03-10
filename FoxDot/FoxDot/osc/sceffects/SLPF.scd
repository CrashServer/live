SynthDef.new(\SLPF,
{|bus, spf, spr, spfslide, spfend, spf_, spf_d, spr_, spr_d, spfslide_, spfslide_d, spfend_, spfend_d, sus|
var osc,spfenv;
osc = In.ar(bus, 2);
spf = if(spf_<=0, spf, Line.kr(spf, spf_, sus*spf_d));
spr = if(spr_<=0, spr, Line.kr(spr, spr_, sus*spr_d));
spfslide = if(spfslide_<=0, spfslide, Line.kr(spfslide, spfslide_, sus*spfslide_d));
spfend = if(spfend_<=0, spfend, Line.kr(spfend, spfend_, sus*spfend_d));
spfenv = EnvGen.ar(Env.new([spf, spfend], [spfslide]));
osc = RLPF.ar(osc, spfenv, spr);
ReplaceOut.ar(bus, osc)}).add;