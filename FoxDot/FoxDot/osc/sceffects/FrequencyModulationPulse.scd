SynthDef.new(\FrequencyModulationPulse,
{|bus, fm_pulse, fm_pulse_i, fm_pulse_, fm_pulse_d, fm_pulselfo, fm_pulselfomul, fm_pulselfoadd, fm_pulse_i_, fm_pulse_i_d, fm_pulse_ilfo, fm_pulse_ilfomul, fm_pulse_ilfoadd, sus|
var osc;
osc = In.kr(bus, 1);
fm_pulse = if(fm_pulse_<=0, fm_pulse, Line.kr(fm_pulse, fm_pulse_, sus*fm_pulse_d));
fm_pulse = if(fm_pulselfo<=0, fm_pulse, fm_pulse * SinOsc.kr(fm_pulselfo, 0, fm_pulselfomul, fm_pulselfoadd));
fm_pulse_i = if(fm_pulse_i_<=0, fm_pulse_i, Line.kr(fm_pulse_i, fm_pulse_i_, sus*fm_pulse_i_d));
fm_pulse_i = if(fm_pulse_ilfo<=0, fm_pulse_i, fm_pulse_i * SinOsc.kr(fm_pulse_ilfo, 0, fm_pulse_ilfomul, fm_pulse_ilfoadd));
osc = osc + (fm_pulse_i * Pulse.kr(osc * fm_pulse));
ReplaceOut.kr(bus, osc)}).add;