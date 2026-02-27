SynthDef.new(\liveRec,
{|buf=0, bus=0, channel=0, source=0, overdub=0, run=1, level=1|
var input, existing;
input = Select.ar(source, [SoundIn.ar(channel), In.ar(bus, 2)]);
input = input * level;
existing = PlayBuf.ar(2, buf, 1, loop: 1) * overdub;
RecordBuf.ar(input + existing, buf, run: run, loop: 1);
},
metadata: (
credit: "CrashServer",
description: "Live recording into buffer with overdub",
category: \utility,
tags: [\recording, \live, \looper]
)).add;
