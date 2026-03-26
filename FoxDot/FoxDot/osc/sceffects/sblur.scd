SynthDef.new(\sblur,
{|bus, sblur, sbluramt, sblur_, sblur_d, sblurlfo, sblurlfomul, sblurlfoadd, sbluramt_, sbluramt_d, sbluramtlfo, sbluramtlfomul, sbluramtlfoadd, sus|
var osc,dry,wetL,wetR,chainL,chainR,bufL,bufR;
osc = In.ar(bus, 2);
sblur = if(sblur_<=0, sblur, Line.kr(sblur, sblur_, sus*sblur_d));
sblur = if(sblurlfo<=0, sblur, sblur * SinOsc.kr(sblurlfo, 0, sblurlfomul, sblurlfoadd));
sbluramt = if(sbluramt_<=0, sbluramt, Line.kr(sbluramt, sbluramt_, sus*sbluramt_d));
sbluramt = if(sbluramtlfo<=0, sbluramt, sbluramt * SinOsc.kr(sbluramtlfo, 0, sbluramtlfomul, sbluramtlfoadd));
dry = osc;
bufL = LocalBuf(2048);
bufR = LocalBuf(2048);
chainL = FFT(bufL, osc[0]);
chainR = FFT(bufR, osc[1]);
chainL = PV_MagSmear(chainL, sbluramt);
chainR = PV_MagSmear(chainR, sbluramt);
chainL = PV_Diffuser(chainL, Dust.kr(2));
chainR = PV_Diffuser(chainR, Dust.kr(2));
wetL = IFFT(chainL);
wetR = IFFT(chainR);
osc = XFade2.ar(dry, [wetL, wetR], sblur * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;