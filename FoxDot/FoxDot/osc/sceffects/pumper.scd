SynthDef.new(\pumper,
{|bus, pumper, pumprate, pumpattack, pumprel, pumpcurve, pumper_, pumper_d, pumperlfo, pumperlfomul, pumperlfoadd, pumperlfophase, pumprate_, pumprate_d, pumpratelfo, pumpratelfomul, pumpratelfoadd, pumpratelfophase, pumpattack_, pumpattack_d, pumpattacklfo, pumpattacklfomul, pumpattacklfoadd, pumpattacklfophase, pumprel_, pumprel_d, pumprellfo, pumprellfomul, pumprellfoadd, pumprellfophase, pumpcurve_, pumpcurve_d, pumpcurvelfo, pumpcurvelfomul, pumpcurvelfoadd, pumpcurvelfophase, sus|
var osc,dry,pumpEnv,rate;
osc = In.ar(bus, 2);
pumper = if(pumper_<=0, pumper, Line.kr(pumper, pumper_, sus*pumper_d));
pumper = if(pumperlfo<=0, pumper, pumper * SinOsc.kr(pumperlfo, pumperlfophase, pumperlfomul, pumperlfoadd));
pumprate = if(pumprate_<=0, pumprate, Line.kr(pumprate, pumprate_, sus*pumprate_d));
pumprate = if(pumpratelfo<=0, pumprate, pumprate * SinOsc.kr(pumpratelfo, pumpratelfophase, pumpratelfomul, pumpratelfoadd));
pumpattack = if(pumpattack_<=0, pumpattack, Line.kr(pumpattack, pumpattack_, sus*pumpattack_d));
pumpattack = if(pumpattacklfo<=0, pumpattack, pumpattack * SinOsc.kr(pumpattacklfo, pumpattacklfophase, pumpattacklfomul, pumpattacklfoadd));
pumprel = if(pumprel_<=0, pumprel, Line.kr(pumprel, pumprel_, sus*pumprel_d));
pumprel = if(pumprellfo<=0, pumprel, pumprel * SinOsc.kr(pumprellfo, pumprellfophase, pumprellfomul, pumprellfoadd));
pumpcurve = if(pumpcurve_<=0, pumpcurve, Line.kr(pumpcurve, pumpcurve_, sus*pumpcurve_d));
pumpcurve = if(pumpcurvelfo<=0, pumpcurve, pumpcurve * SinOsc.kr(pumpcurvelfo, pumpcurvelfophase, pumpcurvelfomul, pumpcurvelfoadd));
dry = osc;
rate = pumprate / sus;
pumpEnv = EnvGen.kr(Env.perc(pumpattack, pumprel, 1, pumpcurve), Impulse.kr(rate));
pumpEnv = 1 - (pumpEnv * pumper);
pumpEnv = pumpEnv.clip(0.05, 1);
osc = osc * pumpEnv;
ReplaceOut.ar(bus, osc)}).add;