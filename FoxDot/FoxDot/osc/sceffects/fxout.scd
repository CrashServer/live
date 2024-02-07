SynthDef.new(\fxout,
{|bus, fx, lpfx, hpfx, fxout, fxmix, fx_, lpfx_, hpfx_, fxout_, fxmix_, sus|
var osc,fxsig;
osc = In.ar(bus, 2);
fx = fx+Line.kr(0, fx_, sus);
lpfx = lpfx+Line.kr(0, lpfx_, sus);
hpfx = hpfx+Line.kr(0, hpfx_, sus);
fxout = fxout+Line.kr(0, fxout_, sus);
fxmix = fxmix+Line.kr(0, fxmix_, sus);
fxsig = LPF.ar(osc, lpfx);
fxsig = HPF.ar(fxsig, hpfx);
Out.ar([fxout, fxout+1], Mix.ar(fxsig*fx));
osc = osc * fxmix;
ReplaceOut.ar(bus, osc)}).add;