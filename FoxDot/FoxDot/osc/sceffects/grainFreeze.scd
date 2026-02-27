SynthDef.new(\grainFreeze,
{|bus, gfreeze, gfreeze_dur, gfreeze_density, gfreeze_, gfreeze_d, gfreezelfo, gfreezelfomul, gfreezelfoadd, gfreeze_dur_, gfreeze_dur_d, gfreeze_durlfo, gfreeze_durlfomul, gfreeze_durlfoadd, gfreeze_density_, gfreeze_density_d, gfreeze_densitylfo, gfreeze_densitylfomul, gfreeze_densitylfoadd, sus|
var osc,freezeBuf,freezeTrig,freezeSig;
osc = In.ar(bus, 2);
gfreeze = if(gfreeze_<=0, gfreeze, Line.kr(gfreeze, gfreeze_, sus*gfreeze_d));
gfreeze = if(gfreezelfo<=0, gfreeze, gfreeze * SinOsc.kr(gfreezelfo, 0, gfreezelfomul, gfreezelfoadd));
gfreeze_dur = if(gfreeze_dur_<=0, gfreeze_dur, Line.kr(gfreeze_dur, gfreeze_dur_, sus*gfreeze_dur_d));
gfreeze_dur = if(gfreeze_durlfo<=0, gfreeze_dur, gfreeze_dur * SinOsc.kr(gfreeze_durlfo, 0, gfreeze_durlfomul, gfreeze_durlfoadd));
gfreeze_density = if(gfreeze_density_<=0, gfreeze_density, Line.kr(gfreeze_density, gfreeze_density_, sus*gfreeze_density_d));
gfreeze_density = if(gfreeze_densitylfo<=0, gfreeze_density, gfreeze_density * SinOsc.kr(gfreeze_densitylfo, 0, gfreeze_densitylfomul, gfreeze_densitylfoadd));
freezeBuf = LocalBuf(SampleRate.ir * gfreeze_dur, 2).clear;
RecordBuf.ar(osc, freezeBuf, loop: 1);
freezeTrig = Impulse.ar(gfreeze_density);
freezeSig = GrainBuf.ar(2, freezeTrig, gfreeze_dur * 0.8, freezeBuf, 1, LFNoise0.kr(gfreeze_density * 0.25).range(0, 1), 2, 0);
osc = XFade2.ar(osc, freezeSig, gfreeze * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;