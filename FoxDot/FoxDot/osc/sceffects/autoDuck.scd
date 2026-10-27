SynthDef.new(\autoDuck,
{|bus, duck, duckamt, duckatk, duckrel, duckthresh, duck_, duck_d, ducklfo, ducklfomul, ducklfoadd, duckamt_, duckamt_d, duckamtlfo, duckamtlfomul, duckamtlfoadd, duckatk_, duckatk_d, duckatklfo, duckatklfomul, duckatklfoadd, duckrel_, duckrel_d, duckrellfo, duckrellfomul, duckrellfoadd, duckthresh_, duckthresh_d, duckthreshlfo, duckthreshlfomul, duckthreshlfoadd, sus|
var osc,duckSrc,duckSlope;
osc = In.ar(bus, 2);
duck = if(duck_<=0, duck, Line.kr(duck, duck_, sus*duck_d));
duck = if(ducklfo<=0, duck, duck * SinOsc.kr(ducklfo, 0, ducklfomul, ducklfoadd));
duckamt = if(duckamt_<=0, duckamt, Line.kr(duckamt, duckamt_, sus*duckamt_d));
duckamt = if(duckamtlfo<=0, duckamt, duckamt * SinOsc.kr(duckamtlfo, 0, duckamtlfomul, duckamtlfoadd));
duckatk = if(duckatk_<=0, duckatk, Line.kr(duckatk, duckatk_, sus*duckatk_d));
duckatk = if(duckatklfo<=0, duckatk, duckatk * SinOsc.kr(duckatklfo, 0, duckatklfomul, duckatklfoadd));
duckrel = if(duckrel_<=0, duckrel, Line.kr(duckrel, duckrel_, sus*duckrel_d));
duckrel = if(duckrellfo<=0, duckrel, duckrel * SinOsc.kr(duckrellfo, 0, duckrellfomul, duckrellfoadd));
duckthresh = if(duckthresh_<=0, duckthresh, Line.kr(duckthresh, duckthresh_, sus*duckthresh_d));
duckthresh = if(duckthreshlfo<=0, duckthresh, duckthresh * SinOsc.kr(duckthreshlfo, 0, duckthreshlfomul, duckthreshlfoadd));
duckSrc = In.ar(duck, 1);
duckSlope = 1 - duckamt;
osc = Compander.ar(osc, duckSrc, thresh: duckthresh, slopeAbove: duckSlope, slopeBelow: 1, clampTime: duckatk, relaxTime: duckrel, mul: 1);
ReplaceOut.ar(bus, osc)}).add;