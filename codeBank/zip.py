# zip
# todo
Clock.bpm = 122/2;
Scale.default = Scale.minor
Root.default = 6

f0 >> plaits(melody(),dur=(1/2, 1/4), engine=3, drive=0, mverb=0.8)
e1 >> bass(melody(), lpf=1200,dur=var([2, 1, 1/4], [1, 2, 4]), drive=linvar([0, 0.1], 32), mverb=0.5, mverbdiff=0.4).slider()
e3 >> bass(melody() + var([7, 3, [4, 0]]),dur=P[1/2, 2], drive=0, oct=4).unison(2).slider()
e0 >> plaits(melody() + PWalk(8, 1, 1),dur=(1/2, P[1/2, 1/4, 1], 4, 2, 1/2, 1/2), engine=var([5, 7, 3], 8), drive=0, mverb=0.1, oct=4, amp=0.1, vol=0.5, pan=PWhite(linvar([-0.5, 0.5])))
e0 >> plaits(melody(),dur=(1/2, 1/4), engine=3, drive=0, mverb=0.2, oct=5)

e0.dur=4

e3 >> bass(melody(),dur=1/4, drive=linvar([0, 0.1], 32), mverb=0.8, delay=var([0, 0.5]), oct=6)
e2 >> bass(melody(),dur=var([1/4, 2],[13, 3]), drive=0, mverb=0).unison(2).every(13, "offmul", 2)
e0.unison(2)

Root.default="G"
Root.default="F#"
Root.default="Eb"

e_all.dur=4

g2 >> bass(melody() + var([7, 3, [4, 0]]),dur=var([1/4, 1/2]), drive=0, vol=0.5, mverb=0.1).unison(0)
g2 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0.04, mpf=linvar([200, 12000], 128), vol=0.5, rate=(0.25, 0.5), oct=7, hpf=linvar([2000, 12000], 32), engine=(3,10)).unison(4)

e1 >> plaits(melody(),dur=var([1/2, (1/2, 2)]), mverb=0.8, engine=var([11, 5], [3, 1]), oct=4, amp=PWhite(0, 1))
g1 >> dbass(delay=0.25,dur=1/4, dist2=0, lpf=120, cut=1/2, mverb=0.01, mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison()
g3 >> lbass(dur=1/4, hpf=400, drive=0.0, lpf=1200, mpf=1600)

f4 >> karp(melody(),dur=PDur(11, 15), lpf=1200, drive=linvar([0, 0.05], 32), mverb=0.8, delay=var([0, 0.5]), oct=PStep(5, 4, 5)).unison(2) + var([0, 2, 0, (0, 2)])

e_all.lpf=0
a3.lpf=200
a2.stop()
f4.dur=2
e_all.dur=8
f_all.lpf=300

f5 >> lbass(dur=16, oct=4, drive=0.0).unison(2)
f6 >> lbass(dur=16, oct=4, drive=0.5).unison(2)
f7 >> lbass(dur=1/2, sus=1/4, oct=5, leg=12, lpf=800, rate=0.25,amp=PBin(16), hpf=0, dist2=0)
f8 >> dbass(dur=1/4, echo=var([1/3, 0]), lpf=0, cut=0, mverb=0.04, mpf=linvar([200, 12000], 128), vol=0.5, rate=(0.25, 0.5), oct=7, hpf=linvar([2000, 12000], 32), engine=(3,10)).unison(2)

g0 >> lbass(dur=[1/2, 1/4, 1/4, 1/2, 1/2, 1/4, 1/8, 1/8], lpf=linvar([1200, 4000]), lpr=0.1, sus=1/4, valadd=1, valad=12) + var([0, P[-2, -3]])
g1 >> dbass(delay=0.25, oct=5,dur=PDur(11, 15), dist2=0, lpf=1200, cut=1/2, mverb=0.01, mpf=linvar([200, 2000], 128), vol=0.5, rate=(0.5, 1)).unison(4)
g3 >> lbass(dur=[1/2, 1/3, 1/3, 1/3, 1/2], oct=4, hpf=400, drive=0.1, lpf=12000, mpf=3200, mverb=0)

e3.dist2=0.5
f6.stop()
k4 >> play("l[::]-x.",dur=1/4)
k5 >> play("s:",dur=1/4, drive=12)

e0 >> tb303(0, dur=1/4, cut=1/2, amp=PBin(), cutoff=var([200, 3200, 4000, 8000], [8, 12, 4, 8]), top=PRand(1200)[:8], rq=0.01, dec=var([0.1, 0.2, 0.5, 12], [4]))
e1 >> tb303(0, dur=var([1/2, 1/4], [4, 8]), cut=1/2, amp=1, oct=var([4, 5], [24, 8]), dist2=0, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:16], rq=[0.01, 0.001, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))
e_all.only()

p1 >> pluck(var([([7, 0], 0), [(12, 0), ([Scale.chromatic, 0], 0), (0, [12, 7])]]),oct=(3, PStep(16, 3, 4)), dur=PwRand([[4, 1, 1/2], P[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2]], [1, 30]), leg=linvar([0, 4], PRand(16)[:4]), dist2=0.8, pan=linvar([-1, 1], [32]), scale=Scale.chromatic, drive=var([PWhite(0.01, 0.1), [0, (0.01, 0.2)]]), hpf=PWhite(30, 60), hpr=(0.1, 0.9)).sometimes("stutter", 1, mverb=0.6, feed=0.2, rate=0.2, shape=1) + var([0, 3, 4], [PRand([24, 128]), 2, 2])

g3.lpf=100

p1.only()

p2 >> tb303([var([0, 4, linvar([P[0, 4], P[4, 0]],4)], [24, 4, 4]), linvar([0, 1])], oct=(var([6, 7, 5, 4]), (PRand(4), 4)), hpf=linvar([(200, 2400), (2000, 1000)], 64), hpr=linvar([0.01, 0.2], 32), dur=1/4, drive=linvar([0.4, 1], 64), vol=0.7, mpf=4000, cut=var([1/4, 1/8], [4, 4]), scale=Scale.chromatic).unison(2)

Clock.bpm = 122;
g3.dist2=0
g3.dist=0
g3.mverb=0.9
g3.lpf=100
g3.hpf=2000

p_all.only()
p_all.lpf=200

p1 >> pluck(var([([7, 0], 0), [(12, 0), ([Scale.chromatic, 0], 0), (0, [12, 7])]]),oct=(3, PStep(16, 3, 4)), dur=PwRand([[4, 1, 1/2], P[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2]], [1, 30]), leg=linvar([0, 4], PRand(16)[:4]), dist2=0.8, pan=linvar([-1, 1], [32]), scale=Scale.chromatic, drive=var([PWhite(0.01, 0.1), [0, (0.01, 0.2)]]), hpf=PWhite(30, 60), hpr=(0.1, 0.9)).sometimes("stutter", 1, mverb=0.6, feed=0.2, rate=0.2, shape=1) + var([0, 3, 4], [PRand([24, 128]), 2, 2])

g3.lpf=100

p1.only()

p2 >> tb303([var([0, 4, linvar([P[0, 4], P[4, 0]],4)], [24, 4, 4]), linvar([0, 1])], oct=(var([6, 7, 5, 4]), (PRand(4), 4)), hpf=linvar([(200, 2400), (2000, 1000)], 64), hpr=linvar([0.01, 0.2], 32), dur=1/4, drive=linvar([0.4, 1], 64), vol=0.7, mpf=4000, cut=var([1/4, 1/8], [4, 4]), scale=Scale.chromatic).unison(2)

Root.default="F"

p_all.only()
p3 >> tb303(p2.degree, dur=4, cut=[1/4, 1/2, 1/2, 1/4], oct=(3,5, 7), amp=0.3, echo=P*[0.5, 0, 0.25], shape=1, chop=4).unison(2)
p4 >> soprano(p1.degree, dur=PRand(1,8), blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(3,4,5)), drive=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), room=0.5, mix=0.5, amplify=0, spin=0, scale=Scale.chromatic).unison(3)

p5 >> pluck([(0, 7.01), (0.0,7.02)], dur=[1/4, 1/2, 1/2, 1/4, 1/2], fmod=p5.dur, leg=0,cut=linvar([1, 2], 16), oct=((3, 6), (4, 5), (5, 6)), hpf=200, amp=0.4, mpf=0, dist=1).unison(0)
p1 >> pluck(var([(0, 0), [(12, 0), ([6, 0], 0), (0, [12, 7])]]),oct=(3, PStep(16, 3, 4)), dur=[1/2, 1/4, 1/4, 1/4, 1/2, 1/4, 1/4, 1/2, 1/4, 1/2], leg=1, scale=Scale.chromatic, drive=PWhite(0.54, 0.9), hpf=50, hpr=(0.1, 0.9))

p_all.oct=3
Clock.bpm = 122;

f4.dist2=1.2
f4 >> faim(0.1 ,dur=var([PDur(4, 8),  2], [12, 2]), amp=PBin(8), mpf=2100, oct=5, leg=12, lpr=linvar([0.1, 0.5], 32), dist2=var([0, [1.2, 0.5, 2]], [12, 2]), echo=(f4.dist2==1.2)/2, shift=(f4.dist2==1.2) * P[1.0, 1.12], beef=0, mverb=(f4.dist2==0.5)/0.5, vol=0.7, hpf=(f4.dist2==1.2)*200).every(4, "stutter") + var([0, (-0.1, 0.1)], hpf=400)

f4.dist2=0.4

p3 >> donk(dur=1/4, oct=(5, linvar([4, 8], 64)), hpf=40, amp=Pvar([0.5, 0]), lpf=4000, echo=PCoin(0, 0.25, 0.5), shift=var([0, Scale.minor], [32, 32]))
p4 >> varicelle(oct=(4, 5), cut=1/4, fmod=4, dur=PDur(11, 16), delay=(var([0.25, 0]), var([0.5, 0.25, 0.25])), bit=2, crush=4, leg=4).sometimes("stutter", formant=linvar([1, 4], 8))

f6 >> loop("nssub8", dur=8, sample=2)
f6 >> loop("futur16", dur=8, sample=3)


f7 >> play(".(c.).(C..[kU]).", drive=0, formant=0, dur=2, sample=7)
f8 >> play("[-].-[--]", amp=0.3, sample=5, echo=(0, 0.5))
f4.hpf=3200

Clock.bpm = var([122/2, 122], [1, 1])

d0 >> tb303(0, dur=PDur(var([4,P*[5,7,1]],[6,2]),8), cut=1/2, amp=PBin(), cutoff=var([200, 3200, 4000, 8000], [8, 12, 4, 8]), top=PRand(1200)[:8], rq=0.01, dec=var([0.1, 0.2, 0.5, 12], [4]))
d1 >> tb303(0, dur=var([1/2, 1/4], [4, 8]), cut=1/2, amp=0.5, oct=var([4, 5], [24, 8]), dist2=1, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:16], rq=[0.01, 0.001, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

Clock.bpm = 122;

k1 >> play("K ")
d0 >> tb303(dur=var([1/2, 1], [4, 8]), cut=1, amp=1, oct=var([3, 7], [24, 8]), dist2=1, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.1, 0.3, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]), vol=0.3)
x1 >> play("<X:><->", sample=(15, 7), dur=1)
x2 >> play("..x...x.", sample=4, dur=1/2).every(4, "stutter", drive=4)

d8 >> tb303(dur=1/2, cut=1/2, delay=0.125, lpf=8000, amp=0.5, oct=var([6, 7], [24, 8]), dist2=1, cutoff=var([2000, 3200, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.04, 0.004, 0.2, 0.5, 1], dec=var([0.1, 0.2, 0.5, 12], [4]))
d1 >> tb303(dur=var([1/4, 1/2], [4, 8]), cut=1, amp=0.6, oct=var([3, 7], [24, 8]), dist2=1, cutoff=var([2000, 32000, 400, 800], [32]), top=PRand(1200)[:8], rq=[0.05, 0.005, 0.2, 0.5], dec=var([0.1, 0.2, 0.5, 12], [4]))

f4.stop()

drop(4, 1, 1)

d1.stop()

d_all.dur=16

attack("filter")

##### attack@filter.ejc:~$ #####

masterAll("lpf", var([0, 4000, 6000, 15000], [24, 4, 2, 2]))
masterAll("hpf", var([0, 20, 30, linvar([3200, 6400], 32)], [24, 4, 2, 2]))
masterAll("cut", var([0, 1, 1/2, linvar([1/4, 1], 32)], [24, 4, 2, 2]))

masterAll("oct", 3)
masterAll("lpf", 800)

masterAll("degree", linvar([1, linvar([0, 2],[4, 0])], 8))
masterAll("rate", 8) 
masterAll("dur", P*[1/2, 1, 1, 1/2, 2])

drop(4, 4, 4)

masterAll("reset")
k1 >> play("K.", amp=4, mverb=0.7, lpf=5400)

masterAll("dur", 0.125)



drop(1, 1, 1)



k_all.only()

Clock.bpm = 170

Clock.bpm = 170

d1 >> loop("break16", dur=16, hpf=4000)
d2 >> loop("break16", sample=1, dur=32, low=4, hpr=0.1, spf=200, spfend=1100, spfslide=(32, 4), hpf=2000, fold=0.4, mverb=0.2, delay=(4, 0), feed=0.4)
d4 >> ebass([3, 0,5.5, _],dur=1/2, scale=Scale.yu)
f5 >> play("V.o.", sample=(3, 6), echo=[0,0.125, 0.25, 0.5], bpf=800, bpr=0.9, cut=PRand([1/4, 1/2]))
f6 >> play("W ")
f9 >> play('(:.)...', amp=2, dur=4)
f0 >> play('X.U.', amp=1, sample=8)
d3 >> loop("break16", sample=2, delay=4, dur=16, hpf=200, fold=0.1, chop=4, leg=4)
d4 >> loop("break16", sample=4, delay=0, beat_dur=1, dur=16, hpf=100, fold=0.1, chop=2, leg=0)

d_all.only()

g1 >> loop("gab16_10sec_180", dur=32)

d5 >> loop("break16", sample=8, dur=16, amp=[0, 1])
d6 >> loop("break16", sample=12, dur=16, amp=[1, 0], lpf=400, lpr=0.1, lowfi=0.4, mverb=0.5, dist2=0.2)
d7 >> loop("hiphop16", sample=1, dur=16, amp=1)
d6 >> loop("hiphop16", sample=2, dur=16, amp=1)
d6.dur=32
d6.mverb=0.9
d5 >> loop("hiphop16", sample=3, dur=16)
d4 >> loop("hiphop16", sample=1, dur=16)
d3 >> loop("hiphop16", sample=4, dur=16)
d2 >> loop("hiphop16", sample=1, dur=16)

d1 >> loop("hiphop16", sample=4, dur=16)
d_all.dur=32


d3 >> play("nN", sample=(2, 1), cut=P*[1/4, 1/2], dur=1, echo=P*[1/2, 4], amp=0.3, mverb=0.3, feed=0.2)
k4 >> play("EmptyItem", amp=0.3, hpr=0.1, hpf=(400, linvar([200, 1200])), sample=(5, 4), echo=1.25, lpf=1200, lpr=0.2, dur=P*[1/2, 4, 1/2])

k5 >> swiss(dur=(PDur(3, 8, 2), PDur(5, 12, 4)),oct=(4, 6), amp=0.3, shift=var([0, 2], [15, 3]), lpr=0.065, cut=1/2, echo=var([0, 0.5]), lpf=400).unison(8)

r2 >> play("u", lpf=linvar([1000, 12000], 32), dur=var([2, 1/2]), mverb=linvar([0.5, 0], 32), high=1, delay=(00.25, 2.25), low=0, sample=var([4, 5], [3, 1]), dist2=2, rate=var([1, 2, 4], [12, 2, 22]))
r3 >> play("b", lpf=linvar([12000, 1200], 32), dur=PDur(3, 4), mverb=0, high=1, delay=(0, 2.25), low=0, sample=var([4, 12], [1, 3]), dist2=1, bits=4, krush=4, rate=4)
k1 >> rsin(lpf=400, dur=4, cut=1/2, sus=2, high=21, hpr=0.01, oct=8, feed=0.5, dist2=0.2,  valad=P*[20, 200, 400], dubd=1, fold=0.1,  phaser=var([0.5, 1], 8), rate=(4, 0.25), mverb=0.0, hpf=linvar([50, 58], 32))


e9 >> plaits(e0.degree, dur=8, mpf=2400, dist2=1, chop=4, spf=200, spfend=4000, spfslide=8,blur=PWhite(0,4),decay=PRand(4), oct=(3,4,PStep(3,2,3)), drive=PWhite(0,0.1), sus=PRand(16), atk=PRand(4), mverb=0.2, amplify=12, spin=0, scale=Scale.chromatic).unison(0)

e8 >> play("-:", dur=4, lpf=1200, mverb=0.5, amp=8, sample=5, echo=1.25, echotime=4)
~e4 >> play("ot[uz][xk].k.", dur=1/4, amp=8, drive=0, sample=2)




k3.dur=4
k5 >> saw(3,oct=3, lpf=linvar([400, 1600], 32), dur=[4, 1/3], engine=1)
k6 >> zap(2,oct=3, dur=4, engine=4)
k7 >> bass(7,oct=3, dur=PDur(5, 8, 0), engine=1, delay=1, mverb=0.5, valadd=10, valad=120)
k8 >> lbass([PWalk(Scale.minor, 1, 1), -14, -14 + PArp([-12, var([2, 0], 4), 2])], scale=Scale.minor, sus=2, dur=1,oct=5, rate=2)
k8 >> cluster([0, 7, 1 + PArp([4, var([1, P[1:10]], 4), 2])], scale=Scale.chromatic, dur=1/3, oct=5, pan=linvar([-1, 1])).unison(2, 0.01, 1)

