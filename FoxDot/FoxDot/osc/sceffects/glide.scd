SynthDef.new(\glide,
{|bus, glide, glidedur, glide_, glide_d, glidedur_, glidedur_d, sus|
var osc;
osc = In.kr(bus, 1);
glide = if(glide_<=0, glide, Line.kr(glide, glide_, sus*glide_d));
glidedur = if(glidedur_<=0, glidedur, Line.kr(glidedur, glidedur_, sus*glidedur_d));
osc = Line.kr(start: (osc * glide).clip(-50,22000), end: osc, dur: glidedur);
ReplaceOut.kr(bus, osc)}).add;