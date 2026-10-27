SynthDef.new(\darkverb,
{|bus, darkverb=0.5, dvdecay=3, dvdamp=0.8, dvcut=2000, sus,
  darkverb_, darkverb_d, darkverblfo, darkverblfomul, darkverblfoadd,
  dvdecay_, dvdecay_d, dvdecaylfo, dvdecaylfomul, dvdecaylfoadd,
  dvdamp_, dvdamp_d, dvdamplfo, dvdamplfomul, dvdamplfoadd,
  dvcut_, dvcut_d, dvcutlfo, dvcutlfomul, dvcutlfoadd|
var osc, dry, wet, filtered;
osc = In.ar(bus, 2);
dry = osc;
darkverb = if(darkverb_<=0, darkverb, Line.kr(darkverb, darkverb_, sus*darkverb_d));
darkverb = if(darkverblfo<=0, darkverb, darkverb * SinOsc.kr(darkverblfo, 0, darkverblfomul, darkverblfoadd));
dvdecay = if(dvdecay_<=0, dvdecay, Line.kr(dvdecay, dvdecay_, sus*dvdecay_d));
dvdecay = if(dvdecaylfo<=0, dvdecay, dvdecay * SinOsc.kr(dvdecaylfo, 0, dvdecaylfomul, dvdecaylfoadd));
dvdamp = if(dvdamp_<=0, dvdamp, Line.kr(dvdamp, dvdamp_, sus*dvdamp_d));
dvdamp = if(dvdamplfo<=0, dvdamp, dvdamp * SinOsc.kr(dvdamplfo, 0, dvdamplfomul, dvdamplfoadd));
dvcut = if(dvcut_<=0, dvcut, Line.kr(dvcut, dvcut_, sus*dvcut_d));
dvcut = if(dvcutlfo<=0, dvcut, dvcut * SinOsc.kr(dvcutlfo, 0, dvcutlfomul, dvcutlfoadd));
// Pre-filter before reverb
filtered = LPF.ar(osc, dvcut);
filtered = HPF.ar(filtered, 100);
// GVerb for dense dark reverb
wet = GVerb.ar(Mix(filtered), 80, dvdecay, dvdamp, 0.5, 15, -12, -12, -12);
wet = LPF.ar(wet, dvcut * 0.8); // Post filter too
wet = LeakDC.ar(wet);
osc = XFade2.ar(dry, wet * 0.3, darkverb * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;
