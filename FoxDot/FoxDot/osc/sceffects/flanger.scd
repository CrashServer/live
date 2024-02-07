SynthDef.new(\flanger,
{|bus, flanger, fdecay, flangermix, flanger_, fdecay_, flangermix_, sus|
var osc;
osc = In.ar(bus, 2);
flanger = flanger+Line.kr(0, flanger_, sus);
fdecay = fdecay+Line.kr(0, fdecay_, sus);
flangermix = flangermix+Line.kr(0, flangermix_, sus);
osc = SelectX.ar(flangermix, [osc, CombC.ar(osc, 0.01, SinOsc.ar(flanger, 0, (0.01 * 0.5) - 0.001, (0.01 * 0.5) + 0.001), fdecay, 1)]);
ReplaceOut.ar(bus, osc)}).add;