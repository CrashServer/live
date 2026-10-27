SynthDef.new(\spectralMorph,
{|bus, smorph, smorphmix, smorphrate, smorphfreeze, smorph_, smorph_d, smorphlfo, smorphlfomul, smorphlfoadd, smorphmix_, smorphmix_d, smorphmixlfo, smorphmixlfomul, smorphmixlfoadd, smorphrate_, smorphrate_d, smorphratelfo, smorphratelfomul, smorphratelfoadd, smorphfreeze_, smorphfreeze_d, smorphfreezelfo, smorphfreezelfomul, smorphfreezelfoadd, sus|
var osc,dry,refBuf,refSig,chainA,chainB,morphed;
osc = In.ar(bus, 2);
smorph = if(smorph_<=0, smorph, Line.kr(smorph, smorph_, sus*smorph_d));
smorph = if(smorphlfo<=0, smorph, smorph * SinOsc.kr(smorphlfo, 0, smorphlfomul, smorphlfoadd));
smorphmix = if(smorphmix_<=0, smorphmix, Line.kr(smorphmix, smorphmix_, sus*smorphmix_d));
smorphmix = if(smorphmixlfo<=0, smorphmix, smorphmix * SinOsc.kr(smorphmixlfo, 0, smorphmixlfomul, smorphmixlfoadd));
smorphrate = if(smorphrate_<=0, smorphrate, Line.kr(smorphrate, smorphrate_, sus*smorphrate_d));
smorphrate = if(smorphratelfo<=0, smorphrate, smorphrate * SinOsc.kr(smorphratelfo, 0, smorphratelfomul, smorphratelfoadd));
smorphfreeze = if(smorphfreeze_<=0, smorphfreeze, Line.kr(smorphfreeze, smorphfreeze_, sus*smorphfreeze_d));
smorphfreeze = if(smorphfreezelfo<=0, smorphfreeze, smorphfreeze * SinOsc.kr(smorphfreezelfo, 0, smorphfreezelfomul, smorphfreezelfoadd));
dry = osc;
refBuf = LocalBuf(SampleRate.ir * 0.25, 2).clear;
RecordBuf.ar(osc, refBuf, run: (1 - smorphfreeze), loop: 1);
refSig = PlayBuf.ar(2, refBuf, smorphrate, loop: 1);
chainA = FFT(Array.fill(2, { LocalBuf(2048, 1) }), osc);
chainB = FFT(Array.fill(2, { LocalBuf(2048, 1) }), refSig);
chainA = PV_MagMul(chainA, chainB);
morphed = IFFT(chainA);
morphed = LeakDC.ar(morphed);
osc = XFade2.ar(dry, (dry * (1 - smorphmix)) + (morphed * smorphmix), smorph * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;