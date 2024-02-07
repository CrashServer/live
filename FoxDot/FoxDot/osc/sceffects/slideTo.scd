SynthDef.new(\slideTo,
{|bus, slide, sus, slidedelay, slide_, slidedelay_|
var osc;
osc = In.kr(bus, 1);
slide = slide+Line.kr(0, slide_, sus);
slidedelay = slidedelay+Line.kr(0, slidedelay_, sus);
osc = osc * EnvGen.ar(Env([1, 1, slide + 1], [sus*slidedelay, sus*(1-slidedelay)]));
ReplaceOut.kr(bus, osc)}).add;