SynthDef.new(\djFilter,
{|bus, djf, djfq, djf_, djfq_, sus|
var osc,lpfCutoffFreq,hpfCutoffFreq;
osc = In.ar(bus, 2);
djf = djf+Line.kr(0, djf_, sus);
djfq = djfq+Line.kr(0, djfq_, sus);
lpfCutoffFreq = djf.linexp(0, 0.5, 50, 15000);
hpfCutoffFreq = djf.linexp(0.5, 1, 50, 15000);
osc = RHPF.ar(RLPF.ar(osc,lpfCutoffFreq, djfq),hpfCutoffFreq, djfq);
ReplaceOut.ar(bus, osc)}).add;