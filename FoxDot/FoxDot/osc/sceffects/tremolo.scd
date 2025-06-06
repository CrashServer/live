SynthDef.new(\tremolo,
{|bus, tremolo, beat_dur, tremolomix, tremolo_, tremolo_d, tremololfo, tremololfomul, tremololfoadd, beat_dur_, beat_dur_d, beat_durlfo, beat_durlfomul, beat_durlfoadd, tremolomix_, tremolomix_d, tremolomixlfo, tremolomixlfomul, tremolomixlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
tremolo = if(tremolo_<=0, tremolo, Line.kr(tremolo, tremolo_, sus*tremolo_d));
tremolo = if(tremololfo<=0, tremolo, tremolo * SinOsc.kr(tremololfo, 0, tremololfomul, tremololfoadd));
beat_dur = if(beat_dur_<=0, beat_dur, Line.kr(beat_dur, beat_dur_, sus*beat_dur_d));
beat_dur = if(beat_durlfo<=0, beat_dur, beat_dur * SinOsc.kr(beat_durlfo, 0, beat_durlfomul, beat_durlfoadd));
tremolomix = if(tremolomix_<=0, tremolomix, Line.kr(tremolomix, tremolomix_, sus*tremolomix_d));
tremolomix = if(tremolomixlfo<=0, tremolomix, tremolomix * SinOsc.kr(tremolomixlfo, 0, tremolomixlfomul, tremolomixlfoadd));
osc = SelectX.ar(tremolomix, [osc, osc * SinOsc.ar( tremolo / beat_dur, mul:0.5, add:0.5)]);
ReplaceOut.ar(bus, osc)}).add;