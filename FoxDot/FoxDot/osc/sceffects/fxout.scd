SynthDef.new(\fxout,
{|bus, fx, lpfx, hpfx, fxout, fxmix, fx_, fx_d, fxlfo, fxlfomul, fxlfoadd, fxlfophase, lpfx_, lpfx_d, lpfxlfo, lpfxlfomul, lpfxlfoadd, lpfxlfophase, hpfx_, hpfx_d, hpfxlfo, hpfxlfomul, hpfxlfoadd, hpfxlfophase, fxout_, fxout_d, fxoutlfo, fxoutlfomul, fxoutlfoadd, fxoutlfophase, fxmix_, fxmix_d, fxmixlfo, fxmixlfomul, fxmixlfoadd, fxmixlfophase, sus|
var osc,fxsig;
osc = In.ar(bus, 2);
fx = if(fx_<=0, fx, Line.kr(fx, fx_, sus*fx_d));
fx = if(fxlfo<=0, fx, fx * SinOsc.kr(fxlfo, fxlfophase, fxlfomul, fxlfoadd));
lpfx = if(lpfx_<=0, lpfx, Line.kr(lpfx, lpfx_, sus*lpfx_d));
lpfx = if(lpfxlfo<=0, lpfx, lpfx * SinOsc.kr(lpfxlfo, lpfxlfophase, lpfxlfomul, lpfxlfoadd));
hpfx = if(hpfx_<=0, hpfx, Line.kr(hpfx, hpfx_, sus*hpfx_d));
hpfx = if(hpfxlfo<=0, hpfx, hpfx * SinOsc.kr(hpfxlfo, hpfxlfophase, hpfxlfomul, hpfxlfoadd));
fxout = if(fxout_<=0, fxout, Line.kr(fxout, fxout_, sus*fxout_d));
fxout = if(fxoutlfo<=0, fxout, fxout * SinOsc.kr(fxoutlfo, fxoutlfophase, fxoutlfomul, fxoutlfoadd));
fxmix = if(fxmix_<=0, fxmix, Line.kr(fxmix, fxmix_, sus*fxmix_d));
fxmix = if(fxmixlfo<=0, fxmix, fxmix * SinOsc.kr(fxmixlfo, fxmixlfophase, fxmixlfomul, fxmixlfoadd));
fxsig = LPF.ar(osc, lpfx);
fxsig = HPF.ar(fxsig, hpfx);
Out.ar([fxout, fxout+1], Mix.ar(fxsig*fx));
osc = osc * 0;
ReplaceOut.ar(bus, osc)}).add;