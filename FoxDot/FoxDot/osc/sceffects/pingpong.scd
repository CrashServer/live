SynthDef.new(\pingpong,
{|bus, pong, beat_dur, pongtime|
var osc,left,right;
osc = In.ar(bus, 2);
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