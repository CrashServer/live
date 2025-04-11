SynthDef.new(\bitcrush,
{|bus, bits, sus, amp, crush, bits_, bits_d, bitslfo, bitslfomul, bitslfoadd, amp_, amp_d, amplfo, amplfomul, amplfoadd, crush_, crush_d, crushlfo, crushlfomul, crushlfoadd|
var osc;
osc = In.ar(bus, 2);
bits = if(bits_<=0, bits, Line.kr(bits, bits_, sus*bits_d));
bits = if(bitslfo<=0, bits, bits * SinOsc.kr(bitslfo, 0, bitslfomul, bitslfoadd));
amp = if(amp_<=0, amp, Line.kr(amp, amp_, sus*amp_d));
amp = if(amplfo<=0, amp, amp * SinOsc.kr(amplfo, 0, amplfomul, amplfoadd));
crush = if(crush_<=0, crush, Line.kr(crush, crush_, sus*crush_d));
crush = if(crushlfo<=0, crush, crush * SinOsc.kr(crushlfo, 0, crushlfomul, crushlfoadd));
osc = Decimator.ar(osc, rate: 44100/crush, bits: bits);
osc = osc * Line.ar(amp * 0.85, 0.0001, sus * 2);
ReplaceOut.ar(bus, osc)}).add;