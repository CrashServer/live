SynthDef.new(\lowPassFilter,
{|bus, lpf, lpr, lpf_, lpr_, sus|
var osc;
osc = In.ar(bus, 2);
lpf = lpf+Line.kr(0, lpf_, sus);
lpr = lpr+Line.kr(0, lpr_, sus);
osc = RLPF.ar(osc, lpf, lpr);
ReplaceOut.ar(bus, osc)}).add;