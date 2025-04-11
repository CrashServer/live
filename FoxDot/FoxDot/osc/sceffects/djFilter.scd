SynthDef.new(\djFilter,
{|bus, djf, djfq, djf_, djf_d, djflfo, djflfomul, djflfoadd, djfq_, djfq_d, djfqlfo, djfqlfomul, djfqlfoadd, sus|
var osc,lpfCutoffFreq,hpfCutoffFreq;
osc = In.ar(bus, 2);
djf = if(djf_<=0, djf, Line.kr(djf, djf_, sus*djf_d));
djf = if(djflfo<=0, djf, djf * SinOsc.kr(djflfo, 0, djflfomul, djflfoadd));
djfq = if(djfq_<=0, djfq, Line.kr(djfq, djfq_, sus*djfq_d));
djfq = if(djfqlfo<=0, djfq, djfq * SinOsc.kr(djfqlfo, 0, djfqlfomul, djfqlfoadd));
lpfCutoffFreq = djf.linexp(0, 0.5, 50, 15000);
hpfCutoffFreq = djf.linexp(0.5, 1, 50, 15000);
osc = RHPF.ar(RLPF.ar(osc,lpfCutoffFreq, djfq),hpfCutoffFreq, djfq);
ReplaceOut.ar(bus, osc)}).add;