SynthDef.new(\flanger,
{|bus, flanger, fdecay, flangermix, flanger_, flanger_d, flangerlfo, flangerlfomul, flangerlfoadd, fdecay_, fdecay_d, fdecaylfo, fdecaylfomul, fdecaylfoadd, flangermix_, flangermix_d, flangermixlfo, flangermixlfomul, flangermixlfoadd, sus|
var osc;
osc = In.ar(bus, 2);
flanger = if(flanger_<=0, flanger, Line.kr(flanger, flanger_, sus*flanger_d));
flanger = if(flangerlfo<=0, flanger, flanger * SinOsc.kr(flangerlfo, 0, flangerlfomul, flangerlfoadd));
fdecay = if(fdecay_<=0, fdecay, Line.kr(fdecay, fdecay_, sus*fdecay_d));
fdecay = if(fdecaylfo<=0, fdecay, fdecay * SinOsc.kr(fdecaylfo, 0, fdecaylfomul, fdecaylfoadd));
flangermix = if(flangermix_<=0, flangermix, Line.kr(flangermix, flangermix_, sus*flangermix_d));
flangermix = if(flangermixlfo<=0, flangermix, flangermix * SinOsc.kr(flangermixlfo, 0, flangermixlfomul, flangermixlfoadd));
osc = SelectX.ar(flangermix, [osc, CombC.ar(osc, 0.01, SinOsc.ar(flanger, 0, (0.01 * 0.5) - 0.001, (0.01 * 0.5) + 0.001), fdecay, 1)]);
ReplaceOut.ar(bus, osc)}).add;