SynthDef.new(\VAKorg,
{|bus, vakorg, vakorgr, vakorgd, vakorgt, vakorgc, vakorg_, vakorg_d, vakorgr_, vakorgr_d, vakorgd_, vakorgd_d, vakorgt_, vakorgt_d, vakorgc_, vakorgc_d, sus|
var osc;
osc = In.ar(bus, 2);
vakorg = if(vakorg_<=0, vakorg, Line.kr(vakorg, vakorg_, sus*vakorg_d));
vakorgr = if(vakorgr_<=0, vakorgr, Line.kr(vakorgr, vakorgr_, sus*vakorgr_d));
vakorgd = if(vakorgd_<=0, vakorgd, Line.kr(vakorgd, vakorgd_, sus*vakorgd_d));
vakorgt = if(vakorgt_<=0, vakorgt, Line.kr(vakorgt, vakorgt_, sus*vakorgt_d));
vakorgc = if(vakorgc_<=0, vakorgc, Line.kr(vakorgc, vakorgc_, sus*vakorgc_d));
osc = VAKorg35.ar(osc*0.4, vakorg, vakorgr, vakorgd,vakorgt);
osc = Compander.ar(osc, osc, vakorgc, 1, 0.1, 0.01, 0.1 );
ReplaceOut.ar(bus, osc)}).add;