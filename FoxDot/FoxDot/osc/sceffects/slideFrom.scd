SynthDef.new(\slideFrom,
{|bus, slidefrom, sus, slidedelay, slidefrom_, slidefrom_d, slidedelay_, slidedelay_d|
var osc;
osc = In.kr(bus, 1);
slidefrom = if(slidefrom_<=0, slidefrom, Line.kr(slidefrom, slidefrom_, sus*slidefrom_d));
slidedelay = if(slidedelay_<=0, slidedelay, Line.kr(slidedelay, slidedelay_, sus*slidedelay_d));
osc = osc * EnvGen.ar(Env([slidefrom + 1, slidefrom + 1, 1], [sus*slidedelay, sus*(1-slidedelay)]));
ReplaceOut.kr(bus, osc)}).add;