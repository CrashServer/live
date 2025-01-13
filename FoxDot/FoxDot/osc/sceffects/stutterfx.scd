SynthDef.new(\stutterfx,
{|bus, stut, stutrate, stutlen, t_reset, stut_, stut_d, stutrate_, stutrate_d, stutlen_, stutlen_d, t_reset_, t_reset_d, sus|
var osc,dry,reset,wet;
osc = In.ar(bus, 2);
stut = if(stut_<=0, stut, Line.kr(stut, stut_, sus*stut_d));
stutrate = if(stutrate_<=0, stutrate, Line.kr(stutrate, stutrate_, sus*stutrate_d));
stutlen = if(stutlen_<=0, stutlen, Line.kr(stutlen, stutlen_, sus*stutlen_d));
~stutter = { |snd, reset, stutlen, maxdelay = 1| var phase, fragment, del; phase = Sweep.ar(reset); fragment = { |ph| (ph - Delay1.ar(ph)) < 0 + Impulse.ar(0) }.value(phase / stutlen % 1); del = Latch.ar(phase, fragment) + ((stutlen - Sweep.ar(fragment)) * (stutrate - 1)); DelayC.ar(snd, maxdelay, del); };
dry = osc;
reset = Onsets.kr(FFT(LocalBuf(1024), osc), t_reset);
wet = ~stutter.(osc, reset, stutlen);
osc = SelectX.ar(stut, [dry, wet], wrap:1);
ReplaceOut.ar(bus, osc)}).add;