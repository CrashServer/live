SynthDef.new(\overdriveDistortion,
{|bus, drive, drivemix, drive_, drive_d, drivelfo, drivemix_, drivemix_d, drivemixlfo, sus|
var osc;
osc = In.ar(bus, 2);
drive = if(drive_<=0, drive, Line.kr(drive, drive_, sus*drive_d));
drive = if(drivelfo<=0, drive, drive * SinOsc.kr(drivelfo, 0, 1, 1));
drivemix = if(drivemix_<=0, drivemix, Line.kr(drivemix, drivemix_, sus*drivemix_d));
drivemix = if(drivemixlfo<=0, drivemix, drivemix * SinOsc.kr(drivemixlfo, 0, 1, 1));
osc = SelectX.ar(drivemix, [osc, (osc * (drive * 50)).clip(0,0.2).fold2(2)]);
ReplaceOut.ar(bus, osc)}).add;