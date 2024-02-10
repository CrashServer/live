SynthDef.new(\MiBlow,
{|bus, blow, bflow, bmodel, bpos, sus, blow_, blow_d, bflow_, bflow_d, bmodel_, bmodel_d, bpos_, bpos_d|
var osc,dry,pitch;
osc = In.ar(bus, 2);
blow = if(blow_<=0, blow, Line.kr(blow, blow_, sus*blow_d));
bflow = if(bflow_<=0, bflow, Line.kr(bflow, bflow_, sus*bflow_d));
bmodel = if(bmodel_<=0, bmodel, Line.kr(bmodel, bmodel_, sus*bmodel_d));
bpos = if(bpos_<=0, bpos, Line.kr(bpos, bpos_, sus*bpos_d));
pitch = In.kr(bus, 1);
dry = osc;
osc = MiElements.ar(osc, 0, 1, pitch.cpsmidi.clip(1,70), blow_level:1, space:0.8, contour: 0.8, flow: bflow, damp:0.7, model:bmodel, pos:bpos);
osc = osc * EnvGen.kr(Env([1,1,0], [sus, 0.5]), doneAction: 2);
osc = LPF.ar(osc, 18000);
osc = Splay.ar(osc);
osc = SelectX.ar(blow, [dry, osc*0.5], wrap:1);
ReplaceOut.ar(bus, osc)}).add;