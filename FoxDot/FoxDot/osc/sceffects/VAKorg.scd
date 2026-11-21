SynthDef.new(\VAKorg,
{|bus, vakorg, vakorgr, vakorgd, vakorgt, vakorgc, vakorg_, vakorg_d, vakorglfo, vakorglfomul, vakorglfoadd, vakorglfophase, vakorgr_, vakorgr_d, vakorgrlfo, vakorgrlfomul, vakorgrlfoadd, vakorgrlfophase, vakorgd_, vakorgd_d, vakorgdlfo, vakorgdlfomul, vakorgdlfoadd, vakorgdlfophase, vakorgt_, vakorgt_d, vakorgtlfo, vakorgtlfomul, vakorgtlfoadd, vakorgtlfophase, vakorgc_, vakorgc_d, vakorgclfo, vakorgclfomul, vakorgclfoadd, vakorgclfophase, sus|
var osc;
osc = In.ar(bus, 2);
vakorg = if(vakorg_<=0, vakorg, Line.kr(vakorg, vakorg_, sus*vakorg_d));
vakorg = if(vakorglfo<=0, vakorg, vakorg * SinOsc.kr(vakorglfo, vakorglfophase, vakorglfomul, vakorglfoadd));
vakorgr = if(vakorgr_<=0, vakorgr, Line.kr(vakorgr, vakorgr_, sus*vakorgr_d));
vakorgr = if(vakorgrlfo<=0, vakorgr, vakorgr * SinOsc.kr(vakorgrlfo, vakorgrlfophase, vakorgrlfomul, vakorgrlfoadd));
vakorgd = if(vakorgd_<=0, vakorgd, Line.kr(vakorgd, vakorgd_, sus*vakorgd_d));
vakorgd = if(vakorgdlfo<=0, vakorgd, vakorgd * SinOsc.kr(vakorgdlfo, vakorgdlfophase, vakorgdlfomul, vakorgdlfoadd));
vakorgt = if(vakorgt_<=0, vakorgt, Line.kr(vakorgt, vakorgt_, sus*vakorgt_d));
vakorgt = if(vakorgtlfo<=0, vakorgt, vakorgt * SinOsc.kr(vakorgtlfo, vakorgtlfophase, vakorgtlfomul, vakorgtlfoadd));
vakorgc = if(vakorgc_<=0, vakorgc, Line.kr(vakorgc, vakorgc_, sus*vakorgc_d));
vakorgc = if(vakorgclfo<=0, vakorgc, vakorgc * SinOsc.kr(vakorgclfo, vakorgclfophase, vakorgclfomul, vakorgclfoadd));
osc = VAKorg35.ar(osc*0.4, vakorg, vakorgr, vakorgd,vakorgt);
osc = Compander.ar(osc, osc, vakorgc, 1, 0.1, 0.01, 0.1 );
ReplaceOut.ar(bus, osc)}).add;