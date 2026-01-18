SynthDef.new(\fbdelay,
{|bus, fbdelay, fbtime, fbfeed, fbcutoff, fbspread, beat_dur, fbdelay_, fbdelay_d, fbdelaylfo, fbdelaylfomul, fbdelaylfoadd, fbtime_, fbtime_d, fbtimelfo, fbtimelfomul, fbtimelfoadd, fbfeed_, fbfeed_d, fbfeedlfo, fbfeedlfomul, fbfeedlfoadd, fbcutoff_, fbcutoff_d, fbcutofflfo, fbcutofflfomul, fbcutofflfoadd, fbspread_, fbspread_d, fbspreadlfo, fbspreadlfomul, fbspreadlfoadd, beat_dur_, beat_dur_d, beat_durlfo, beat_durlfomul, beat_durlfoadd, sus|
var osc,dry,delayed,leftDelay,rightDelay,fb,delTime;
osc = In.ar(bus, 2);
fbdelay = if(fbdelay_<=0, fbdelay, Line.kr(fbdelay, fbdelay_, sus*fbdelay_d));
fbdelay = if(fbdelaylfo<=0, fbdelay, fbdelay * SinOsc.kr(fbdelaylfo, 0, fbdelaylfomul, fbdelaylfoadd));
fbtime = if(fbtime_<=0, fbtime, Line.kr(fbtime, fbtime_, sus*fbtime_d));
fbtime = if(fbtimelfo<=0, fbtime, fbtime * SinOsc.kr(fbtimelfo, 0, fbtimelfomul, fbtimelfoadd));
fbfeed = if(fbfeed_<=0, fbfeed, Line.kr(fbfeed, fbfeed_, sus*fbfeed_d));
fbfeed = if(fbfeedlfo<=0, fbfeed, fbfeed * SinOsc.kr(fbfeedlfo, 0, fbfeedlfomul, fbfeedlfoadd));
fbcutoff = if(fbcutoff_<=0, fbcutoff, Line.kr(fbcutoff, fbcutoff_, sus*fbcutoff_d));
fbcutoff = if(fbcutofflfo<=0, fbcutoff, fbcutoff * SinOsc.kr(fbcutofflfo, 0, fbcutofflfomul, fbcutofflfoadd));
fbspread = if(fbspread_<=0, fbspread, Line.kr(fbspread, fbspread_, sus*fbspread_d));
fbspread = if(fbspreadlfo<=0, fbspread, fbspread * SinOsc.kr(fbspreadlfo, 0, fbspreadlfomul, fbspreadlfoadd));
beat_dur = if(beat_dur_<=0, beat_dur, Line.kr(beat_dur, beat_dur_, sus*beat_dur_d));
beat_dur = if(beat_durlfo<=0, beat_dur, beat_dur * SinOsc.kr(beat_durlfo, 0, beat_durlfomul, beat_durlfoadd));
dry = osc;
delTime = fbtime * beat_dur;
fb = LocalIn.ar(2) * fbfeed;
fb = HPF.ar(fb, 80);
fb = LPF.ar(fb, fbcutoff);
fb = (fb * 1.1).softclip;
leftDelay = DelayC.ar(osc[0] + fb[1], 2, delTime.clip(0.001, 2));
rightDelay = DelayC.ar(osc[1] + fb[0], 2, (delTime * (1 + fbspread)).clip(0.001, 2));
LocalOut.ar([leftDelay, rightDelay]);
delayed = [leftDelay, rightDelay] * 0.7;
osc = XFade2.ar(dry, dry + delayed, fbdelay * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;