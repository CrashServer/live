SynthDef.new(\bandPassFilter,
{|bus, bpf, bpr, bpnoise, sus, bpf_, bpf_d, bpr_, bpr_d, bpnoise_, bpnoise_d|
var osc;
osc = In.ar(bus, 2);
bpf = if(bpf_<=0, bpf, Line.kr(bpf, bpf_, sus*bpf_d));
bpr = if(bpr_<=0, bpr, Line.kr(bpr, bpr_, sus*bpr_d));
bpnoise = if(bpnoise_<=0, bpnoise, Line.kr(bpnoise, bpnoise_, sus*bpnoise_d));
bpnoise = bpnoise / sus;
bpf = LFNoise1.kr(bpnoise).exprange(bpf * 0.5, bpf * 2);
bpr = LFNoise1.kr(bpnoise).exprange(bpr * 0.5, bpr * 2);
osc = BPF.ar(osc, bpf, bpr);
ReplaceOut.ar(bus, osc)}).add;