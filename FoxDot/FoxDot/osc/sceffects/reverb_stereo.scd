SynthDef.new(\reverb_stereo,
{|bus, room2, mix2, damp2, revatk, revsus, room2_, room2_d, mix2_, mix2_d, damp2_, damp2_d, revatk_, revatk_d, revsus_, revsus_d, sus|
var osc,dry;
osc = In.ar(bus, 2);
room2 = if(room2_<=0, room2, Line.kr(room2, room2_, sus*room2_d));
mix2 = if(mix2_<=0, mix2, Line.kr(mix2, mix2_, sus*mix2_d));
damp2 = if(damp2_<=0, damp2, Line.kr(damp2, damp2_, sus*damp2_d));
revatk = if(revatk_<=0, revatk, Line.kr(revatk, revatk_, sus*revatk_d));
revsus = if(revsus_<=0, revsus, Line.kr(revsus, revsus_, sus*revsus_d));
dry = osc;
osc = HPF.ar(osc, 100);
osc = LPF.ar(osc, 10000);
osc = FreeVerb2.ar(osc[0], osc[1], 1, room2, damp2);
osc = osc * EnvGen.ar(Env([0,1,0], [revatk,revsus], curve: 'welch'));
osc = SelectX.ar(mix2, [dry, osc]);
ReplaceOut.ar(bus, osc)}).add;