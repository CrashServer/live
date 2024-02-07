SynthDef.new(\wavefold,
{|bus, fold, symetry, smooth, fold_, symetry_, smooth_, sus|
var osc,gain,compensationGain,envFollower,ampgain;
osc = In.ar(bus, 2);
fold = fold+Line.kr(0, fold_, sus);
symetry = symetry+Line.kr(0, symetry_, sus);
smooth = smooth+Line.kr(0, smooth_, sus);
compensationGain = max(LinLin.kr(fold, 0, 1, 1, 20) * 0.75, 1).reciprocal;
envFollower = EnvFollow.ar((osc * 2).softclip, 0.9999);
ampgain = (compensationGain * (1 - 0.4)) + (envFollower * 0.4);
osc = SmoothFoldS.ar((osc + LinLin.kr(symetry, 0, 1, 1, 0)) * LinLin.kr(fold, 0, 1, 1, 20), smoothAmount: smooth);
osc = LeakDC.ar(osc*ampgain);
ReplaceOut.ar(bus, osc)}).add;