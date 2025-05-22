SynthDef.new(\glissandoriginal,
{|bus, glide2, glide2dur, sus, glide2_, glide2_d, glide2lfo, glide2lfomul, glide2lfoadd, glide2dur_, glide2dur_d, glide2durlfo, glide2durlfomul, glide2durlfoadd|
var osc;
osc = In.kr(bus, 1);
glide2 = if(glide2_<=0, glide2, Line.kr(glide2, glide2_, sus*glide2_d));
glide2 = if(glide2lfo<=0, glide2, glide2 * SinOsc.kr(glide2lfo, 0, glide2lfomul, glide2lfoadd));
glide2dur = if(glide2dur_<=0, glide2dur, Line.kr(glide2dur, glide2dur_, sus*glide2dur_d));
glide2dur = if(glide2durlfo<=0, glide2dur, glide2dur * SinOsc.kr(glide2durlfo, 0, glide2durlfomul, glide2durlfoadd));
osc = osc * EnvGen.ar(Env([1, 1, (1.059463**glide2)], [sus*glide2dur, sus*(1-glide2dur)]));
ReplaceOut.kr(bus, osc)}).add;