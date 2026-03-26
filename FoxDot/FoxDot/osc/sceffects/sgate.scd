SynthDef.new(\sgate,
{|bus, sgate, sgthresh, sgmode, sgate_, sgate_d, sgatelfo, sgatelfomul, sgatelfoadd, sgthresh_, sgthresh_d, sgthreshlfo, sgthreshlfomul, sgthreshlfoadd, sgmode_, sgmode_d, sgmodelfo, sgmodelfomul, sgmodelfoadd, sus|
var osc,dry,wetL,wetR,chainL,chainR,bufL,bufR;
osc = In.ar(bus, 2);
sgate = if(sgate_<=0, sgate, Line.kr(sgate, sgate_, sus*sgate_d));
sgate = if(sgatelfo<=0, sgate, sgate * SinOsc.kr(sgatelfo, 0, sgatelfomul, sgatelfoadd));
sgthresh = if(sgthresh_<=0, sgthresh, Line.kr(sgthresh, sgthresh_, sus*sgthresh_d));
sgthresh = if(sgthreshlfo<=0, sgthresh, sgthresh * SinOsc.kr(sgthreshlfo, 0, sgthreshlfomul, sgthreshlfoadd));
sgmode = if(sgmode_<=0, sgmode, Line.kr(sgmode, sgmode_, sus*sgmode_d));
sgmode = if(sgmodelfo<=0, sgmode, sgmode * SinOsc.kr(sgmodelfo, 0, sgmodelfomul, sgmodelfoadd));
dry = osc;
bufL = LocalBuf(2048);
bufR = LocalBuf(2048);
chainL = FFT(bufL, osc[0]);
chainR = FFT(bufR, osc[1]);
chainL = Select.kr(sgmode.round, [PV_MagAbove(chainL, sgthresh), PV_MagBelow(chainL, sgthresh)]);
chainR = Select.kr(sgmode.round, [PV_MagAbove(chainR, sgthresh), PV_MagBelow(chainR, sgthresh)]);
wetL = IFFT(chainL);
wetR = IFFT(chainR);
osc = XFade2.ar(dry, [wetL, wetR], sgate * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;