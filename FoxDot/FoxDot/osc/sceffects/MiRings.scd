SynthDef.new(\MiRings,
{|bus, mring, rstruct, rbright, rdamp, rpos, rmodel, rpoly, regg, sus, rsus, mring_, rstruct_, rbright_, rdamp_, rpos_, rmodel_, rpoly_, regg_, rsus_|
var osc,dry,pitch;
osc = In.ar(bus, 2);
mring = mring+Line.kr(0, mring_, sus);
rstruct = rstruct+Line.kr(0, rstruct_, sus);
rbright = rbright+Line.kr(0, rbright_, sus);
rdamp = rdamp+Line.kr(0, rdamp_, sus);
rpos = rpos+Line.kr(0, rpos_, sus);
rmodel = rmodel+Line.kr(0, rmodel_, sus);
rpoly = rpoly+Line.kr(0, rpoly_, sus);
regg = regg+Line.kr(0, regg_, sus);
rsus = rsus+Line.kr(0, rsus_, sus);
pitch = In.kr(bus, 1);
dry = osc;
osc = MiRings.ar(in: osc,trig:1,pit: pitch.cpsmidi.clip(1,80),struct: rstruct, bright: rbright, damp: rdamp, pos: rpos, model: rmodel, poly: rpoly, intern_exciter: 1, easteregg: regg, mul: 1);
osc = osc * EnvGen.kr(Env([1,1,0], [sus*rsus, 0.01]), doneAction: 2);
osc = SelectX.ar(mring, [dry, osc], wrap:1);
ReplaceOut.ar(bus, osc)}).add;