SynthDef.new(\darkpad,
{|bus=0, amp=1, pan=0, freq=440, fmod=0, sus=4, atk=0.5, rel=1,
  cutoff=1200, res=0.25, drive=1.2, detune=0.008, dark=0.5, sub=0.4|
var sig, env, osc1, osc2, osc3, osc4, osc5, osc6, subOsc, filtered, final;

freq = In.kr(bus, 1);
freq = freq.clip(20, 10000);

env = EnvGen.ar(Env([0, 1, 1, 0], [atk, sus, rel], [-4, 0, -4]), doneAction: 2);

osc1 = LFSaw.ar(freq);
osc2 = LFSaw.ar(freq * (1 + detune));
osc3 = LFSaw.ar(freq * (1 - detune));
osc4 = LFSaw.ar(freq * (1 + (detune * 2))) * 0.5;
osc5 = LFSaw.ar(freq * (1 - (detune * 2))) * 0.5;
osc6 = LFTri.ar(freq) * 0.4;

sig = (osc1 + osc2 + osc3 + osc4 + osc5 + osc6) * 0.12;

subOsc = SinOsc.ar(freq * 0.5) * sub;
sig = sig + subOsc;

filtered = RLPF.ar(sig, (cutoff * (1.5 - dark).clip(0.2, 1.5)).clip(100, 8000), res.clip(0.1, 0.7));
filtered = LPF.ar(filtered, (cutoff * (2 - dark).clip(0.5, 2)).clip(200, 12000));

filtered = (filtered * drive).softclip;

final = filtered * env * amp * 0.5;
final = Pan2.ar(final, pan);
ReplaceOut.ar(bus, final);
}).add;
