SynthDef.new(\djFilter,
{|bus, djf, djfq, djf_, djf_d, djfq_, djfq_d, sus|
var osc,lpfCutoffFreq,hpfCutoffFreq;
osc = In.ar(bus, 2);
djf = if(djf_<=0, djf, Line.kr(djf, djf_, sus*djf_d));
djfq = if(djfq_<=0, djfq, Line.kr(djfq, djfq_, sus*djfq_d));
lpfCutoffFreq = djf.linexp(0, 0.5, 50, 15000);
hpfCutoffFreq = djf.linexp(0.5, 1, 50, 15000);
osc = RHPF.ar(RLPF.ar(osc,lpfCutoffFreq, djfq),hpfCutoffFreq, djfq);
ReplaceOut.ar(bus, osc)}).add;