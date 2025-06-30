SynthDef.new(\VAKorg,
{|bus, vakorg, vakorgr, vakorgd, vakorgt, vakorgc, vakorg_, vakorg_d, vakorglfo, vakorglfomul, vakorglfoadd, vakorgr_, vakorgr_d, vakorgrlfo, vakorgrlfomul, vakorgrlfoadd, vakorgd_, vakorgd_d, vakorgdlfo, vakorgdlfomul, vakorgdlfoadd, vakorgt_, vakorgt_d, vakorgtlfo, vakorgtlfomul, vakorgtlfoadd, vakorgc_, vakorgc_d, vakorgclfo, vakorgclfomul, vakorgclfoadd, sus|
var osc;
osc = In.ar(bus, 2);
vakorg = if(vakorg_<=0, vakorg, Line.kr(vakorg, vakorg_, sus*vakorg_d));
vakorg = if(vakorglfo<=0, vakorg, vakorg * SinOsc.kr(vakorglfo, 0, vakorglfomul, vakorglfoadd));
vakorgr = if(vakorgr_<=0, vakorgr, Line.kr(vakorgr, vakorgr_, sus*vakorgr_d));
vakorgr = if(vakorgrlfo<=0, vakorgr, vakorgr * SinOsc.kr(vakorgrlfo, 0, vakorgrlfomul, vakorgrlfoadd));
vakorgd = if(vakorgd_<=0, vakorgd, Line.kr(vakorgd, vakorgd_, sus*vakorgd_d));
vakorgd = if(vakorgdlfo<=0, vakorgd, vakorgd * SinOsc.kr(vakorgdlfo, 0, vakorgdlfomul, vakorgdlfoadd));
vakorgt = if(vakorgt_<=0, vakorgt, Line.kr(vakorgt, vakorgt_, sus*vakorgt_d));
vakorgt = if(vakorgtlfo<=0, vakorgt, vakorgt * SinOsc.kr(vakorgtlfo, 0, vakorgtlfomul, vakorgtlfoadd));
vakorgc = if(vakorgc_<=0, vakorgc, Line.kr(vakorgc, vakorgc_, sus*vakorgc_d));
vakorgc = if(vakorgclfo<=0, vakorgc, vakorgc * SinOsc.kr(vakorgclfo, 0, vakorgclfomul, vakorgclfoadd));
osc = VAKorg35.ar(osc*0.4, vakorg, vakorgr, vakorgd,vakorgt);
osc = Compander.ar(osc, osc, vakorgc, 1, 0.1, 0.01, 0.1 );
ReplaceOut.ar(bus, osc)}).add;