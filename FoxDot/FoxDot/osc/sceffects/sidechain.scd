SynthDef.new(\sidechain,
{|bus, sidechain, sidechain_atk, sidechain_rel, thresh, sidechain_, sidechain_d, sidechain_atk_, sidechain_atk_d, sidechain_rel_, sidechain_rel_d, thresh_, thresh_d, sus|
var osc,schain;
osc = In.ar(bus, 2);
sidechain = if(sidechain_<=0, sidechain, Line.kr(sidechain, sidechain_, sus*sidechain_d));
thresh = if(thresh_<=0, thresh, Line.kr(thresh, thresh_, sus*thresh_d));
schain = In.ar(sidechain,1);
osc = Compander.ar(osc, schain, thresh: thresh, slopeAbove: 0.1, slopeBelow: 1, clampTime: sidechain_atk, relaxTime: sidechain_rel, mul: 1);
ReplaceOut.ar(bus, osc)}).add;