SynthDef.new(\MiBlow,
{|bus, blow, bflow, bmodel, bpos, sus|
var osc,dry,pitch;
osc = In.ar(bus, 2);
pitch = In.kr(bus, 1);
dry = osc;
osc = MiElements.ar(osc, 0, 1, pitch.cpsmidi.clip(1,70), blow_level:1, space:0.8, contour: 0.8, flow: bflow, damp:0.7, model:bmodel, pos:bpos);
osc = osc * EnvGen.kr(Env([1,1,0], [sus, 0.5]), doneAction: 2);
osc = LPF.ar(osc, 18000);
osc = Splay.ar(osc);
osc = SelectX.ar(blow, [dry, osc*0.5], wrap:1);
ReplaceOut.ar(bus, osc)}).add;