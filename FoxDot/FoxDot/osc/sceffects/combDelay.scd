SynthDef.new(\combDelay,
{|bus, echo, echomix, beat_dur, echotime, echo_, echo_d, echolfo, echomix_, echomix_d, echomixlfo, beat_dur_, beat_dur_d, beat_durlfo, echotime_, echotime_d, echotimelfo, sus|
var osc;
osc = In.ar(bus, 2);
echo = if(echo_<=0, echo, Line.kr(echo, echo_, sus*echo_d));
echo = if(echolfo<=0, echo, echo * SinOsc.kr(echolfo, 0, 1, 1));
echomix = if(echomix_<=0, echomix, Line.kr(echomix, echomix_, sus*echomix_d));
echomix = if(echomixlfo<=0, echomix, echomix * SinOsc.kr(echomixlfo, 0, 1, 1));
beat_dur = if(beat_dur_<=0, beat_dur, Line.kr(beat_dur, beat_dur_, sus*beat_dur_d));
beat_dur = if(beat_durlfo<=0, beat_dur, beat_dur * SinOsc.kr(beat_durlfo, 0, 1, 1));
echotime = if(echotime_<=0, echotime, Line.kr(echotime, echotime_, sus*echotime_d));
echotime = if(echotimelfo<=0, echotime, echotime * SinOsc.kr(echotimelfo, 0, 1, 1));
osc = SelectX.ar(echomix, [osc, osc + CombL.ar(osc, delaytime: echo * beat_dur, maxdelaytime: 2 * beat_dur, decaytime: echotime * beat_dur)]);
ReplaceOut.ar(bus, osc)}).add;