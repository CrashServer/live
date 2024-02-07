SynthDef.new(\fx2out,
{|bus, fx2, lpfx2, hpfx2, fx2mix, fx2_, lpfx2_, hpfx2_, fx2mix_, sus|
var osc,fxsig;
osc = In.ar(bus, 2);
fx2 = fx2+Line.kr(0, fx2_, sus);
lpfx2 = lpfx2+Line.kr(0, lpfx2_, sus);
hpfx2 = hpfx2+Line.kr(0, hpfx2_, sus);
fx2mix = fx2mix+Line.kr(0, fx2mix_, sus);
fxsig = LPF.ar(osc, lpfx2);
fxsig = HPF.ar(fxsig, hpfx2);
Out.ar(5, Mix.ar(fxsig*fx2));
osc = osc * fx2mix;
ReplaceOut.ar(bus, osc)}).add;