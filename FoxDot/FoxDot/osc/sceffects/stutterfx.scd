SynthDef.new(\stutterfx,
{|bus, t_reset, stut, stutrate, stutlen, t_reset_, stut_, stutrate_, stutlen_, sus|
var osc,dry,reset,wet;
osc = In.ar(bus, 2);
t_reset = t_reset+Line.kr(0, t_reset_, sus);
stut = stut+Line.kr(0, stut_, sus);
stutrate = stutrate+Line.kr(0, stutrate_, sus);
stutlen = stutlen+Line.kr(0, stutlen_, sus);
~stutter = { |snd, reset, stutlen, maxdelay = 1| var phase, fragment, del; phase = Sweep.ar(reset); fragment = { |ph| (ph - Delay1.ar(ph)) < 0 + Impulse.ar(0) }.value(phase / stutlen % 1); del = Latch.ar(phase, fragment) + ((stutlen - Sweep.ar(fragment)) * (stutrate - 1)); DelayC.ar(snd, maxdelay, del); };
dry = osc;
reset = Onsets.kr(FFT(LocalBuf(1024), osc), t_reset);
wet = ~stutter.(osc, reset, stutlen);
osc = SelectX.ar(stut, [dry, wet], wrap:1);
ReplaceOut.ar(bus, osc)}).add;