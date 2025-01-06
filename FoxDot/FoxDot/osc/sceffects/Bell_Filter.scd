SynthDef.new(\Bell_Filter,
{|bus, bell, bellf, bellq, bell_, bell_d, bellf_, bellf_d, bellq_, bellq_d, sus|
var osc;
osc = In.ar(bus, 2);
bell = if(bell_<=0, bell, Line.kr(bell, bell_, sus*bell_d));
bellf = if(bellf_<=0, bellf, Line.kr(bellf, bellf_, sus*bellf_d));
bellq = if(bellq_<=0, bellq, Line.kr(bellq, bellq_, sus*bellq_d));
osc = NonlinearFilter.ar(osc, freq: bellf, shape:0, gain:bell, q:bellq, saturation: 1);
ReplaceOut.ar(bus, osc)}).add;