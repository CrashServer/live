SynthDef.new(\stutterfx,
{|bus, stut, stutrate, stutlen, t_reset, stut_, stut_d, stutlfo, stutlfomul, stutlfoadd, stutrate_, stutrate_d, stutratelfo, stutratelfomul, stutratelfoadd, stutlen_, stutlen_d, stutlenlfo, stutlenlfomul, stutlenlfoadd, t_reset_, t_reset_d, t_resetlfo, t_resetlfomul, t_resetlfoadd, sus|
var osc,dry,reset,wet;
osc = In.ar(bus, 2);
stut = if(stut_<=0, stut, Line.kr(stut, stut_, sus*stut_d));
stut = if(stutlfo<=0, stut, stut * SinOsc.kr(stutlfo, 0, stutlfomul, stutlfoadd));
stutrate = if(stutrate_<=0, stutrate, Line.kr(stutrate, stutrate_, sus*stutrate_d));
stutrate = if(stutratelfo<=0, stutrate, stutrate * SinOsc.kr(stutratelfo, 0, stutratelfomul, stutratelfoadd));
stutlen = if(stutlen_<=0, stutlen, Line.kr(stutlen, stutlen_, sus*stutlen_d));
stutlen = if(stutlenlfo<=0, stutlen, stutlen * SinOsc.kr(stutlenlfo, 0, stutlenlfomul, stutlenlfoadd));
t_reset = if(t_reset_<=0, t_reset, Line.kr(t_reset, t_reset_, sus*t_reset_d));
t_reset = if(t_resetlfo<=0, t_reset, t_reset * SinOsc.kr(t_resetlfo, 0, t_resetlfomul, t_resetlfoadd));
~stutter = { |snd, reset, stutlen, maxdelay = 1| var phase, fragment, del; phase = Sweep.ar(reset); fragment = { |ph| (ph - Delay1.ar(ph)) < 0 + Impulse.ar(0) }.value(phase / stutlen % 1); del = Latch.ar(phase, fragment) + ((stutlen - Sweep.ar(fragment)) * (stutrate - 1)); DelayC.ar(snd, maxdelay, del); };
dry = osc;
reset = Onsets.kr(FFT(LocalBuf(1024), osc), t_reset);
wet = ~stutter.(osc, reset, stutlen);
osc = SelectX.ar(stut, [dry, wet], wrap:1);
ReplaceOut.ar(bus, osc)}).add;