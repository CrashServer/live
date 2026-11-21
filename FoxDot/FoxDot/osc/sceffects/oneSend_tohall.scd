SynthDef.new(\oneSend_tohall,
{|bus, tohall, tohall_, tohall_d, tohalllfo, tohalllfomul, tohalllfoadd, tohalllfophase, sus|
var osc;
osc = In.ar(bus, 2);
tohall = if(tohall_<=0, tohall, Line.kr(tohall, tohall_, sus*tohall_d));
tohall = if(tohalllfo<=0, tohall, tohall * SinOsc.kr(tohalllfo, tohalllfophase, tohalllfomul, tohalllfoadd));
Out.ar(8, osc * tohall);
ReplaceOut.ar(bus, osc)}).add;