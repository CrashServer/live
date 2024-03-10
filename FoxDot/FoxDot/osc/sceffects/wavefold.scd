SynthDef.new(\wavefold,
{|bus, fold, symetry, smooth, fold_, fold_d, symetry_, symetry_d, smooth_, smooth_d, sus|
var osc,gain,compensationGain,envFollower,ampgain;
osc = In.ar(bus, 2);
fold = if(fold_<=0, fold, Line.kr(fold, fold_, sus*fold_d));
symetry = if(symetry_<=0, symetry, Line.kr(symetry, symetry_, sus*symetry_d));
smooth = if(smooth_<=0, smooth, Line.kr(smooth, smooth_, sus*smooth_d));
compensationGain = max(LinLin.kr(fold, 0, 1, 1, 20) * 0.75, 1).reciprocal;
envFollower = EnvFollow.ar((osc * 2).softclip, 0.9999);
ampgain = (compensationGain * (1 - 0.4)) + (envFollower * 0.4);
osc = SmoothFoldS.ar((osc + LinLin.kr(symetry, 0, 1, 1, 0)) * LinLin.kr(fold, 0, 1, 1, 20), smoothAmount: smooth);
osc = LeakDC.ar(osc*ampgain);
ReplaceOut.ar(bus, osc)}).add;