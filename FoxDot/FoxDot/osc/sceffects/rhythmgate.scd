SynthDef.new(\rhythmgate,
{|bus, rgate, rgaterate, rgatewave, beat_dur, rgate_, rgate_d, rgatelfo, rgatelfomul, rgatelfoadd, rgaterate_, rgaterate_d, rgateratelfo, rgateratelfomul, rgateratelfoadd, rgatewave_, rgatewave_d, rgatewavelfo, rgatewavelfomul, rgatewavelfoadd, beat_dur_, beat_dur_d, beat_durlfo, beat_durlfomul, beat_durlfoadd, sus|
var osc,dry,gateEnv,rate;
osc = In.ar(bus, 2);
rgate = if(rgate_<=0, rgate, Line.kr(rgate, rgate_, sus*rgate_d));
rgate = if(rgatelfo<=0, rgate, rgate * SinOsc.kr(rgatelfo, 0, rgatelfomul, rgatelfoadd));
rgaterate = if(rgaterate_<=0, rgaterate, Line.kr(rgaterate, rgaterate_, sus*rgaterate_d));
rgaterate = if(rgateratelfo<=0, rgaterate, rgaterate * SinOsc.kr(rgateratelfo, 0, rgateratelfomul, rgateratelfoadd));
rgatewave = if(rgatewave_<=0, rgatewave, Line.kr(rgatewave, rgatewave_, sus*rgatewave_d));
rgatewave = if(rgatewavelfo<=0, rgatewave, rgatewave * SinOsc.kr(rgatewavelfo, 0, rgatewavelfomul, rgatewavelfoadd));
beat_dur = if(beat_dur_<=0, beat_dur, Line.kr(beat_dur, beat_dur_, sus*beat_dur_d));
beat_dur = if(beat_durlfo<=0, beat_dur, beat_dur * SinOsc.kr(beat_durlfo, 0, beat_durlfomul, beat_durlfoadd));
dry = osc;
rate = rgaterate / beat_dur;
gateEnv = Select.kr(rgatewave, [LFPulse.kr(rate, width: 0.5), LFSaw.kr(rate).range(0, 1), SinOsc.kr(rate).range(0, 1)]);
osc = XFade2.ar(dry, osc * Lag.kr(gateEnv, 0.01), rgate * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;