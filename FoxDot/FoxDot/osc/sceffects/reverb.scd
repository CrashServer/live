SynthDef.new(\reverb,
{|bus, room, mix, room_, room_d, mix_, mix_d, sus|
var osc;
osc = In.ar(bus, 2);
room = if(room_<=0, room, Line.kr(room, room_, sus*room_d));
mix = if(mix_<=0, mix, Line.kr(mix, mix_, sus*mix_d));
osc = FreeVerb.ar(osc, mix, room);
ReplaceOut.ar(bus, osc)}).add;