SynthDef.new(\formantFilter,
{|bus, formant, formantmix, formant_, formant_d, formantmix_, formantmix_d, sus|
var osc;
osc = In.ar(bus, 2);
formant = if(formant_<=0, formant, Line.kr(formant, formant_, sus*formant_d));
formantmix = if(formantmix_<=0, formantmix, Line.kr(formantmix, formantmix_, sus*formantmix_d));
formant = (formant % 8) + 1;
osc = SelectX.ar(formantmix, [osc, Formlet.ar(osc, formant * 200, ((formant % 5 + 1)) / 1000, (formant * 1.5) / 600).tanh]);
ReplaceOut.ar(bus, osc)}).add;