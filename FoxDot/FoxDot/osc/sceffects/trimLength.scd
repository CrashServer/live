SynthDef.new(\trimLength,
{|bus, cut, sus, cut_|
var osc;
osc = In.ar(bus, 2);
cut = cut+Line.kr(0, cut_, sus);
osc = osc * EnvGen.ar(Env(levels: [1,1,0.01], curve: 'linear', times: [sus * cut, 0.01]));
ReplaceOut.ar(bus, osc)}).add;