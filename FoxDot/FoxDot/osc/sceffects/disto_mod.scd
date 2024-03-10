SynthDef.new(\disto_mod,
{|bus, disto, smooth, distomix, disto_, disto_d, smooth_, smooth_d, distomix_, distomix_d, sus|
var osc;
osc = In.ar(bus, 2);
disto = if(disto_<=0, disto, Line.kr(disto, disto_, sus*disto_d));
smooth = if(smooth_<=0, smooth, Line.kr(smooth, smooth_, sus*smooth_d));
distomix = if(distomix_<=0, distomix, Line.kr(distomix, distomix_, sus*distomix_d));
osc = LinXFade2.ar(CrossoverDistortion.ar(osc, amp:0.5*disto, smooth:smooth),  osc, 1-distomix);
ReplaceOut.ar(bus, osc)}).add;