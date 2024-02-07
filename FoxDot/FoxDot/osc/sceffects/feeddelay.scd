SynthDef.new(\feeddelay,
{|bus, feed, feedfreq, feed_, feedfreq_, sus|
var osc,out;
osc = In.ar(bus, 2);
feed = feed+Line.kr(0, feed_, sus);
feedfreq = feedfreq+Line.kr(0, feedfreq_, sus);
out = osc + Fb({		arg feedback;		osc = CombN.ar(HPF.ar(feedback*feed, feedfreq) + osc, 0.5, 0.25).tanh;	},0.5,0.125);
ReplaceOut.ar(bus, osc)}).add;