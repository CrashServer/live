SynthDef.new(\slideTo,
{|bus, slide, sus, slidedelay, slide_, slide_d, slidedelay_, slidedelay_d|
var osc;
osc = In.kr(bus, 1);
slide = if(slide_<=0, slide, Line.kr(slide, slide_, sus*slide_d));
slidedelay = if(slidedelay_<=0, slidedelay, Line.kr(slidedelay, slidedelay_, sus*slidedelay_d));
osc = osc * EnvGen.ar(Env([1, 1, slide + 1], [sus*slidedelay, sus*(1-slidedelay)]));
ReplaceOut.kr(bus, osc)}).add;