SynthDef.new(\pitchBend,
{|bus, bend, sus, benddelay, bend_, bend_d, benddelay_, benddelay_d|
var osc;
osc = In.kr(bus, 1);
bend = if(bend_<=0, bend, Line.kr(bend, bend_, sus*bend_d));
benddelay = if(benddelay_<=0, benddelay, Line.kr(benddelay, benddelay_, sus*benddelay_d));
osc = osc * EnvGen.ar(Env([1, 1, 1 + bend, 1], [sus * benddelay, (sus*(1-benddelay)/2), (sus*(1-benddelay)/2)]));
ReplaceOut.kr(bus, osc)}).add;