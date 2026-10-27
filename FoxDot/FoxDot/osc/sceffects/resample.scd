SynthDef.new(\resample,
{|bus, resample=0.5, rsrate=0.5, rsgrains=8, rsjitter=0.1, sus, beat_dur,
  resample_, resample_d, resamplelfo, resamplelfomul, resamplelfoadd,
  rsrate_, rsrate_d, rsratelfo, rsratelfomul, rsratelfoadd,
  rsgrains_, rsgrains_d, rsgrainslfo, rsgrainslfomul, rsgrainslfoadd,
  rsjitter_, rsjitter_d, rsjitterlfo, rsjitterlfomul, rsjitterlfoadd|
var osc, dry, granular;
osc = In.ar(bus, 2);
dry = osc;
resample = if(resample_<=0, resample, Line.kr(resample, resample_, sus*resample_d));
resample = if(resamplelfo<=0, resample, resample * SinOsc.kr(resamplelfo, 0, resamplelfomul, resamplelfoadd));
rsrate = if(rsrate_<=0, rsrate, Line.kr(rsrate, rsrate_, sus*rsrate_d));
rsrate = if(rsratelfo<=0, rsrate, rsrate * SinOsc.kr(rsratelfo, 0, rsratelfomul, rsratelfoadd));
rsgrains = if(rsgrains_<=0, rsgrains, Line.kr(rsgrains, rsgrains_, sus*rsgrains_d));
rsgrains = if(rsgrainslfo<=0, rsgrains, rsgrains * SinOsc.kr(rsgrainslfo, 0, rsgrainslfomul, rsgrainslfoadd));
rsjitter = if(rsjitter_<=0, rsjitter, Line.kr(rsjitter, rsjitter_, sus*rsjitter_d));
rsjitter = if(rsjitterlfo<=0, rsjitter, rsjitter * SinOsc.kr(rsjitterlfo, 0, rsjitterlfomul, rsjitterlfoadd));
// Granular time stretching with jitter
granular = PitchShift.ar(osc,
    windowSize: 0.1,
    pitchRatio: rsrate.linlin(0, 1, 0.5, 2),
    pitchDispersion: rsjitter,
    timeDispersion: rsjitter * 0.1
);
// Add stutter grains
granular = granular * LFPulse.ar(rsgrains, width: LFNoise1.kr(2).range(0.3, 0.7));
granular = LeakDC.ar(granular);
osc = XFade2.ar(dry, granular, resample * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;
