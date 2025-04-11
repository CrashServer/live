SynthDef.new(\M_Equalizer,
{|bus, mid, midfreq, midq, mid_, mid_d, midlfo, midfreq_, midfreq_d, midfreqlfo, midq_, midq_d, midqlfo, sus|
var osc;
osc = In.ar(bus, 2);
mid = if(mid_<=0, mid, Line.kr(mid, mid_, sus*mid_d));
mid = if(midlfo<=0, mid, mid * SinOsc.kr(midlfo, 0, 1, 1));
midfreq = if(midfreq_<=0, midfreq, Line.kr(midfreq, midfreq_, sus*midfreq_d));
midfreq = if(midfreqlfo<=0, midfreq, midfreq * SinOsc.kr(midfreqlfo, 0, 1, 1));
midq = if(midq_<=0, midq, Line.kr(midq, midq_, sus*midq_d));
midq = if(midqlfo<=0, midq, midq * SinOsc.kr(midqlfo, 0, 1, 1));
osc = BPeakEQ.ar(osc, freq: midfreq, rq: midq.reciprocal, db: abs(mid).ampdb);
ReplaceOut.ar(bus, osc)}).add;