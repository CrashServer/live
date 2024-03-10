SynthDef.new(\chop,
{|bus, chop, sus, chopmix, chopwave, chopi, chop_, chop_d, chopmix_, chopmix_d, chopwave_, chopwave_d, chopi_, chopi_d|
var osc;
osc = In.ar(bus, 2);
chop = if(chop_<=0, chop, Line.kr(chop, chop_, sus*chop_d));
chopmix = if(chopmix_<=0, chopmix, Line.kr(chopmix, chopmix_, sus*chopmix_d));
chopwave = if(chopwave_<=0, chopwave, Line.kr(chopwave, chopwave_, sus*chopwave_d));
chopi = if(chopi_<=0, chopi, Line.kr(chopi, chopi_, sus*chopi_d));
osc = SelectX.ar(chopmix, [osc, osc * SelectX.kr(chopwave, [LFPulse.kr(chop / sus, iphase:chopi, add: 0.01), LFTri.kr(chop / sus, iphase:chopi, add: 0.01), LFSaw.kr(chop / sus, iphase:chopi, add: 0.01), FSinOsc.kr(chop / sus, iphase:chopi, add: 0.01), LFPar.kr(chop / sus, iphase:chopi, add: 0.01)])]);
ReplaceOut.ar(bus, osc)}).add;