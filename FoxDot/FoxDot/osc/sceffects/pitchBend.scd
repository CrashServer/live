SynthDef.new(\pitchBend,
{|bus, bend, sus, benddelay, bend_, benddelay_|
var osc;
osc = In.kr(bus, 1);
bend = bend+Line.kr(0, bend_, sus);
benddelay = benddelay+Line.kr(0, benddelay_, sus);
osc = osc * EnvGen.ar(Env([1, 1, 1 + bend, 1], [sus * benddelay, (sus*(1-benddelay)/2), (sus*(1-benddelay)/2)]));
ReplaceOut.kr(bus, osc)}).add;