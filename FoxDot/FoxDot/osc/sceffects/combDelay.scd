SynthDef.new(\combDelay,
{|bus, echo, echomix, beat_dur, echotime, echo_, echo_d, echolfo, echolfomul, echolfoadd, echolfophase, echomix_, echomix_d, echomixlfo, echomixlfomul, echomixlfoadd, echomixlfophase, beat_dur_, beat_dur_d, beat_durlfo, beat_durlfomul, beat_durlfoadd, beat_durlfophase, echotime_, echotime_d, echotimelfo, echotimelfomul, echotimelfoadd, echotimelfophase, sus|
var osc;
osc = In.ar(bus, 2);
echo = if(echo_<=0, echo, Line.kr(echo, echo_, sus*echo_d));
echo = if(echolfo<=0, echo, echo * SinOsc.kr(echolfo, echolfophase, echolfomul, echolfoadd));
echomix = if(echomix_<=0, echomix, Line.kr(echomix, echomix_, sus*echomix_d));
echomix = if(echomixlfo<=0, echomix, echomix * SinOsc.kr(echomixlfo, echomixlfophase, echomixlfomul, echomixlfoadd));
beat_dur = if(beat_dur_<=0, beat_dur, Line.kr(beat_dur, beat_dur_, sus*beat_dur_d));
beat_dur = if(beat_durlfo<=0, beat_dur, beat_dur * SinOsc.kr(beat_durlfo, beat_durlfophase, beat_durlfomul, beat_durlfoadd));
echotime = if(echotime_<=0, echotime, Line.kr(echotime, echotime_, sus*echotime_d));
echotime = if(echotimelfo<=0, echotime, echotime * SinOsc.kr(echotimelfo, echotimelfophase, echotimelfomul, echotimelfoadd));
osc = SelectX.ar(echomix, [osc, osc + CombL.ar(osc, delaytime: echo * beat_dur, maxdelaytime: 2 * beat_dur, decaytime: echotime * beat_dur)]);
ReplaceOut.ar(bus, osc)}).add;