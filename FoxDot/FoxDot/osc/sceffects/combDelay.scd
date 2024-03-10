SynthDef.new(\combDelay,
{|bus, echo, echomix, beat_dur, echotime, echo_, echo_d, echomix_, echomix_d, beat_dur_, beat_dur_d, echotime_, echotime_d, sus|
var osc;
osc = In.ar(bus, 2);
echo = if(echo_<=0, echo, Line.kr(echo, echo_, sus*echo_d));
echomix = if(echomix_<=0, echomix, Line.kr(echomix, echomix_, sus*echomix_d));
echotime = if(echotime_<=0, echotime, Line.kr(echotime, echotime_, sus*echotime_d));
osc = SelectX.ar(echomix, [osc, osc + CombL.ar(osc, delaytime: echo * beat_dur, maxdelaytime: 2 * beat_dur, decaytime: echotime * beat_dur)]);
ReplaceOut.ar(bus, osc)}).add;