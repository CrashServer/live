SynthDef.new(\oneSend_toecho,
{|bus, toecho, toecho_, toecho_d, toecholfo, toecholfomul, toecholfoadd, toecholfophase, sus|
var osc;
osc = In.ar(bus, 2);
toecho = if(toecho_<=0, toecho, Line.kr(toecho, toecho_, sus*toecho_d));
toecho = if(toecholfo<=0, toecho, toecho * SinOsc.kr(toecholfo, toecholfophase, toecholfomul, toecholfoadd));
Out.ar(10, osc * toecho);
ReplaceOut.ar(bus, osc)}).add;