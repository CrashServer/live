SynthDef.new(\glitch,
{|bus, glitch, glitchrate, glitchdepth, glitchcrush, glitchchance, beat_dur, glitch_, glitch_d, glitchlfo, glitchlfomul, glitchlfoadd, glitchrate_, glitchrate_d, glitchratelfo, glitchratelfomul, glitchratelfoadd, glitchdepth_, glitchdepth_d, glitchdepthlfo, glitchdepthlfomul, glitchdepthlfoadd, glitchcrush_, glitchcrush_d, glitchcrushlfo, glitchcrushlfomul, glitchcrushlfoadd, glitchchance_, glitchchance_d, glitchchancelfo, glitchchancelfomul, glitchchancelfoadd, beat_dur_, beat_dur_d, beat_durlfo, beat_durlfomul, beat_durlfoadd, sus|
var osc,dry,glitched,trig,rate,shouldGlitch,crushed,pitched,bits;
osc = In.ar(bus, 2);
glitch = if(glitch_<=0, glitch, Line.kr(glitch, glitch_, sus*glitch_d));
glitch = if(glitchlfo<=0, glitch, glitch * SinOsc.kr(glitchlfo, 0, glitchlfomul, glitchlfoadd));
glitchrate = if(glitchrate_<=0, glitchrate, Line.kr(glitchrate, glitchrate_, sus*glitchrate_d));
glitchrate = if(glitchratelfo<=0, glitchrate, glitchrate * SinOsc.kr(glitchratelfo, 0, glitchratelfomul, glitchratelfoadd));
glitchdepth = if(glitchdepth_<=0, glitchdepth, Line.kr(glitchdepth, glitchdepth_, sus*glitchdepth_d));
glitchdepth = if(glitchdepthlfo<=0, glitchdepth, glitchdepth * SinOsc.kr(glitchdepthlfo, 0, glitchdepthlfomul, glitchdepthlfoadd));
glitchcrush = if(glitchcrush_<=0, glitchcrush, Line.kr(glitchcrush, glitchcrush_, sus*glitchcrush_d));
glitchcrush = if(glitchcrushlfo<=0, glitchcrush, glitchcrush * SinOsc.kr(glitchcrushlfo, 0, glitchcrushlfomul, glitchcrushlfoadd));
glitchchance = if(glitchchance_<=0, glitchchance, Line.kr(glitchchance, glitchchance_, sus*glitchchance_d));
glitchchance = if(glitchchancelfo<=0, glitchchance, glitchchance * SinOsc.kr(glitchchancelfo, 0, glitchchancelfomul, glitchchancelfoadd));
beat_dur = if(beat_dur_<=0, beat_dur, Line.kr(beat_dur, beat_dur_, sus*beat_dur_d));
beat_dur = if(beat_durlfo<=0, beat_dur, beat_dur * SinOsc.kr(beat_durlfo, 0, beat_durlfomul, beat_durlfoadd));
dry = osc;
rate = glitchrate / beat_dur;
trig = Impulse.kr(rate);
shouldGlitch = TRand.kr(0, 1, trig) < glitchchance;
bits = TRand.kr(4, 12, trig);
crushed = Latch.ar(osc, Impulse.ar(TRand.kr(2000, 8000, trig)));
crushed = crushed.round(2.pow(bits.neg));
pitched = PitchShift.ar(osc, 0.1, TRand.kr(0.8, 1.2, trig) ** (glitchdepth * 2), 0, 0.01);
glitched = SelectX.ar(glitchcrush, [pitched, crushed]);
glitched = Select.ar(shouldGlitch, [osc, glitched]);
glitched = LeakDC.ar(glitched);
osc = XFade2.ar(dry, glitched, glitch * 2 - 1);
ReplaceOut.ar(bus, osc)}).add;