SynthDef.new(\tapestop,
{|bus, tstop, tstoptime, tstopcurve, tstopdir, sus, tstop_, tstop_d, tstoplfo, tstoplfomul, tstoplfoadd, tstoptime_, tstoptime_d, tstoptimelfo, tstoptimelfomul, tstoptimelfoadd, tstopcurve_, tstopcurve_d, tstopcurvelfo, tstopcurvelfomul, tstopcurvelfoadd, tstopdir_, tstopdir_d, tstopdirlfo, tstopdirlfomul, tstopdirlfoadd|
var osc,dry,rate,stopped,startRate,endRate;
osc = In.ar(bus, 2);
tstop = if(tstop_<=0, tstop, Line.kr(tstop, tstop_, sus*tstop_d));
tstop = if(tstoplfo<=0, tstop, tstop * SinOsc.kr(tstoplfo, 0, tstoplfomul, tstoplfoadd));
tstoptime = if(tstoptime_<=0, tstoptime, Line.kr(tstoptime, tstoptime_, sus*tstoptime_d));
tstoptime = if(tstoptimelfo<=0, tstoptime, tstoptime * SinOsc.kr(tstoptimelfo, 0, tstoptimelfomul, tstoptimelfoadd));
tstopcurve = if(tstopcurve_<=0, tstopcurve, Line.kr(tstopcurve, tstopcurve_, sus*tstopcurve_d));
tstopcurve = if(tstopcurvelfo<=0, tstopcurve, tstopcurve * SinOsc.kr(tstopcurvelfo, 0, tstopcurvelfomul, tstopcurvelfoadd));
tstopdir = if(tstopdir_<=0, tstopdir, Line.kr(tstopdir, tstopdir_, sus*tstopdir_d));
tstopdir = if(tstopdirlfo<=0, tstopdir, tstopdir * SinOsc.kr(tstopdirlfo, 0, tstopdirlfomul, tstopdirlfoadd));
dry = osc;
startRate = Select.kr(tstopdir, [1, 0.1]);
endRate = Select.kr(tstopdir, [0.1, 1]);
rate = EnvGen.kr(Env([startRate, endRate], [tstoptime * sus], tstopcurve));
stopped = PitchShift.ar(osc, 0.1, rate, 0, 0.01);
stopped = stopped * rate.sqrt;
osc = XFade2.ar(dry, stopped, tstop * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;