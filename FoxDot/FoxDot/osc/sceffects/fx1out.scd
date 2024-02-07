SynthDef.new(\fx1out,
{|bus, fx1, lpfx1, hpfx1, fx1mix, fx1_, lpfx1_, hpfx1_, fx1mix_, sus|
var osc,fxsig;
osc = In.ar(bus, 2);
fx1 = fx1+Line.kr(0, fx1_, sus);
lpfx1 = lpfx1+Line.kr(0, lpfx1_, sus);
hpfx1 = hpfx1+Line.kr(0, hpfx1_, sus);
fx1mix = fx1mix+Line.kr(0, fx1mix_, sus);
fxsig = LPF.ar(osc, lpfx1);
fxsig = HPF.ar(fxsig, hpfx1);
Out.ar(4, Mix.ar(fxsig*fx1));
osc = osc * fx1mix;
ReplaceOut.ar(bus, osc)}).add;