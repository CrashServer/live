SynthDef.new(\spectralShift,
{|bus, sshift, sshiftmix, sshiftamt, sshiftstretch, sshift_, sshift_d, sshiftlfo, sshiftlfomul, sshiftlfoadd, sshiftmix_, sshiftmix_d, sshiftmixlfo, sshiftmixlfomul, sshiftmixlfoadd, sshiftamt_, sshiftamt_d, sshiftamtlfo, sshiftamtlfomul, sshiftamtlfoadd, sshiftstretch_, sshiftstretch_d, sshiftstretchlfo, sshiftstretchlfomul, sshiftstretchlfoadd, sus|
var osc,dry,chain,shifted;
osc = In.ar(bus, 2);
sshift = if(sshift_<=0, sshift, Line.kr(sshift, sshift_, sus*sshift_d));
sshift = if(sshiftlfo<=0, sshift, sshift * SinOsc.kr(sshiftlfo, 0, sshiftlfomul, sshiftlfoadd));
sshiftmix = if(sshiftmix_<=0, sshiftmix, Line.kr(sshiftmix, sshiftmix_, sus*sshiftmix_d));
sshiftmix = if(sshiftmixlfo<=0, sshiftmix, sshiftmix * SinOsc.kr(sshiftmixlfo, 0, sshiftmixlfomul, sshiftmixlfoadd));
sshiftamt = if(sshiftamt_<=0, sshiftamt, Line.kr(sshiftamt, sshiftamt_, sus*sshiftamt_d));
sshiftamt = if(sshiftamtlfo<=0, sshiftamt, sshiftamt * SinOsc.kr(sshiftamtlfo, 0, sshiftamtlfomul, sshiftamtlfoadd));
sshiftstretch = if(sshiftstretch_<=0, sshiftstretch, Line.kr(sshiftstretch, sshiftstretch_, sus*sshiftstretch_d));
sshiftstretch = if(sshiftstretchlfo<=0, sshiftstretch, sshiftstretch * SinOsc.kr(sshiftstretchlfo, 0, sshiftstretchlfomul, sshiftstretchlfoadd));
dry = osc;
chain = FFT(Array.fill(2, { LocalBuf(2048, 1) }), osc);
chain = PV_BinShift(chain, sshiftstretch, sshiftamt);
shifted = IFFT(chain);
shifted = LeakDC.ar(shifted);
osc = XFade2.ar(dry, (dry * (1 - sshiftmix)) + (shifted * sshiftmix), sshift * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;