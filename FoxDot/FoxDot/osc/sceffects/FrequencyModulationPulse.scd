SynthDef.new(\FrequencyModulationPulse,
{|bus, fm_pulse, fm_pulse_i, fm_pulse_, fm_pulse_i_, sus|
var osc;
osc = In.kr(bus, 1);
fm_pulse = fm_pulse+Line.kr(0, fm_pulse_, sus);
fm_pulse_i = fm_pulse_i+Line.kr(0, fm_pulse_i_, sus);
osc = osc + (fm_pulse_i * Pulse.kr(osc * fm_pulse));
ReplaceOut.kr(bus, osc)}).add;