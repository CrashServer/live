SynthDef.new(\slideFrom,
{|bus, slidefrom, sus, slidedelay, slidefrom_, slidedelay_|
var osc;
osc = In.kr(bus, 1);
slidefrom = slidefrom+Line.kr(0, slidefrom_, sus);
slidedelay = slidedelay+Line.kr(0, slidedelay_, sus);
osc = osc * EnvGen.ar(Env([slidefrom + 1, slidefrom + 1, 1], [sus*slidedelay, sus*(1-slidedelay)]));
ReplaceOut.kr(bus, osc)}).add;