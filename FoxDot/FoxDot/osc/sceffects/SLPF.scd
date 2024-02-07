SynthDef.new(\SLPF,
{|bus, spf, spr, spfslide, spfend, spf_, spr_, spfslide_, spfend_, sus|
var osc,spfenv;
osc = In.ar(bus, 2);
spf = spf+Line.kr(0, spf_, sus);
spr = spr+Line.kr(0, spr_, sus);
spfslide = spfslide+Line.kr(0, spfslide_, sus);
spfend = spfend+Line.kr(0, spfend_, sus);
spfenv = EnvGen.ar(Env.new([spf, spfend], [spfslide]));
osc = RLPF.ar(osc, spfenv, spr);
ReplaceOut.ar(bus, osc)}).add;