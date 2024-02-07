SynthDef.new(\FrequencyModulationSaw,
{|bus, fm_saw, fm_saw_i, fm_saw_, fm_saw_i_, sus|
var osc;
osc = In.kr(bus, 1);
fm_saw = fm_saw+Line.kr(0, fm_saw_, sus);
fm_saw_i = fm_saw_i+Line.kr(0, fm_saw_i_, sus);
osc = osc + (fm_saw_i * Saw.kr(osc * fm_saw));
ReplaceOut.kr(bus, osc)}).add;