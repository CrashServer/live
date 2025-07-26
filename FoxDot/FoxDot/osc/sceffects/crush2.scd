SynthDef.new(\crush2,
{|bus, crush2, bits2, crush2mix, crush2_, crush2_d, crush2lfo, crush2lfomul, crush2lfoadd, bits2_, bits2_d, bits2lfo, bits2lfomul, bits2lfoadd, crush2mix_, crush2mix_d, crush2mixlfo, crush2mixlfomul, crush2mixlfoadd, sus|
var osc,trig;
osc = In.ar(bus, 2);
crush2 = if(crush2_<=0, crush2, Line.kr(crush2, crush2_, sus*crush2_d));
crush2 = if(crush2lfo<=0, crush2, crush2 * SinOsc.kr(crush2lfo, 0, crush2lfomul, crush2lfoadd));
bits2 = if(bits2_<=0, bits2, Line.kr(bits2, bits2_, sus*bits2_d));
bits2 = if(bits2lfo<=0, bits2, bits2 * SinOsc.kr(bits2lfo, 0, bits2lfomul, bits2lfoadd));
crush2mix = if(crush2mix_<=0, crush2mix, Line.kr(crush2mix, crush2mix_, sus*crush2mix_d));
crush2mix = if(crush2mixlfo<=0, crush2mix, crush2mix * SinOsc.kr(crush2mixlfo, 0, crush2mixlfomul, crush2mixlfoadd));
trig = Impulse.ar(SampleRate.ir/bits2);
osc = osc.round(2.pow(crush2).reciprocal);
osc = SelectX.ar(crush2mix, [osc, Latch.ar(osc, trig)]);
ReplaceOut.ar(bus, osc)}).add;