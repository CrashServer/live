SynthDef.new(\tanhDisto,
{|bus, tanh, tanhmix, tanh_, tanh_d, tanhlfo, tanhlfomul, tanhlfoadd, tanhmix_, tanhmix_d, tanhmixlfo, tanhmixlfomul, tanhmixlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
tanh = if(tanh_<=0, tanh, Line.kr(tanh, tanh_, sus*tanh_d));
tanh = if(tanhlfo<=0, tanh, tanh * SinOsc.kr(tanhlfo, 0, tanhlfomul, tanhlfoadd));
tanhmix = if(tanhmix_<=0, tanhmix, Line.kr(tanhmix, tanhmix_, sus*tanhmix_d));
tanhmix = if(tanhmixlfo<=0, tanhmix, tanhmix * SinOsc.kr(tanhmixlfo, 0, tanhmixlfomul, tanhmixlfoadd));
osc = SelectX.ar(tanhmix, [osc, osc + (osc*tanh).tanh.sqrt()]);
ReplaceOut.ar(bus, osc)}).add;