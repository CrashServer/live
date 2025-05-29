SynthDef.new(\wavefold,
{|bus, fold, symetry, smooth, fold_, fold_d, foldlfo, foldlfomul, foldlfoadd, symetry_, symetry_d, symetrylfo, symetrylfomul, symetrylfoadd, smooth_, smooth_d, smoothlfo, smoothlfomul, smoothlfoadd, sus|
var osc,gain,compensationGain,envFollower,ampgain;
osc = In.ar(bus, 2);
fold = if(fold_<=0, fold, Line.kr(fold, fold_, sus*fold_d));
fold = if(foldlfo<=0, fold, fold * SinOsc.kr(foldlfo, 0, foldlfomul, foldlfoadd));
symetry = if(symetry_<=0, symetry, Line.kr(symetry, symetry_, sus*symetry_d));
symetry = if(symetrylfo<=0, symetry, symetry * SinOsc.kr(symetrylfo, 0, symetrylfomul, symetrylfoadd));
smooth = if(smooth_<=0, smooth, Line.kr(smooth, smooth_, sus*smooth_d));
smooth = if(smoothlfo<=0, smooth, smooth * SinOsc.kr(smoothlfo, 0, smoothlfomul, smoothlfoadd));
compensationGain = max(LinLin.kr(fold, 0, 1, 1, 20) * 0.75, 1).reciprocal;
envFollower = EnvFollow.ar((osc * 2).softclip, 0.9999);
ampgain = (compensationGain * (1 - 0.4)) + (envFollower * 0.4);
osc = SmoothFoldS.ar((osc + LinLin.kr(symetry, 0, 1, 1, 0)) * LinLin.kr(fold, 0, 1, 1, 20), smoothAmount: smooth);
osc = LeakDC.ar(osc*ampgain);
ReplaceOut.ar(bus, osc)}).add;