SynthDef.new(\volume,
{|bus, vol, vol_, sus|
var osc;
osc = In.ar(bus, 2);
vol = vol+Line.kr(0, vol_, sus);
osc = osc*vol;
ReplaceOut.ar(bus, osc)}).add;