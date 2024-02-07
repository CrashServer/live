SynthDef.new(\combDelay,
{|bus, echo, echomix, beat_dur, echotime, echo_, echomix_, beat_dur_, echotime_, sus|
var osc;
osc = In.ar(bus, 2);
echo = echo+Line.kr(0, echo_, sus);
echomix = echomix+Line.kr(0, echomix_, sus);
beat_dur = beat_dur+Line.kr(0, beat_dur_, sus);
echotime = echotime+Line.kr(0, echotime_, sus);
osc = SelectX.ar(echomix, [osc, osc + CombL.ar(osc, delaytime: echo * beat_dur, maxdelaytime: 2 * beat_dur, decaytime: echotime * beat_dur)]);
ReplaceOut.ar(bus, osc)}).add;