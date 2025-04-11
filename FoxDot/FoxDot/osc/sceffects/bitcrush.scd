SynthDef.new(\bitcrush,
{|bus, bits, sus, amp, crush, bits_, bits_d, bitslfo, amp_, amp_d, amplfo, crush_, crush_d, crushlfo|
var osc;
osc = In.ar(bus, 2);
bits = if(bits_<=0, bits, Line.kr(bits, bits_, sus*bits_d));
bits = if(bitslfo<=0, bits, bits * SinOsc.kr(bitslfo, 0, 1, 1));
amp = if(amp_<=0, amp, Line.kr(amp, amp_, sus*amp_d));
amp = if(amplfo<=0, amp, amp * SinOsc.kr(amplfo, 0, 1, 1));
crush = if(crush_<=0, crush, Line.kr(crush, crush_, sus*crush_d));
crush = if(crushlfo<=0, crush, crush * SinOsc.kr(crushlfo, 0, 1, 1));
osc = Decimator.ar(osc, rate: 44100/crush, bits: bits);
osc = osc * Line.ar(amp * 0.85, 0.0001, sus * 2);
ReplaceOut.ar(bus, osc)}).add;