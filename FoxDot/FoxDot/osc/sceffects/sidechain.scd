SynthDef.new(\sidechain,
{|bus, sidechain, sidechain_atk, sidechain_rel, thresh, sidechain_, sidechain_atk_, sidechain_rel_, thresh_, sus|
var osc,schain;
osc = In.ar(bus, 2);
sidechain = sidechain+Line.kr(0, sidechain_, sus);
sidechain_atk = sidechain_atk+Line.kr(0, sidechain_atk_, sus);
sidechain_rel = sidechain_rel+Line.kr(0, sidechain_rel_, sus);
thresh = thresh+Line.kr(0, thresh_, sus);
schain = In.ar(sidechain,1);
osc = Compander.ar(osc, schain, thresh: thresh, slopeAbove: 0.1, slopeBelow: 1, clampTime: sidechain_atk, relaxTime: sidechain_rel, mul: 1);
ReplaceOut.ar(bus, osc)}).add;