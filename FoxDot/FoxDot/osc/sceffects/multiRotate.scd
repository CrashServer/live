SynthDef.new(\multiRotate,
{|bus, rotate, rotwidth, rotate_, rotate_d, rotatelfo, rotatelfomul, rotatelfoadd, rotwidth_, rotwidth_d, rotwidthlfo, rotwidthlfomul, rotwidthlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
rotate = if(rotate_<=0, rotate, Line.kr(rotate, rotate_, sus*rotate_d));
rotate = if(rotatelfo<=0, rotate, rotate * SinOsc.kr(rotatelfo, 0, rotatelfomul, rotatelfoadd));
rotwidth = if(rotwidth_<=0, rotwidth, Line.kr(rotwidth, rotwidth_, sus*rotwidth_d));
rotwidth = if(rotwidthlfo<=0, rotwidth, rotwidth * SinOsc.kr(rotwidthlfo, 0, rotwidthlfomul, rotwidthlfoadd));
osc = PanAz.ar(4, Mix.ar(osc), LFSaw.kr(rotate / beat_dur), 1, rotwidth).clump(2).collect({|pair| pair.sum});
ReplaceOut.ar(bus, osc)}).add;