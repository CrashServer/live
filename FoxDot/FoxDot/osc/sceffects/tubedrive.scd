SynthDef.new(\tubedrive,
{|bus, tube, tubegain, tubewarm, tubebias, tube_, tube_d, tubelfo, tubelfomul, tubelfoadd, tubegain_, tubegain_d, tubegainlfo, tubegainlfomul, tubegainlfoadd, tubewarm_, tubewarm_d, tubewarmlfo, tubewarmlfomul, tubewarmlfoadd, tubebias_, tubebias_d, tubebiaslfo, tubebiaslfomul, tubebiaslfoadd, sus|
var osc,dry,biased,saturated,harmonics,compressed;
osc = In.ar(bus, 2);
tube = if(tube_<=0, tube, Line.kr(tube, tube_, sus*tube_d));
tube = if(tubelfo<=0, tube, tube * SinOsc.kr(tubelfo, 0, tubelfomul, tubelfoadd));
tubegain = if(tubegain_<=0, tubegain, Line.kr(tubegain, tubegain_, sus*tubegain_d));
tubegain = if(tubegainlfo<=0, tubegain, tubegain * SinOsc.kr(tubegainlfo, 0, tubegainlfomul, tubegainlfoadd));
tubewarm = if(tubewarm_<=0, tubewarm, Line.kr(tubewarm, tubewarm_, sus*tubewarm_d));
tubewarm = if(tubewarmlfo<=0, tubewarm, tubewarm * SinOsc.kr(tubewarmlfo, 0, tubewarmlfomul, tubewarmlfoadd));
tubebias = if(tubebias_<=0, tubebias, Line.kr(tubebias, tubebias_, sus*tubebias_d));
tubebias = if(tubebiaslfo<=0, tubebias, tubebias * SinOsc.kr(tubebiaslfo, 0, tubebiaslfomul, tubebiaslfoadd));
dry = osc;
osc = Compander.ar(osc, osc, 0.3, 1, 0.5, 0.001, 0.06, 1.3);
biased = osc + (tubebias * 0.15);
saturated = biased * tubegain * 1.8;
saturated = saturated - (saturated.cubed * 0.25);
saturated = saturated + (saturated.squared.sign * saturated.squared.abs * 0.1);
harmonics = (osc.squared * tubewarm * 0.4).softclip;
harmonics = harmonics + (osc.cubed * tubewarm * 0.15);
saturated = saturated + harmonics;
saturated = saturated.softclip;
saturated = LeakDC.ar(saturated);
saturated = LPF.ar(saturated, 9000);
saturated = BLowShelf.ar(saturated, 150, 0.7, tubewarm * 2);
saturated = BPeakEQ.ar(saturated, 2500, 0.6, tubewarm * 1.5);
compressed = Compander.ar(saturated, saturated, 0.35, 1, 0.6, 0.003, 0.06, 1.3);
osc = XFade2.ar(dry, compressed * 0.8, tube * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;