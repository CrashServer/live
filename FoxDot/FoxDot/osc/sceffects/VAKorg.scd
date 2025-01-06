SynthDef.new(\VAKorg,
{|bus, vakorg, vakorgr, vakorgd, vakorgt, vakorg_, vakorg_d, vakorgr_, vakorgr_d, vakorgd_, vakorgd_d, vakorgt_, vakorgt_d, sus|
var osc;
osc = In.ar(bus, 2);
vakorg = if(vakorg_<=0, vakorg, Line.kr(vakorg, vakorg_, sus*vakorg_d));
vakorgr = if(vakorgr_<=0, vakorgr, Line.kr(vakorgr, vakorgr_, sus*vakorgr_d));
vakorgd = if(vakorgd_<=0, vakorgd, Line.kr(vakorgd, vakorgd_, sus*vakorgd_d));
vakorgt = if(vakorgt_<=0, vakorgt, Line.kr(vakorgt, vakorgt_, sus*vakorgt_d));
osc = VAKorg35.ar(osc*0.4, vakorg, vakorgr, vakorgd,vakorgt);
ReplaceOut.ar(bus, osc)}).add;