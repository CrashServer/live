SynthDef.new(\fdist,
{|bus, fdist, fdistfreq, fdist_, fdist_d, fdistlfo, fdistlfomul, fdistlfoadd, fdistfreq_, fdistfreq_d, fdistfreqlfo, fdistfreqlfomul, fdistfreqlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
fdist = if(fdist_<=0, fdist, Line.kr(fdist, fdist_, sus*fdist_d));
fdist = if(fdistlfo<=0, fdist, fdist * SinOsc.kr(fdistlfo, 0, fdistlfomul, fdistlfoadd));
fdistfreq = if(fdistfreq_<=0, fdistfreq, Line.kr(fdistfreq, fdistfreq_, sus*fdistfreq_d));
fdistfreq = if(fdistfreqlfo<=0, fdistfreq, fdistfreq * SinOsc.kr(fdistfreqlfo, 0, fdistfreqlfomul, fdistfreqlfoadd));
osc = LPF.ar(osc, fdistfreq);
osc = (osc * 1.1 * fdist).tanh;
osc = LPF.ar(osc, fdistfreq);
osc = (osc * 1.1 * fdist).tanh;
osc = LPF.ar(osc, fdistfreq);
osc = (osc * 1.4 * fdist).tanh;
osc = LPF.ar(osc, fdistfreq);
osc = (osc * 2 * fdist).tanh;
osc = osc*0.2;
ReplaceOut.ar(bus, osc)}).add;