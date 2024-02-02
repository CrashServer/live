SynthDef.new(\overdriveDistortion,
{|bus, drive, drivemix|
var osc;
osc = In.ar(bus, 2);
osc = SelectX.ar(drivemix, [osc, (osc * (drive * 50)).clip(0,0.2).fold2(2)]);
ReplaceOut.ar(bus, osc)}).add;