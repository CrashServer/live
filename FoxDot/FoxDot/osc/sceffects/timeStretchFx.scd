SynthDef.new(\timeStretchFx, {
    arg bus, tstretch=1, tstretchsize=0.2;
    var osc, stretched, xfade;
    osc = In.ar(bus, 2);
    stretched = PitchShift.ar(osc, tstretchsize, 1, 0, 0.004);
    xfade = (1 - tstretch).abs.min(1);
    osc = XFade2.ar(osc, stretched, xfade * 2 - 1);
    ReplaceOut.ar(bus, osc);
}).add;
