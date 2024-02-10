SynthDef.new(\lowPassFilter,
{|bus, lpf, lpr, lpf_, lpf_d, lpr_, lpr_d, sus|
var osc;
osc = In.ar(bus, 2);
lpf = if(lpf_<=0, lpf, Line.kr(lpf, lpf_, sus*lpf_d));
lpr = if(lpr_<=0, lpr, Line.kr(lpr, lpr_, sus*lpr_d));
osc = RLPF.ar(osc, lpf, lpr);
ReplaceOut.ar(bus, osc)}).add;