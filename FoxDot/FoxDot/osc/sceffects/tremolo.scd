SynthDef.new(\tremolo,
{|bus, tremolo, beat_dur, tremolomix|
var osc;
osc = In.ar(bus, 2);
osc = SelectX.ar(tremolomix, [osc, osc * SinOsc.ar( tremolo / beat_dur, mul:0.5, add:0.5)]);
ReplaceOut.ar(bus, osc)}).add;