SynthDef.new(\sidechain,
{|bus, sidechain, sidechain_atk, sidechain_rel, thresh, sidechain_, sidechain_d, sidechainlfo, sidechainlfomul, sidechainlfoadd, sidechain_atk_, sidechain_atk_d, sidechain_atklfo, sidechain_atklfomul, sidechain_atklfoadd, sidechain_rel_, sidechain_rel_d, sidechain_rellfo, sidechain_rellfomul, sidechain_rellfoadd, thresh_, thresh_d, threshlfo, threshlfomul, threshlfoadd, sus|
var osc,schain;
osc = In.ar(bus, 2);
sidechain = if(sidechain_<=0, sidechain, Line.kr(sidechain, sidechain_, sus*sidechain_d));
sidechain = if(sidechainlfo<=0, sidechain, sidechain * SinOsc.kr(sidechainlfo, 0, sidechainlfomul, sidechainlfoadd));
sidechain_atk = if(sidechain_atk_<=0, sidechain_atk, Line.kr(sidechain_atk, sidechain_atk_, sus*sidechain_atk_d));
sidechain_atk = if(sidechain_atklfo<=0, sidechain_atk, sidechain_atk * SinOsc.kr(sidechain_atklfo, 0, sidechain_atklfomul, sidechain_atklfoadd));
sidechain_rel = if(sidechain_rel_<=0, sidechain_rel, Line.kr(sidechain_rel, sidechain_rel_, sus*sidechain_rel_d));
sidechain_rel = if(sidechain_rellfo<=0, sidechain_rel, sidechain_rel * SinOsc.kr(sidechain_rellfo, 0, sidechain_rellfomul, sidechain_rellfoadd));
thresh = if(thresh_<=0, thresh, Line.kr(thresh, thresh_, sus*thresh_d));
thresh = if(threshlfo<=0, thresh, thresh * SinOsc.kr(threshlfo, 0, threshlfomul, threshlfoadd));
schain = In.ar(sidechain,1);
osc = Compander.ar(osc, schain, thresh: thresh, slopeAbove: 0.1, slopeBelow: 1, clampTime: sidechain_atk, relaxTime: sidechain_rel, mul: 1);
ReplaceOut.ar(bus, osc)}).add;