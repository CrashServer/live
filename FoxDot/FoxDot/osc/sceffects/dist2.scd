SynthDef.new(\dist2,
{|bus, dist2, dist2mix, dist2shape, dist2_, dist2_d, dist2lfo, dist2mix_, dist2mix_d, dist2mixlfo, dist2shape_, dist2shape_d, dist2shapelfo, sus|
var osc,tmp;
osc = In.ar(bus, 2);
dist2 = if(dist2_<=0, dist2, Line.kr(dist2, dist2_, sus*dist2_d));
dist2 = if(dist2lfo<=0, dist2, dist2 * SinOsc.kr(dist2lfo, 0, 1, 1));
dist2mix = if(dist2mix_<=0, dist2mix, Line.kr(dist2mix, dist2mix_, sus*dist2mix_d));
dist2mix = if(dist2mixlfo<=0, dist2mix, dist2mix * SinOsc.kr(dist2mixlfo, 0, 1, 1));
dist2shape = if(dist2shape_<=0, dist2shape, Line.kr(dist2shape, dist2shape_, sus*dist2shape_d));
dist2shape = if(dist2shapelfo<=0, dist2shape, dist2shape * SinOsc.kr(dist2shapelfo, 0, 1, 1));
tmp = Fold.ar(osc, -1*dist2shape,dist2shape);
tmp = (tmp * 16.dbamp * dist2).tanh;
tmp = BHiShelf.ar(tmp, 9000, 0.8, -12);
tmp = LPF.ar(tmp, 9000);
osc = SelectX.ar(dist2mix, [osc, tmp]);
ReplaceOut.ar(bus, osc)}).add;