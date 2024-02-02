SynthDef.new(\stutbreak,
{|bus, sbrk, t_reset, sbrkdur, sus|
var osc,dry,reset,wet,stuti,stutlen,stutrate;
osc = In.ar(bus, 2);
stutrate=Rand(0.01, 1.0);
stutlen=Rand(0.01,0.08);
~stutter = { |snd, reset, stutlen, maxdelay = 1| var phase, fragment, del; phase = Sweep.ar(reset); fragment = { |ph| (ph - Delay1.ar(ph)) < 0 + Impulse.ar(0) }.value(phase / stutlen % 1); del = Latch.ar(phase, fragment) + ((stutlen - Sweep.ar(fragment)) * (stutrate - 1)); DelayC.ar(snd, maxdelay, del); };
dry = osc;
stuti = IRand(1,sus*sbrkdur).round(2);
reset = Onsets.kr(FFT(LocalBuf(1024), osc), t_reset);
wet = ~stutter.(osc, reset, stutlen);
wet = wet * LFPulse.kr(stuti/sus, 0.5, mul:1.0);
dry = dry * LFPulse.kr(stuti/sus, mul:1.5);
osc = SelectX.ar(sbrk, [dry, wet], wrap:1);
ReplaceOut.ar(bus, osc)}).add;