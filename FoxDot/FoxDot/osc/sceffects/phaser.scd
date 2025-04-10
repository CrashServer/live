SynthDef.new(\phaser,
{|bus, phaser, phaserdepth, phaser_, phaser_d, phaserdepth_, phaserdepth_d, sus|
var osc,delayedSignal;
osc = In.ar(bus, 2);
phaser = if(phaser_<=0, phaser, Line.kr(phaser, phaser_, sus*phaser_d));
phaserdepth = if(phaserdepth_<=0, phaserdepth, Line.kr(phaserdepth, phaserdepth_, sus*phaserdepth_d));
delayedSignal = osc;
for(1, 4, {|i| delayedSignal = AllpassL.ar(delayedSignal, 0.01 * 4.reciprocal, LFPar.kr(LinExp.kr(phaser, 0, 1, 0.275, 16), i + 0.5.rand, LinExp.kr(phaserdepth*4.reciprocal, 0, 1, 0.0005, 0.01 * 0.5), LinExp.kr(phaserdepth*4.reciprocal, 0, 1, 0.0005, 0.01 * 0.5)), 0)});
osc = osc + delayedSignal;
ReplaceOut.ar(bus, osc)}).add;