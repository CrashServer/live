SynthDef.new(\DafunkFilter,
{|bus, dafilter, dastart, darel, darq, datype, sus, dafilter_, dafilter_d, dafilterlfo, dastart_, dastart_d, dastartlfo, darel_, darel_d, darellfo, darq_, darq_d, darqlfo, datype_, datype_d, datypelfo|
var osc,env,filGen;
osc = In.ar(bus, 2);
dafilter = if(dafilter_<=0, dafilter, Line.kr(dafilter, dafilter_, sus*dafilter_d));
dafilter = if(dafilterlfo<=0, dafilter, dafilter * SinOsc.kr(dafilterlfo, 0, 1, 1));
dastart = if(dastart_<=0, dastart, Line.kr(dastart, dastart_, sus*dastart_d));
dastart = if(dastartlfo<=0, dastart, dastart * SinOsc.kr(dastartlfo, 0, 1, 1));
darel = if(darel_<=0, darel, Line.kr(darel, darel_, sus*darel_d));
darel = if(darellfo<=0, darel, darel * SinOsc.kr(darellfo, 0, 1, 1));
darq = if(darq_<=0, darq, Line.kr(darq, darq_, sus*darq_d));
darq = if(darqlfo<=0, darq, darq * SinOsc.kr(darqlfo, 0, 1, 1));
datype = if(datype_<=0, datype, Line.kr(datype, datype_, sus*datype_d));
datype = if(datypelfo<=0, datype, datype * SinOsc.kr(datypelfo, 0, 1, 1));
env = EnvGen.ar(Env.adsr(0.3, 0.2, sus, darel);, Line.kr(1.0, 0.0, sus/2), doneAction:2);
filGen = EnvGen.ar(Env.adsr(0.4, 0.5, 0.2, 0.5);, Line.kr(1.0, 0.0, sus/2), levelScale: dafilter);
osc = SelectX.ar(datype, [BPF.ar(osc, dastart + filGen, darq), BRF.ar(osc, dastart + filGen, darq)]);
osc = (osc.clip2(0.007) * 24).distort();
ReplaceOut.ar(bus, osc)}).add;