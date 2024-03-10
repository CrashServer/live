SynthDef.new(\dubdelay,
{|bus, dubd, dublen, dubwidth, dubfeed, dubd_, dubd_d, dublen_, dublen_d, dubwidth_, dubwidth_d, dubfeed_, dubfeed_d, sus|
var osc,dry;
osc = In.ar(bus, 2);
dubd = if(dubd_<=0, dubd, Line.kr(dubd, dubd_, sus*dubd_d));
dublen = if(dublen_<=0, dublen, Line.kr(dublen, dublen_, sus*dublen_d));
dubwidth = if(dubwidth_<=0, dubwidth, Line.kr(dubwidth, dubwidth_, sus*dubwidth_d));
dubfeed = if(dubfeed_<=0, dubfeed, Line.kr(dubfeed, dubfeed_, sus*dubfeed_d));
dry = osc;
osc = osc + Fb({ |feedback| var left, right; var magic = LeakDC.ar(feedback*dubfeed + osc); magic = HPF.ar(magic, 400); magic = LPF.ar(magic, 5000); magic = magic.tanh; #left, right = magic; magic = [DelayC.ar(left, 1, LFNoise2.ar(12).range(0,dubwidth)), DelayC.ar(right, 1, LFNoise2.ar(12).range(dubwidth,0))].reverse;	},dublen);
osc = SelectX.ar(dubd, [dry, osc]);
ReplaceOut.ar(bus, osc)}).add;