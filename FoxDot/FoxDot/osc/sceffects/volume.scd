SynthDef.new(\volume,
{|bus, vol, vol_, vol_d, vollfo, vollfomul, vollfoadd, sus|
var osc;
osc = In.ar(bus, 2);
vol = if(vol_<=0, vol, Line.kr(vol, vol_, sus*vol_d));
vol = if(vollfo<=0, vol, vol * SinOsc.kr(vollfo, 0, vollfomul, vollfoadd));
osc = osc*vol;
ReplaceOut.ar(bus, osc)}).add;