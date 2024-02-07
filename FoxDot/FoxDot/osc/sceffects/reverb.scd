SynthDef.new(\reverb,
{|bus, room, mix, room_, mix_, sus|
var osc;
osc = In.ar(bus, 2);
room = room+Line.kr(0, room_, sus);
mix = mix+Line.kr(0, mix_, sus);
osc = FreeVerb.ar(osc, mix, room);
ReplaceOut.ar(bus, osc)}).add;