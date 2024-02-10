SynthDef.new(\fxout,
{|bus, fx, lpfx, hpfx, fxout, fxmix, fx_, fx_d, lpfx_, lpfx_d, hpfx_, hpfx_d, fxout_, fxout_d, fxmix_, fxmix_d, sus|
var osc,fxsig;
osc = In.ar(bus, 2);
fx = if(fx_<=0, fx, Line.kr(fx, fx_, sus*fx_d));
lpfx = if(lpfx_<=0, lpfx, Line.kr(lpfx, lpfx_, sus*lpfx_d));
hpfx = if(hpfx_<=0, hpfx, Line.kr(hpfx, hpfx_, sus*hpfx_d));
fxout = if(fxout_<=0, fxout, Line.kr(fxout, fxout_, sus*fxout_d));
fxmix = if(fxmix_<=0, fxmix, Line.kr(fxmix, fxmix_, sus*fxmix_d));
fxsig = LPF.ar(osc, lpfx);
fxsig = HPF.ar(fxsig, hpfx);
Out.ar([fxout, fxout+1], Mix.ar(fxsig*fx));
osc = osc * fxmix;
ReplaceOut.ar(bus, osc)}).add;