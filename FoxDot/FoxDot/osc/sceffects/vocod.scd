SynthDef.new(\vocod,
{|bus, vocod, voccarr, vocbw, vocod_, vocod_d, vocodlfo, vocodlfomul, vocodlfoadd, voccarr_, voccarr_d, voccarrlfo, voccarrlfomul, voccarrlfoadd, vocbw_, vocbw_d, vocbwlfo, vocbwlfomul, vocbwlfoadd, sus|
var osc,dry,carrier,wet,freqs,amps;
osc = In.ar(bus, 2);
vocod = if(vocod_<=0, vocod, Line.kr(vocod, vocod_, sus*vocod_d));
vocod = if(vocodlfo<=0, vocod, vocod * SinOsc.kr(vocodlfo, 0, vocodlfomul, vocodlfoadd));
voccarr = if(voccarr_<=0, voccarr, Line.kr(voccarr, voccarr_, sus*voccarr_d));
voccarr = if(voccarrlfo<=0, voccarr, voccarr * SinOsc.kr(voccarrlfo, 0, voccarrlfomul, voccarrlfoadd));
vocbw = if(vocbw_<=0, vocbw, Line.kr(vocbw, vocbw_, sus*vocbw_d));
vocbw = if(vocbwlfo<=0, vocbw, vocbw * SinOsc.kr(vocbwlfo, 0, vocbwlfomul, vocbwlfoadd));
dry = osc;
carrier = (Pulse.ar([80, 80.5], 0.5) * voccarr) + (WhiteNoise.ar(0.3) * (1 - voccarr));
wet = [100, 250, 500, 1000, 2000, 3500, 6000, 10000].collect({|f| BPF.ar(carrier, f, vocbw) * Amplitude.kr(BPF.ar(osc, f, vocbw), 0.005, 0.05)}).sum;
wet = LeakDC.ar(wet * 4);
osc = XFade2.ar(dry, wet, vocod * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;