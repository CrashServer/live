SynthDef.new(\reverb_stereo,
{|bus, room2, mix2, damp2, revatk, revsus, room2_, room2_d, room2lfo, mix2_, mix2_d, mix2lfo, damp2_, damp2_d, damp2lfo, revatk_, revatk_d, revatklfo, revsus_, revsus_d, revsuslfo, sus|
var osc,dry;
osc = In.ar(bus, 2);
room2 = if(room2_<=0, room2, Line.kr(room2, room2_, sus*room2_d));
room2 = if(room2lfo<=0, room2, room2 * SinOsc.kr(room2lfo, 0, 1, 1));
mix2 = if(mix2_<=0, mix2, Line.kr(mix2, mix2_, sus*mix2_d));
mix2 = if(mix2lfo<=0, mix2, mix2 * SinOsc.kr(mix2lfo, 0, 1, 1));
damp2 = if(damp2_<=0, damp2, Line.kr(damp2, damp2_, sus*damp2_d));
damp2 = if(damp2lfo<=0, damp2, damp2 * SinOsc.kr(damp2lfo, 0, 1, 1));
revatk = if(revatk_<=0, revatk, Line.kr(revatk, revatk_, sus*revatk_d));
revatk = if(revatklfo<=0, revatk, revatk * SinOsc.kr(revatklfo, 0, 1, 1));
revsus = if(revsus_<=0, revsus, Line.kr(revsus, revsus_, sus*revsus_d));
revsus = if(revsuslfo<=0, revsus, revsus * SinOsc.kr(revsuslfo, 0, 1, 1));
dry = osc;
osc = HPF.ar(osc, 100);
osc = LPF.ar(osc, 10000);
osc = FreeVerb2.ar(osc[0], osc[1], 1, room2, damp2);
osc = osc * EnvGen.ar(Env([0,1,0], [revatk,revsus], curve: 'welch'));
osc = SelectX.ar(mix2, [dry, osc]);
ReplaceOut.ar(bus, osc)}).add;