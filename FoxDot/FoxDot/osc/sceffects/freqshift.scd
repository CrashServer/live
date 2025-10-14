SynthDef.new(\freqshift,
{|bus, fshift, fphase, fmix, fshift_, fshift_d, fshiftlfo, fshiftlfomul, fshiftlfoadd, fphase_, fphase_d, fphaselfo, fphaselfomul, fphaselfoadd, fmix_, fmix_d, fmixlfo, fmixlfomul, fmixlfoadd, sus|
var osc,dry,wet;
osc = In.ar(bus, 2);
fshift = if(fshift_<=0, fshift, Line.kr(fshift, fshift_, sus*fshift_d));
fshift = if(fshiftlfo<=0, fshift, fshift * SinOsc.kr(fshiftlfo, 0, fshiftlfomul, fshiftlfoadd));
fphase = if(fphase_<=0, fphase, Line.kr(fphase, fphase_, sus*fphase_d));
fphase = if(fphaselfo<=0, fphase, fphase * SinOsc.kr(fphaselfo, 0, fphaselfomul, fphaselfoadd));
fmix = if(fmix_<=0, fmix, Line.kr(fmix, fmix_, sus*fmix_d));
fmix = if(fmixlfo<=0, fmix, fmix * SinOsc.kr(fmixlfo, 0, fmixlfomul, fmixlfoadd));
dry = osc;
wet = FreqShift.ar(osc, fshift, fphase);
osc = SelectX.ar(fmix, [dry, wet]);
ReplaceOut.ar(bus, osc)}).add;