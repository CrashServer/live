SynthDef.new(\tek,
{|bus, tek, tekr, tekd, tek_, tek_d, teklfo, tekr_, tekr_d, tekrlfo, tekd_, tekd_d, tekdlfo, sus|
var osc,osc_low,osc_med,osc_high,osc_base,lfo;
osc = In.ar(bus, 2);
tek = if(tek_<=0, tek, Line.kr(tek, tek_, sus*tek_d));
tek = if(teklfo<=0, tek, tek * SinOsc.kr(teklfo, 0, 1, 1));
tekr = if(tekr_<=0, tekr, Line.kr(tekr, tekr_, sus*tekr_d));
tekr = if(tekrlfo<=0, tekr, tekr * SinOsc.kr(tekrlfo, 0, 1, 1));
tekd = if(tekd_<=0, tekd, Line.kr(tekd, tekd_, sus*tekd_d));
tekd = if(tekdlfo<=0, tekd, tekd * SinOsc.kr(tekdlfo, 0, 1, 1));
lfo = SinOsc.ar(0.5, phase: 0, mul: 50, add: 800);
osc = In.ar(bus, 2);
osc_base = osc;
osc_low = LPF.ar(osc, lfo) * 1;
osc_med = BPF.ar(osc, lfo * 2);
osc_med = osc_med + Ringz.ar(CrossoverDistortion.ar(osc_med, 1, 0.1, 0.4),100, decaytime: 0.15, mul:0.1);
osc_med = LeakDC.ar(osc_med);
osc_high = HPF.ar(osc, 4000 + SinOsc.ar(4, mul: 24));
osc = osc_low + osc_med + osc_high;
osc = DFM1.ar(osc, [400, 600], 0.99, tekd, 0) + osc;
osc = RHPF.ar(Gammatone.ar(osc, tekr), tekr, mul:2) + osc;
osc = SelectX.ar(tek, [osc_base, osc]);
ReplaceOut.ar(bus, osc)}).add;