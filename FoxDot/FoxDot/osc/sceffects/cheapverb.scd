SynthDef.new(\cheapverb,
{|bus, cheapverb, cvdecay, cvdamp, cheapverb_, cheapverb_d, cheapverblfo, cheapverblfomul, cheapverblfoadd, cvdecay_, cvdecay_d, cvdecaylfo, cvdecaylfomul, cvdecaylfoadd, cvdamp_, cvdamp_d, cvdamplfo, cvdamplfomul, cvdamplfoadd, sus|
var osc,dry,src,c1,c2,c3,c4,wet,lpf;
osc = In.ar(bus, 2);
cheapverb = if(cheapverb_<=0, cheapverb, Line.kr(cheapverb, cheapverb_, sus*cheapverb_d));
cheapverb = if(cheapverblfo<=0, cheapverb, cheapverb * SinOsc.kr(cheapverblfo, 0, cheapverblfomul, cheapverblfoadd));
cvdecay = if(cvdecay_<=0, cvdecay, Line.kr(cvdecay, cvdecay_, sus*cvdecay_d));
cvdecay = if(cvdecaylfo<=0, cvdecay, cvdecay * SinOsc.kr(cvdecaylfo, 0, cvdecaylfomul, cvdecaylfoadd));
cvdamp = if(cvdamp_<=0, cvdamp, Line.kr(cvdamp, cvdamp_, sus*cvdamp_d));
cvdamp = if(cvdamplfo<=0, cvdamp, cvdamp * SinOsc.kr(cvdamplfo, 0, cvdamplfomul, cvdamplfoadd));
dry = osc;
src = HPF.ar(osc, 80);
lpf = 2000 + ((1 - cvdamp) * 8000);
c1 = LPF.ar(CombC.ar(src, 0.05, 0.0297, cvdecay), lpf);
c2 = LPF.ar(CombC.ar(src, 0.05, 0.0371, cvdecay * 0.9), lpf);
c3 = LPF.ar(CombC.ar(src, 0.05, 0.0411, cvdecay * 1.1), lpf);
c4 = LPF.ar(CombC.ar(src, 0.05, 0.0437, cvdecay * 0.95), lpf);
wet = c1 + c2 + c3 + c4;
wet = AllpassC.ar(wet, 0.02, 0.005, 0.08);
wet = AllpassC.ar(wet, 0.02, 0.012, 0.06);
wet = LeakDC.ar(wet * 0.25);
osc = XFade2.ar(dry, wet, cheapverb * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;