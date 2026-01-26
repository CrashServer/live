SynthDef.new(\envdist,
{|bus, envdist, envdistgain, envdistsens, envdistattack, envdist_, envdist_d, envdistlfo, envdistlfomul, envdistlfoadd, envdistgain_, envdistgain_d, envdistgainlfo, envdistgainlfomul, envdistgainlfoadd, envdistsens_, envdistsens_d, envdistsenslfo, envdistsenslfomul, envdistsenslfoadd, envdistattack_, envdistattack_d, envdistattacklfo, envdistattacklfomul, envdistattacklfoadd, sus|
var osc,dry,env,distAmount,distorted,lowDist,highDist;
osc = In.ar(bus, 2);
envdist = if(envdist_<=0, envdist, Line.kr(envdist, envdist_, sus*envdist_d));
envdist = if(envdistlfo<=0, envdist, envdist * SinOsc.kr(envdistlfo, 0, envdistlfomul, envdistlfoadd));
envdistgain = if(envdistgain_<=0, envdistgain, Line.kr(envdistgain, envdistgain_, sus*envdistgain_d));
envdistgain = if(envdistgainlfo<=0, envdistgain, envdistgain * SinOsc.kr(envdistgainlfo, 0, envdistgainlfomul, envdistgainlfoadd));
envdistsens = if(envdistsens_<=0, envdistsens, Line.kr(envdistsens, envdistsens_, sus*envdistsens_d));
envdistsens = if(envdistsenslfo<=0, envdistsens, envdistsens * SinOsc.kr(envdistsenslfo, 0, envdistsenslfomul, envdistsenslfoadd));
envdistattack = if(envdistattack_<=0, envdistattack, Line.kr(envdistattack, envdistattack_, sus*envdistattack_d));
envdistattack = if(envdistattacklfo<=0, envdistattack, envdistattack * SinOsc.kr(envdistattacklfo, 0, envdistattacklfomul, envdistattacklfoadd));
dry = osc;
env = Amplitude.kr(osc, envdistattack, 0.08);
env = (env * envdistsens * 8).clip(0, 1);
distAmount = envdistgain * (0.8 + (env * 4));
lowDist = LPF.ar(osc, 400);
lowDist = (lowDist * distAmount * 0.8).softclip;
highDist = HPF.ar(osc, 400);
highDist = LPF.ar(highDist, 8000);
highDist = (highDist * distAmount * 1.2);
highDist = highDist + (highDist.cubed * 0.2);
highDist = highDist.fold(-0.9, 0.9);
distorted = lowDist + (highDist * 0.7);
distorted = distorted + ((distorted * env * 1.5).wrap(-0.6, 0.6) * 0.25);
distorted = LPF.ar(distorted, 7000);
distorted = LeakDC.ar(distorted);
osc = XFade2.ar(dry, distorted * 0.75, envdist * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;