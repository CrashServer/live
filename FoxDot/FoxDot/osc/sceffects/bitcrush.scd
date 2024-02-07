SynthDef.new(\bitcrush,
{|bus, bits, sus, amp, crush, bits_, amp_, crush_|
var osc;
osc = In.ar(bus, 2);
bits = bits+Line.kr(0, bits_, sus);
amp = amp+Line.kr(0, amp_, sus);
crush = crush+Line.kr(0, crush_, sus);
osc = Decimator.ar(osc, rate: 44100/crush, bits: bits);
osc = osc * Line.ar(amp * 0.85, 0.0001, sus * 2);
ReplaceOut.ar(bus, osc)}).add;