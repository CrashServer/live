SynthDef.new(\tremolo,
{|bus, tremolo, beat_dur, tremolomix, tremolo_, beat_dur_, tremolomix_, sus|
var osc;
osc = In.ar(bus, 2);
tremolo = tremolo+Line.kr(0, tremolo_, sus);
beat_dur = beat_dur+Line.kr(0, beat_dur_, sus);
tremolomix = tremolomix+Line.kr(0, tremolomix_, sus);
osc = SelectX.ar(tremolomix, [osc, osc * SinOsc.ar( tremolo / beat_dur, mul:0.5, add:0.5)]);
ReplaceOut.ar(bus, osc)}).add;