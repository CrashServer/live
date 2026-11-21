SynthDef.new(\spectralShift,
{|bus, sshift, sshiftmix, sshiftamt, sshiftstretch, sshift_, sshift_d, sshiftlfo, sshiftlfomul, sshiftlfoadd, sshiftlfophase, sshiftmix_, sshiftmix_d, sshiftmixlfo, sshiftmixlfomul, sshiftmixlfoadd, sshiftmixlfophase, sshiftamt_, sshiftamt_d, sshiftamtlfo, sshiftamtlfomul, sshiftamtlfoadd, sshiftamtlfophase, sshiftstretch_, sshiftstretch_d, sshiftstretchlfo, sshiftstretchlfomul, sshiftstretchlfoadd, sshiftstretchlfophase, sus|
var osc,dry,chain,shifted;
osc = In.ar(bus, 2);
sshift = if(sshift_<=0, sshift, Line.kr(sshift, sshift_, sus*sshift_d));
sshift = if(sshiftlfo<=0, sshift, sshift * SinOsc.kr(sshiftlfo, sshiftlfophase, sshiftlfomul, sshiftlfoadd));
sshiftmix = if(sshiftmix_<=0, sshiftmix, Line.kr(sshiftmix, sshiftmix_, sus*sshiftmix_d));
sshiftmix = if(sshiftmixlfo<=0, sshiftmix, sshiftmix * SinOsc.kr(sshiftmixlfo, sshiftmixlfophase, sshiftmixlfomul, sshiftmixlfoadd));
sshiftamt = if(sshiftamt_<=0, sshiftamt, Line.kr(sshiftamt, sshiftamt_, sus*sshiftamt_d));
sshiftamt = if(sshiftamtlfo<=0, sshiftamt, sshiftamt * SinOsc.kr(sshiftamtlfo, sshiftamtlfophase, sshiftamtlfomul, sshiftamtlfoadd));
sshiftstretch = if(sshiftstretch_<=0, sshiftstretch, Line.kr(sshiftstretch, sshiftstretch_, sus*sshiftstretch_d));
sshiftstretch = if(sshiftstretchlfo<=0, sshiftstretch, sshiftstretch * SinOsc.kr(sshiftstretchlfo, sshiftstretchlfophase, sshiftstretchlfomul, sshiftstretchlfoadd));
dry = osc;
chain = FFT(Array.fill(2, { LocalBuf(2048, 1) }), osc);
chain = PV_BinShift(chain, sshiftstretch, sshiftamt);
shifted = IFFT(chain);
shifted = LeakDC.ar(shifted);
osc = XFade2.ar(dry, (dry * (1 - sshiftmix)) + (shifted * sshiftmix), sshift * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;