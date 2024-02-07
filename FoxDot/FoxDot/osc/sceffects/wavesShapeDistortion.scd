SynthDef.new(\wavesShapeDistortion,
{|bus, shape, shapemix, shape_, shapemix_, sus|
var osc;
osc = In.ar(bus, 2);
shape = shape+Line.kr(0, shape_, sus);
shapemix = shapemix+Line.kr(0, shapemix_, sus);
osc = SelectX.ar(shapemix, [osc, (osc * (shape * 50)).fold2(1).distort / 5]);
ReplaceOut.ar(bus, osc)}).add;