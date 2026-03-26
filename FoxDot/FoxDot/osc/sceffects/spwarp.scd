SynthDef.new(\spwarp,
{|bus, spwarp, spwstr, spwshift, spwarp_, spwarp_d, spwarplfo, spwarplfomul, spwarplfoadd, spwstr_, spwstr_d, spwstrlfo, spwstrlfomul, spwstrlfoadd, spwshift_, spwshift_d, spwshiftlfo, spwshiftlfomul, spwshiftlfoadd, sus|
var osc,dry,wetL,wetR,chainL,chainR,bufL,bufR;
osc = In.ar(bus, 2);
spwarp = if(spwarp_<=0, spwarp, Line.kr(spwarp, spwarp_, sus*spwarp_d));
spwarp = if(spwarplfo<=0, spwarp, spwarp * SinOsc.kr(spwarplfo, 0, spwarplfomul, spwarplfoadd));
spwstr = if(spwstr_<=0, spwstr, Line.kr(spwstr, spwstr_, sus*spwstr_d));
spwstr = if(spwstrlfo<=0, spwstr, spwstr * SinOsc.kr(spwstrlfo, 0, spwstrlfomul, spwstrlfoadd));
spwshift = if(spwshift_<=0, spwshift, Line.kr(spwshift, spwshift_, sus*spwshift_d));
spwshift = if(spwshiftlfo<=0, spwshift, spwshift * SinOsc.kr(spwshiftlfo, 0, spwshiftlfomul, spwshiftlfoadd));
dry = osc;
bufL = LocalBuf(2048);
bufR = LocalBuf(2048);
chainL = FFT(bufL, osc[0]);
chainR = FFT(bufR, osc[1]);
chainL = PV_BinShift(chainL, spwstr, spwshift);
chainR = PV_BinShift(chainR, spwstr, spwshift);
wetL = IFFT(chainL);
wetR = IFFT(chainR);
osc = XFade2.ar(dry, [wetL, wetR], spwarp * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;