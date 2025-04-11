SynthDef.new(\slideTo,
{|bus, slide, sus, slidedelay, slide_, slide_d, slidelfo, slidelfomul, slidelfoadd, slidedelay_, slidedelay_d, slidedelaylfo, slidedelaylfomul, slidedelaylfoadd|
var osc;
osc = In.kr(bus, 1);
slide = if(slide_<=0, slide, Line.kr(slide, slide_, sus*slide_d));
slide = if(slidelfo<=0, slide, slide * SinOsc.kr(slidelfo, 0, slidelfomul, slidelfoadd));
slidedelay = if(slidedelay_<=0, slidedelay, Line.kr(slidedelay, slidedelay_, sus*slidedelay_d));
slidedelay = if(slidedelaylfo<=0, slidedelay, slidedelay * SinOsc.kr(slidedelaylfo, 0, slidedelaylfomul, slidedelaylfoadd));
osc = osc * EnvGen.ar(Env([1, 1, slide + 1], [sus*slidedelay, sus*(1-slidedelay)]));
ReplaceOut.kr(bus, osc)}).add;