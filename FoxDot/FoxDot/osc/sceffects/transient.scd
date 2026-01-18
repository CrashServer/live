SynthDef.new(\transient,
{|bus, transient, transattack, transsustain, transtime, transient_, transient_d, transientlfo, transientlfomul, transientlfoadd, transattack_, transattack_d, transattacklfo, transattacklfomul, transattacklfoadd, transsustain_, transsustain_d, transsustainlfo, transsustainlfomul, transsustainlfoadd, transtime_, transtime_d, transtimelfo, transtimelfomul, transtimelfoadd, sus|
var osc,dry,env,attack,sustain,shaped;
osc = In.ar(bus, 2);
transient = if(transient_<=0, transient, Line.kr(transient, transient_, sus*transient_d));
transient = if(transientlfo<=0, transient, transient * SinOsc.kr(transientlfo, 0, transientlfomul, transientlfoadd));
transattack = if(transattack_<=0, transattack, Line.kr(transattack, transattack_, sus*transattack_d));
transattack = if(transattacklfo<=0, transattack, transattack * SinOsc.kr(transattacklfo, 0, transattacklfomul, transattacklfoadd));
transsustain = if(transsustain_<=0, transsustain, Line.kr(transsustain, transsustain_, sus*transsustain_d));
transsustain = if(transsustainlfo<=0, transsustain, transsustain * SinOsc.kr(transsustainlfo, 0, transsustainlfomul, transsustainlfoadd));
transtime = if(transtime_<=0, transtime, Line.kr(transtime, transtime_, sus*transtime_d));
transtime = if(transtimelfo<=0, transtime, transtime * SinOsc.kr(transtimelfo, 0, transtimelfomul, transtimelfoadd));
dry = osc;
env = Amplitude.ar(osc, transtime, 0.1);
attack = Amplitude.ar(osc, 0.001, transtime);
sustain = Amplitude.ar(osc, transtime * 2, 0.3);
shaped = osc * ((attack / (env + 0.001)).clip(0, 3) * (transattack - 1) + 1);
shaped = shaped * ((sustain / (env + 0.001)).clip(0, 2) * (transsustain - 1) + 1);
shaped = Limiter.ar(shaped, 0.95, 0.001);
osc = XFade2.ar(dry, shaped, transient * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;