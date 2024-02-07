SynthDef.new(\disto_mod,
{|bus, disto, smooth, distomix, disto_, smooth_, distomix_, sus|
var osc;
osc = In.ar(bus, 2);
disto = disto+Line.kr(0, disto_, sus);
smooth = smooth+Line.kr(0, smooth_, sus);
distomix = distomix+Line.kr(0, distomix_, sus);
osc = LinXFade2.ar(CrossoverDistortion.ar(osc, amp:0.5*disto, smooth:smooth),  osc, 1-distomix);
ReplaceOut.ar(bus, osc)}).add;