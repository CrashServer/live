SynthDef.new(\combres,
{|bus, combres, combfreq, combdecay, combspread, combres_, combres_d, combreslfo, combreslfomul, combreslfoadd, combfreq_, combfreq_d, combfreqlfo, combfreqlfomul, combfreqlfoadd, combdecay_, combdecay_d, combdecaylfo, combdecaylfomul, combdecaylfoadd, combspread_, combspread_d, combspreadlfo, combspreadlfomul, combspreadlfoadd, sus|
var osc,dry,comb1,comb2,resonated,delayTime;
osc = In.ar(bus, 2);
combres = if(combres_<=0, combres, Line.kr(combres, combres_, sus*combres_d));
combres = if(combreslfo<=0, combres, combres * SinOsc.kr(combreslfo, 0, combreslfomul, combreslfoadd));
combfreq = if(combfreq_<=0, combfreq, Line.kr(combfreq, combfreq_, sus*combfreq_d));
combfreq = if(combfreqlfo<=0, combfreq, combfreq * SinOsc.kr(combfreqlfo, 0, combfreqlfomul, combfreqlfoadd));
combdecay = if(combdecay_<=0, combdecay, Line.kr(combdecay, combdecay_, sus*combdecay_d));
combdecay = if(combdecaylfo<=0, combdecay, combdecay * SinOsc.kr(combdecaylfo, 0, combdecaylfomul, combdecaylfoadd));
combspread = if(combspread_<=0, combspread, Line.kr(combspread, combspread_, sus*combspread_d));
combspread = if(combspreadlfo<=0, combspread, combspread * SinOsc.kr(combspreadlfo, 0, combspreadlfomul, combspreadlfoadd));
dry = osc;
delayTime = combfreq.reciprocal;
comb1 = CombC.ar(osc, 0.1, delayTime.clip(0.0001, 0.1), combdecay);
comb2 = CombC.ar(osc, 0.1, (delayTime * (1 + combspread)).clip(0.0001, 0.1), combdecay * 0.9);
resonated = (comb1 + comb2) * 0.5;
resonated = LPF.ar(resonated, 10000);
resonated = LeakDC.ar(resonated);
osc = XFade2.ar(dry, dry + (resonated * 0.5), combres * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;