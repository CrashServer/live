SynthDef.new(\output,
{|bus, output, output_, output_d, sus|
var osc;
osc = In.ar(bus, 2);
output = if(output_<=0, output, Line.kr(output, output_, sus*output_d));
Out.ar(output, osc);
ReplaceOut.ar(bus, osc)}).add;