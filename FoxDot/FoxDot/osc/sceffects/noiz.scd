SynthDef.new(\noiz,
{|bus, noiz, noizr, noizt, sus, noiz_, noiz_d, noizlfo, noizr_, noizr_d, noizrlfo, noizt_, noizt_d, noiztlfo|
var osc,noizType,env;
osc = In.ar(bus, 2);
noiz = if(noiz_<=0, noiz, Line.kr(noiz, noiz_, sus*noiz_d));
noiz = if(noizlfo<=0, noiz, noiz * SinOsc.kr(noizlfo, 0, 1, 1));
noizr = if(noizr_<=0, noizr, Line.kr(noizr, noizr_, sus*noizr_d));
noizr = if(noizrlfo<=0, noizr, noizr * SinOsc.kr(noizrlfo, 0, 1, 1));
noizt = if(noizt_<=0, noizt, Line.kr(noizt, noizt_, sus*noizt_d));
noizt = if(noiztlfo<=0, noizt, noizt * SinOsc.kr(noiztlfo, 0, 1, 1));
env=EnvGen.ar(Env.perc(attackTime: 0,releaseTime: noizr*sus, level: noiz,curve: \linear), doneAction: 0);
noizType = Select.ar(noizt, [BrownNoise.ar(0.1), WhiteNoise.ar(0.1), ClipNoise.ar(0.1),	GrayNoise.ar(0.1), PinkNoise.ar(0.1)]);
osc = osc + (noizType * env);
ReplaceOut.ar(bus, osc)}).add;