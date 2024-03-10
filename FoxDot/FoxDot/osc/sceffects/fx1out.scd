SynthDef.new(\fx1out,
{|bus, fx1, lpfx1, hpfx1, fx1mix, fx1_, fx1_d, lpfx1_, lpfx1_d, hpfx1_, hpfx1_d, fx1mix_, fx1mix_d, sus|
var osc,fxsig;
osc = In.ar(bus, 2);
fx1 = if(fx1_<=0, fx1, Line.kr(fx1, fx1_, sus*fx1_d));
lpfx1 = if(lpfx1_<=0, lpfx1, Line.kr(lpfx1, lpfx1_, sus*lpfx1_d));
hpfx1 = if(hpfx1_<=0, hpfx1, Line.kr(hpfx1, hpfx1_, sus*hpfx1_d));
fx1mix = if(fx1mix_<=0, fx1mix, Line.kr(fx1mix, fx1mix_, sus*fx1mix_d));
fxsig = LPF.ar(osc, lpfx1);
fxsig = HPF.ar(fxsig, hpfx1);
Out.ar(4, Mix.ar(fxsig*fx1));
osc = osc * fx1mix;
ReplaceOut.ar(bus, osc)}).add;