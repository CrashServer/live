SynthDef.new(\spectralGate,
{|bus, sgate, sgatemix, sgatethresh, sgate_, sgate_d, sgatelfo, sgatelfomul, sgatelfoadd, sgatemix_, sgatemix_d, sgatemixlfo, sgatemixlfomul, sgatemixlfoadd, sgatethresh_, sgatethresh_d, sgatethreshlfo, sgatethreshlfomul, sgatethreshlfoadd, sus|
var osc,dry,chain,gated;
osc = In.ar(bus, 2);
sgate = if(sgate_<=0, sgate, Line.kr(sgate, sgate_, sus*sgate_d));
sgate = if(sgatelfo<=0, sgate, sgate * SinOsc.kr(sgatelfo, 0, sgatelfomul, sgatelfoadd));
sgatemix = if(sgatemix_<=0, sgatemix, Line.kr(sgatemix, sgatemix_, sus*sgatemix_d));
sgatemix = if(sgatemixlfo<=0, sgatemix, sgatemix * SinOsc.kr(sgatemixlfo, 0, sgatemixlfomul, sgatemixlfoadd));
sgatethresh = if(sgatethresh_<=0, sgatethresh, Line.kr(sgatethresh, sgatethresh_, sus*sgatethresh_d));
sgatethresh = if(sgatethreshlfo<=0, sgatethresh, sgatethresh * SinOsc.kr(sgatethreshlfo, 0, sgatethreshlfomul, sgatethreshlfoadd));
dry = osc;
chain = FFT(Array.fill(2, { LocalBuf(2048, 1) }), osc);
chain = PV_MagAbove(chain, sgatethresh);
gated = IFFT(chain);
gated = LeakDC.ar(gated);
osc = XFade2.ar(dry, (dry * (1 - sgatemix)) + (gated * sgatemix), sgate * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;