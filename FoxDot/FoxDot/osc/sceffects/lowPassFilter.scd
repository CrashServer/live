SynthDef.new(\lowPassFilter,
{|bus, lpf, lpr, lpf_, lpf_d, lpflfo, lpr_, lpr_d, lprlfo, sus|
var osc;
osc = In.ar(bus, 2);
lpf = if(lpf_<=0, lpf, Line.kr(lpf, lpf_, sus*lpf_d));
lpf = if(lpflfo<=0, lpf, lpf * SinOsc.kr(lpflfo, 0, 1, 1));
lpr = if(lpr_<=0, lpr, Line.kr(lpr, lpr_, sus*lpr_d));
lpr = if(lprlfo<=0, lpr, lpr * SinOsc.kr(lprlfo, 0, 1, 1));
osc = RLPF.ar(osc, lpf, lpr);
ReplaceOut.ar(bus, osc)}).add;