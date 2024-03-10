SynthDef.new(\comp,
{|bus, comp, comp_down, comp_up, comp_, comp_d, comp_down_, comp_down_d, comp_up_, comp_up_d, sus|
var osc;
osc = In.ar(bus, 2);
comp = if(comp_<=0, comp, Line.kr(comp, comp_, sus*comp_d));
osc = Compander.ar(osc, osc, thresh: comp, slopeAbove: comp_down, slopeBelow: comp_up, clampTime: 0.01, relaxTime: 0.01, mul: 1);
ReplaceOut.ar(bus, osc)}).add;