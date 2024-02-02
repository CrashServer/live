SynthDef.new(\flanger,
{|bus, flanger, fdecay, flangermix|
var osc;
osc = In.ar(bus, 2);
osc = SelectX.ar(flangermix, [osc, CombC.ar(osc, 0.01, SinOsc.ar(flanger, 0, (0.01 * 0.5) - 0.001, (0.01 * 0.5) + 0.001), fdecay, 1)]);
ReplaceOut.ar(bus, osc)}).add;