SynthDef.new(\FrequencyModulationSine,
{|bus, fm_sin, fm_sin_i, fm_sin_, fm_sin_d, fm_sin_i_, fm_sin_i_d, sus|
var osc;
osc = In.kr(bus, 1);
osc = osc + (fm_sin_i * SinOsc.kr(osc * fm_sin));
ReplaceOut.kr(bus, osc)}).add;