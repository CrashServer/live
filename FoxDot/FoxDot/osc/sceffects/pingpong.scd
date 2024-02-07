SynthDef.new(\pingpong,
{|bus, pong, beat_dur, pongtime, pong_, beat_dur_, pongtime_, sus|
var osc,left,right;
osc = In.ar(bus, 2);
pong = pong+Line.kr(0, pong_, sus);
beat_dur = beat_dur+Line.kr(0, beat_dur_, sus);
pongtime = pongtime+Line.kr(0, pongtime_, sus);
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