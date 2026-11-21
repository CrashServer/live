SynthDef.new(\SLPF,
{|bus, spf, spr, spfslide, spfend, spf_, spf_d, spflfo, spflfomul, spflfoadd, spflfophase, spr_, spr_d, sprlfo, sprlfomul, sprlfoadd, sprlfophase, spfslide_, spfslide_d, spfslidelfo, spfslidelfomul, spfslidelfoadd, spfslidelfophase, spfend_, spfend_d, spfendlfo, spfendlfomul, spfendlfoadd, spfendlfophase, sus|
var osc,spfenv;
osc = In.ar(bus, 2);
spf = if(spf_<=0, spf, Line.kr(spf, spf_, sus*spf_d));
spf = if(spflfo<=0, spf, spf * SinOsc.kr(spflfo, spflfophase, spflfomul, spflfoadd));
spr = if(spr_<=0, spr, Line.kr(spr, spr_, sus*spr_d));
spr = if(sprlfo<=0, spr, spr * SinOsc.kr(sprlfo, sprlfophase, sprlfomul, sprlfoadd));
spfslide = if(spfslide_<=0, spfslide, Line.kr(spfslide, spfslide_, sus*spfslide_d));
spfslide = if(spfslidelfo<=0, spfslide, spfslide * SinOsc.kr(spfslidelfo, spfslidelfophase, spfslidelfomul, spfslidelfoadd));
spfend = if(spfend_<=0, spfend, Line.kr(spfend, spfend_, sus*spfend_d));
spfend = if(spfendlfo<=0, spfend, spfend * SinOsc.kr(spfendlfo, spfendlfophase, spfendlfomul, spfendlfoadd));
spfenv = EnvGen.ar(Env.new([spf, spfend], [spfslide]));
osc = RLPF.ar(osc, spfenv, spr);
ReplaceOut.ar(bus, osc)}).add;