SynthDef.new(\tape,
{|bus, tape, tapedrive, tapewarm, tapewobble, tape_, tape_d, tapelfo, tapelfomul, tapelfoadd, tapedrive_, tapedrive_d, tapedrivelfo, tapedrivelfomul, tapedrivelfoadd, tapewarm_, tapewarm_d, tapewarmlfo, tapewarmlfomul, tapewarmlfoadd, tapewobble_, tapewobble_d, tapewobblelfo, tapewobblelfomul, tapewobblelfoadd, sus|
var osc,dry,saturated,wobble;
osc = In.ar(bus, 2);
tape = if(tape_<=0, tape, Line.kr(tape, tape_, sus*tape_d));
tape = if(tapelfo<=0, tape, tape * SinOsc.kr(tapelfo, 0, tapelfomul, tapelfoadd));
tapedrive = if(tapedrive_<=0, tapedrive, Line.kr(tapedrive, tapedrive_, sus*tapedrive_d));
tapedrive = if(tapedrivelfo<=0, tapedrive, tapedrive * SinOsc.kr(tapedrivelfo, 0, tapedrivelfomul, tapedrivelfoadd));
tapewarm = if(tapewarm_<=0, tapewarm, Line.kr(tapewarm, tapewarm_, sus*tapewarm_d));
tapewarm = if(tapewarmlfo<=0, tapewarm, tapewarm * SinOsc.kr(tapewarmlfo, 0, tapewarmlfomul, tapewarmlfoadd));
tapewobble = if(tapewobble_<=0, tapewobble, Line.kr(tapewobble, tapewobble_, sus*tapewobble_d));
tapewobble = if(tapewobblelfo<=0, tapewobble, tapewobble * SinOsc.kr(tapewobblelfo, 0, tapewobblelfomul, tapewobblelfoadd));
dry = osc;
osc = Compander.ar(osc, osc, 0.25, 1, 0.4, 0.002, 0.08, 1.4);
wobble = SinOsc.kr(LFNoise1.kr(0.5).range(0.3, 1.5)).range(0.98, 1.02);
saturated = osc * tapedrive * wobble;
saturated = saturated + (saturated.squared * tapewarm * 0.5);
saturated = saturated + (saturated.cubed * 0.08);
saturated = saturated.softclip;
saturated = saturated + DelayC.ar(saturated * 0.15, 0.01, LFNoise2.kr(3).range(0.0001, 0.001 + (tapewobble * 0.003)));
saturated = LPF.ar(saturated, 10000 - (tapewarm * 4000));
saturated = BLowShelf.ar(saturated, 120, 0.7, tapewarm * 2.5);
saturated = BHiShelf.ar(saturated, 6000, 0.8, tapewarm * -2);
saturated = LeakDC.ar(saturated);
osc = XFade2.ar(dry, saturated * 0.85, tape * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;