SynthDef.new(\distortion,
{|bus, dist, tmp, dist_, dist_d, tmp_, tmp_d, sus|
var osc;
osc = In.ar(bus, 2);
dist = if(dist_<=0, dist, Line.kr(dist, dist_, sus*dist_d));
tmp = if(tmp_<=0, tmp, Line.kr(tmp, tmp_, sus*tmp_d));
tmp = osc;
osc = CrossoverDistortion.ar(osc, amp:0.2, smooth:0.01);
osc = osc + (0.1 * dist * DynKlank.ar(`[[60,61,240,3000 + SinOsc.ar(62,mul:100)],nil,[0.1, 0.1, 0.05, 0.01]], osc));
osc = (osc.cubed * 8).softclip * 0.5;
osc = SelectX.ar(dist, [tmp, osc]);
ReplaceOut.ar(bus, osc)}).add;