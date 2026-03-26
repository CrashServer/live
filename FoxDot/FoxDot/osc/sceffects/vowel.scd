SynthDef.new(\vowel,
{|bus, vowel, vowelf, vowelq, vowel_, vowel_d, vowellfo, vowellfomul, vowellfoadd, vowelf_, vowelf_d, vowelflfo, vowelflfomul, vowelflfoadd, vowelq_, vowelq_d, vowelqlfo, vowelqlfomul, vowelqlfoadd, sus|
var osc,dry,wet,f1,f2,f3,b1,b2,b3;
osc = In.ar(bus, 2);
vowel = if(vowel_<=0, vowel, Line.kr(vowel, vowel_, sus*vowel_d));
vowel = if(vowellfo<=0, vowel, vowel * SinOsc.kr(vowellfo, 0, vowellfomul, vowellfoadd));
vowelf = if(vowelf_<=0, vowelf, Line.kr(vowelf, vowelf_, sus*vowelf_d));
vowelf = if(vowelflfo<=0, vowelf, vowelf * SinOsc.kr(vowelflfo, 0, vowelflfomul, vowelflfoadd));
vowelq = if(vowelq_<=0, vowelq, Line.kr(vowelq, vowelq_, sus*vowelq_d));
vowelq = if(vowelqlfo<=0, vowelq, vowelq * SinOsc.kr(vowelqlfo, 0, vowelqlfomul, vowelqlfoadd));
dry = osc;
f1 = Select.kr(vowelf.floor.clip(0,3), [LinXFade2.kr(800, 400, vowelf.frac * 2 - 1), LinXFade2.kr(400, 350, (vowelf - 1).frac * 2 - 1), LinXFade2.kr(350, 450, (vowelf - 2).frac * 2 - 1), LinXFade2.kr(450, 325, (vowelf - 3).frac * 2 - 1)]);
f2 = Select.kr(vowelf.floor.clip(0,3), [LinXFade2.kr(1150, 1600, vowelf.frac * 2 - 1), LinXFade2.kr(1600, 2100, (vowelf - 1).frac * 2 - 1), LinXFade2.kr(2100, 800, (vowelf - 2).frac * 2 - 1), LinXFade2.kr(800, 700, (vowelf - 3).frac * 2 - 1)]);
f3 = Select.kr(vowelf.floor.clip(0,3), [LinXFade2.kr(2800, 2700, vowelf.frac * 2 - 1), LinXFade2.kr(2700, 3000, (vowelf - 1).frac * 2 - 1), LinXFade2.kr(3000, 2830, (vowelf - 2).frac * 2 - 1), LinXFade2.kr(2830, 2530, (vowelf - 3).frac * 2 - 1)]);
b1 = (80 / vowelq).max(20);
b2 = (60 / vowelq).max(15);
b3 = (50 / vowelq).max(12);
wet = BPF.ar(osc, f1, b1/f1) * 3;
wet = wet + (BPF.ar(osc, f2, b2/f2) * 2);
wet = wet + (BPF.ar(osc, f3, b3/f3) * 1.5);
wet = LeakDC.ar(wet);
osc = XFade2.ar(dry, wet, vowel * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;