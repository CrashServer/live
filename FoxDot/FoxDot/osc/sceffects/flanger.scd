SynthDef.new(\flanger,
{|bus, flanger, fdecay, flangermix, flanger_, flanger_d, flangerlfo, fdecay_, fdecay_d, fdecaylfo, flangermix_, flangermix_d, flangermixlfo, sus|
var osc;
osc = In.ar(bus, 2);
flanger = if(flanger_<=0, flanger, Line.kr(flanger, flanger_, sus*flanger_d));
flanger = if(flangerlfo<=0, flanger, flanger * SinOsc.kr(flangerlfo, 0, 1, 1));
fdecay = if(fdecay_<=0, fdecay, Line.kr(fdecay, fdecay_, sus*fdecay_d));
fdecay = if(fdecaylfo<=0, fdecay, fdecay * SinOsc.kr(fdecaylfo, 0, 1, 1));
flangermix = if(flangermix_<=0, flangermix, Line.kr(flangermix, flangermix_, sus*flangermix_d));
flangermix = if(flangermixlfo<=0, flangermix, flangermix * SinOsc.kr(flangermixlfo, 0, 1, 1));
osc = SelectX.ar(flangermix, [osc, CombC.ar(osc, 0.01, SinOsc.ar(flanger, 0, (0.01 * 0.5) - 0.001, (0.01 * 0.5) + 0.001), fdecay, 1)]);
ReplaceOut.ar(bus, osc)}).add;