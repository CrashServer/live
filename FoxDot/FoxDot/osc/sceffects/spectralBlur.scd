SynthDef.new(\spectralBlur,
{|bus, sblur, sblurmix, sbluramt, sblur_, sblur_d, sblurlfo, sblurlfomul, sblurlfoadd, sblurmix_, sblurmix_d, sblurmixlfo, sblurmixlfomul, sblurmixlfoadd, sbluramt_, sbluramt_d, sbluramtlfo, sbluramtlfomul, sbluramtlfoadd, sus|
var osc,dry,chain,blurred;
osc = In.ar(bus, 2);
sblur = if(sblur_<=0, sblur, Line.kr(sblur, sblur_, sus*sblur_d));
sblur = if(sblurlfo<=0, sblur, sblur * SinOsc.kr(sblurlfo, 0, sblurlfomul, sblurlfoadd));
sblurmix = if(sblurmix_<=0, sblurmix, Line.kr(sblurmix, sblurmix_, sus*sblurmix_d));
sblurmix = if(sblurmixlfo<=0, sblurmix, sblurmix * SinOsc.kr(sblurmixlfo, 0, sblurmixlfomul, sblurmixlfoadd));
sbluramt = if(sbluramt_<=0, sbluramt, Line.kr(sbluramt, sbluramt_, sus*sbluramt_d));
sbluramt = if(sbluramtlfo<=0, sbluramt, sbluramt * SinOsc.kr(sbluramtlfo, 0, sbluramtlfomul, sbluramtlfoadd));
dry = osc;
chain = FFT(Array.fill(2, { LocalBuf(2048, 1) }), osc);
chain = PV_MagSmear(chain, sbluramt * 20);
blurred = IFFT(chain);
blurred = LeakDC.ar(blurred);
osc = XFade2.ar(dry, (dry * (1 - sblurmix)) + (blurred * sblurmix), sblur * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;