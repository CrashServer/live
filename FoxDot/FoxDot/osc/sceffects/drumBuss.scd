SynthDef.new(\drumBuss,
{|bus, drumBuss, drumBuss_drive, drumBuss_crunch, drumBuss_transients, drumBuss_boom, drumBuss_, drumBuss_d, drumBusslfo, drumBusslfomul, drumBusslfoadd, drumBuss_drive_, drumBuss_drive_d, drumBuss_drivelfo, drumBuss_drivelfomul, drumBuss_drivelfoadd, drumBuss_crunch_, drumBuss_crunch_d, drumBuss_crunchlfo, drumBuss_crunchlfomul, drumBuss_crunchlfoadd, drumBuss_transients_, drumBuss_transients_d, drumBuss_transientslfo, drumBuss_transientslfomul, drumBuss_transientslfoadd, drumBuss_boom_, drumBuss_boom_d, drumBuss_boomlfo, drumBuss_boomlfomul, drumBuss_boomlfoadd, sus|
var osc,dry,transPresence,sustainPresence,boostAmt,transGain;
osc = In.ar(bus, 2);
drumBuss = if(drumBuss_<=0, drumBuss, Line.kr(drumBuss, drumBuss_, sus*drumBuss_d));
drumBuss = if(drumBusslfo<=0, drumBuss, drumBuss * SinOsc.kr(drumBusslfo, 0, drumBusslfomul, drumBusslfoadd));
drumBuss_drive = if(drumBuss_drive_<=0, drumBuss_drive, Line.kr(drumBuss_drive, drumBuss_drive_, sus*drumBuss_drive_d));
drumBuss_drive = if(drumBuss_drivelfo<=0, drumBuss_drive, drumBuss_drive * SinOsc.kr(drumBuss_drivelfo, 0, drumBuss_drivelfomul, drumBuss_drivelfoadd));
drumBuss_crunch = if(drumBuss_crunch_<=0, drumBuss_crunch, Line.kr(drumBuss_crunch, drumBuss_crunch_, sus*drumBuss_crunch_d));
drumBuss_crunch = if(drumBuss_crunchlfo<=0, drumBuss_crunch, drumBuss_crunch * SinOsc.kr(drumBuss_crunchlfo, 0, drumBuss_crunchlfomul, drumBuss_crunchlfoadd));
drumBuss_transients = if(drumBuss_transients_<=0, drumBuss_transients, Line.kr(drumBuss_transients, drumBuss_transients_, sus*drumBuss_transients_d));
drumBuss_transients = if(drumBuss_transientslfo<=0, drumBuss_transients, drumBuss_transients * SinOsc.kr(drumBuss_transientslfo, 0, drumBuss_transientslfomul, drumBuss_transientslfoadd));
drumBuss_boom = if(drumBuss_boom_<=0, drumBuss_boom, Line.kr(drumBuss_boom, drumBuss_boom_, sus*drumBuss_boom_d));
drumBuss_boom = if(drumBuss_boomlfo<=0, drumBuss_boom, drumBuss_boom * SinOsc.kr(drumBuss_boomlfo, 0, drumBuss_boomlfomul, drumBuss_boomlfoadd));
dry = osc;
osc = Compander.ar(osc, osc, thresh: 0.5, slopeBelow: 1, slopeAbove: 4, clampTime: 0.01, relaxTime: 0.15);
osc = osc + (drumBuss_drive * (((osc*(1+(4*drumBuss_drive))).tanh - osc) + (0.3*LPF.ar(osc,120))));
osc = osc + (drumBuss_crunch * 0.6 * (HPF.ar(osc,800)*(1+(8*drumBuss_crunch))).distort);
osc = LPF.ar(osc, 20000 - (drumBuss_crunch*12000));
transPresence = ((Amplitude.kr(dry, 0.001, 0.03) - Amplitude.kr(dry, 0.05, 0.3)) / Amplitude.kr(dry, 0.01, 0.3).max(0.001)).clip(0, 2);
sustainPresence = 1 - transPresence.clip(0, 1);
boostAmt   = drumBuss_transients.max(0);
transGain = 1 + (boostAmt * transPresence * 1.5) + (boostAmt * sustainPresence * 0.3) - ((drumBuss_transients.neg).max(0) * sustainPresence * 0.7);
transGain = transGain.max(0).lag(0.003);
osc = osc * transGain;
osc = osc + (drumBuss_boom * SinOsc.ar(55) * Amplitude.kr(LPF.ar(dry,100).abs, 0.001, 0.2) * 3);
osc = SelectX.ar(drumBuss, [dry, osc*0.75]);
osc = Limiter.ar(osc, 0.95);
ReplaceOut.ar(bus, osc)}).add;