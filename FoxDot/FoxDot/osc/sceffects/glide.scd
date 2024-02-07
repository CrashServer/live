SynthDef.new(\glide,
{|bus, glide, glidedur, glide_, glidedur_, sus|
var osc;
osc = In.kr(bus, 1);
glide = glide+Line.kr(0, glide_, sus);
glidedur = glidedur+Line.kr(0, glidedur_, sus);
osc = Line.kr(start: (osc * glide).clip(-50,22000), end: osc, dur: glidedur);
ReplaceOut.kr(bus, osc)}).add;