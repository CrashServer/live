#fakezip
Clock.bpm = 122/2;
Scale.default = Scale.minor
Root.default = "F#"
e0 >> plaits(melody(),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=3, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=(1, 4), drive=0, mverb=0.8, oct=5)
e1 >> bass(melody()[:8],dur=var([1/4, 2],[13, 3]), a=PWhite(0, 1), drive=0, amp=0.7, mverb=0.8).unison(2).every(13, "offmul", 2)
e0.every(4, "shuffle")
e1 >> bass(melody(),dur=1/4, oct=5, drive=0, mverb=0.8).unison(0)
e1 >> bass(melody(),dur=1/4, drive=linvar([0, 0.02], 32), mverb=0.8).unison(0)
g2 >> bass(melody() + var([7, 3, [4, 0]]),dur=var([1/4, 1/2]), drive=0, vol=0.5, mverb=0.1).unison(0)

Root.default = "E"
Scale.default = Scale.minor

~r1 >> organ(P[var([0,-2,-3,-4],16), 2, PStep(8,5,4), 2], dur=PDur(6,8),amp=0.7,    crush=0.5,bits=8,fmod=0.5, lpf=2000,  lpr=0.3, reverb=0.2  
).spread(2)
r0 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([PDur(4,8),PDur([5,3,6],8)]), amp=1, crush=1, crush_=4, crush_d=2, bits=6, bits_=var([12, 16]), fmod=1, lpf=2800, lpr=0.4).solo(0)
r2 >> organ(P[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.8, crush=1, crush_=4, crush_d=2, fx2=0.2, bits=6, bits_=var([12, 8]), oct=(5, 7), fmod=1, lpf=2800, lpr=0.2).unison(2).every(4, "shuffle")
e_all.stop()
~r3 >> bell(P[var([0,-2,-3,-4],16), 4, PStep(4,6,8), 2],dur=PDur(5,8),amp=0.5,crush=0.3, mverb=0.3, delay=0.25, oct=(5, 6, 7),lpf=2800, fmod=0.3
).every(4, "rotate") 
e1 >> plaits(melody(),dur=var([1/2, (1/2, 2)]), drive=0, mverb=0.8, engine=var([11, 5], [3, 1]), oct=5).unison(0)

r4 >> bell(P[var([0,-2,-3,-4],8),4,PStep(4,6,8),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.6, crush=1, crush_=4, crush_d=2, mverb=0.2, bits=6, bits_=var([12, 8]), delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")
r5 >> bell(P*[var([0,-2,-3,-4],8),2,PStep(8,5,4),2], dur=var([4, PDur(4,8)], [8, 4]), amp=0.5, crush=1, crush_=4, crush_d=2, mverb=0.5, bits=6, bits_=var([12, 8]), r1=0.5, delay=0.5, oct=(6, 5, 7), fmod=1, lpf=3200, lpr=0.2).unison(2).every(4, "shuffle")
g2.stop()
e0.dur=var([2, 1/4, 1/4, 1/4, 1/4])
e3 >> bass(melody(),dur=1/4, drive=linvar([0, 0.05], 32), mverb=0.8, delay=var([0, 0.5]), oct=6)
r1.stop()
r0.stop()
e3 >> lbass(dur=1/2, oct=4, drive=1, amp=PBin(8))
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=(1, 4), drive=0, mverb=0.8, oct=5)
r2 >> varsaw(oct=(3, PStep(4, 5, 6), 5), cut=4, cutmix=0.2, lpf=(800, linvar([400, 12000], 128)), dur=[6, 2], sus=[4, 8], lpr=0.1, a=0.5).unison(3)
r3.stop()
g1 >> dbass(delay=0.25,dur=1/4, dist2=0, lpf=120, cut=1/2, mverb=0.01, mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison()
g3 >> lbass(dur=1/4, hpf=400, drive=0.0, lpf=1200, mpf=1600)
r2.stop()
g_all.lpr=linvar([0.5, 0.1], [1, 4, 8])
e3.dist2=0.8
e1.stop()
Clock.bpm = 122;
g_all.only()
g3.dur=1/2
e3.dur=4
e3.sus=4
e3.glide=0.2
