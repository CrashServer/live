SynthDef.new(\chorus2,
{|bus, chorus2, chorus2rate, chorus2depth, chorus2mode, chorus2_, chorus2_d, chorus2lfo, chorus2lfomul, chorus2lfoadd, chorus2rate_, chorus2rate_d, chorus2ratelfo, chorus2ratelfomul, chorus2ratelfoadd, chorus2depth_, chorus2depth_d, chorus2depthlfo, chorus2depthlfomul, chorus2depthlfoadd, chorus2mode_, chorus2mode_d, chorus2modelfo, chorus2modelfomul, chorus2modelfoadd, sus|
var osc,dry,wet,wetL,wetR,lfo1,lfo2,lfo3,rate,depth,baseDelay;
osc = In.ar(bus, 2);
chorus2 = if(chorus2_<=0, chorus2, Line.kr(chorus2, chorus2_, sus*chorus2_d));
chorus2 = if(chorus2lfo<=0, chorus2, chorus2 * SinOsc.kr(chorus2lfo, 0, chorus2lfomul, chorus2lfoadd));
chorus2rate = if(chorus2rate_<=0, chorus2rate, Line.kr(chorus2rate, chorus2rate_, sus*chorus2rate_d));
chorus2rate = if(chorus2ratelfo<=0, chorus2rate, chorus2rate * SinOsc.kr(chorus2ratelfo, 0, chorus2ratelfomul, chorus2ratelfoadd));
chorus2depth = if(chorus2depth_<=0, chorus2depth, Line.kr(chorus2depth, chorus2depth_, sus*chorus2depth_d));
chorus2depth = if(chorus2depthlfo<=0, chorus2depth, chorus2depth * SinOsc.kr(chorus2depthlfo, 0, chorus2depthlfomul, chorus2depthlfoadd));
chorus2mode = if(chorus2mode_<=0, chorus2mode, Line.kr(chorus2mode, chorus2mode_, sus*chorus2mode_d));
chorus2mode = if(chorus2modelfo<=0, chorus2mode, chorus2mode * SinOsc.kr(chorus2modelfo, 0, chorus2modelfomul, chorus2modelfoadd));
dry = osc;
rate = LinExp.kr(chorus2rate, 0.0, 1.0, 0.2, 1.2);
depth = LinLin.kr(chorus2depth, 0.0, 1.0, 0.001, 0.004);
baseDelay = 0.003;
lfo1 = SinOsc.kr(rate * 0.51, 0, depth, baseDelay);
lfo2 = SinOsc.kr(rate * 0.73, 1.2, depth * 0.9, baseDelay);
lfo3 = SinOsc.kr(rate * 1.19, 2.4, depth * 0.8, baseDelay);
wetL = Select.kr(chorus2mode.clip(1,3) - 1, [DelayC.ar(osc[0], 0.02, lfo1), DelayC.ar(osc[0], 0.02, lfo1) + DelayC.ar(osc[0], 0.02, lfo2), DelayC.ar(osc[0], 0.02, lfo1) + DelayC.ar(osc[0], 0.02, lfo2) + DelayC.ar(osc[0], 0.02, lfo3)]);
wetR = Select.kr(chorus2mode.clip(1,3) - 1, [DelayC.ar(osc[1], 0.02, lfo1), DelayC.ar(osc[1], 0.02, lfo2) + DelayC.ar(osc[1], 0.02, lfo3), DelayC.ar(osc[1], 0.02, lfo2) + DelayC.ar(osc[1], 0.02, lfo3) + DelayC.ar(osc[1], 0.02, lfo1)]);
wet = [wetL, wetR];
wet = HPF.kr(wet, 30);
osc = SelectX.ar(chorus2, [dry, (dry * 0.7) + (wet * 0.6)]);
ReplaceOut.ar(bus, osc)}).add;