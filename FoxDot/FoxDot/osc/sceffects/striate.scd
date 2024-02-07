SynthDef.new(\striate,
{|bus, striate, sus, buf, rate, striate_, buf_, rate_|
var osc;
osc = In.kr(bus, 1);
striate = striate+Line.kr(0, striate_, sus);
buf = buf+Line.kr(0, buf_, sus);
rate = rate+Line.kr(0, rate_, sus);
rate = (BufDur.kr(buf) / sus);
rate = Select.kr(rate > 1, [1, rate]);
osc = osc * LFPulse.ar(striate / sus, width:  (BufDur.kr(buf) / rate) / sus) * rate;
ReplaceOut.kr(bus, osc)}).add;