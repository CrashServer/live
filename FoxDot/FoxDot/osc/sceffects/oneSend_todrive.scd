SynthDef.new(\oneSend_todrive,
{|bus, todrive, todrive_, todrive_d, todrivelfo, todrivelfomul, todrivelfoadd, todrivelfophase, sus|
var osc;
osc = In.ar(bus, 2);
todrive = if(todrive_<=0, todrive, Line.kr(todrive, todrive_, sus*todrive_d));
todrive = if(todrivelfo<=0, todrive, todrive * SinOsc.kr(todrivelfo, todrivelfophase, todrivelfomul, todrivelfoadd));
Out.ar(2, osc * todrive);
ReplaceOut.ar(bus, osc)}).add;