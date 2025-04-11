SynthDef.new(\striate,
{|bus, striate, sus, buf, rate, striate_, striate_d, striatelfo, buf_, buf_d, buflfo, rate_, rate_d, ratelfo|
var osc;
osc = In.kr(bus, 1);
striate = if(striate_<=0, striate, Line.kr(striate, striate_, sus*striate_d));
striate = if(striatelfo<=0, striate, striate * SinOsc.kr(striatelfo, 0, 1, 1));
buf = if(buf_<=0, buf, Line.kr(buf, buf_, sus*buf_d));
buf = if(buflfo<=0, buf, buf * SinOsc.kr(buflfo, 0, 1, 1));
rate = if(rate_<=0, rate, Line.kr(rate, rate_, sus*rate_d));
rate = if(ratelfo<=0, rate, rate * SinOsc.kr(ratelfo, 0, 1, 1));
rate = (BufDur.kr(buf) / sus);
rate = Select.kr(rate > 1, [1, rate]);
osc = osc * LFPulse.ar(striate / sus, width:  (BufDur.kr(buf) / rate) / sus) * rate;
ReplaceOut.kr(bus, osc)}).add;