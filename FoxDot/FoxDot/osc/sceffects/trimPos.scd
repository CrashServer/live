SynthDef.new(\trimPos,
{|bus, position, sus, position_, position_d|
var osc;
osc = In.ar(bus, 2);
position = if(position_<=0, position, Line.kr(position, position_, sus*position_d));
osc = osc * EnvGen.ar(Env(levels: [0,0,1], curve: 'step', times: [sus * position, 0]));
ReplaceOut.ar(bus, osc)}).add;