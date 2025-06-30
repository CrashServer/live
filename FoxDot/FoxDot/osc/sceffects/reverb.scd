SynthDef.new(\reverb,
{|bus, room, mix, room_, room_d, roomlfo, roomlfomul, roomlfoadd, mix_, mix_d, mixlfo, mixlfomul, mixlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
room = if(room_<=0, room, Line.kr(room, room_, sus*room_d));
room = if(roomlfo<=0, room, room * SinOsc.kr(roomlfo, 0, roomlfomul, roomlfoadd));
mix = if(mix_<=0, mix, Line.kr(mix, mix_, sus*mix_d));
mix = if(mixlfo<=0, mix, mix * SinOsc.kr(mixlfo, 0, mixlfomul, mixlfoadd));
osc = FreeVerb.ar(osc, mix, room);
ReplaceOut.ar(bus, osc)}).add;