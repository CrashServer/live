SynthDef.new(\autopan,
{|bus, apan, awidth, apwave, beat_dur, apan_, apan_d, apanlfo, apanlfomul, apanlfoadd, awidth_, awidth_d, awidthlfo, awidthlfomul, awidthlfoadd, apwave_, apwave_d, apwavelfo, apwavelfomul, apwavelfoadd, beat_dur_, beat_dur_d, beat_durlfo, beat_durlfomul, beat_durlfoadd, sus|
var osc,panLfo,rate;
osc = In.ar(bus, 2);
apan = if(apan_<=0, apan, Line.kr(apan, apan_, sus*apan_d));
apan = if(apanlfo<=0, apan, apan * SinOsc.kr(apanlfo, 0, apanlfomul, apanlfoadd));
awidth = if(awidth_<=0, awidth, Line.kr(awidth, awidth_, sus*awidth_d));
awidth = if(awidthlfo<=0, awidth, awidth * SinOsc.kr(awidthlfo, 0, awidthlfomul, awidthlfoadd));
apwave = if(apwave_<=0, apwave, Line.kr(apwave, apwave_, sus*apwave_d));
apwave = if(apwavelfo<=0, apwave, apwave * SinOsc.kr(apwavelfo, 0, apwavelfomul, apwavelfoadd));
beat_dur = if(beat_dur_<=0, beat_dur, Line.kr(beat_dur, beat_dur_, sus*beat_dur_d));
beat_dur = if(beat_durlfo<=0, beat_dur, beat_dur * SinOsc.kr(beat_durlfo, 0, beat_durlfomul, beat_durlfoadd));
rate = apan / beat_dur;
panLfo = SelectX.kr(apwave, [SinOsc.kr(rate), LFTri.kr(rate), LFSaw.kr(rate), LFPulse.kr(rate)]);
osc = Pan2.ar(osc[0] + osc[1], panLfo * awidth);
ReplaceOut.ar(bus, osc)}).add;