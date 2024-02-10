SynthDef.new(\flanger,
{|bus, flanger, fdecay, flangermix, flanger_, flanger_d, fdecay_, fdecay_d, flangermix_, flangermix_d, sus|
var osc;
osc = In.ar(bus, 2);
flanger = if(flanger_<=0, flanger, Line.kr(flanger, flanger_, sus*flanger_d));
fdecay = if(fdecay_<=0, fdecay, Line.kr(fdecay, fdecay_, sus*fdecay_d));
flangermix = if(flangermix_<=0, flangermix, Line.kr(flangermix, flangermix_, sus*flangermix_d));
osc = SelectX.ar(flangermix, [osc, CombC.ar(osc, 0.01, SinOsc.ar(flanger, 0, (0.01 * 0.5) - 0.001, (0.01 * 0.5) + 0.001), fdecay, 1)]);
ReplaceOut.ar(bus, osc)}).add;