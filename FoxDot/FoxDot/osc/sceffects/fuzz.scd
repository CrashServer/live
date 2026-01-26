SynthDef.new(\fuzz,
{|bus, fuzz, fuzzgain, fuzztone, fuzzoctave, fuzz_, fuzz_d, fuzzlfo, fuzzlfomul, fuzzlfoadd, fuzzgain_, fuzzgain_d, fuzzgainlfo, fuzzgainlfomul, fuzzgainlfoadd, fuzztone_, fuzztone_d, fuzztonelfo, fuzztonelfomul, fuzztonelfoadd, fuzzoctave_, fuzzoctave_d, fuzzoctavelfo, fuzzoctavelfomul, fuzzoctavelfoadd, sus|
var osc,dry,fuzzed,octaveUp,subHarm;
osc = In.ar(bus, 2);
fuzz = if(fuzz_<=0, fuzz, Line.kr(fuzz, fuzz_, sus*fuzz_d));
fuzz = if(fuzzlfo<=0, fuzz, fuzz * SinOsc.kr(fuzzlfo, 0, fuzzlfomul, fuzzlfoadd));
fuzzgain = if(fuzzgain_<=0, fuzzgain, Line.kr(fuzzgain, fuzzgain_, sus*fuzzgain_d));
fuzzgain = if(fuzzgainlfo<=0, fuzzgain, fuzzgain * SinOsc.kr(fuzzgainlfo, 0, fuzzgainlfomul, fuzzgainlfoadd));
fuzztone = if(fuzztone_<=0, fuzztone, Line.kr(fuzztone, fuzztone_, sus*fuzztone_d));
fuzztone = if(fuzztonelfo<=0, fuzztone, fuzztone * SinOsc.kr(fuzztonelfo, 0, fuzztonelfomul, fuzztonelfoadd));
fuzzoctave = if(fuzzoctave_<=0, fuzzoctave, Line.kr(fuzzoctave, fuzzoctave_, sus*fuzzoctave_d));
fuzzoctave = if(fuzzoctavelfo<=0, fuzzoctave, fuzzoctave * SinOsc.kr(fuzzoctavelfo, 0, fuzzoctavelfomul, fuzzoctavelfoadd));
dry = osc;
osc = LPF.ar(osc, 6000);
osc = Compander.ar(osc, osc, 0.2, 1, 0.6, 0.002, 0.05, 1.5);
fuzzed = (osc * fuzzgain * 2.5);
fuzzed = fuzzed + (fuzzed.cubed * 0.15);
fuzzed = fuzzed.clip(-0.85, 0.55);
octaveUp = (osc.abs * fuzzgain * 1.5).softclip * fuzzoctave;
subHarm = LPF.ar(osc * 0.5, 200).wrap(-0.3, 0.3) * (1 - fuzztone) * 0.4;
fuzzed = fuzzed + octaveUp + subHarm;
fuzzed = BPeakEQ.ar(fuzzed, 800, 0.8, fuzztone * 3);
fuzzed = LPF.ar(fuzzed, 4000 + (fuzztone * 6000));
fuzzed = LeakDC.ar(fuzzed);
osc = XFade2.ar(dry, fuzzed * 0.7, fuzz * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;