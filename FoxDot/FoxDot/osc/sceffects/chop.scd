SynthDef.new(\chop,
{|bus, chop, sus, chopmix, chopwave, chopi, chop_, chopmix_, chopwave_, chopi_|
var osc;
osc = In.ar(bus, 2);
chop = chop+Line.kr(0, chop_, sus);
chopmix = chopmix+Line.kr(0, chopmix_, sus);
chopwave = chopwave+Line.kr(0, chopwave_, sus);
chopi = chopi+Line.kr(0, chopi_, sus);
osc = SelectX.ar(chopmix, [osc, osc * SelectX.kr(chopwave, [LFPulse.kr(chop / sus, iphase:chopi, add: 0.01), LFTri.kr(chop / sus, iphase:chopi, add: 0.01), LFSaw.kr(chop / sus, iphase:chopi, add: 0.01), FSinOsc.kr(chop / sus, iphase:chopi, add: 0.01), LFPar.kr(chop / sus, iphase:chopi, add: 0.01)])]);
ReplaceOut.ar(bus, osc)}).add;