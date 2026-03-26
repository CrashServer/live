SynthDef.new(\mbcomp,
{|bus, mbcomp, mbcxlo, mbcxhi, mbcrat, mbcatk, mbcrel, mbcomp_, mbcomp_d, mbcomplfo, mbcomplfomul, mbcomplfoadd, mbcxlo_, mbcxlo_d, mbcxlolfo, mbcxlolfomul, mbcxlolfoadd, mbcxhi_, mbcxhi_d, mbcxhilfo, mbcxhilfomul, mbcxhilfoadd, mbcrat_, mbcrat_d, mbcratlfo, mbcratlfomul, mbcratlfoadd, mbcatk_, mbcatk_d, mbcatklfo, mbcatklfomul, mbcatklfoadd, mbcrel_, mbcrel_d, mbcrellfo, mbcrellfomul, mbcrellfoadd, sus|
var osc,dry,lo,mid,hi,slopeBelow;
osc = In.ar(bus, 2);
mbcomp = if(mbcomp_<=0, mbcomp, Line.kr(mbcomp, mbcomp_, sus*mbcomp_d));
mbcomp = if(mbcomplfo<=0, mbcomp, mbcomp * SinOsc.kr(mbcomplfo, 0, mbcomplfomul, mbcomplfoadd));
mbcxlo = if(mbcxlo_<=0, mbcxlo, Line.kr(mbcxlo, mbcxlo_, sus*mbcxlo_d));
mbcxlo = if(mbcxlolfo<=0, mbcxlo, mbcxlo * SinOsc.kr(mbcxlolfo, 0, mbcxlolfomul, mbcxlolfoadd));
mbcxhi = if(mbcxhi_<=0, mbcxhi, Line.kr(mbcxhi, mbcxhi_, sus*mbcxhi_d));
mbcxhi = if(mbcxhilfo<=0, mbcxhi, mbcxhi * SinOsc.kr(mbcxhilfo, 0, mbcxhilfomul, mbcxhilfoadd));
mbcrat = if(mbcrat_<=0, mbcrat, Line.kr(mbcrat, mbcrat_, sus*mbcrat_d));
mbcrat = if(mbcratlfo<=0, mbcrat, mbcrat * SinOsc.kr(mbcratlfo, 0, mbcratlfomul, mbcratlfoadd));
mbcatk = if(mbcatk_<=0, mbcatk, Line.kr(mbcatk, mbcatk_, sus*mbcatk_d));
mbcatk = if(mbcatklfo<=0, mbcatk, mbcatk * SinOsc.kr(mbcatklfo, 0, mbcatklfomul, mbcatklfoadd));
mbcrel = if(mbcrel_<=0, mbcrel, Line.kr(mbcrel, mbcrel_, sus*mbcrel_d));
mbcrel = if(mbcrellfo<=0, mbcrel, mbcrel * SinOsc.kr(mbcrellfo, 0, mbcrellfomul, mbcrellfoadd));
dry = osc;
slopeBelow = 1 / mbcrat.max(1);
lo = LPF.ar(LPF.ar(osc, mbcxlo), mbcxlo);
hi = HPF.ar(HPF.ar(osc, mbcxhi), mbcxhi);
mid = osc - lo - hi;
lo = Compander.ar(lo, lo, 0.3, slopeBelow, 1, mbcatk, mbcrel);
mid = Compander.ar(mid, mid, 0.25, slopeBelow, 1, mbcatk, mbcrel);
hi = Compander.ar(hi, hi, 0.2, slopeBelow, 1, mbcatk, mbcrel);
osc = XFade2.ar(dry, LeakDC.ar(lo + mid + hi), mbcomp * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;