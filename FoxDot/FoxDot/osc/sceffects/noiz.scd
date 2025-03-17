SynthDef.new(\noiz,
{|bus, noiz, noizr, noizt, sus, noiz_, noiz_d, noizr_, noizr_d, noizt_, noizt_d|
var osc,noizType,env;
osc = In.ar(bus, 2);
noiz = if(noiz_<=0, noiz, Line.kr(noiz, noiz_, sus*noiz_d));
noizr = if(noizr_<=0, noizr, Line.kr(noizr, noizr_, sus*noizr_d));
noizt = if(noizt_<=0, noizt, Line.kr(noizt, noizt_, sus*noizt_d));
env=EnvGen.ar(Env.perc(attackTime: 0,releaseTime: noizr*sus, level: noiz,curve: \linear), doneAction: 0);
noizType = Select.ar(noizt, [BrownNoise.ar(0.1), WhiteNoise.ar(0.1), ClipNoise.ar(0.1),	GrayNoise.ar(0.1), PinkNoise.ar(0.1)]);
osc = osc + (noizType * env);
ReplaceOut.ar(bus, osc)}).add;