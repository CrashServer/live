SynthDef.new(\FrequencyModulationSine,
{|bus, fm_sin, fm_sin_i, fm_sin_, fm_sin_d, fm_sinlfo, fm_sinlfomul, fm_sinlfoadd, fm_sin_i_, fm_sin_i_d, fm_sin_ilfo, fm_sin_ilfomul, fm_sin_ilfoadd, sus|
var osc;
osc = In.kr(bus, 1);
fm_sin = if(fm_sin_<=0, fm_sin, Line.kr(fm_sin, fm_sin_, sus*fm_sin_d));
fm_sin = if(fm_sinlfo<=0, fm_sin, fm_sin * SinOsc.kr(fm_sinlfo, 0, fm_sinlfomul, fm_sinlfoadd));
fm_sin_i = if(fm_sin_i_<=0, fm_sin_i, Line.kr(fm_sin_i, fm_sin_i_, sus*fm_sin_i_d));
fm_sin_i = if(fm_sin_ilfo<=0, fm_sin_i, fm_sin_i * SinOsc.kr(fm_sin_ilfo, 0, fm_sin_ilfomul, fm_sin_ilfoadd));
osc = osc + (fm_sin_i * SinOsc.kr(osc * fm_sin));
ReplaceOut.kr(bus, osc)}).add;