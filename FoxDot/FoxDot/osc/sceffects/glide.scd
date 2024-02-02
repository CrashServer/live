SynthDef.new(\glide,
{|bus, glide, glidedur|
var osc;
osc = In.kr(bus, 1);
osc = Line.kr(start: (osc * glide).clip(-50,22000), end: osc, dur: glidedur);
ReplaceOut.kr(bus, osc)}).add;