SynthDef.new(\wavesShapeDistortion,
{|bus, shape, shapemix, shape_, shape_d, shapelfo, shapemix_, shapemix_d, shapemixlfo, sus|
var osc;
osc = In.ar(bus, 2);
shape = if(shape_<=0, shape, Line.kr(shape, shape_, sus*shape_d));
shape = if(shapelfo<=0, shape, shape * SinOsc.kr(shapelfo, 0, 1, 1));
shapemix = if(shapemix_<=0, shapemix, Line.kr(shapemix, shapemix_, sus*shapemix_d));
shapemix = if(shapemixlfo<=0, shapemix, shapemix * SinOsc.kr(shapemixlfo, 0, 1, 1));
osc = SelectX.ar(shapemix, [osc, (osc * (shape * 50)).fold2(1).distort / 5]);
ReplaceOut.ar(bus, osc)}).add;