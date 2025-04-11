SynthDef.new(\leg,
{|bus, leg, sus, leg_, leg_d, leglfo|
var osc;
osc = In.kr(bus, 1);
leg = if(leg_<=0, leg, Line.kr(leg, leg_, sus*leg_d));
leg = if(leglfo<=0, leg, leg * SinOsc.kr(leglfo, 0, 1, 1));
osc = osc * XLine.ar(Rand(0.5,1.5)*abs(leg),1,0.05*sus);
ReplaceOut.kr(bus, osc)}).add;