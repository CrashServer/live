SynthDef.new(\dist2,
{|bus, dist2, dist2mix, dist2shape|
var osc,tmp;
osc = In.ar(bus, 2);
tmp = Fold.ar(osc, -1*dist2shape,dist2shape);
tmp = (tmp * 16.dbamp * dist2).tanh;
tmp = BHiShelf.ar(tmp, 9000, 0.8, -12);
tmp = LPF.ar(tmp, 9000);
osc = LinXFade2.ar(tmp, osc, 1-dist2mix);
ReplaceOut.ar(bus, osc)}).add;