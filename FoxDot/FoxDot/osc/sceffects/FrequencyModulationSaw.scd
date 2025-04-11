SynthDef.new(\FrequencyModulationSaw,
{|bus, fm_saw, fm_saw_i, fm_saw_, fm_saw_d, fm_sawlfo, fm_sawlfomul, fm_sawlfoadd, fm_saw_i_, fm_saw_i_d, fm_saw_ilfo, fm_saw_ilfomul, fm_saw_ilfoadd, sus|
var osc;
osc = In.kr(bus, 1);
fm_saw = if(fm_saw_<=0, fm_saw, Line.kr(fm_saw, fm_saw_, sus*fm_saw_d));
fm_saw = if(fm_sawlfo<=0, fm_saw, fm_saw * SinOsc.kr(fm_sawlfo, 0, fm_sawlfomul, fm_sawlfoadd));
fm_saw_i = if(fm_saw_i_<=0, fm_saw_i, Line.kr(fm_saw_i, fm_saw_i_, sus*fm_saw_i_d));
fm_saw_i = if(fm_saw_ilfo<=0, fm_saw_i, fm_saw_i * SinOsc.kr(fm_saw_ilfo, 0, fm_saw_ilfomul, fm_saw_ilfoadd));
osc = osc + (fm_saw_i * Saw.kr(osc * fm_saw));
ReplaceOut.kr(bus, osc)}).add;