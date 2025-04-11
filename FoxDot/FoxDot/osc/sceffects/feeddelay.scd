SynthDef.new(\feeddelay,
{|bus, feed, feedfreq, feed_, feed_d, feedlfo, feedlfomul, feedlfoadd, feedfreq_, feedfreq_d, feedfreqlfo, feedfreqlfomul, feedfreqlfoadd, sus|
var osc,out;
osc = In.ar(bus, 2);
feed = if(feed_<=0, feed, Line.kr(feed, feed_, sus*feed_d));
feed = if(feedlfo<=0, feed, feed * SinOsc.kr(feedlfo, 0, feedlfomul, feedlfoadd));
feedfreq = if(feedfreq_<=0, feedfreq, Line.kr(feedfreq, feedfreq_, sus*feedfreq_d));
feedfreq = if(feedfreqlfo<=0, feedfreq, feedfreq * SinOsc.kr(feedfreqlfo, 0, feedfreqlfomul, feedfreqlfoadd));
out = osc + Fb({		arg feedback;		osc = CombN.ar(HPF.ar(feedback*feed, feedfreq) + osc, 0.5, 0.25).tanh;	},0.5,0.125);
ReplaceOut.ar(bus, osc)}).add;