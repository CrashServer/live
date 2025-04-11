SynthDef.new(\output,
{|bus, output, output_, output_d, outputlfo, sus|
var osc;
osc = In.ar(bus, 2);
output = if(output_<=0, output, Line.kr(output, output_, sus*output_d));
output = if(outputlfo<=0, output, output * SinOsc.kr(outputlfo, 0, 1, 1));
Out.ar(output, osc);
ReplaceOut.ar(bus, osc)}).add;