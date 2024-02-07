SynthDef.new(\tanhDisto,
{|bus, tanh, tanhmix, tanh_, tanhmix_, sus|
var osc;
osc = In.ar(bus, 2);
tanh = tanh+Line.kr(0, tanh_, sus);
tanhmix = tanhmix+Line.kr(0, tanhmix_, sus);
osc = SelectX.ar(tanhmix, [osc, osc + (osc*tanh).tanh.sqrt()]);
ReplaceOut.ar(bus, osc)}).add;