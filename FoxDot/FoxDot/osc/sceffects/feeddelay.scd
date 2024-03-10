SynthDef.new(\feeddelay,
{|bus, feed, feedfreq, feed_, feed_d, feedfreq_, feedfreq_d, sus|
var osc,out;
osc = In.ar(bus, 2);
feed = if(feed_<=0, feed, Line.kr(feed, feed_, sus*feed_d));
feedfreq = if(feedfreq_<=0, feedfreq, Line.kr(feedfreq, feedfreq_, sus*feedfreq_d));
out = osc + Fb({		arg feedback;		osc = CombN.ar(HPF.ar(feedback*feed, feedfreq) + osc, 0.5, 0.25).tanh;	},0.5,0.125);
ReplaceOut.ar(bus, osc)}).add;