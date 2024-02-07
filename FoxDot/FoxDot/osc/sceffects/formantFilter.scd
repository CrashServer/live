SynthDef.new(\formantFilter,
{|bus, formant, formantmix, formant_, formantmix_, sus|
var osc;
osc = In.ar(bus, 2);
formant = formant+Line.kr(0, formant_, sus);
formantmix = formantmix+Line.kr(0, formantmix_, sus);
formant = (formant % 8) + 1;
osc = SelectX.ar(formantmix, [osc, Formlet.ar(osc, formant * 200, ((formant % 5 + 1)) / 1000, (formant * 1.5) / 600).tanh]);
ReplaceOut.ar(bus, osc)}).add;