SynthDef.new(\MiRings,
{|bus, mring, rstruct, rbright, rdamp, rpos, rmodel, rpoly, regg, sus, rsus, mring_, mring_d, mringlfo, mringlfomul, mringlfoadd, rstruct_, rstruct_d, rstructlfo, rstructlfomul, rstructlfoadd, rbright_, rbright_d, rbrightlfo, rbrightlfomul, rbrightlfoadd, rdamp_, rdamp_d, rdamplfo, rdamplfomul, rdamplfoadd, rpos_, rpos_d, rposlfo, rposlfomul, rposlfoadd, rmodel_, rmodel_d, rmodellfo, rmodellfomul, rmodellfoadd, rpoly_, rpoly_d, rpolylfo, rpolylfomul, rpolylfoadd, regg_, regg_d, regglfo, regglfomul, regglfoadd, rsus_, rsus_d, rsuslfo, rsuslfomul, rsuslfoadd|
var osc,dry,pitch;
osc = In.ar(bus, 2);
mring = if(mring_<=0, mring, Line.kr(mring, mring_, sus*mring_d));
mring = if(mringlfo<=0, mring, mring * SinOsc.kr(mringlfo, 0, mringlfomul, mringlfoadd));
rstruct = if(rstruct_<=0, rstruct, Line.kr(rstruct, rstruct_, sus*rstruct_d));
rstruct = if(rstructlfo<=0, rstruct, rstruct * SinOsc.kr(rstructlfo, 0, rstructlfomul, rstructlfoadd));
rbright = if(rbright_<=0, rbright, Line.kr(rbright, rbright_, sus*rbright_d));
rbright = if(rbrightlfo<=0, rbright, rbright * SinOsc.kr(rbrightlfo, 0, rbrightlfomul, rbrightlfoadd));
rdamp = if(rdamp_<=0, rdamp, Line.kr(rdamp, rdamp_, sus*rdamp_d));
rdamp = if(rdamplfo<=0, rdamp, rdamp * SinOsc.kr(rdamplfo, 0, rdamplfomul, rdamplfoadd));
rpos = if(rpos_<=0, rpos, Line.kr(rpos, rpos_, sus*rpos_d));
rpos = if(rposlfo<=0, rpos, rpos * SinOsc.kr(rposlfo, 0, rposlfomul, rposlfoadd));
rmodel = if(rmodel_<=0, rmodel, Line.kr(rmodel, rmodel_, sus*rmodel_d));
rmodel = if(rmodellfo<=0, rmodel, rmodel * SinOsc.kr(rmodellfo, 0, rmodellfomul, rmodellfoadd));
rpoly = if(rpoly_<=0, rpoly, Line.kr(rpoly, rpoly_, sus*rpoly_d));
rpoly = if(rpolylfo<=0, rpoly, rpoly * SinOsc.kr(rpolylfo, 0, rpolylfomul, rpolylfoadd));
regg = if(regg_<=0, regg, Line.kr(regg, regg_, sus*regg_d));
regg = if(regglfo<=0, regg, regg * SinOsc.kr(regglfo, 0, regglfomul, regglfoadd));
rsus = if(rsus_<=0, rsus, Line.kr(rsus, rsus_, sus*rsus_d));
rsus = if(rsuslfo<=0, rsus, rsus * SinOsc.kr(rsuslfo, 0, rsuslfomul, rsuslfoadd));
pitch = In.kr(bus, 1);
dry = osc;
osc = MiRings.ar(in: osc,trig:1,pit: pitch.cpsmidi.clip(1,80),struct: rstruct, bright: rbright, damp: rdamp, pos: rpos, model: rmodel, poly: rpoly, intern_exciter: 1, easteregg: regg, mul: 1);
osc = osc * EnvGen.kr(Env([1,1,0], [sus*rsus, 0.01]), doneAction: 2);
osc = SelectX.ar(mring, [dry, osc], wrap:1);
ReplaceOut.ar(bus, osc)}).add;