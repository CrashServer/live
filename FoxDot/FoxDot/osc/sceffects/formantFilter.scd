SynthDef.new(\formantFilter,
{|bus, formant, formantmix, formant_, formant_d, formantlfo, formantmix_, formantmix_d, formantmixlfo, sus|
var osc;
osc = In.ar(bus, 2);
formant = if(formant_<=0, formant, Line.kr(formant, formant_, sus*formant_d));
formant = if(formantlfo<=0, formant, formant * SinOsc.kr(formantlfo, 0, 1, 1));
formantmix = if(formantmix_<=0, formantmix, Line.kr(formantmix, formantmix_, sus*formantmix_d));
formantmix = if(formantmixlfo<=0, formantmix, formantmix * SinOsc.kr(formantmixlfo, 0, 1, 1));
formant = (formant % 8) + 1;
osc = SelectX.ar(formantmix, [osc, Formlet.ar(osc, formant * 200, ((formant % 5 + 1)) / 1000, (formant * 1.5) / 600).tanh]);
ReplaceOut.ar(bus, osc)}).add;