SynthDef.new(\reverb_stereo,
{|bus, room2, mix2, damp2, revatk, revsus, room2_, mix2_, damp2_, revatk_, revsus_, sus|
var osc,dry;
osc = In.ar(bus, 2);
room2 = room2+Line.kr(0, room2_, sus);
mix2 = mix2+Line.kr(0, mix2_, sus);
damp2 = damp2+Line.kr(0, damp2_, sus);
revatk = revatk+Line.kr(0, revatk_, sus);
revsus = revsus+Line.kr(0, revsus_, sus);
dry = osc;
osc = HPF.ar(osc, 100);
osc = LPF.ar(osc, 10000);
osc = FreeVerb2.ar(osc[0], osc[1], 1, room2, damp2);
osc = osc * EnvGen.ar(Env([0,1,0], [revatk,revsus], curve: 'welch'));
osc = SelectX.ar(mix2, [dry, osc]);
ReplaceOut.ar(bus, osc)}).add;