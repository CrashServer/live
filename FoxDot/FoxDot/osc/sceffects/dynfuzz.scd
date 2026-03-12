SynthDef.new(\dynfuzz,
{|bus, dynfuzz, dfgain, dfatk, dfdec, dftone, dynfuzz_, dynfuzz_d, dynfuzzlfo, dynfuzzlfomul, dynfuzzlfoadd, dfgain_, dfgain_d, dfgainlfo, dfgainlfomul, dfgainlfoadd, dfatk_, dfatk_d, dfatklfo, dfatklfomul, dfatklfoadd, dfdec_, dfdec_d, dfdeclfo, dfdeclfomul, dfdeclfoadd, dftone_, dftone_d, dftonelfo, dftonelfomul, dftonelfoadd, sus|
var osc,dry,trig,env,driven,fuzzed;
osc = In.ar(bus, 2);
dynfuzz = if(dynfuzz_<=0, dynfuzz, Line.kr(dynfuzz, dynfuzz_, sus*dynfuzz_d));
dynfuzz = if(dynfuzzlfo<=0, dynfuzz, dynfuzz * SinOsc.kr(dynfuzzlfo, 0, dynfuzzlfomul, dynfuzzlfoadd));
dfgain = if(dfgain_<=0, dfgain, Line.kr(dfgain, dfgain_, sus*dfgain_d));
dfgain = if(dfgainlfo<=0, dfgain, dfgain * SinOsc.kr(dfgainlfo, 0, dfgainlfomul, dfgainlfoadd));
dfatk = if(dfatk_<=0, dfatk, Line.kr(dfatk, dfatk_, sus*dfatk_d));
dfatk = if(dfatklfo<=0, dfatk, dfatk * SinOsc.kr(dfatklfo, 0, dfatklfomul, dfatklfoadd));
dfdec = if(dfdec_<=0, dfdec, Line.kr(dfdec, dfdec_, sus*dfdec_d));
dfdec = if(dfdeclfo<=0, dfdec, dfdec * SinOsc.kr(dfdeclfo, 0, dfdeclfomul, dfdeclfoadd));
dftone = if(dftone_<=0, dftone, Line.kr(dftone, dftone_, sus*dftone_d));
dftone = if(dftonelfo<=0, dftone, dftone * SinOsc.kr(dftonelfo, 0, dftonelfomul, dftonelfoadd));
dry = osc;
trig = Trig1.kr(Amplitude.kr(osc, 0.001, 0.05) > 0.02, 0.01);
env = Decay2.kr(trig, dfatk, dfdec);
driven = osc * (1 + (env * dfgain));
fuzzed = driven.tanh;
fuzzed = BPeakEQ.ar(fuzzed, 900, 0.7, dftone.clip(0, 1) * 2);
fuzzed = LPF.ar(fuzzed, 3000 + (dftone.clip(0, 1) * 7000));
fuzzed = LeakDC.ar(fuzzed);
osc = XFade2.ar(dry, fuzzed * 0.75, dynfuzz * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;