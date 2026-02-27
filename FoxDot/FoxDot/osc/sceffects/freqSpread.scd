SynthDef.new(\freqSpread,
{|bus, fspread, fspreadfreq, fspread_, fspread_d, fspreadlfo, fspreadlfomul, fspreadlfoadd, fspreadfreq_, fspreadfreq_d, fspreadfreqlfo, fspreadfreqlfomul, fspreadfreqlfoadd, sus|
var osc,low,mid,high,mono;
osc = In.ar(bus, 2);
fspread = if(fspread_<=0, fspread, Line.kr(fspread, fspread_, sus*fspread_d));
fspread = if(fspreadlfo<=0, fspread, fspread * SinOsc.kr(fspreadlfo, 0, fspreadlfomul, fspreadlfoadd));
fspreadfreq = if(fspreadfreq_<=0, fspreadfreq, Line.kr(fspreadfreq, fspreadfreq_, sus*fspreadfreq_d));
fspreadfreq = if(fspreadfreqlfo<=0, fspreadfreq, fspreadfreq * SinOsc.kr(fspreadfreqlfo, 0, fspreadfreqlfomul, fspreadfreqlfoadd));
mono = Mix.ar(osc);
low = LPF.ar(mono, fspreadfreq);
mid = BPF.ar(mono, fspreadfreq, 1);
high = HPF.ar(mono, fspreadfreq * 2);
osc = Pan2.ar(low, 0) + Pan2.ar(mid, LFNoise1.kr(0.5) * fspread * 0.5) + Pan2.ar(high, LFNoise1.kr(0.7) * fspread);
ReplaceOut.ar(bus, osc)}).add;