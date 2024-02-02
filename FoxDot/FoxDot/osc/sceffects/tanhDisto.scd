SynthDef.new(\tanhDisto,
{|bus, tanh, tanhmix|
var osc;
osc = In.ar(bus, 2);
osc = SelectX.ar(tanhmix, [osc, osc + (osc*tanh).tanh.sqrt()]);
ReplaceOut.ar(bus, osc)}).add;