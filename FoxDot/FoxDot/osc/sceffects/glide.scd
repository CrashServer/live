SynthDef.new(\glide,
{|bus, glide, glidedur, glide_, glide_d, glidelfo, glidedur_, glidedur_d, glidedurlfo, sus|
var osc;
osc = In.kr(bus, 1);
glide = if(glide_<=0, glide, Line.kr(glide, glide_, sus*glide_d));
glide = if(glidelfo<=0, glide, glide * SinOsc.kr(glidelfo, 0, 1, 1));
glidedur = if(glidedur_<=0, glidedur, Line.kr(glidedur, glidedur_, sus*glidedur_d));
glidedur = if(glidedurlfo<=0, glidedur, glidedur * SinOsc.kr(glidedurlfo, 0, 1, 1));
osc = Line.kr(start: (osc * glide).clip(-50,22000), end: osc, dur: glidedur);
ReplaceOut.kr(bus, osc)}).add;