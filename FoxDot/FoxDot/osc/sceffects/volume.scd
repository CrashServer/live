SynthDef.new(\volume,
{|bus, vol, vol_, vol_d, sus|
var osc;
osc = In.ar(bus, 2);
vol = if(vol_<=0, vol, Line.kr(vol, vol_, sus*vol_d));
osc = osc*vol;
ReplaceOut.ar(bus, osc)}).add;