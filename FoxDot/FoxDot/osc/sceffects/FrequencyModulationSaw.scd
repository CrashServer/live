SynthDef.new(\FrequencyModulationSaw,
{|bus, fm_saw, fm_saw_i, fm_saw_, fm_saw_d, fm_saw_i_, fm_saw_i_d, sus|
var osc;
osc = In.kr(bus, 1);
osc = osc + (fm_saw_i * Saw.kr(osc * fm_saw));
ReplaceOut.kr(bus, osc)}).add;