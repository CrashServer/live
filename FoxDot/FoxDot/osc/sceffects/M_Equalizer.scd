SynthDef.new(\M_Equalizer,
{|bus, mid, midfreq, midq, mid_, mid_d, midfreq_, midfreq_d, midq_, midq_d, sus|
var osc;
osc = In.ar(bus, 2);
mid = if(mid_<=0, mid, Line.kr(mid, mid_, sus*mid_d));
midfreq = if(midfreq_<=0, midfreq, Line.kr(midfreq, midfreq_, sus*midfreq_d));
midq = if(midq_<=0, midq, Line.kr(midq, midq_, sus*midq_d));
osc = BPeakEQ.ar(osc, freq: midfreq, rq: midq.reciprocal, db: abs(mid).ampdb);
ReplaceOut.ar(bus, osc)}).add;