SynthDef.new(\pitchshifter,
{|bus, shift, shiftsize, shift_, shiftsize_, sus|
var osc;
osc = In.ar(bus, 2);
shift = shift+Line.kr(0, shift_, sus);
shiftsize = shiftsize+Line.kr(0, shiftsize_, sus);
osc = PitchShift.ar(osc, shiftsize, shift, 0.02, 0.01);
ReplaceOut.ar(bus, osc)}).add;