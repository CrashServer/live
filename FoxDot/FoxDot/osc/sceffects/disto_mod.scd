SynthDef.new(\disto_mod,
{|bus, disto, smooth, distomix, disto_, disto_d, distolfo, distolfomul, distolfoadd, smooth_, smooth_d, smoothlfo, smoothlfomul, smoothlfoadd, distomix_, distomix_d, distomixlfo, distomixlfomul, distomixlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
disto = if(disto_<=0, disto, Line.kr(disto, disto_, sus*disto_d));
disto = if(distolfo<=0, disto, disto * SinOsc.kr(distolfo, 0, distolfomul, distolfoadd));
smooth = if(smooth_<=0, smooth, Line.kr(smooth, smooth_, sus*smooth_d));
smooth = if(smoothlfo<=0, smooth, smooth * SinOsc.kr(smoothlfo, 0, smoothlfomul, smoothlfoadd));
distomix = if(distomix_<=0, distomix, Line.kr(distomix, distomix_, sus*distomix_d));
distomix = if(distomixlfo<=0, distomix, distomix * SinOsc.kr(distomixlfo, 0, distomixlfomul, distomixlfoadd));
osc = LinXFade2.ar(CrossoverDistortion.ar(osc, amp:0.5*disto, smooth:smooth),  osc, 1-distomix);
ReplaceOut.ar(bus, osc)}).add;