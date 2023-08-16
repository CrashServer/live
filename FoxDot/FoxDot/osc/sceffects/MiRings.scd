SynthDef.new(\MiRings,
{|bus, mring, rstruct, rbright, rdamp, rpos, rmodel, rpoly, regg, sus, rsus|
var osc,dry,pitch;
osc = In.ar(bus, 2);
pitch = In.kr(bus, 1);
dry = osc;
osc = MiRings.ar(in: osc,trig:1,pit: pitch.cpsmidi.clip(1,80),struct: rstruct, bright: rbright, damp: rdamp, pos: rpos, model: rmodel, poly: rpoly, intern_exciter: 1, easteregg: regg, mul: 1);
osc = osc * EnvGen.kr(Env([1,1,0], [sus*rsus, 0.01]), doneAction: 2);
osc = SelectX.ar(mring, [dry, osc], wrap:1);
ReplaceOut.ar(bus, osc)}).add;