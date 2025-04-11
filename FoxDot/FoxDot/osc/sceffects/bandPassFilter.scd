SynthDef.new(\bandPassFilter,
{|bus, bpf, bpr, bpnoise, sus, bpf_, bpf_d, bpflfo, bpr_, bpr_d, bprlfo, bpnoise_, bpnoise_d, bpnoiselfo|
var osc;
osc = In.ar(bus, 2);
bpf = if(bpf_<=0, bpf, Line.kr(bpf, bpf_, sus*bpf_d));
bpf = if(bpflfo<=0, bpf, bpf * SinOsc.kr(bpflfo, 0, 1, 1));
bpr = if(bpr_<=0, bpr, Line.kr(bpr, bpr_, sus*bpr_d));
bpr = if(bprlfo<=0, bpr, bpr * SinOsc.kr(bprlfo, 0, 1, 1));
bpnoise = if(bpnoise_<=0, bpnoise, Line.kr(bpnoise, bpnoise_, sus*bpnoise_d));
bpnoise = if(bpnoiselfo<=0, bpnoise, bpnoise * SinOsc.kr(bpnoiselfo, 0, 1, 1));
bpnoise = bpnoise / sus;
bpf = LFNoise1.kr(bpnoise).exprange(bpf * 0.5, bpf * 2);
bpr = LFNoise1.kr(bpnoise).exprange(bpr * 0.5, bpr * 2);
osc = BPF.ar(osc, bpf, bpr);
ReplaceOut.ar(bus, osc)}).add;