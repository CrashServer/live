SynthDef.new(\decimate,
{|bus, decimate, decbits, decrate, decsmooth, decimate_, decimate_d, decimatelfo, decimatelfomul, decimatelfoadd, decbits_, decbits_d, decbitslfo, decbitslfomul, decbitslfoadd, decrate_, decrate_d, decratelfo, decratelfomul, decratelfoadd, decsmooth_, decsmooth_d, decsmoothlfo, decsmoothlfomul, decsmoothlfoadd, sus|
var osc,dry,destroyed,preFiltered;
osc = In.ar(bus, 2);
decimate = if(decimate_<=0, decimate, Line.kr(decimate, decimate_, sus*decimate_d));
decimate = if(decimatelfo<=0, decimate, decimate * SinOsc.kr(decimatelfo, 0, decimatelfomul, decimatelfoadd));
decbits = if(decbits_<=0, decbits, Line.kr(decbits, decbits_, sus*decbits_d));
decbits = if(decbitslfo<=0, decbits, decbits * SinOsc.kr(decbitslfo, 0, decbitslfomul, decbitslfoadd));
decrate = if(decrate_<=0, decrate, Line.kr(decrate, decrate_, sus*decrate_d));
decrate = if(decratelfo<=0, decrate, decrate * SinOsc.kr(decratelfo, 0, decratelfomul, decratelfoadd));
decsmooth = if(decsmooth_<=0, decsmooth, Line.kr(decsmooth, decsmooth_, sus*decsmooth_d));
decsmooth = if(decsmoothlfo<=0, decsmooth, decsmooth * SinOsc.kr(decsmoothlfo, 0, decsmoothlfomul, decsmoothlfoadd));
dry = osc;
preFiltered = LPF.ar(osc, decrate * 0.4);
destroyed = Latch.ar(preFiltered, Impulse.ar(decrate));
destroyed = destroyed.round(2.pow(decbits.neg));
destroyed = Select.ar(decsmooth > 0, [destroyed, LPF.ar(destroyed, decrate * decsmooth.linlin(0, 1, 0.5, 2))]);
destroyed = (destroyed * 2).wrap(-0.9, 0.9);
destroyed = LeakDC.ar(destroyed);
osc = XFade2.ar(dry, destroyed * 0.8, decimate * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;