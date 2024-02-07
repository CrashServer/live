SynthDef.new(\dirt_krush,
{|bus, krush, kutoff, krushmix, krush_, kutoff_, krushmix_, sus|
var osc,signal,freq;
osc = In.ar(bus, 2);
krush = krush+Line.kr(0, krush_, sus);
kutoff = kutoff+Line.kr(0, kutoff_, sus);
krushmix = krushmix+Line.kr(0, krushmix_, sus);
freq = Select.kr(kutoff > 0, [DC.kr(4000), kutoff]);
signal = (osc.squared + (krush * osc)) / (osc.squared + (osc.abs * (krush-1.0)) + 1.0);
signal = RLPF.ar(signal, clip(freq, 20, 10000), 1);
osc = SelectX.ar(krushmix, [osc, signal]);
ReplaceOut.ar(bus, osc)}).add;