SynthDef.new(\M_Equalizer,
{|bus, mid, midfreq, midq, mid_, midfreq_, midq_, sus|
var osc;
osc = In.ar(bus, 2);
mid = mid+Line.kr(0, mid_, sus);
midfreq = midfreq+Line.kr(0, midfreq_, sus);
midq = midq+Line.kr(0, midq_, sus);
osc = BPeakEQ.ar(osc, freq: midfreq, rq: midq.reciprocal, db: abs(mid).ampdb);
ReplaceOut.ar(bus, osc)}).add;