SynthDef.new(\slideFrom,
{|bus, slidefrom, sus, slidedelay, slidefrom_, slidefrom_d, slidefromlfo, slidefromlfomul, slidefromlfoadd, slidedelay_, slidedelay_d, slidedelaylfo, slidedelaylfomul, slidedelaylfoadd|
var osc;
osc = In.kr(bus, 1);
slidefrom = if(slidefrom_<=0, slidefrom, Line.kr(slidefrom, slidefrom_, sus*slidefrom_d));
slidefrom = if(slidefromlfo<=0, slidefrom, slidefrom * SinOsc.kr(slidefromlfo, 0, slidefromlfomul, slidefromlfoadd));
slidedelay = if(slidedelay_<=0, slidedelay, Line.kr(slidedelay, slidedelay_, sus*slidedelay_d));
slidedelay = if(slidedelaylfo<=0, slidedelay, slidedelay * SinOsc.kr(slidedelaylfo, 0, slidedelaylfomul, slidedelaylfoadd));
osc = osc * EnvGen.ar(Env([slidefrom + 1, slidefrom + 1, 1], [sus*slidedelay, sus*(1-slidedelay)]));
ReplaceOut.kr(bus, osc)}).add;