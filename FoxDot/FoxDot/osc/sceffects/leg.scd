SynthDef.new(\leg,
{|bus, leg, sus, leg_|
var osc;
osc = In.kr(bus, 1);
leg = leg+Line.kr(0, leg_, sus);
osc = osc * XLine.ar(Rand(0.5,1.5)*abs(leg),1,0.05*sus);
ReplaceOut.kr(bus, osc)}).add;