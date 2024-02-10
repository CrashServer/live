SynthDef.new(\pitchshifter,
{|bus, shift, shiftsize, shift_, shift_d, shiftsize_, shiftsize_d, sus|
var osc;
osc = In.ar(bus, 2);
shift = if(shift_<=0, shift, Line.kr(shift, shift_, sus*shift_d));
shiftsize = if(shiftsize_<=0, shiftsize, Line.kr(shiftsize, shiftsize_, sus*shiftsize_d));
osc = PitchShift.ar(osc, shiftsize, shift, 0.02, 0.01);
ReplaceOut.ar(bus, osc)}).add;