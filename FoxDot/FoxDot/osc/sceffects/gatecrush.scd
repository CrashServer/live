SynthDef.new(\gatecrush,
{|bus, gatecrush=1, gcrate=8, gcbits=6, gcdepth=0.5, sus, beat_dur,
  gatecrush_, gatecrush_d, gatecrushlfo, gatecrushlfomul, gatecrushlfoadd,
  gcrate_, gcrate_d, gcratelfo, gcratelfomul, gcratelfoadd,
  gcbits_, gcbits_d, gcbitslfo, gcbitslfomul, gcbitslfoadd,
  gcdepth_, gcdepth_d, gcdepthlfo, gcdepthlfomul, gcdepthlfoadd|
var osc, dry, gated, crushed, trig, rate;
osc = In.ar(bus, 2);
dry = osc;
gatecrush = if(gatecrush_<=0, gatecrush, Line.kr(gatecrush, gatecrush_, sus*gatecrush_d));
gatecrush = if(gatecrushlfo<=0, gatecrush, gatecrush * SinOsc.kr(gatecrushlfo, 0, gatecrushlfomul, gatecrushlfoadd));
gcrate = if(gcrate_<=0, gcrate, Line.kr(gcrate, gcrate_, sus*gcrate_d));
gcrate = if(gcratelfo<=0, gcrate, gcrate * SinOsc.kr(gcratelfo, 0, gcratelfomul, gcratelfoadd));
gcbits = if(gcbits_<=0, gcbits, Line.kr(gcbits, gcbits_, sus*gcbits_d));
gcbits = if(gcbitslfo<=0, gcbits, gcbits * SinOsc.kr(gcbitslfo, 0, gcbitslfomul, gcbitslfoadd));
gcdepth = if(gcdepth_<=0, gcdepth, Line.kr(gcdepth, gcdepth_, sus*gcdepth_d));
gcdepth = if(gcdepthlfo<=0, gcdepth, gcdepth * SinOsc.kr(gcdepthlfo, 0, gcdepthlfomul, gcdepthlfoadd));
rate = gcrate / beat_dur;
trig = LFPulse.ar(rate, width: 0.5);
// Gate the signal
gated = osc * trig;
// Crush only the gated portions
crushed = Latch.ar(gated, Impulse.ar(8000 * (1.1 - gcdepth)));
crushed = crushed.round(2.pow(gcbits.neg));
crushed = LeakDC.ar(crushed);
osc = SelectX.ar(gcdepth, [gated, crushed]);
osc = XFade2.ar(dry, osc, gatecrush * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;
