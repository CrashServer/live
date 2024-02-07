SynthDef.new(\DafunkFilter,
{|bus, dafilter, dastart, darel, darq, datype, sus, dafilter_, dastart_, darel_, darq_, datype_|
var osc,env,filGen;
osc = In.ar(bus, 2);
dafilter = dafilter+Line.kr(0, dafilter_, sus);
dastart = dastart+Line.kr(0, dastart_, sus);
darel = darel+Line.kr(0, darel_, sus);
darq = darq+Line.kr(0, darq_, sus);
datype = datype+Line.kr(0, datype_, sus);
env = EnvGen.ar(Env.adsr(0.3, 0.2, sus, darel);, Line.kr(1.0, 0.0, sus/2), doneAction:2);
filGen = EnvGen.ar(Env.adsr(0.4, 0.5, 0.2, 0.5);, Line.kr(1.0, 0.0, sus/2), levelScale: dafilter);
osc = SelectX.ar(datype, [BPF.ar(osc, dastart + filGen, darq), BRF.ar(osc, dastart + filGen, darq)]);
osc = (osc.clip2(0.007) * 24).distort();
ReplaceOut.ar(bus, osc)}).add;