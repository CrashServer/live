SynthDef.new(\bandPassFilter,
{|bus, bpf, bpr, bpnoise, sus, bpf_, bpf_d, bpflfo, bpflfomul, bpflfoadd, bpflfophase, bpr_, bpr_d, bprlfo, bprlfomul, bprlfoadd, bprlfophase, bpnoise_, bpnoise_d, bpnoiselfo, bpnoiselfomul, bpnoiselfoadd, bpnoiselfophase|
var osc;
osc = In.ar(bus, 2);
bpf = if(bpf_<=0, bpf, Line.kr(bpf, bpf_, sus*bpf_d));
bpf = if(bpflfo<=0, bpf, bpf * SinOsc.kr(bpflfo, bpflfophase, bpflfomul, bpflfoadd));
bpr = if(bpr_<=0, bpr, Line.kr(bpr, bpr_, sus*bpr_d));
bpr = if(bprlfo<=0, bpr, bpr * SinOsc.kr(bprlfo, bprlfophase, bprlfomul, bprlfoadd));
bpnoise = if(bpnoise_<=0, bpnoise, Line.kr(bpnoise, bpnoise_, sus*bpnoise_d));
bpnoise = if(bpnoiselfo<=0, bpnoise, bpnoise * SinOsc.kr(bpnoiselfo, bpnoiselfophase, bpnoiselfomul, bpnoiselfoadd));
bpnoise = bpnoise / sus;
bpf = LFNoise1.kr(bpnoise).exprange(bpf * 0.5, bpf * 2);
bpr = LFNoise1.kr(bpnoise).exprange(bpr * 0.5, bpr * 2);
osc = BPF.ar(osc, bpf, bpr);
ReplaceOut.ar(bus, osc)}).add;