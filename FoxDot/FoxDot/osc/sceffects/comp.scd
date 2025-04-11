SynthDef.new(\comp,
{|bus, comp, comp_down, comp_up, comp_, comp_d, complfo, comp_down_, comp_down_d, comp_downlfo, comp_up_, comp_up_d, comp_uplfo, sus|
var osc;
osc = In.ar(bus, 2);
comp = if(comp_<=0, comp, Line.kr(comp, comp_, sus*comp_d));
comp = if(complfo<=0, comp, comp * SinOsc.kr(complfo, 0, 1, 1));
comp_down = if(comp_down_<=0, comp_down, Line.kr(comp_down, comp_down_, sus*comp_down_d));
comp_down = if(comp_downlfo<=0, comp_down, comp_down * SinOsc.kr(comp_downlfo, 0, 1, 1));
comp_up = if(comp_up_<=0, comp_up, Line.kr(comp_up, comp_up_, sus*comp_up_d));
comp_up = if(comp_uplfo<=0, comp_up, comp_up * SinOsc.kr(comp_uplfo, 0, 1, 1));
osc = Compander.ar(osc, osc, thresh: comp, slopeAbove: comp_down, slopeBelow: comp_up, clampTime: 0.01, relaxTime: 0.01, mul: 1);
ReplaceOut.ar(bus, osc)}).add;