SynthDef.new(\overdriveDistortion,
{|bus, drive, drivemix, drive_, drive_d, drivemix_, drivemix_d, sus|
var osc;
osc = In.ar(bus, 2);
drive = if(drive_<=0, drive, Line.kr(drive, drive_, sus*drive_d));
drivemix = if(drivemix_<=0, drivemix, Line.kr(drivemix, drivemix_, sus*drivemix_d));
osc = SelectX.ar(drivemix, [osc, (osc * (drive * 50)).clip(0,0.2).fold2(2)]);
ReplaceOut.ar(bus, osc)}).add;