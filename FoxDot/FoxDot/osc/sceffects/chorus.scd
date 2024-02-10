SynthDef.new(\chorus,
{|bus, chorus, chorusrate, chorus_, chorus_d, chorusrate_, chorusrate_d, sus|
var osc,lfos,numDelays = 4,chrate,maxDelayTime,minDelayTime;
osc = In.ar(bus, 2);
chorus = if(chorus_<=0, chorus, Line.kr(chorus, chorus_, sus*chorus_d));
chorusrate = if(chorusrate_<=0, chorusrate, Line.kr(chorusrate, chorusrate_, sus*chorusrate_d));
chrate = Select.kr(chorusrate > 0.5, [LinExp.kr(chorusrate, 0.0, 0.5, 0.025, 0.125),LinExp.kr(chorusrate, 0.5, 1.0, 0.125, 2)]);
maxDelayTime = LinLin.kr(chorus, 0.0, 1.0, 0.016, 0.052);
minDelayTime = LinLin.kr(chorus, 0.0, 1.0, 0.012, 0.022);
osc = osc * numDelays.reciprocal;
lfos = Array.fill(numDelays, {|i| LFPar.kr(chrate * {rrand(0.95, 1.05)},0.9 * i,(maxDelayTime - minDelayTime) * 0.5,(maxDelayTime + minDelayTime) * 0.5,)});
osc = DelayC.ar(osc, (maxDelayTime * 2), lfos).sum;
osc = Mix(osc);
ReplaceOut.ar(bus, osc)}).add;