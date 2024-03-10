SynthDef.new(\tanhDisto,
{|bus, tanh, tanhmix, tanh_, tanh_d, tanhmix_, tanhmix_d, sus|
var osc;
osc = In.ar(bus, 2);
tanh = if(tanh_<=0, tanh, Line.kr(tanh, tanh_, sus*tanh_d));
tanhmix = if(tanhmix_<=0, tanhmix, Line.kr(tanhmix, tanhmix_, sus*tanhmix_d));
osc = SelectX.ar(tanhmix, [osc, osc + (osc*tanh).tanh.sqrt()]);
ReplaceOut.ar(bus, osc)}).add;