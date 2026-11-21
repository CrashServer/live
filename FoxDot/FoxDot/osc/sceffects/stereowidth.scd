SynthDef.new(\stereowidth,
{|bus, stereowidth, swfreq, swnarrow, swwide, stereowidth_, stereowidth_d, stereowidthlfo, stereowidthlfomul, stereowidthlfoadd, stereowidthlfophase, swfreq_, swfreq_d, swfreqlfo, swfreqlfomul, swfreqlfoadd, swfreqlfophase, swnarrow_, swnarrow_d, swnarrowlfo, swnarrowlfomul, swnarrowlfoadd, swnarrowlfophase, swwide_, swwide_d, swwidelfo, swwidelfomul, swwidelfoadd, swwidelfophase, sus|
var osc,dry,low,high,mid,side,widened;
osc = In.ar(bus, 2);
stereowidth = if(stereowidth_<=0, stereowidth, Line.kr(stereowidth, stereowidth_, sus*stereowidth_d));
stereowidth = if(stereowidthlfo<=0, stereowidth, stereowidth * SinOsc.kr(stereowidthlfo, stereowidthlfophase, stereowidthlfomul, stereowidthlfoadd));
swfreq = if(swfreq_<=0, swfreq, Line.kr(swfreq, swfreq_, sus*swfreq_d));
swfreq = if(swfreqlfo<=0, swfreq, swfreq * SinOsc.kr(swfreqlfo, swfreqlfophase, swfreqlfomul, swfreqlfoadd));
swnarrow = if(swnarrow_<=0, swnarrow, Line.kr(swnarrow, swnarrow_, sus*swnarrow_d));
swnarrow = if(swnarrowlfo<=0, swnarrow, swnarrow * SinOsc.kr(swnarrowlfo, swnarrowlfophase, swnarrowlfomul, swnarrowlfoadd));
swwide = if(swwide_<=0, swwide, Line.kr(swwide, swwide_, sus*swwide_d));
swwide = if(swwidelfo<=0, swwide, swwide * SinOsc.kr(swwidelfo, swwidelfophase, swwidelfomul, swwidelfoadd));
dry = osc;
low = LPF.ar(osc, swfreq);
low = (low[0] + low[1]) * 0.5;
low = low * (1 - swnarrow);
low = [low, low];
high = HPF.ar(osc, swfreq);
mid = (high[0] + high[1]) * 0.5;
side = (high[0] - high[1]) * 0.5 * swwide;
high = [mid + side, mid - side];
widened = low + high;
osc = XFade2.ar(dry, widened, stereowidth * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;