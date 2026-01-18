SynthDef.new(\spectralfreeze,
{|bus, freeze, freezemix, freezerand, freeze_, freeze_d, freezelfo, freezelfomul, freezelfoadd, freezemix_, freezemix_d, freezemixlfo, freezemixlfomul, freezemixlfoadd, freezerand_, freezerand_d, freezerandlfo, freezerandlfomul, freezerandlfoadd, sus|
var osc,dry,chain,frozen;
osc = In.ar(bus, 2);
freeze = if(freeze_<=0, freeze, Line.kr(freeze, freeze_, sus*freeze_d));
freeze = if(freezelfo<=0, freeze, freeze * SinOsc.kr(freezelfo, 0, freezelfomul, freezelfoadd));
freezemix = if(freezemix_<=0, freezemix, Line.kr(freezemix, freezemix_, sus*freezemix_d));
freezemix = if(freezemixlfo<=0, freezemix, freezemix * SinOsc.kr(freezemixlfo, 0, freezemixlfomul, freezemixlfoadd));
freezerand = if(freezerand_<=0, freezerand, Line.kr(freezerand, freezerand_, sus*freezerand_d));
freezerand = if(freezerandlfo<=0, freezerand, freezerand * SinOsc.kr(freezerandlfo, 0, freezerandlfomul, freezerandlfoadd));
dry = osc;
chain = FFT(Array.fill(2, { LocalBuf(2048, 1) }), osc);
chain = PV_MagFreeze(chain, freeze > 0.5);
chain = PV_MagSmear(chain, freezerand * 10);
frozen = IFFT(chain);
frozen = LeakDC.ar(frozen);
osc = XFade2.ar(dry, (dry * (1 - freezemix)) + (frozen * freezemix), freeze * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;