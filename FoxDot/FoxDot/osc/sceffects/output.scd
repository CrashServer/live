SynthDef.new(\output,
{|bus, output, output_, output_d, outputlfo, outputlfomul, outputlfoadd, outputlfophase, sus|
var osc;
osc = In.ar(bus, 2);
output = if(output_<=0, output, Line.kr(output, output_, sus*output_d));
output = if(outputlfo<=0, output, output * SinOsc.kr(outputlfo, outputlfophase, outputlfomul, outputlfoadd));
Out.ar(output, osc);
ReplaceOut.ar(bus, osc)}).add;