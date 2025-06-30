SynthDef.new(\trimLength,
{|bus, cut, sus, cut_, cut_d, cutlfo, cutlfomul, cutlfoadd|
var osc;
osc = In.ar(bus, 2);
cut = if(cut_<=0, cut, Line.kr(cut, cut_, sus*cut_d));
cut = if(cutlfo<=0, cut, cut * SinOsc.kr(cutlfo, 0, cutlfomul, cutlfoadd));
osc = osc * EnvGen.ar(Env(levels: [1,1,0.01], curve: 'linear', times: [sus * cut, 0.01]));
ReplaceOut.ar(bus, osc)}).add;