SynthDef.new(\FrequencyModulationPulse,
{|bus, fm_pulse, fm_pulse_i, fm_pulse_, fm_pulse_d, fm_pulse_i_, fm_pulse_i_d, sus|
var osc;
osc = In.kr(bus, 1);
osc = osc + (fm_pulse_i * Pulse.kr(osc * fm_pulse));
ReplaceOut.kr(bus, osc)}).add;