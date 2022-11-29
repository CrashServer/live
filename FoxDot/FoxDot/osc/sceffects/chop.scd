SynthDef.new(\chop,
{|bus, chop, sus, chopmix, chopwave, chopi|
var osc;
osc = In.ar(bus, 2);
osc = SelectX.ar(chopmix, [osc, osc * SelectX.kr(chopwave, [LFPulse.kr(chop / sus, iphase:chopi, add: 0.01), LFTri.kr(chop / sus, iphase:chopi, add: 0.01), LFSaw.kr(chop / sus, iphase:chopi, add: 0.01), FSinOsc.kr(chop / sus, iphase:chopi, add: 0.01), LFPar.kr(chop / sus, iphase:chopi, add: 0.01)])]);
ReplaceOut.ar(bus, osc)}).add;