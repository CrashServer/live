SynthDef.new(\wavesShapeDistortion,
{|bus, shape, shapemix, shape_, shape_d, shapemix_, shapemix_d, sus|
var osc;
osc = In.ar(bus, 2);
shape = if(shape_<=0, shape, Line.kr(shape, shape_, sus*shape_d));
shapemix = if(shapemix_<=0, shapemix, Line.kr(shapemix, shapemix_, sus*shapemix_d));
osc = SelectX.ar(shapemix, [osc, (osc * (shape * 50)).fold2(1).distort / 5]);
ReplaceOut.ar(bus, osc)}).add;