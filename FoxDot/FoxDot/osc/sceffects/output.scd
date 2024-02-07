SynthDef.new(\output,
{|bus, output, output_, sus|
var osc;
osc = In.ar(bus, 2);
output = output+Line.kr(0, output_, sus);
Out.ar(output, osc);
ReplaceOut.ar(bus, osc)}).add;