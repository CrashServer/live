SynthDef.new(\pitchshifter,
{|bus, shift, shiftsize, shift_, shift_d, shiftlfo, shiftsize_, shiftsize_d, shiftsizelfo, sus|
var osc;
osc = In.ar(bus, 2);
shift = if(shift_<=0, shift, Line.kr(shift, shift_, sus*shift_d));
shift = if(shiftlfo<=0, shift, shift * SinOsc.kr(shiftlfo, 0, 1, 1));
shiftsize = if(shiftsize_<=0, shiftsize, Line.kr(shiftsize, shiftsize_, sus*shiftsize_d));
shiftsize = if(shiftsizelfo<=0, shiftsize, shiftsize * SinOsc.kr(shiftsizelfo, 0, 1, 1));
osc = PitchShift.ar(osc, shiftsize, shift, 0.02, 0.01);
ReplaceOut.ar(bus, osc)}).add;