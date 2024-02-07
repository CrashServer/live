SynthDef.new(\FrequencyModulationSine,
{|bus, fm_sin, fm_sin_i, fm_sin_, fm_sin_i_, sus|
var osc;
osc = In.kr(bus, 1);
fm_sin = fm_sin+Line.kr(0, fm_sin_, sus);
fm_sin_i = fm_sin_i+Line.kr(0, fm_sin_i_, sus);
osc = osc + (fm_sin_i * SinOsc.kr(osc * fm_sin));
ReplaceOut.kr(bus, osc)}).add;