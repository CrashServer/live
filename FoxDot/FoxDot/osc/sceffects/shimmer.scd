SynthDef.new(\shimmer,
{|bus, shimmer, shimsize, shimpitch, shimmix, shimmer_, shimmer_d, shimmerlfo, shimmerlfomul, shimmerlfoadd, shimsize_, shimsize_d, shimsizelfo, shimsizelfomul, shimsizelfoadd, shimpitch_, shimpitch_d, shimpitchlfo, shimpitchlfomul, shimpitchlfoadd, shimmix_, shimmix_d, shimmixlfo, shimmixlfomul, shimmixlfoadd, sus|
var osc,dry,pitched,reverbed,wet;
osc = In.ar(bus, 2);
shimmer = if(shimmer_<=0, shimmer, Line.kr(shimmer, shimmer_, sus*shimmer_d));
shimmer = if(shimmerlfo<=0, shimmer, shimmer * SinOsc.kr(shimmerlfo, 0, shimmerlfomul, shimmerlfoadd));
shimsize = if(shimsize_<=0, shimsize, Line.kr(shimsize, shimsize_, sus*shimsize_d));
shimsize = if(shimsizelfo<=0, shimsize, shimsize * SinOsc.kr(shimsizelfo, 0, shimsizelfomul, shimsizelfoadd));
shimpitch = if(shimpitch_<=0, shimpitch, Line.kr(shimpitch, shimpitch_, sus*shimpitch_d));
shimpitch = if(shimpitchlfo<=0, shimpitch, shimpitch * SinOsc.kr(shimpitchlfo, 0, shimpitchlfomul, shimpitchlfoadd));
shimmix = if(shimmix_<=0, shimmix, Line.kr(shimmix, shimmix_, sus*shimmix_d));
shimmix = if(shimmixlfo<=0, shimmix, shimmix * SinOsc.kr(shimmixlfo, 0, shimmixlfomul, shimmixlfoadd));
dry = osc;
pitched = PitchShift.ar(osc, 0.2, LinExp.kr(shimpitch, 0, 1, 1, 2), 0, 0.01);
reverbed = FreeVerb.ar(osc + (pitched * 0.5), shimmix, shimsize);
wet = reverbed * LinLin.kr(shimmer, 0, 1, 0.3, 1.5);
osc = SelectX.ar(shimmer, [dry, wet]);
ReplaceOut.ar(bus, osc)}).add;