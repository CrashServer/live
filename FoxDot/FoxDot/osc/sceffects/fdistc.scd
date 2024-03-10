SynthDef.new(\fdistc,
{|bus, fdistc, fdistcfreq1, fdistcfreq2, fdistcfreq3, fdistcfreq4, fdistcm1, fdistcm2, fdistcm3, fdistcm4, fdistcq1, fdistcq2, fdistcq3, fdistcq4, fdistc_, fdistc_d, fdistcfreq1_, fdistcfreq1_d, fdistcfreq2_, fdistcfreq2_d, fdistcfreq3_, fdistcfreq3_d, fdistcfreq4_, fdistcfreq4_d, fdistcm1_, fdistcm1_d, fdistcm2_, fdistcm2_d, fdistcm3_, fdistcm3_d, fdistcm4_, fdistcm4_d, fdistcq1_, fdistcq1_d, fdistcq2_, fdistcq2_d, fdistcq3_, fdistcq3_d, fdistcq4_, fdistcq4_d, sus|
var osc;
osc = In.ar(bus, 2);
fdistc = if(fdistc_<=0, fdistc, Line.kr(fdistc, fdistc_, sus*fdistc_d));
fdistcfreq1 = if(fdistcfreq1_<=0, fdistcfreq1, Line.kr(fdistcfreq1, fdistcfreq1_, sus*fdistcfreq1_d));
fdistcfreq2 = if(fdistcfreq2_<=0, fdistcfreq2, Line.kr(fdistcfreq2, fdistcfreq2_, sus*fdistcfreq2_d));
fdistcfreq3 = if(fdistcfreq3_<=0, fdistcfreq3, Line.kr(fdistcfreq3, fdistcfreq3_, sus*fdistcfreq3_d));
fdistcfreq4 = if(fdistcfreq4_<=0, fdistcfreq4, Line.kr(fdistcfreq4, fdistcfreq4_, sus*fdistcfreq4_d));
fdistcm1 = if(fdistcm1_<=0, fdistcm1, Line.kr(fdistcm1, fdistcm1_, sus*fdistcm1_d));
fdistcm2 = if(fdistcm2_<=0, fdistcm2, Line.kr(fdistcm2, fdistcm2_, sus*fdistcm2_d));
fdistcm3 = if(fdistcm3_<=0, fdistcm3, Line.kr(fdistcm3, fdistcm3_, sus*fdistcm3_d));
fdistcm4 = if(fdistcm4_<=0, fdistcm4, Line.kr(fdistcm4, fdistcm4_, sus*fdistcm4_d));
fdistcq1 = if(fdistcq1_<=0, fdistcq1, Line.kr(fdistcq1, fdistcq1_, sus*fdistcq1_d));
fdistcq2 = if(fdistcq2_<=0, fdistcq2, Line.kr(fdistcq2, fdistcq2_, sus*fdistcq2_d));
fdistcq3 = if(fdistcq3_<=0, fdistcq3, Line.kr(fdistcq3, fdistcq3_, sus*fdistcq3_d));
fdistcq4 = if(fdistcq4_<=0, fdistcq4, Line.kr(fdistcq4, fdistcq4_, sus*fdistcq4_d));
osc = RLPF.ar(osc, fdistcfreq1, fdistcq1);
osc = (osc * fdistcm1 * fdistc).tanh;
osc = RLPF.ar(osc, fdistcfreq2, fdistcq2);
osc = (osc * fdistcm2 * fdistc).tanh;
osc = RLPF.ar(osc, fdistcfreq3, fdistcq3);
osc = (osc * fdistcm3 * fdistc).tanh;
osc = RLPF.ar(osc, fdistcfreq4, fdistcq4);
osc = (osc * fdistcm4 * fdistc).tanh;
ReplaceOut.ar(bus, osc)}).add;