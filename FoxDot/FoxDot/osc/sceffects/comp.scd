SynthDef.new(\comp,
{|bus, comp, comp_down, comp_up, comp_, comp_down_, comp_up_, sus|
var osc;
osc = In.ar(bus, 2);
comp = comp+Line.kr(0, comp_, sus);
comp_down = comp_down+Line.kr(0, comp_down_, sus);
comp_up = comp_up+Line.kr(0, comp_up_, sus);
osc = Compander.ar(osc, osc, thresh: comp, slopeAbove: comp_down, slopeBelow: comp_up, clampTime: 0.01, relaxTime: 0.01, mul: 1);
ReplaceOut.ar(bus, osc)}).add;