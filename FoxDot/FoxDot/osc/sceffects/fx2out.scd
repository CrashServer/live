SynthDef.new(\fx2out,
{|bus, fx2, lpfx2, hpfx2, fx2mix|
var osc,fxsig;
osc = In.ar(bus, 2);
fxsig = LPF.ar(osc, lpfx2);
fxsig = HPF.ar(fxsig, hpfx2);
Out.ar(5, Mix.ar(fxsig*fx2));
osc = osc * fx2mix;
ReplaceOut.ar(bus, osc)}).add;