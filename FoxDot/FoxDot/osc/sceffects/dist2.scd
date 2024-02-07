SynthDef.new(\dist2,
{|bus, dist2, dist2mix, dist2shape, dist2_, dist2mix_, dist2shape_, sus|
var osc,tmp;
osc = In.ar(bus, 2);
dist2 = dist2+Line.kr(0, dist2_, sus);
dist2mix = dist2mix+Line.kr(0, dist2mix_, sus);
dist2shape = dist2shape+Line.kr(0, dist2shape_, sus);
tmp = Fold.ar(osc, -1*dist2shape,dist2shape);
tmp = (tmp * 16.dbamp * dist2).tanh;
tmp = BHiShelf.ar(tmp, 9000, 0.8, -12);
tmp = LPF.ar(tmp, 9000);
osc = SelectX.ar(dist2mix, [osc, tmp]);
ReplaceOut.ar(bus, osc)}).add;