SynthDef.new(\pingpong,
{|bus, pong, beat_dur, pongtime, pong_, pong_d, ponglfo, beat_dur_, beat_dur_d, beat_durlfo, pongtime_, pongtime_d, pongtimelfo, sus|
var osc,left,right;
osc = In.ar(bus, 2);
pong = if(pong_<=0, pong, Line.kr(pong, pong_, sus*pong_d));
pong = if(ponglfo<=0, pong, pong * SinOsc.kr(ponglfo, 0, 1, 1));
beat_dur = if(beat_dur_<=0, beat_dur, Line.kr(beat_dur, beat_dur_, sus*beat_dur_d));
beat_dur = if(beat_durlfo<=0, beat_dur, beat_dur * SinOsc.kr(beat_durlfo, 0, 1, 1));
pongtime = if(pongtime_<=0, pongtime, Line.kr(pongtime, pongtime_, sus*pongtime_d));
pongtime = if(pongtimelfo<=0, pongtime, pongtime * SinOsc.kr(pongtimelfo, 0, 1, 1));
left = CombN.ar(osc, delaytime: pong * beat_dur, maxdelaytime: 2 * beat_dur, decaytime: pongtime * beat_dur);
left = left*2.distort.tanh;
left = LPF.ar(left,12000);
left = HPF.ar(left,300);
right = CombN.ar(osc, delaytime: pong * beat_dur + pong * beat_dur*0.5, maxdelaytime: 2 * beat_dur, decaytime: pongtime * beat_dur);
right = right*2.distort.tanh;
right = LPF.ar(right,12000);
right = HPF.ar(right,300);
osc= osc + [left, right];
ReplaceOut.ar(bus, osc)}).add;