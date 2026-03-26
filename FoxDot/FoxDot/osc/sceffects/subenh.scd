SynthDef.new(\subenh,
{|bus, subenh, subhfreq, subhgain, subenh_, subenh_d, subenhlfo, subenhlfomul, subenhlfoadd, subhfreq_, subhfreq_d, subhfreqlfo, subhfreqlfomul, subhfreqlfoadd, subhgain_, subhgain_d, subhgainlfo, subhgainlfomul, subhgainlfoadd, sus|
var osc,dry,low,sub;
osc = In.ar(bus, 2);
subenh = if(subenh_<=0, subenh, Line.kr(subenh, subenh_, sus*subenh_d));
subenh = if(subenhlfo<=0, subenh, subenh * SinOsc.kr(subenhlfo, 0, subenhlfomul, subenhlfoadd));
subhfreq = if(subhfreq_<=0, subhfreq, Line.kr(subhfreq, subhfreq_, sus*subhfreq_d));
subhfreq = if(subhfreqlfo<=0, subhfreq, subhfreq * SinOsc.kr(subhfreqlfo, 0, subhfreqlfomul, subhfreqlfoadd));
subhgain = if(subhgain_<=0, subhgain, Line.kr(subhgain, subhgain_, sus*subhgain_d));
subhgain = if(subhgainlfo<=0, subhgain, subhgain * SinOsc.kr(subhgainlfo, 0, subhgainlfomul, subhgainlfoadd));
dry = osc;
low = LPF.ar(osc, subhfreq);
sub = PitchShift.ar(low, 0.1, 0.5, 0, 0.004);
sub = LPF.ar(sub, subhfreq);
sub = LeakDC.ar(sub);
osc = dry + (sub * subhgain * subenh);
ReplaceOut.ar(bus, osc)}).add;