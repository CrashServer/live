SynthDef.new(\dirt_krush,
{|bus, krush, kutoff, krushmix, krush_, krush_d, krushlfo, kutoff_, kutoff_d, kutofflfo, krushmix_, krushmix_d, krushmixlfo, sus|
var osc,signal,freq;
osc = In.ar(bus, 2);
krush = if(krush_<=0, krush, Line.kr(krush, krush_, sus*krush_d));
krush = if(krushlfo<=0, krush, krush * SinOsc.kr(krushlfo, 0, 1, 1));
kutoff = if(kutoff_<=0, kutoff, Line.kr(kutoff, kutoff_, sus*kutoff_d));
kutoff = if(kutofflfo<=0, kutoff, kutoff * SinOsc.kr(kutofflfo, 0, 1, 1));
krushmix = if(krushmix_<=0, krushmix, Line.kr(krushmix, krushmix_, sus*krushmix_d));
krushmix = if(krushmixlfo<=0, krushmix, krushmix * SinOsc.kr(krushmixlfo, 0, 1, 1));
freq = Select.kr(kutoff > 0, [DC.kr(4000), kutoff]);
signal = (osc.squared + (krush * osc)) / (osc.squared + (osc.abs * (krush-1.0)) + 1.0);
signal = RLPF.ar(signal, clip(freq, 20, 10000), 1);
osc = SelectX.ar(krushmix, [osc, signal]);
ReplaceOut.ar(bus, osc)}).add;