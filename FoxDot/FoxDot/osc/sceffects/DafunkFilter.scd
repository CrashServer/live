SynthDef.new(\DafunkFilter,
{|bus, dafilter, dastart, darel, darq, datype, sus|
var osc,env,filGen;
osc = In.ar(bus, 2);
env = EnvGen.ar(Env.adsr(0.3, 0.2, sus, darel);, Line.kr(1.0, 0.0, sus/2), doneAction:2);
filGen = EnvGen.ar(Env.adsr(0.4, 0.5, 0.2, 0.5);, Line.kr(1.0, 0.0, sus/2), levelScale: dafilter);
osc = SelectX.ar(datype, [BPF.ar(osc, dastart + filGen, darq), BRF.ar(osc, dastart + filGen, darq)]);
osc = (osc.clip2(0.007) * 24).distort();
ReplaceOut.ar(bus, osc)}).add;
// source https://github.com/jivimberg/punkt