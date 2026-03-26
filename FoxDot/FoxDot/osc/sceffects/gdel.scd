SynthDef.new(\gdel,
{|bus, gdel, gdeltime, gdelsize, gdelsprd, gdelfb, gdel_, gdel_d, gdellfo, gdellfomul, gdellfoadd, gdeltime_, gdeltime_d, gdeltimelfo, gdeltimelfomul, gdeltimelfoadd, gdelsize_, gdelsize_d, gdelsizelfo, gdelsizelfomul, gdelsizelfoadd, gdelsprd_, gdelsprd_d, gdelsprdlfo, gdelsprdlfomul, gdelsprdlfoadd, gdelfb_, gdelfb_d, gdelfblfo, gdelfblfomul, gdelfblfoadd, sus|
var osc,dry,delayed,grains,fbIn;
osc = In.ar(bus, 2);
gdel = if(gdel_<=0, gdel, Line.kr(gdel, gdel_, sus*gdel_d));
gdel = if(gdellfo<=0, gdel, gdel * SinOsc.kr(gdellfo, 0, gdellfomul, gdellfoadd));
gdeltime = if(gdeltime_<=0, gdeltime, Line.kr(gdeltime, gdeltime_, sus*gdeltime_d));
gdeltime = if(gdeltimelfo<=0, gdeltime, gdeltime * SinOsc.kr(gdeltimelfo, 0, gdeltimelfomul, gdeltimelfoadd));
gdelsize = if(gdelsize_<=0, gdelsize, Line.kr(gdelsize, gdelsize_, sus*gdelsize_d));
gdelsize = if(gdelsizelfo<=0, gdelsize, gdelsize * SinOsc.kr(gdelsizelfo, 0, gdelsizelfomul, gdelsizelfoadd));
gdelsprd = if(gdelsprd_<=0, gdelsprd, Line.kr(gdelsprd, gdelsprd_, sus*gdelsprd_d));
gdelsprd = if(gdelsprdlfo<=0, gdelsprd, gdelsprd * SinOsc.kr(gdelsprdlfo, 0, gdelsprdlfomul, gdelsprdlfoadd));
gdelfb = if(gdelfb_<=0, gdelfb, Line.kr(gdelfb, gdelfb_, sus*gdelfb_d));
gdelfb = if(gdelfblfo<=0, gdelfb, gdelfb * SinOsc.kr(gdelfblfo, 0, gdelfblfomul, gdelfblfoadd));
dry = osc;
fbIn = osc + (LocalIn.ar(2) * gdelfb);
delayed = DelayC.ar(fbIn, 2.0, gdeltime);
grains = PitchShift.ar(delayed, gdelsize, 1.0, gdelsprd, gdelsprd);
grains = LPF.ar(grains, 8000);
grains = LeakDC.ar(grains);
LocalOut.ar(grains);
osc = XFade2.ar(dry, grains, gdel * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;