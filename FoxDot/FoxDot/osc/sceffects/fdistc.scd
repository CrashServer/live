SynthDef.new(\fdistc,
{|bus, fdistc, fdistcfreq1, fdistcfreq2, fdistcfreq3, fdistcfreq4, fdistcm1, fdistcm2, fdistcm3, fdistcm4, fdistcq1, fdistcq2, fdistcq3, fdistcq4, fdistc_, fdistcfreq1_, fdistcfreq2_, fdistcfreq3_, fdistcfreq4_, fdistcm1_, fdistcm2_, fdistcm3_, fdistcm4_, fdistcq1_, fdistcq2_, fdistcq3_, fdistcq4_, sus|
var osc;
osc = In.ar(bus, 2);
fdistc = fdistc+Line.kr(0, fdistc_, sus);
fdistcfreq1 = fdistcfreq1+Line.kr(0, fdistcfreq1_, sus);
fdistcfreq2 = fdistcfreq2+Line.kr(0, fdistcfreq2_, sus);
fdistcfreq3 = fdistcfreq3+Line.kr(0, fdistcfreq3_, sus);
fdistcfreq4 = fdistcfreq4+Line.kr(0, fdistcfreq4_, sus);
fdistcm1 = fdistcm1+Line.kr(0, fdistcm1_, sus);
fdistcm2 = fdistcm2+Line.kr(0, fdistcm2_, sus);
fdistcm3 = fdistcm3+Line.kr(0, fdistcm3_, sus);
fdistcm4 = fdistcm4+Line.kr(0, fdistcm4_, sus);
fdistcq1 = fdistcq1+Line.kr(0, fdistcq1_, sus);
fdistcq2 = fdistcq2+Line.kr(0, fdistcq2_, sus);
fdistcq3 = fdistcq3+Line.kr(0, fdistcq3_, sus);
fdistcq4 = fdistcq4+Line.kr(0, fdistcq4_, sus);
osc = RLPF.ar(osc, fdistcfreq1, fdistcq1);
osc = (osc * fdistcm1 * fdistc).tanh;
osc = RLPF.ar(osc, fdistcfreq2, fdistcq2);
osc = (osc * fdistcm2 * fdistc).tanh;
osc = RLPF.ar(osc, fdistcfreq3, fdistcq3);
osc = (osc * fdistcm3 * fdistc).tanh;
osc = RLPF.ar(osc, fdistcfreq4, fdistcq4);
osc = (osc * fdistcm4 * fdistc).tanh;
ReplaceOut.ar(bus, osc)}).add;