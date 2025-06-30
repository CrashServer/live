# Mini mall
Clock.bpm=132
l4 >>  loop("break4", dur=4,pos=0, poslfo=2, room=0.1, sample=PRand(8), beat_stretch=1, looping=1.0, fx=1).lclip(2)
l8 >> loop("xtech8", dur=8, sample=PRand(8), blur=1, amp=1, rate=1, mverb=0.5,ratelfo=2,  beat_stretch=0, ratelfoadd=linvar([1.2, 1.6], 64), ratelfomul=0.4).lclip(P*[1,2,4])
l9 >> loop("xtech8", dur=8, vol_=1, vol=0.0, sample=PRand(8), blur=1, amp=1, rate=1, mverb=0.5,ratelfo=4,  beat_stretch=0, ratelfoadd=var([1, 2, 2, 4]), ratelfomul=1).lclip(1)
b6 >> play("..X.", shape=0.5, dist2=0.5, dist2lfo=PRand(10), mverb=0.5, echo=var([0, 0.5], [2, 4]), amp=PBin())
a4 >> play("<x.><-><..(*..*).>", sample=4, amp=1, rate=PStep(19, -1,1)).sometimes("stutter").human(40, 5)
