SynthDef.new(\bandPassFilter,
{|bus, bpf, bpr, bpnoise, sus, bpf_, bpr_, bpnoise_|
var osc;
osc = In.ar(bus, 2);
bpf = bpf+Line.kr(0, bpf_, sus);
bpr = bpr+Line.kr(0, bpr_, sus);
bpnoise = bpnoise+Line.kr(0, bpnoise_, sus);
bpnoise = bpnoise / sus;
bpf = LFNoise1.kr(bpnoise).exprange(bpf * 0.5, bpf * 2);
bpr = LFNoise1.kr(bpnoise).exprange(bpr * 0.5, bpr * 2);
osc = BPF.ar(osc, bpf, bpr);
ReplaceOut.ar(bus, osc)}).add;