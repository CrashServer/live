SynthDef.new(\fx2out,
{|bus, fx2, lpfx2, hpfx2, fx2mix, fx2_, fx2_d, fx2lfo, lpfx2_, lpfx2_d, lpfx2lfo, hpfx2_, hpfx2_d, hpfx2lfo, fx2mix_, fx2mix_d, fx2mixlfo, sus|
var osc,fxsig;
osc = In.ar(bus, 2);
fx2 = if(fx2_<=0, fx2, Line.kr(fx2, fx2_, sus*fx2_d));
fx2 = if(fx2lfo<=0, fx2, fx2 * SinOsc.kr(fx2lfo, 0, 1, 1));
lpfx2 = if(lpfx2_<=0, lpfx2, Line.kr(lpfx2, lpfx2_, sus*lpfx2_d));
lpfx2 = if(lpfx2lfo<=0, lpfx2, lpfx2 * SinOsc.kr(lpfx2lfo, 0, 1, 1));
hpfx2 = if(hpfx2_<=0, hpfx2, Line.kr(hpfx2, hpfx2_, sus*hpfx2_d));
hpfx2 = if(hpfx2lfo<=0, hpfx2, hpfx2 * SinOsc.kr(hpfx2lfo, 0, 1, 1));
fx2mix = if(fx2mix_<=0, fx2mix, Line.kr(fx2mix, fx2mix_, sus*fx2mix_d));
fx2mix = if(fx2mixlfo<=0, fx2mix, fx2mix * SinOsc.kr(fx2mixlfo, 0, 1, 1));
fxsig = LPF.ar(osc, lpfx2);
fxsig = HPF.ar(fxsig, hpfx2);
Out.ar(5, Mix.ar(fxsig*fx2));
osc = osc * fx2mix;
ReplaceOut.ar(bus, osc)}).add;