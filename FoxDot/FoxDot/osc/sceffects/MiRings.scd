SynthDef.new(\MiRings,
{|bus, mring, rstruct, rbright, rdamp, rpos, rmodel, rpoly, regg, sus, rsus, mring_, mring_d, rstruct_, rstruct_d, rbright_, rbright_d, rdamp_, rdamp_d, rpos_, rpos_d, rmodel_, rmodel_d, rpoly_, rpoly_d, regg_, regg_d, rsus_, rsus_d|
var osc,dry,pitch;
osc = In.ar(bus, 2);
mring = if(mring_<=0, mring, Line.kr(mring, mring_, sus*mring_d));
rstruct = if(rstruct_<=0, rstruct, Line.kr(rstruct, rstruct_, sus*rstruct_d));
rbright = if(rbright_<=0, rbright, Line.kr(rbright, rbright_, sus*rbright_d));
rdamp = if(rdamp_<=0, rdamp, Line.kr(rdamp, rdamp_, sus*rdamp_d));
rpos = if(rpos_<=0, rpos, Line.kr(rpos, rpos_, sus*rpos_d));
rmodel = if(rmodel_<=0, rmodel, Line.kr(rmodel, rmodel_, sus*rmodel_d));
rpoly = if(rpoly_<=0, rpoly, Line.kr(rpoly, rpoly_, sus*rpoly_d));
regg = if(regg_<=0, regg, Line.kr(regg, regg_, sus*regg_d));
rsus = if(rsus_<=0, rsus, Line.kr(rsus, rsus_, sus*rsus_d));
pitch = In.kr(bus, 1);
dry = osc;
osc = MiRings.ar(in: osc,trig:1,pit: pitch.cpsmidi.clip(1,80),struct: rstruct, bright: rbright, damp: rdamp, pos: rpos, model: rmodel, poly: rpoly, intern_exciter: 1, easteregg: regg, mul: 1);
osc = osc * EnvGen.kr(Env([1,1,0], [sus*rsus, 0.01]), doneAction: 2);
osc = SelectX.ar(mring, [dry, osc], wrap:1);
ReplaceOut.ar(bus, osc)}).add;