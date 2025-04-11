SynthDef.new(\chop,
{|bus, chop, sus, chopmix, chopwave, chopi, chop_, chop_d, choplfo, chopmix_, chopmix_d, chopmixlfo, chopwave_, chopwave_d, chopwavelfo, chopi_, chopi_d, chopilfo|
var osc;
osc = In.ar(bus, 2);
chop = if(chop_<=0, chop, Line.kr(chop, chop_, sus*chop_d));
chop = if(choplfo<=0, chop, chop * SinOsc.kr(choplfo, 0, 1, 1));
chopmix = if(chopmix_<=0, chopmix, Line.kr(chopmix, chopmix_, sus*chopmix_d));
chopmix = if(chopmixlfo<=0, chopmix, chopmix * SinOsc.kr(chopmixlfo, 0, 1, 1));
chopwave = if(chopwave_<=0, chopwave, Line.kr(chopwave, chopwave_, sus*chopwave_d));
chopwave = if(chopwavelfo<=0, chopwave, chopwave * SinOsc.kr(chopwavelfo, 0, 1, 1));
chopi = if(chopi_<=0, chopi, Line.kr(chopi, chopi_, sus*chopi_d));
chopi = if(chopilfo<=0, chopi, chopi * SinOsc.kr(chopilfo, 0, 1, 1));
osc = SelectX.ar(chopmix, [osc, osc * SelectX.kr(chopwave, [LFPulse.kr(chop / sus, iphase:chopi, add: 0.01), LFTri.kr(chop / sus, iphase:chopi, add: 0.01), LFSaw.kr(chop / sus, iphase:chopi, add: 0.01), FSinOsc.kr(chop / sus, iphase:chopi, add: 0.01), LFPar.kr(chop / sus, iphase:chopi, add: 0.01)])]);
ReplaceOut.ar(bus, osc)}).add;