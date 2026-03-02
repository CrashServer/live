SynthDef.new(\resonbank,
{|bus, resonbank, rbfreq, rbdecay, rbspread|
var osc,resonated,dry;
osc = In.ar(bus, 2);

dry = osc;
resonated = Ringz.ar(osc, rbfreq * (1 ** rbspread), rbdecay) + Ringz.ar(osc, rbfreq * (2 ** rbspread), rbdecay) + Ringz.ar(osc, rbfreq * (3 ** rbspread), rbdecay) + Ringz.ar(osc, rbfreq * (4 ** rbspread), rbdecay) + Ringz.ar(osc, rbfreq * (5 ** rbspread), rbdecay) + Ringz.ar(osc, rbfreq * (6 ** rbspread), rbdecay);
resonated = LeakDC.ar(resonated * 0.5);
resonated = Limiter.ar(resonated, 0.95);
osc = SelectX.ar(resonbank, [dry, dry + (resonated * 0.5)]);
ReplaceOut.ar(bus, osc)}).add;