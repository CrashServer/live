SynthDef.new(\fxout,
{|bus, fx, lpfx, hpfx, fxout, fxmix|
var osc,fxsig;
osc = In.ar(bus, 2);
fxsig = LPF.ar(osc, lpfx);
fxsig = HPF.ar(fxsig, hpfx);
Out.ar([fxout, fxout+1], Mix.ar(fxsig*fx));
osc = osc * fxmix;
ReplaceOut.ar(bus, osc)}).add;