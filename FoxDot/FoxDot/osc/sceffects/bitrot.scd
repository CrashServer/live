SynthDef.new(\bitrot,
{|bus, bitrot, rotbits, rotrate, rotjitter, bitrot_, bitrot_d, bitrotlfo, bitrotlfomul, bitrotlfoadd, rotbits_, rotbits_d, rotbitslfo, rotbitslfomul, rotbitslfoadd, rotrate_, rotrate_d, rotratelfo, rotratelfomul, rotratelfoadd, rotjitter_, rotjitter_d, rotjitterlfo, rotjitterlfomul, rotjitterlfoadd, sus|
var osc,dry,degraded,bits,sampleRate,jitter;
osc = In.ar(bus, 2);
bitrot = if(bitrot_<=0, bitrot, Line.kr(bitrot, bitrot_, sus*bitrot_d));
bitrot = if(bitrotlfo<=0, bitrot, bitrot * SinOsc.kr(bitrotlfo, 0, bitrotlfomul, bitrotlfoadd));
rotbits = if(rotbits_<=0, rotbits, Line.kr(rotbits, rotbits_, sus*rotbits_d));
rotbits = if(rotbitslfo<=0, rotbits, rotbits * SinOsc.kr(rotbitslfo, 0, rotbitslfomul, rotbitslfoadd));
rotrate = if(rotrate_<=0, rotrate, Line.kr(rotrate, rotrate_, sus*rotrate_d));
rotrate = if(rotratelfo<=0, rotrate, rotrate * SinOsc.kr(rotratelfo, 0, rotratelfomul, rotratelfoadd));
rotjitter = if(rotjitter_<=0, rotjitter, Line.kr(rotjitter, rotjitter_, sus*rotjitter_d));
rotjitter = if(rotjitterlfo<=0, rotjitter, rotjitter * SinOsc.kr(rotjitterlfo, 0, rotjitterlfomul, rotjitterlfoadd));
dry = osc;
bits = rotbits + (LFNoise1.kr(3).range(-1, 1) * rotjitter * 4);
bits = bits.clip(2, 16);
sampleRate = LinExp.kr(rotrate, 0, 1, 44100, 1000);
sampleRate = sampleRate + (LFNoise2.kr(5) * rotjitter * sampleRate * 0.3);
jitter = LFNoise0.kr(20).range(0.98, 1.02) ** (rotjitter * 5);
degraded = Latch.ar(osc, Impulse.ar(sampleRate * jitter));
degraded = degraded.round(2.pow(bits.neg));
degraded = (degraded * 1.2).fold(-0.95, 0.95);
degraded = LeakDC.ar(degraded);
osc = XFade2.ar(dry, degraded, bitrot * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;