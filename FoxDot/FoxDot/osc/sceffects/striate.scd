SynthDef.new(\striate,
{|bus, striate, sus, buf, rate, striate_, striate_d, buf_, buf_d, rate_, rate_d|
var osc;
osc = In.kr(bus, 1);
striate = if(striate_<=0, striate, Line.kr(striate, striate_, sus*striate_d));
buf = if(buf_<=0, buf, Line.kr(buf, buf_, sus*buf_d));
rate = if(rate_<=0, rate, Line.kr(rate, rate_, sus*rate_d));
rate = (BufDur.kr(buf) / sus);
rate = Select.kr(rate > 1, [1, rate]);
osc = osc * LFPulse.ar(striate / sus, width:  (BufDur.kr(buf) / rate) / sus) * rate;
ReplaceOut.kr(bus, osc)}).add;