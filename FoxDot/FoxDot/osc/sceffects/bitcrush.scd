SynthDef.new(\bitcrush,
{|bus, bits, sus, amp, crush, bits_, bits_d, amp_, amp_d, crush_, crush_d|
var osc;
osc = In.ar(bus, 2);
bits = if(bits_<=0, bits, Line.kr(bits, bits_, sus*bits_d));
amp = if(amp_<=0, amp, Line.kr(amp, amp_, sus*amp_d));
crush = if(crush_<=0, crush, Line.kr(crush, crush_, sus*crush_d));
osc = Decimator.ar(osc, rate: 44100/crush, bits: bits);
osc = osc * Line.ar(amp * 0.85, 0.0001, sus * 2);
ReplaceOut.ar(bus, osc)}).add;