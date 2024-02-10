SynthDef.new(\tremolo,
{|bus, tremolo, beat_dur, tremolomix, tremolo_, tremolo_d, beat_dur_, beat_dur_d, tremolomix_, tremolomix_d, sus|
var osc;
osc = In.ar(bus, 2);
tremolo = if(tremolo_<=0, tremolo, Line.kr(tremolo, tremolo_, sus*tremolo_d));
tremolomix = if(tremolomix_<=0, tremolomix, Line.kr(tremolomix, tremolomix_, sus*tremolomix_d));
osc = SelectX.ar(tremolomix, [osc, osc * SinOsc.ar( tremolo / beat_dur, mul:0.5, add:0.5)]);
ReplaceOut.ar(bus, osc)}).add;