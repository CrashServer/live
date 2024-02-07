SynthDef.new(\overdriveDistortion,
{|bus, drive, drivemix, drive_, drivemix_, sus|
var osc;
osc = In.ar(bus, 2);
drive = drive+Line.kr(0, drive_, sus);
drivemix = drivemix+Line.kr(0, drivemix_, sus);
osc = SelectX.ar(drivemix, [osc, (osc * (drive * 50)).clip(0,0.2).fold2(2)]);
ReplaceOut.ar(bus, osc)}).add;